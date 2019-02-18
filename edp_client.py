#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import struct
import six
CONN_SUCCESS = 0x00
CONN_REQ = 0x10
CONN_RESP = 0x20
PUSH_DATA = 0x30
CONN_CLOSE = 0x40
SAVE_DATA = 0x80
SAVE_ACK = 0x90
CMD_REQ = 0xA0
CMD_RESP = 0xB0
PING_REQ = 0xC0
PING_RESP = 0xD0
ENCRYPT_REQ = 0xE0
ENCRYPT_RESP = 0xF0

EDP1 = 1
PROTOCOL_NAME1 = "EDP"

class mysocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                    socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
        #self.sock.setblocking( False )
        self.sock.settimeout( 1 )
    def close(self):
        self.sock.close()
    def connect(self, host, port):
        try:
          self.sock.connect((host, port))
        except:
            print("Socket connect Error")
            pass
    def connect_ex(self,host,port):
        try:
           t= self.sock.connect_ex((host,port))
        except:
            print("Socket Error")
            return -1
        return t
    def mysend(self, msg, msg_len):
        totallen = 0
        sent = 0
        while totallen < msg_len:
            try:
              sent = self.sock.send(msg[totallen:])
            except:
                print("socket con close")
                pass
            if sent == 0:
                print("socket connection broken")
                break
            totallen = totallen + sent

    def myreceive(self):
        b1=bytearray()
        self.sock.setblocking( False )

            # 每次最多接收1k字节
            #print( u"开始接收" )
        try:
              d = self.sock.recv( 1024 )
            #print( u"接收完成" )
        except :
                d=None
                #continue
                #buf=str(d)
                #b1.join(buf)
        try:
          for i in d:
             b1.append(int(i))
        except:
            pass
                #print(d[1])
                #print(d[2])
                #da=str(d)
                #print(da)
        #print( "_______" )
        #print( b1 )
        return b1

class Client:
    def __init__(self, sock, username, password, protocol=EDP1, keepalive=128):
        if username == "" or username is None:
            raise ValueError('username must not be empty')
        if password == "" or password is None:
            raise ValueError('password must not be empty')
        self._username = username
        self._password = password
        self._keepalive = keepalive
        self._protocol = protocol
        self._sock = sock
        self._from_packet = None
        self._to_packet = None

        self._cmdid = None
        self._cmdlen = None
        self._cmdmsglen = None
        self._cmdmsg = None

    def _pack_remaining_length(self, packet, remaining_length):
        q = remaining_length / 128
        w = remaining_length
        #print( q )
        if q >= 1:
            q1 = ((w & 0x7F) | 0x80) & 0xFF
            packet.extend( struct.pack( "!B", q1 ) )
            q2 = (w >> 7) & 0xFF
            packet.extend( struct.pack( "!B", q2 ) )
            #print( "1" )
        else:
            q1 = w & 0x7F
            packet.extend( struct.pack( "!B", q1 ) )
            #print( "2" )
        # packet.extend(b)
        #print( packet )

    def _unpack_remaining_length(self, packet):
        if packet[1] & 0x80:
            b1 = packet[1] & 0x7F
            b2 = (packet[2] << 7) | b1
        else:
            b2 = packet[1] & 0x7F
        return b2

    def _pack_str16(self, packet, data):
        if isinstance(data, bytearray):
            packet.extend(struct.pack("!H", len(data)))
            packet.extend(data)
        elif isinstance(data, str):
            udata = data.encode('utf-8')
            packet_format = "!H" + str(len(udata)) + "s"
            packet.extend(struct.pack(packet_format, len(udata), udata))
        #elif isinstance(data, Unicode):
           # packet_format = "!H" + str(len(udata)) + "s"
           # packet.extend(struct.pack(packet_format, len(udata), udata))
        else:
            raise TypeError

    def _pack_str32(self, packet, data):
        if isinstance(data, bytearray):
            packet.extend(struct.pack("!I", len(data)))
            packet.extend(data)
        elif isinstance(data, str):
            udata = data.encode('utf-8')
            packet_format = "!I" + str(len(udata)) + "s"
            packet.extend(struct.pack(packet_format, len(udata), udata))
        #elif isinstance(data, unicode):
           # udata = data.encode('utf-8')
           # packet_format = "!I" + str(len(udata)) + "s"
            #packet.extend(struct.pack(packet_format, len(udata), udata))
        else:
            raise TypeError


    def _read(self):
        #packet=bytes()
        packet = self._sock.myreceive()
        self._from_packet = packet

    def _build_connect(self):
        if self._protocol == EDP1:#1
            protocol = PROTOCOL_NAME1#EDP
            proto_ver = 1
        keepalive = self._keepalive
        remaining_length = 2+len(protocol)+1+1+2 +2+len(self._username) +2+len(self._password)
        connect_flags = 0
        connect_flags = connect_flags | 0x40

        command = CONN_REQ
        packet = bytearray()
        packet.extend(struct.pack("!B", command))

        self._pack_remaining_length(packet, remaining_length)
        packet.extend(struct.pack("!H"+str(len(protocol))+"sBBH", len(protocol), protocol.encode('utf-8'), proto_ver, connect_flags, keepalive))

        self._pack_str16(packet, self._username)
        self._pack_str16(packet, self._password)
        self._to_packet = packet

    def _build_push_data(self, dst_device_id=None, data=None):
        command = PUSH_DATA
        packet = bytearray()
        packet.extend(struct.pack("!B", command))

        if dst_device_id is None or dst_device_id == '':
            remaining_length = 2+len(data)
            self._pack_remaining_length(packet, remaining_length)
            packet.extend(struct.pack("!H", 0))
        else:
            remaining_length = 2+len(dst_device_id)+len(data)
            self._pack_remaining_length(packet, remaining_length)
            packet.extend(struct.pack("!H"+str(len(dst_device_id))+"s", len(dst_device_id), dst_device_id.encode('utf-8')))
        self._pack_str16(packet, data)
        self._to_packet = packet

    def _build_save_data(self, dst_device_id, data, data_type):
        command = SAVE_DATA
        packet = bytearray()
        packet.extend(struct.pack("!B", command))

        if dst_device_id is None or dst_device_id == '':
            remaining_length = 1+1+2+len(data)
            #remaining_length = flag+datatype+2+data_len
            self._pack_remaining_length(packet, remaining_length)
            packet.extend(struct.pack("!B", 0))
        else:
            remaining_length = 1+2+len(dst_device_id)+1+2+len(data)
            self._pack_remaining_length(packet, remaining_length)
            packet.extend(struct.pack("!BH"+str(len(dst_device_id))+"s", 0x80, len(dst_device_id), dst_device_id))

        packet.extend(struct.pack("!B", data_type))
        if data_type == 2:
            self._pack_str32(packet, data)
        else:
            self._pack_str16(packet, data)
        self._to_packet = packet

    def _build_cmd_resp(self, cmdid, resp_body):
        command = CMD_RESP
        packet = bytearray()
        packet.extend(struct.pack("!B", command))
        remaining_length = 2+len(cmdid)+4+len(resp_body)
        self._pack_remaining_length(packet, remaining_length)

        self._pack_str16(packet, cmdid)
        self._pack_str32(packet, resp_body)
        self._to_packet = packet

    def _build_ping_req(self):
        command = PING_REQ
        packet = bytearray()
        packet.extend(struct.pack("!BB", command, 0))
        self._to_packet = packet

    def handle_cmd_req(self):
        len = self._unpack_remaining_length(self._from_packet)

       # print("#######")
        #print(len)
        try:
            _cmdlen=self._from_packet[2]<<8|self._from_packet[3]
            _msglen=self._from_packet[4+_cmdlen]<<24|self._from_packet[5+_cmdlen]<<16|self._from_packet[6+_cmdlen]<<8|self._from_packet[7+_cmdlen]
            # get remaining_length
            (rtype, remaining_length, cmd_len, cmdid, msg_len, msg) = struct.unpack(
                '!BBH' + str( _cmdlen ) + 'si' + str( _msglen ) + 's', self._from_packet )
           # print("&&&&&&")
           # print(_cmdlen)
           # print( _msglen )
            self._cmdid = cmdid
            self._cmdlen = cmd_len
            self._cmdmsglen = msg_len
            self._cmdmsg = msg
            self.cmd_resp( self._cmdid )
        except:
            pass

        return msg

    def handle_save_ack(self):
        (have_json,) = struct.unpack('!B', self._from_packet[2])
        if have_json & 0x80 == 0:
            (rtype, remaining_length, desc_flag) = struct.unpack('!BBB', self._from_packet)
            return(0, 0)
        elif have_json & 0x80 == 128:
            (len,) = struct.unpack('!H', str(self._from_packet[3])+str(self._from_packet[4]))
            (rtype, remaining_length, desc_flag, desc_len, desc) = struct.unpack('!BBBH'+str(len)+'s',
                    self._from_packet)
            return (desc_len, desc)

    def handle_ping_resp(self):
        (rtype, remaining_length) = struct.unpack('!BB', self._from_packet)

    def conn_req(self):
        self._build_connect()
        self._sock.mysend(self._to_packet, len(self._to_packet))

    def push_data(self, dst_device_id, data):
        self._build_push_data(dst_device_id, data)
        self._sock.mysend(self._to_packet, len(self._to_packet))

    def save_data(self, data, data_type, dst_device_id=None):
        self._build_save_data(dst_device_id, data, data_type)
        self._sock.mysend(self._to_packet, len(self._to_packet))

    def cmd_resp(self, cmdid, resp_body="ok"):
        self._build_cmd_resp(cmdid, resp_body)
        self._sock.mysend(self._to_packet, len(self._to_packet))

    def conn_close(self):
        pass

    def ping_req(self):
        self._build_ping_req()
        self._sock.mysend(self._to_packet, len(self._to_packet))

    def edp_packet_type(self):
        #b = self._from_packet.encode( encoding='utf-8' )
        #b=self._from_packet.decode( 'hex' )
       # (_result,)= struct.unpack('!B', b[0])
        #q=self._from_packet.decode('utf-8')
        #print(self._from_packet)
        return self._from_packet

    def read_packet(self):
        self._read()

    def is_conn_resp(self):
        self._read()
        _result = struct.unpack('!BBBB', self._from_packet)
        if _result[0] == CONN_RESP and _result[3] == CONN_SUCCESS:
            return True
        else:
            return False

    def clear_packet(self):
        self._from_packet = None
        self._to_packet = None

    def encrypt_req(self):
        pass
    def _print_pack(self):
        print(self._from_packet)