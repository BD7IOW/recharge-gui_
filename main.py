import wx
import ui
import time
import datetime
import queue
import serial.tools.list_ports
import threading
from edp_client import *
import select
import json
import configparser
import os

class _Serial_Proc_Thread( threading.Thread ):
    def __init__(self, q_in, q_out, _ser):
        super( _Serial_Proc_Thread, self ).__init__()
        self._serial = _ser
        self.q_input = q_in
        self.q_out = q_out
        #self.DEVICEID=''
        #self.APIKEY=''
        self.serial_cnt=0
        self._time_dev = {}  # num(1-32)[timer_flag(定时标志),start_time(定时起始时间),time(定时时间s),yu]
        self.init_dev()  # 初始化字典，用于管理定时事件
        self.setDaemon( True )
        self.start()
        # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒),数据有效1,0无效


    def init_dev(self):
        for i in range( 32 ):
            _q = str( i + 1 )
            self._time_dev.update( {_q: [0, 0, 0,0]} )

    def uchar_checksum(self, data, byteorder='little',msg='a'):
        '''
        #char_checksum 按字节计算校验和。每个字节被翻译为无符号整数
        @param data: 字节串
        @param byteorder: 大/小端
        '''
        checksum = 0
        if msg is 'a':
           length = len( data )
           for i in range( 0, length ):
              checksum += int.from_bytes( data[i:i + 1], byteorder, signed=False )
              #checksum &= 0xFF  # 强制截断
        elif msg is 'b':
            length = len( data )
            for i in range( 0, (length-1) ):
                checksum += int.from_bytes( data[i:i + 1], byteorder, signed=False )
        checksum &= 0xFF  # 强制截断
        return checksum

    def cmd_stream(self, addr, cmd="close", argv=0):  # 打开 关闭，定时关闭argv=秒数
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
        elif cmd is "read_all_output":#读取所有继电器状态
            b[2]=0x10
            b[3]=b[4]=b[5]=b[6]=0
            b[7]=0x66
        return b
    def ui_time_flash(self):
        for key in self._time_dev:
            if self._time_dev[key][0] == 1:  # 定时开启
                w = (datetime.datetime.now() - self._time_dev[key][1])
                if w.seconds == self._time_dev[key][2]:  # 定时时间到
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream(key, cmd="close", argv=0) )
                    self._time_dev[key][0] = 0
                    # elif data_arry[2] is "2":#更新网络信息
                    continue
                elif w.seconds < self._time_dev[key][2]:
                    q=self._time_dev[key][2]-w.seconds
                    self._time_dev[key][3]=q
                    #_str =str(q)
                    #self.q_out.put(key+",1"+",1,"+_str ,block=True, timeout=1 )


    def run(self):
        t1=0
        t2=0
    #num(1-32):timer_flag(定时标志),start_time(定时起始时间),time(定时时间s)
    #number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
        while True:
            t1+=1
            t2+=1
            if t1 == 10:
               t1=0
               self.ui_time_flash()
            while self.q_input.empty() is not True:  # 输入队列非空
                _str = self.q_input.get( block=True, timeout=1 )
                data_arry = _str.split( ',' )
                if data_arry[1] is "1" and data_arry[2] is "1":  # 定时开启
                    self._time_dev[data_arry[0]][0] = 1 #
                    self._time_dev[data_arry[0]][1] = datetime.datetime.now()
                    self._time_dev[data_arry[0]][2] = int( data_arry[3] )
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream( data_arry[0], cmd="open", argv=int( data_arry[3] ) ) )
                elif data_arry[2] is "1":
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream( data_arry[0], cmd="open", argv=int( data_arry[3] ) ) )
                elif data_arry[2] is "0":
                    self._time_dev[data_arry[0]][0] = 0
                    self._time_dev[data_arry[0]][1] = 0
                    self._time_dev[data_arry[0]][2] = 0
                    self._time_dev[data_arry[0]][3] = 0
                    if self._serial.isOpen():
                        self._serial.write( self.cmd_stream( data_arry[0], cmd="close", argv=int( data_arry[3] ) ) )
                #elif data_arry[2] is "2":#更新网络信息
                    #self.conf.read( self.cfgpath, encoding="utf-8" )
                   # self.DEVICEID = self.conf.get( "NET_CONF", "DEVID" )
                    #self.APIKEY = self.conf.get( "NET_CONF", "APIKEY" )
                    #print(self.DEVICEID)
                    #print(self.APIKEY)
            if t2==30:#定时读取继电器状态
                t2=0
                #"read_all_output"
                if self._serial.isOpen():
                     self._serial.write( self.cmd_stream( 0, cmd="read_all_output", argv=0) )
                #elif data_arry[2] is "2":#更新网络信息
            time.sleep( 0.04 )
            if self._serial.isOpen() and self._serial.inWaiting():
                try:
                   _recv = self._serial.read( 8 )

                except:
                    pass
                # pub.sendMessage, "update", msg="Thread finished!"
                # wx.CallAfter( pub.sendMessage,'update', msg=text )
                #print( _recv )

                if _recv[0] == 0x22 and _recv[7]==self.uchar_checksum(_recv,msg='b'):
                    cnt=1
                    para = (_recv[3] << 24 | _recv[4] << 16 | _recv[5] << 8 | _recv[6])
                    #print( str( para ) )


                    self.q_out.put( ("67,67,67,"+str(self.serial_cnt)), block=True, timeout=1 )
                    self.serial_cnt += 1
                    for i in range(32):
                        if para&0x00000001 == 1:
                            #print("11")
                            if self._time_dev[str(cnt)][0] == 1:#定时开启
                               #temp=str(cnt)+",1,1,"+
                               self.q_out.put( str(cnt)+",1,1,"+str(self._time_dev[str(cnt)][3]), block=True, timeout=1 )
                            else:
                                self.q_out.put( str( cnt ) + ",0,1,0", block=True,
                                                timeout=1 )
                        else:
                            self.q_out.put( str( cnt ) + ",0,0,0", block=True,
                                            timeout=1 )
                        para=para>>1
                        cnt+=1

                   # print( str( para ) )


            time.sleep( 0.04 )

class edp_handle(threading.Thread):
    def __init__(self, q_in, q_out):
        super( edp_handle, self ).__init__()
        self.qin=q_in
        self.qout=q_out

        self.web_ava=False
        self.con_net=False
        self.dev_val=[]
        self.curpath = os.path.dirname( os.path.realpath( __file__ ) )
        self.cfgpath = os.path.join( self.curpath, "cfg.ini" )
        # 创建管理对象
        self.conf = configparser.ConfigParser()
        self.DEVICEID = ''
        self.APIKEY = ''
        #self.host = "jjfaedp.hedevice.com"
        self.port = 876
        self.host = "jjfaedp.hedevice.com"
        #port = 876
        #self.DEVICEID = "517194963"
        #self.APIKEY = "yIACiEig3lVrtLBBlFPAaXHBlVM="
        try:
            # 先读出来
            self.conf.read( self.cfgpath, encoding="utf-8" )
            self.DEVICEID = self.conf.get( "NET_CONF", "DEVID" )
            self.APIKEY = self.conf.get( "NET_CONF", "APIKEY" )
        except:
            pass
        self.sock = mysocket(None)
        self.client = Client( self.sock, self.DEVICEID, self.APIKEY )
        k=self.sock.connect_ex(self.host,self.port)
        print("trtrtrtr")
        print(k)
        try:
          self.client.conn_req()
        except:
            pass
        # client.ping_req()
        #edp_save_data( client )
        # doRead( client, sock )
        self.link_cnt = 0
        for i in range(32):
            self.dev_val.append(0)
        self.setDaemon( True )
        self.start()

    def edp_save_data(self,c):
        dict = {"CH1":0,"CH2":0,"CH3":0,"CH4":0,"CH5":0,"CH6":0,"CH7":0,"CH8":0,"CH9":0,"CH10":0
            , "CH11": 0,"CH12":0,"CH13":0,"CH14":0,"CH15":0,"CH16":0,"CH17":0,"CH18":0,"CH19":0,"CH20":0
            , "CH21": 0,"CH22":0,"CH23":0,"CH24":0,"CH25":0,"CH26":0,"CH27":0,"CH28":0,"CH29":0,"CH30":0,"CH31":0,"CH32":0
                }

        k=0
        for i in range(32):
            if self.dev_val[k] == 1:
                dict[("CH"+str(k+1))]=1
            else:dict[("CH"+str(k+1))]=0
            k+=1
        data = json.dumps( dict )
        c.save_data( data, 3 )
        print( "after save_data" )
        c.clear_packet()
    def doRead(self,c, s):

        rlist = [s.sock]
        while True:
            r, w, e = select.select( rlist, [], [], 4 )
            # edp_save_data( client )
            #time.sleep(1)
            if not r:
                print( 'timeout...' )
                break
            else:
                for sock in r:
                    if sock is s.sock:
                        #type1 = bytearray()
                        c.read_packet()
                        type1 = c.edp_packet_type()
                        if not type1:
                            continue
                        else:
                            type = type1[0]

                            print( type )
                            if type == CONN_RESP:
                            #self.socket_cnt = True

                               print( "<<CONN_RESP+" )
                            elif type == CMD_REQ:
                                print( "<<CMD_REQ" )
                                msg = c.handle_cmd_req()
                                cmd=str( msg, encoding='utf-8' )
                                print( 'command is' + cmd )
                                #_cmd=cmd.split(':')
                                self.qout.put(cmd, block=True, timeout=1 )
                            elif type == SAVE_ACK:
                                print( "<<SAVE_ACK" )
                                (desc_len, desc) = c.handle_save_ack()
                                print( 'result is ' + desc )
                            elif type == PING_RESP:
                                #  self.socket_timeout[0] = 0
                                self.link_cnt=0
                                self.web_ava = True
                                self.qout.put( "CONN_CNNT:none", block=True, timeout=1 )
                                print( "<<PING_RESP" )
                            else:
                                print( "not done or unknown type" )
                                break
            break

    def run(self):

      while True:

          while self.qin.empty() is not True:
              _str = self.qin.get( block=True, timeout=1 )
              data_arry = _str.split( ':' )
              #print(_str)
              if data_arry[0] == "send_cnn":
                self.con_net = True
                print( "self.con_net = True")
              elif data_arry[0] == "cnn_close":
                self.con_net = False
              elif data_arry[0] == "1" or data_arry[0] == "0":
                  k=0
                  for i in range(32):
                      if data_arry[k] == "1":
                          self.dev_val[k]=1
                      elif data_arry[k] == "0":
                          self.dev_val[k]=0
                      k+=1
              else:break
          if self.con_net is True:
            print("self.con_net is True:")
            if self.web_ava == False :
              #self.con_net = True
              self.sock = mysocket( None )
              self.client = Client( self.sock, self.DEVICEID, self.APIKEY )
              k = self.sock.connect_ex( self.host, self.port )
              #print( "trtrtrtr" )
              #print( k )
              self.client.conn_req()
              self.qout.put("CONN_CLOSE:"+str(k), block=True, timeout=1)
              print( u"sock正在重连" )
            try:
                self.edp_save_data( self.client )
                self.doRead( self.client, self.sock )
                self.client.ping_req()
                self.doRead( self.client, self.sock )
            except:

                pass

          #ping( client )
          #doRead( client, sock )
          time.sleep( 2 )
          self.link_cnt+=1
          if  self.link_cnt > 6:
              self.link_cnt=0
              self.web_ava = False
              print("link timeout")
        #self.doRead( self.client, self.sock )



if __name__ == '__main__':
    _ser = serial.Serial()
    q1 = queue.Queue()
    q2 = queue.Queue()
    #######################
    q3 = queue.Queue()
    q4 = queue.Queue()
    app = wx.App()
    serialThread = _Serial_Proc_Thread( q2, q1, _ser )
    edpThread = edp_handle(q4,q3)
    frame = ui.MyFrame( None, q1, q2, _ser ,q3,q4)
    frame.Show()
    app.MainLoop()


