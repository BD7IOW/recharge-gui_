import wx
import ui
import time
import datetime
import queue
import serial.tools.list_ports
import threading
#from web_men import _Device
#import os
#import configparser

# class main_Frame(ui.MyFrame):
#   def __init__(self, parent):
#       ui.MyFrame.__init__( self, parent )
class _Serial_Proc_Thread( threading.Thread ):
    def __init__(self, q_in, q_out, _ser):
        super( _Serial_Proc_Thread, self ).__init__()
        self._serial = _ser
        self.q_input = q_in
        self.q_out = q_out
        #self.DEVICEID=''
        #self.APIKEY=''
        self._time_dev = {}  # num(1-32),timer_flag(定时标志),start_time(定时起始时间),time(定时时间s)
        self.init_dev()  # 初始化字典，用于管理定时事件
        self.start()
        # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)


    def init_dev(self):
        for i in range( 32 ):
            _q = str( i + 1 )
            self._time_dev.update( {_q: [0, 0, 0]} )

    def uchar_checksum(self, data, byteorder='little'):
        '''
        #char_checksum 按字节计算校验和。每个字节被翻译为无符号整数
        @param data: 字节串
        @param byteorder: 大/小端
        '''
        length = len( data )
        checksum = 0
        for i in range( 0, length ):
            checksum += int.from_bytes( data[i:i + 1], byteorder, signed=False )
            checksum &= 0xFF  # 强制截断
        return checksum

    def cmd_stream(self, addr, cmd="close", argv=0):  # 打开 关闭，定时关闭argv=miao
        # t.write("\x55\x53".encode('utf-8'))
        b = bytearray( 8 )
        n = (argv * 1000) & 0xFFFFFF  # 转为ms
        b[0] = 0x55
        b[1] = 0x01
        if cmd is "close":
            b[2] = 0x11
            b[3] = 0
            b[4] = 0
            b[5] = 0
            b[6] = int( addr ) & 0xff
            b[7] = self.uchar_checksum( b )
            # print(b)
        elif cmd is "open":
            b[2] = 0x12
            b[3] = 0
            b[4] = 0
            b[5] = 0
            b[6] = int( addr ) & 0xff
            b[7] = self.uchar_checksum( b )
            # print( b )
        elif cmd is "on_time":  # 定时关闭
            b[2] = 0x21
            b[3] = ((n & 0xFF0000) >> 16) & 0xFF
            b[4] = ((n & 0x00FF00) >> 8) & 0xFF
            b[5] = (n & 0x0000FF) & 0xFF
            b[6] = int( addr ) & 0xff
            b[7] = self.uchar_checksum( b )
            # print( b )
        return b
    def ui_time_flash(self):
        for key in self._time_dev:
            #print( key + ':')
            #print(self._time_dev[key])
            if self._time_dev[key][0] is 1:  # 定时开启
                w = (datetime.datetime.now() - self._time_dev[key][1])
                if w.seconds == self._time_dev[key][2]:  # 定时时间到
                    continue
                elif w.seconds < self._time_dev[key][2]:
                    q=self._time_dev[key][2]-w.seconds
                    _str =str(q)
                    self.q_out.put(key+",1"+",1,"+_str ,block=True, timeout=1 )


    def run(self):
        t1=0
    #num(1-32):timer_flag(定时标志),start_time(定时起始时间),time(定时时间s)
    #number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
        while True:
            t1+=1
            if t1 == 8:
               t1=0
               self.ui_time_flash()
            while self.q_input.empty() is not True:  # 输入队列非空
                _str = self.q_input.get( block=True, timeout=1 )
                data_arry = _str.split( ',' )
                if data_arry[1] is "1" and data_arry[2] is "1":  # 定时开启
                    self._time_dev[data_arry[0]][0] = 1  # 标志等待设备返回设置
                    self._time_dev[data_arry[0]][1] = datetime.datetime.now()
                    self._time_dev[data_arry[0]][2] = int( data_arry[3] )
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream( data_arry[0], cmd="on_time", argv=int( data_arry[3] ) ) )
                elif data_arry[2] is "1":
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream( data_arry[0], cmd="open", argv=int( data_arry[3] ) ) )
                elif data_arry[2] is "0":
                    self._time_dev[data_arry[0]][0] = 0
                    self._time_dev[data_arry[0]][1] = 0
                    self._time_dev[data_arry[0]][2] = 0
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream( data_arry[0], cmd="close", argv=int( data_arry[3] ) ) )
                #elif data_arry[2] is "2":#更新网络信息
                    #self.conf.read( self.cfgpath, encoding="utf-8" )
                   # self.DEVICEID = self.conf.get( "NET_CONF", "DEVID" )
                    #self.APIKEY = self.conf.get( "NET_CONF", "APIKEY" )
                    #print(self.DEVICEID)
                    #print(self.APIKEY)
            time.sleep( 0.04 )
            if self._serial.isOpen() and self._serial.inWaiting():
                _recv = self._serial.read( 8 )
                # pub.sendMessage, "update", msg="Thread finished!"
                # wx.CallAfter( pub.sendMessage,'update', msg=text )
                print( _recv )
            time.sleep( 0.04 )


if __name__ == '__main__':
    # multiprocessing.freeze_support()#据说必须在代码入口添加multiprocessing.freeze_support( )，
    # 否则用pyinstaller打包成exe，执行中会出现主进程无限循环的问题。
    # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)

    _ser = serial.Serial()
    q1 = queue.Queue()
    #q1.put( "32,1,1,66666", block=False, timeout=1 )
    q2 = queue.Queue()
    app = wx.App()
    serialThread = _Serial_Proc_Thread( q2, q1, _ser )
    frame = ui.MyFrame( None, q1, q2, _ser )
    frame.Show()
    app.MainLoop()
