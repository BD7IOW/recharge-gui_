# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import datetime
import serial.tools.list_ports
import os
import configparser
from net_conf import netDialog
from debug_view import DebugView
import requests

import time

import json
###########################################################################
## Class MyFrame
###########################################################################

class MyFrame( wx.Frame ):
    def __init__(self, parent,q_in,q_out,ser,eqin,eqout):
        wx.Frame.__init__( self, parent, id=wx.ID_ANY, title=u"充电管理", pos=wx.DefaultPosition, size=wx.Size( 1043, 512 ),
                           style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"端口：", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetMinSize( wx.Size( -1, 50 ) )

        bSizer2.Add( self.m_staticText1, 0, wx.ALL | wx.EXPAND | wx.LEFT, 5 )

        m_comboBox0Choices = []
        self.m_comboBox0 = wx.ComboBox( self, wx.ID_ANY, u"端口号", wx.DefaultPosition, wx.DefaultSize, m_comboBox0Choices,
                                        0 )
        self.m_comboBox0.SetMinSize( wx.Size( -1, 50 ) )

        bSizer2.Add( self.m_comboBox0, 0, wx.ALL | wx.EXPAND | wx.LEFT, 5 )

        self.m_button_find_com = wx.Button( self, wx.ID_ANY, u"搜索端口", wx.DefaultPosition, wx.Size( -1, -1 ), 0 )
        self.m_button_find_com.SetMinSize( wx.Size( -1, 50 ) )

        bSizer2.Add( self.m_button_find_com, 0, wx.ALL | wx.EXPAND | wx.LEFT, 5 )

        self.m_button_open_com = wx.Button( self, wx.ID_ANY, u"打开端口", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_open_com.SetMinSize( wx.Size( -1, 50 ) )

        bSizer2.Add( self.m_button_open_com, 0, wx.ALL | wx.EXPAND | wx.LEFT, 5 )

        self.m_button_connection_ser = wx.Button( self, wx.ID_ANY, u"允许联网", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_button_connection_ser.SetMinSize( wx.Size( -1, 50 ) )

        bSizer2.Add( self.m_button_connection_ser, 0, wx.ALL | wx.EXPAND | wx.LEFT, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString,wx.DefaultPosition, wx.Size( 400, 60 ), style =wx.TE_MULTILINE)
        bSizer2.Add( self.m_textCtrl1, 0, wx.ALL | wx.LEFT, 5 )

        bSizer1.Add( bSizer2, 1,
                     wx.ALIGN_LEFT | wx.ALL | wx.BOTTOM | wx.EXPAND | wx.FIXED_MINSIZE | wx.LEFT | wx.RESERVE_SPACE_EVEN_IF_HIDDEN | wx.RIGHT | wx.SHAPED,
                     5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox1 = wx.CheckBox( self, 2000, u"1号定时", wx.DefaultPosition, wx.Size( -1, 20 ), 0 )
        bSizer10.Add( self.m_checkBox1, 0, wx.ALL, 5 )

        m_comboBox1Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox1 = wx.ComboBox( self, 3000, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox1Choices, 0 )
        self.m_comboBox1.SetSelection( 0 )
        bSizer10.Add( self.m_comboBox1, 0, wx.ALL, 5 )

        self.m_button1 = wx.ToggleButton( self,1000, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button1, 0, wx.ALL, 5 )
        #self.m_button1_1 = wx.ToggleButton()
        self.m_checkBox2 = wx.CheckBox( self,2001, u"2号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_checkBox2, 0, wx.ALL, 5 )

        m_comboBox2Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox2 = wx.ComboBox( self, 3001, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox2Choices, 0 )
        self.m_comboBox2.SetSelection( 0 )
        bSizer10.Add( self.m_comboBox2, 0, wx.ALL, 5 )

        self.m_button2 = wx.ToggleButton( self, 1001, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button2, 0, wx.ALL, 5 )

        self.m_checkBox3 = wx.CheckBox( self, 2002, u"3号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_checkBox3, 0, wx.ALL, 5 )

        m_comboBox3Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox3 = wx.ComboBox( self, 3002, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox3Choices, 0 )
        self.m_comboBox3.SetSelection( 0 )
        bSizer10.Add( self.m_comboBox3, 0, wx.ALL, 5 )

        self.m_button3 = wx.ToggleButton( self, 1002, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer10.Add( self.m_button3, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer10, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox4 = wx.CheckBox( self, 2003, u"4号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_checkBox4, 0, wx.ALL, 5 )

        m_comboBox4Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox4 = wx.ComboBox( self, 3003, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox4Choices, 0 )
        self.m_comboBox4.SetSelection( 0 )
        bSizer13.Add( self.m_comboBox4, 0, wx.ALL, 5 )

        self.m_button4 = wx.ToggleButton( self,1003, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_button4, 0, wx.ALL, 5 )

        self.m_checkBox5 = wx.CheckBox( self, 2004, u"5号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_checkBox5, 0, wx.ALL, 5 )

        m_comboBox5Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox5 = wx.ComboBox( self, 3004, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox5Choices, 0 )
        self.m_comboBox5.SetSelection( 0 )
        bSizer13.Add( self.m_comboBox5, 0, wx.ALL, 5 )

        self.m_button5 = wx.ToggleButton( self, 1004, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_button5, 0, wx.ALL, 5 )

        self.m_checkBox6 = wx.CheckBox( self, 2005, u"6号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_checkBox6, 0, wx.ALL, 5 )

        m_comboBox6Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox6 = wx.ComboBox( self, 3005, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox6Choices, 0 )
        self.m_comboBox6.SetSelection( 0 )
        bSizer13.Add( self.m_comboBox6, 0, wx.ALL, 5 )

        self.m_button6 = wx.ToggleButton( self,1005, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.m_button6, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer13, 1, wx.EXPAND, 5 )

        bSizer17 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox7 = wx.CheckBox( self, 2006, u"7号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_checkBox7, 0, wx.ALL, 5 )

        m_comboBox7Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox7 = wx.ComboBox( self, 3006, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox7Choices, 0 )
        self.m_comboBox7.SetSelection( 0 )
        bSizer17.Add( self.m_comboBox7, 0, wx.ALL, 5 )

        self.m_button7 = wx.ToggleButton( self, 1006, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_button7, 0, wx.ALL, 5 )

        self.m_checkBox8 = wx.CheckBox( self, 2007, u"8号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_checkBox8, 0, wx.ALL, 5 )

        m_comboBox8Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox8 = wx.ComboBox( self, 3007, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox8Choices, 0 )
        self.m_comboBox8.SetSelection( 0 )
        bSizer17.Add( self.m_comboBox8, 0, wx.ALL, 5 )

        self.m_button8 = wx.ToggleButton( self,1007, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_button8, 0, wx.ALL, 5 )

        self.m_checkBox9 = wx.CheckBox( self, 2008, u"9号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_checkBox9, 0, wx.ALL, 5 )

        m_comboBox9Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox9 = wx.ComboBox( self, 3008, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                        m_comboBox9Choices, 0 )
        self.m_comboBox9.SetSelection( 0 )
        bSizer17.Add( self.m_comboBox9, 0, wx.ALL, 5 )

        self.m_button9 = wx.ToggleButton( self, 1008, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer17.Add( self.m_button9, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer17, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox10 = wx.CheckBox( self, 2009, u"10号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_checkBox10, 0, wx.ALL, 5 )

        m_comboBox10Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox10 = wx.ComboBox( self, 3009, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox10Choices, 0 )
        self.m_comboBox10.SetSelection( 0 )
        bSizer6.Add( self.m_comboBox10, 0, wx.ALL, 5 )

        self.m_button10 = wx.ToggleButton( self, 1009, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button10, 0, wx.ALL, 5 )

        self.m_checkBox11 = wx.CheckBox( self, 2010, u"11号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_checkBox11, 0, wx.ALL, 5 )

        m_comboBox11Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox11 = wx.ComboBox( self, 3010, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox11Choices, 0 )
        self.m_comboBox11.SetSelection( 0 )
        bSizer6.Add( self.m_comboBox11, 0, wx.ALL, 5 )

        self.m_button11 = wx.ToggleButton( self, 1010, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button11, 0, wx.ALL, 5 )

        self.m_checkBox12 = wx.CheckBox( self, 2011, u"12号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_checkBox12, 0, wx.ALL, 5 )

        m_comboBox12Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox12 = wx.ComboBox( self, 3011, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox12Choices, 0 )
        self.m_comboBox12.SetSelection( 0 )
        bSizer6.Add( self.m_comboBox12, 0, wx.ALL, 5 )

        self.m_button12 = wx.ToggleButton( self,1011, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer6.Add( self.m_button12, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer6, 1, wx.EXPAND, 5 )

        bSizer8 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox13 = wx.CheckBox( self, 2012, u"13号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_checkBox13, 0, wx.ALL, 5 )

        m_comboBox13Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox13 = wx.ComboBox( self, 3012, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox13Choices, 0 )
        self.m_comboBox13.SetSelection( 0 )
        bSizer8.Add( self.m_comboBox13, 0, wx.ALL, 5 )

        self.m_button13 = wx.ToggleButton( self, 1012, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button13, 0, wx.ALL, 5 )

        self.m_checkBox14 = wx.CheckBox( self, 2013, u"14号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_checkBox14, 0, wx.ALL, 5 )

        m_comboBox14Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox14 = wx.ComboBox( self, 3013, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox14Choices, 0 )
        self.m_comboBox14.SetSelection( 0 )
        bSizer8.Add( self.m_comboBox14, 0, wx.ALL, 5 )

        self.m_button14 = wx.ToggleButton( self, 1013, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button14, 0, wx.ALL, 5 )

        self.m_checkBox15 = wx.CheckBox( self, 2014, u"15号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_checkBox15, 0, wx.ALL, 5 )

        m_comboBox15Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox15 = wx.ComboBox( self, 3014, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox15Choices, 0 )
        self.m_comboBox15.SetSelection( 0 )
        bSizer8.Add( self.m_comboBox15, 0, wx.ALL, 5 )

        self.m_button15 = wx.ToggleButton( self, 1014, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer8.Add( self.m_button15, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer8, 1, wx.EXPAND, 5 )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox16 = wx.CheckBox( self, 2015, u"16号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_checkBox16, 0, wx.ALL, 5 )

        m_comboBox16Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox16 = wx.ComboBox( self, 3015, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox16Choices, 0 )
        self.m_comboBox16.SetSelection( 0 )
        bSizer9.Add( self.m_comboBox16, 0, wx.ALL, 5 )

        self.m_button16 = wx.ToggleButton( self, 1015, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button16, 0, wx.ALL, 5 )

        self.m_checkBox17 = wx.CheckBox( self, 2016, u"17号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_checkBox17, 0, wx.ALL, 5 )

        m_comboBox17Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox17 = wx.ComboBox( self, 3016, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox17Choices, 0 )
        self.m_comboBox17.SetSelection( 0 )
        bSizer9.Add( self.m_comboBox17, 0, wx.ALL, 5 )

        self.m_button17 = wx.ToggleButton( self,1016, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button17, 0, wx.ALL, 5 )

        self.m_checkBox18 = wx.CheckBox( self, 2017, u"18号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_checkBox18, 0, wx.ALL, 5 )

        m_comboBox18Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox18 = wx.ComboBox( self, 3017, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox18Choices, 0 )
        self.m_comboBox18.SetSelection( 0 )
        bSizer9.Add( self.m_comboBox18, 0, wx.ALL, 5 )

        self.m_button18 = wx.ToggleButton( self, 1017, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer9.Add( self.m_button18, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer9, 1, wx.EXPAND, 5 )

        bSizer101 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox19 = wx.CheckBox( self, 2018, u"19号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_checkBox19, 0, wx.ALL, 5 )

        m_comboBox19Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox19 = wx.ComboBox( self, 3018, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox19Choices, 0 )
        self.m_comboBox19.SetSelection( 0 )
        bSizer101.Add( self.m_comboBox19, 0, wx.ALL, 5 )

        self.m_button19 = wx.ToggleButton( self, 1018, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_button19, 0, wx.ALL, 5 )

        self.m_checkBox20 = wx.CheckBox( self, 2019, u"20号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_checkBox20, 0, wx.ALL, 5 )

        m_comboBox20Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox20 = wx.ComboBox( self, 3019, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox20Choices, 0 )
        self.m_comboBox20.SetSelection( 0 )
        bSizer101.Add( self.m_comboBox20, 0, wx.ALL, 5 )

        self.m_button20 = wx.ToggleButton( self, 1019, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_button20, 0, wx.ALL, 5 )

        self.m_checkBox21 = wx.CheckBox( self, 2020, u"21号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_checkBox21, 0, wx.ALL, 5 )

        m_comboBox21Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox21 = wx.ComboBox( self, 3020, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox21Choices, 0 )
        self.m_comboBox21.SetSelection( 0 )
        bSizer101.Add( self.m_comboBox21, 0, wx.ALL, 5 )

        self.m_button21 = wx.ToggleButton( self, 1020, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer101.Add( self.m_button21, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer101, 1, wx.EXPAND, 5 )

        bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox22 = wx.CheckBox( self, 2021, u"22号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox22, 0, wx.ALL, 5 )

        m_comboBox22Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox22 = wx.ComboBox( self, 3021, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox22Choices, 0 )
        self.m_comboBox22.SetSelection( 0 )
        bSizer11.Add( self.m_comboBox22, 0, wx.ALL, 5 )

        self.m_button22 = wx.ToggleButton( self, 1021, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button22, 0, wx.ALL, 5 )

        self.m_checkBox23 = wx.CheckBox( self, 2022, u"23号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox23, 0, wx.ALL, 5 )

        m_comboBox23Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox23 = wx.ComboBox( self, 3022, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox23Choices, 0 )
        self.m_comboBox23.SetSelection( 0 )
        bSizer11.Add( self.m_comboBox23, 0, wx.ALL, 5 )

        self.m_button23 = wx.ToggleButton( self, 1022, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button23, 0, wx.ALL, 5 )

        self.m_checkBox24 = wx.CheckBox( self, 2023, u"24号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_checkBox24, 0, wx.ALL, 5 )

        m_comboBox24Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox24 = wx.ComboBox( self,3023, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox24Choices, 0 )
        self.m_comboBox24.SetSelection( 0 )
        bSizer11.Add( self.m_comboBox24, 0, wx.ALL, 5 )

        self.m_button24 = wx.ToggleButton( self, 1023, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer11.Add( self.m_button24, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer11, 1, wx.EXPAND, 5 )

        bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox25 = wx.CheckBox( self,2024, u"25号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_checkBox25, 0, wx.ALL, 5 )

        m_comboBox25Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox25 = wx.ComboBox( self, 3024, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox25Choices, 0 )
        self.m_comboBox25.SetSelection( 0 )
        bSizer12.Add( self.m_comboBox25, 0, wx.ALL, 5 )

        self.m_button25 = wx.ToggleButton( self, 1024, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button25, 0, wx.ALL, 5 )

        self.m_checkBox26 = wx.CheckBox( self, 2025, u"26号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_checkBox26, 0, wx.ALL, 5 )

        m_comboBox26Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox26 = wx.ComboBox( self, 3024, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox26Choices, 0 )
        self.m_comboBox26.SetSelection( 0 )
        bSizer12.Add( self.m_comboBox26, 0, wx.ALL, 5 )

        self.m_button26 = wx.ToggleButton( self, 1025, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button26, 0, wx.ALL, 5 )

        self.m_checkBox27 = wx.CheckBox( self, 2026, u"27号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_checkBox27, 0, wx.ALL, 5 )

        m_comboBox27Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox27 = wx.ComboBox( self, 3026, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox27Choices, 0 )
        self.m_comboBox27.SetSelection( 0 )
        bSizer12.Add( self.m_comboBox27, 0, wx.ALL, 5 )

        self.m_button27 = wx.ToggleButton( self, 1026, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer12.Add( self.m_button27, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer12, 1, wx.EXPAND, 5 )

        bSizer131 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox28 = wx.CheckBox( self, 2027, u"28号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.m_checkBox28, 0, wx.ALL, 5 )

        m_comboBox28Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox28 = wx.ComboBox( self, 3027, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox28Choices, 0 )
        self.m_comboBox28.SetSelection( 0 )
        bSizer131.Add( self.m_comboBox28, 0, wx.ALL, 5 )

        self.m_button28 = wx.ToggleButton( self, 1027, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.m_button28, 0, wx.ALL, 5 )

        self.m_checkBox29 = wx.CheckBox( self, 2028, u"29号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.m_checkBox29, 0, wx.ALL, 5 )

        m_comboBox29Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox29 = wx.ComboBox( self, 3028, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox29Choices, 0 )
        self.m_comboBox29.SetSelection( 0 )
        bSizer131.Add( self.m_comboBox29, 0, wx.ALL, 5 )

        self.m_button29 = wx.ToggleButton( self, 1028, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.m_button29, 0, wx.ALL, 5 )

        self.m_checkBox30 = wx.CheckBox( self, 2029, u"30号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.m_checkBox30, 0, wx.ALL, 5 )

        m_comboBox30Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox30 = wx.ComboBox( self, 3029, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox30Choices, 0 )
        self.m_comboBox30.SetSelection( 0 )
        bSizer131.Add( self.m_comboBox30, 0, wx.ALL, 5 )

        self.m_button30 = wx.ToggleButton( self, 1029, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer131.Add( self.m_button30, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer131, 1, wx.EXPAND, 5 )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_checkBox31 = wx.CheckBox( self, 2030, u"31号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_checkBox31, 0, wx.ALL, 5 )

        m_comboBox31Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox31 = wx.ComboBox( self, 3030, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox31Choices, 0 )
        self.m_comboBox31.SetSelection( 0 )
        bSizer14.Add( self.m_comboBox31, 0, wx.ALL, 5 )

        self.m_button31 = wx.ToggleButton( self, 1030, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button31, 0, wx.ALL, 5 )

        self.m_checkBox32 = wx.CheckBox( self, 2031, u"32号定时", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_checkBox32, 0, wx.ALL, 5 )

        m_comboBox32Choices = [u"30分钟", u"1小时", u"1小时30分", u"2小时", u"2小时30分", u"3小时", u"3小时30分", u"4小时", u"4小时30分",
                               u"5小时", u"5小时30分", u"6小时", u"6小时30分", u"7小时", u"7小时30分", u"8小时", u"8小时30分", u"9小时",
                               u"9小时30分", u"10小时", u"10小时30分", u"11小时", u"11小时30分", u"12小时",u"12小时30分", u"13小时",u"13小时30分", u"14小时",  u"14小时30分",u"15小时",
                               u"15小时30分",u"16小时",u"16小时30分", u"17小时"]
        self.m_comboBox32 = wx.ComboBox( self, 3031, u"30分钟", wx.DefaultPosition, wx.DefaultSize,
                                         m_comboBox32Choices, 0 )
        self.m_comboBox32.SetSelection( 0 )
        bSizer14.Add( self.m_comboBox32, 0, wx.ALL, 5 )

        self.m_button32 = wx.ToggleButton( self, 1031, u"状态：关 定时：", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer14.Add( self.m_button32, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer14, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()
        self.m_statusBar = self.CreateStatusBar( 3, wx.STB_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_button_find_com.Bind( wx.EVT_BUTTON, self.find_com )
        self.m_button_open_com.Bind( wx.EVT_BUTTON, self.open_com )
        self.m_button_connection_ser.Bind( wx.EVT_BUTTON, self.connetion_ser )
        self.m_button1.Bind( wx.EVT_TOGGLEBUTTON, self.btn1_event )
        self.m_button2.Bind( wx.EVT_TOGGLEBUTTON, self.btn2_event )
        self.m_button3.Bind( wx.EVT_TOGGLEBUTTON, self.btn3_event )
        self.m_button4.Bind( wx.EVT_TOGGLEBUTTON, self.btn4_event )
        self.m_button5.Bind( wx.EVT_TOGGLEBUTTON, self.btn5_event )
        self.m_button6.Bind( wx.EVT_TOGGLEBUTTON, self.btn6_event )
        self.m_button7.Bind( wx.EVT_TOGGLEBUTTON, self.btn7_event )
        self.m_button8.Bind( wx.EVT_TOGGLEBUTTON, self.btn8_event )
        self.m_button9.Bind( wx.EVT_TOGGLEBUTTON, self.btn9_event )
        self.m_button10.Bind( wx.EVT_TOGGLEBUTTON, self.btn10_event )
        self.m_button11.Bind( wx.EVT_TOGGLEBUTTON, self.btn11_event )
        self.m_button12.Bind( wx.EVT_TOGGLEBUTTON, self.btn12_event )
        self.m_button13.Bind( wx.EVT_TOGGLEBUTTON, self.btn13_event )
        self.m_button14.Bind( wx.EVT_TOGGLEBUTTON, self.btn14_event )
        self.m_button15.Bind( wx.EVT_TOGGLEBUTTON, self.btn15_event )
        self.m_button16.Bind( wx.EVT_TOGGLEBUTTON, self.btn16_event )
        self.m_button17.Bind( wx.EVT_TOGGLEBUTTON, self.btn17_event )
        self.m_button18.Bind( wx.EVT_TOGGLEBUTTON, self.btn18_event )
        self.m_button19.Bind( wx.EVT_TOGGLEBUTTON, self.btn19_event )
        self.m_button20.Bind( wx.EVT_TOGGLEBUTTON, self.btn20_event )
        self.m_button21.Bind( wx.EVT_TOGGLEBUTTON, self.btn21_event )
        self.m_button22.Bind( wx.EVT_TOGGLEBUTTON, self.btn22_event )
        self.m_button23.Bind( wx.EVT_TOGGLEBUTTON, self.btn23_event )
        self.m_button24.Bind( wx.EVT_TOGGLEBUTTON, self.btn24_event )
        self.m_button25.Bind( wx.EVT_TOGGLEBUTTON, self.btn25_event )
        self.m_button26.Bind( wx.EVT_TOGGLEBUTTON, self.btn26_event )
        self.m_button27.Bind( wx.EVT_TOGGLEBUTTON, self.btn27_event )
        self.m_button28.Bind( wx.EVT_TOGGLEBUTTON, self.btn28_event )
        self.m_button29.Bind( wx.EVT_TOGGLEBUTTON, self.btn29_event )
        self.m_button30.Bind( wx.EVT_TOGGLEBUTTON, self.btn30_event )
        self.m_button31.Bind( wx.EVT_TOGGLEBUTTON, self.btn31_event )
        self.m_button32.Bind( wx.EVT_TOGGLEBUTTON, self.btn32_event )
        self.sw_val = {}#缓存开关状态
        self.button_color_init()
        self.timer=wx.Timer(self)
        self.timer_edp = wx.Timer( self )
        self.Bind( wx.EVT_TIMER, self.on_timer, self.timer )  # 绑定一个定时器事件
        self.Bind( wx.EVT_TIMER, self._edp_data_get, self.timer_edp)

        self.serial_is_open=False#串口连接指示
        self.web_is_ava=False#联网指示
        self.web_error_cnt=0#
        self.web_post_cnt = 0  #

        #self.socket_cnt=False#socket连接指示
        #self.socket_timeout=[0,0]#连接指示位+超时时间
        #self.edp_cmd_order=True
        self.serial_cnt=0
        menuBar = wx.MenuBar()#菜单
        menu = wx.Menu()
        self._menu_net_conf = menu.Append( 0, u'网络配置' )  #
        self._menu_debug_view = menu.Append(1,u'操作日志查看')
        menuBar.Append( menu, u'设置')
        self.Bind( wx.EVT_MENU, self.menu_net_conf, self._menu_net_conf )
        self.Bind( wx.EVT_MENU, self.debug_view, self._menu_debug_view )
        self.SetMenuBar( menuBar )

        self.q_input=q_in#外部数据输入
        self.q_output=q_out#界面数据传出
        self._serial=ser#串口

        self.edp_qin=eqin
        self.edp_qout=eqout

        self.DEVICEID=''
        self.APIKEY=''

        #self.rec_thread = Thread( target=self.edp_rec_msg_handle, args=(self.client,self.sock) )
        # 设置成守护线程
        #self.rec_thread.setDaemon( True )
        self.timer.Start( 900 )  # 设定时间间隔为900毫秒,并启动定时器,刷新按键显示
        self.timer_edp.Start( 1500 )
        #self.rec_thread.start()
    def __del__(self):
        pass
    def menu_net_conf(self, event):#保存网络配置信息
        #print("twtwtwt")
        #cfgpath
        #_argv=""
        curpath = os.path.dirname( os.path.realpath( __file__ ) )
        cfgpath = os.path.join( curpath, "cfg.ini" )
        # 创建管理对象
        conf = configparser.ConfigParser()
        try:
            # 先读出来
            conf.read( cfgpath, encoding="utf-8" )
        except:
            self.display_debug_msg(u"读取配置文件出错！")
            self.DEVICEID = conf.get( "NET_CONF", "DEVID" )
            self.APIKEY = conf.get( "NET_CONF", "APIKEY" )

        # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
        self.dlg=netDialog(self,self.DEVICEID,self.APIKEY)
        if self.dlg.ShowModal() == wx.ID_OK:
            #print(self.dlg.GetText())
            _argv=self.dlg.GetText()
            d=_argv.split( '|' )
            self.DEVICEID=d[0]
            self.APIKEY=d[1]
            try:
               conf.set( "NET_CONF", "DEVID", d[0] )
               conf.set( "NET_CONF", "APIKEY",d[1] )
               conf.write( open( cfgpath, "r+", encoding="utf-8" ) )  # r+模式
               self.display_debug_msg( u"云平台信息配置成功！" )
            except:
               conf.add_section( "NET_CONF" )
               conf.set( "NET_CONF", "DEVID", d[0] )
               conf.set( "NET_CONF", "APIKEY", d[1] )
               conf.write( open( cfgpath, "r+", encoding="utf-8" ) )  # r+模式
               self.display_debug_msg(u"云平台信息配置成功！！")
        self.dlg.Destroy()
    def debug_view(self,event):
        self.dlgv=DebugView(self)
        self.dlgv.Set_Text(self.m_textCtrl1.GetValue())
        if self.dlgv.ShowModal()==wx.ID_OK:
            self.m_textCtrl1.Clear()

        #elif self.dlgv.ShowModal()==wx.ID_CANCEL:
    #def net_msg_proc(self):

        self.dlgv.Destroy()

    def button_color_init(self):
        for i in range(32):
            wx.ToggleButton.FindWindowById(1000+i).SetBackgroundColour(colour='green')
            self.sw_val.update({str(i+1): 0})#初始化开关值为0
    def on_timer(self,evt):#

        now_time = datetime.datetime.now().strftime( '%Y/%m/%d-%H/%M/%S' )
        self.m_statusBar.SetStatusText(now_time , 2 )

        if self.serial_is_open is True:
            self.m_statusBar.SetStatusText(u"端口已打开 "+"设备数据接收计数："+str(self.serial_cnt),0)
        else:
            self.m_statusBar.SetStatusText(u"端口已关闭",0)

        while self.q_input.empty() is not True:#输入队列非空
           #数据格式如下：
           #number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _str=self.q_input.get(block=True,timeout=1)
            data_arry=_str.split(',')
               #wx.FindWindowById
            #_btn=""
            #if data_arry[0] is "67":#错误码
                #67,num(1-32),flag(1成功，0失败)，
             #   if data_arry[1] is
            if data_arry[1] == "1":#定时
                if data_arry[2] == "1":#打开状态

                    wx.ToggleButton.FindWindowById( 999+int(data_arry[0]) ).SetLabelText(str(datetime.timedelta(seconds=int(data_arry[3])))+u"后关")
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour(colour='red')
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetValue(True)
                    self.sw_val[data_arry[0]] = 1

                   #wx.Button.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour(colour=(255, 0, 0, 255))
                else:
                    self.sw_val[data_arry[0]]=0
                    #self.m_button1.SetLabelText( u"状态：关闭" )
                    wx.ToggleButton.FindWindowById(999+int(data_arry[0])).SetLabelText( u"状态：关闭" )
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetValue( False )
                    #wx.Button.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour(colour=(212, 208, 200, 255))
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour(colour='green')
            elif data_arry[1] == "0":
                if data_arry[2] == "1":#打开状态
                    self.sw_val[data_arry[0]] = 1
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetValue( True )
                    wx.ToggleButton.FindWindowById( 999+int(data_arry[0]) ).SetLabelText(u"已打开")
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour( colour='red' )
                   # wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour( colour=(255, 0, 0, 255) )

                else:
                    self.sw_val[data_arry[0]] = 0
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetValue( False )
                    wx.ToggleButton.FindWindowById( 999+int(data_arry[0]) ).SetLabelText( u"已关闭" )
                    wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour( colour='green' )
                    #wx.ToggleButton.FindWindowById( 999 + int( data_arry[0] ) ).SetBackgroundColour( colour=(255,  208, 200, 255) )
            if data_arry[0] == "67":#串口接收数据指示
                self.serial_cnt=int(data_arry[3])



    def Port_List(self):# 获取COM号列表
       Com_List = []
       port_list = list( serial.tools.list_ports.comports() )
       for port in port_list:
            Com_List.append( port[0] )
       return Com_List

    def display_debug_msg(self,msg):
        #显示调试信息
        now_time = datetime.datetime.now().strftime( 'LOG:%Y-%m-%d-%H-%M' )
        self.m_textCtrl1.write( now_time + msg+"\n")
            # print("ser")
    # Virtual event handlers, overide them in your derived class
    def find_com(self, event):
        event.Skip()
        self.display_debug_msg(u"查找端口···")
        self.m_comboBox0.Clear()
        self.m_comboBox0.Append(self.Port_List())
        self.display_debug_msg( u"查找完成。" )
    def open_com(self, event):
        event.Skip()
        self.display_debug_msg( u"正在打开端口···" )
        if not self._serial.isOpen():
            try:
                self._serial.timeout = 0.5
                self._serial.xonxoff = 0
                # self.ser.parity = serial.PARITY_NONE
                self._serial.port = self.m_comboBox0.GetValue()
                self._serial.baudrate = 9600
                self._serial.open()
                self.serial_is_open=True

            except Exception:
                self.display_debug_msg(u"串口打开失败")
            else:
            #self.display_debug_msg( u"101-182关闭串口")
                self.m_button_open_com.SetLabelText(u"关闭端口")
                #self.serial_cnt=0
                #print(self.m_button_open_com.GetBackgroundColour())
                self.m_button_open_com.SetBackgroundColour(colour=(255, 0, 0, 255))
        else:
            self._serial.close()
            self.serial_is_open=False
            while self._serial.isOpen(): pass
            self.m_button_open_com.SetLabelText( u"打开端口" )
            self.m_textCtrl1.Clear()
            self.m_button_open_com.SetBackgroundColour( colour=(212, 208, 200, 255))
        self.serial_cnt = 0



    def _edp_data_get(self,evt):
        s=""
        k=0
        #wx.ComboBox.
        #print( wx.ComboBox.FindWindowById() )
        for i in range(32):
            if self.sw_val[str(k+1)]  == 1:
                s=s+"1:"
            elif self.sw_val[str(k+1)] == 0:
                s=s+"0:"
            k+=1

        #print(s[:-1])
        self.edp_qout.put( s[:-1], block=True, timeout=1 )
        while self.edp_qin.empty() is not True:
            _str = self.edp_qin.get( block=True, timeout=1 )
            data_arry = _str.split( ':' )
            if data_arry[0] == "CONN_CNNT":#socket已连接
                self.m_statusBar.SetStatusText(u"网络连接成功", 1 )
            elif data_arry[0].isdigit():
                if data_arry[1]=="0":#关闭
                    self.q_output.put( data_arry[0]+",0,0,0", block=False )
                    self.display_debug_msg( u"注意--正在远程关闭通道"+data_arry[0] )
                elif data_arry[1]=="1":
                     if wx.CheckBox.FindWindowById(1999+int(data_arry[0])).IsChecked():#定时开启
                         #wx.CheckBox.IsChecked()
                         _temp = str( (1 + wx.ComboBox.FindWindowById(2999+int(data_arry[0])).FindString( wx.ComboBox.FindWindowById(2999+int(data_arry[0])).GetValue() )) * 30 * 60 )
                         self.q_output.put( data_arry[0] + ",1,1,"+_temp, block=False )
                         self.display_debug_msg( u"注意--正在远程定时通道" + data_arry[0] )
                     else:
                         self.q_output.put( data_arry[0] + ",0,1,0" , block=False )
                         self.display_debug_msg( u"注意--正在远程打开通道" + data_arry[0] )
            elif data_arry[0] == "CONN_CLOSE":
                self.m_statusBar.SetStatusText( u"网络连接断开:"+data_arry[1], 1 )
            else:continue


    def connetion_ser(self, event):
        event.Skip()
        if  self.web_is_ava is False:
            self.web_is_ava = True
            self.web_error_cnt=0
            self.display_debug_msg( u"设置允许连接OneNet···" )
            self.m_button_connection_ser.SetBackgroundColour(colour='red')
            self.m_button_connection_ser.SetLabelText(u"已允许联网")
            self.edp_qout.put("send_cnn:none",block=True,timeout=1)
        else:
            self.web_is_ava = False
            self.edp_qout.put("cnn_close:none",block=True,timeout=1)
            self.display_debug_msg( u"设置禁止连接OneNet···" )
            self.m_button_connection_ser.SetBackgroundColour(colour=(212, 208, 200, 255) )
            self.m_button_connection_ser.SetLabelText( u"已禁止联网" )
    def btn1_event(self, event):
        event.Skip()
        #print(self.m_button1.GetValue())
        #self.m_button1.SetLabelText("SAS")
        _cmd="1,"
        if self.m_checkBox1.IsChecked():#开启定时
           # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd=_cmd+"1,"
        else:
            _cmd=_cmd+"0,"
        if self.m_button1.GetValue() == False:#按键已被打开，现在关闭
            #print(u"红色")
            #打开状态 Queue.put(item, [block[, timeout]])
            _cmd=_cmd+"0,0"
            #self.m_checkBox1.Enable( True )
            self.q_output.put(_cmd, block=False)
            #print(_cmd)
            self.display_debug_msg(u"正在发送通道1关闭指令·····")
        else :#按键被关闭现在打开
            #print(u"其他色")
            #关闭状态，现在要打开
            _cmd=_cmd+"1,"
            if self.m_checkBox1.IsChecked():
                #self.m_checkBox1.Enable(False)
                _temp=str((1+self.m_comboBox1.FindString(self.m_comboBox1.GetValue()))*30*60)
                #30m 30*2m 30*3m
                _cmd=_cmd+_temp
                #print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
           # print( _cmd )
            self.display_debug_msg( u"正在发送通道1打开指令·····" )
    def btn2_event(self, event):
        event.Skip()
        _cmd = "2,"
        if self.m_checkBox2.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button2.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道2关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox2.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox2.FindString( self.m_comboBox2.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道2打开指令·····" )
    def btn3_event(self, event):
        event.Skip()
        _cmd = "3,"
        if self.m_checkBox3.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button3.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道3关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox3.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox3.FindString( self.m_comboBox3.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道3打开指令·····" )
    def btn4_event(self, event):
        event.Skip()
        _cmd = "4,"
        if self.m_checkBox4.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button4.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道4关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox4.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox4.FindString( self.m_comboBox4.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道4打开指令·····" )
    def btn5_event(self, event):
        event.Skip()
        _cmd = "5,"
        if self.m_checkBox5.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button5.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道5关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox5.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox5.FindString( self.m_comboBox5.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道5打开指令·····" )
    def btn6_event(self, event):
        event.Skip()
        _cmd = "6,"
        if self.m_checkBox6.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button6.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道6关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox6.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox6.FindString( self.m_comboBox6.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道6打开指令·····" )
    def btn7_event(self, event):
        event.Skip()
        _cmd = "7,"
        if self.m_checkBox7.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button7.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道7关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox7.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox7.FindString( self.m_comboBox7.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道7打开指令·····" )
    def btn8_event(self, event):
        event.Skip()
        _cmd = "8,"
        if self.m_checkBox8.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button8.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道8关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox8.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox8.FindString( self.m_comboBox8.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道8打开指令·····" )
    def btn9_event(self, event):
        event.Skip()
        _cmd = "9,"
        if self.m_checkBox9.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button9.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道9关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox9.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox9.FindString( self.m_comboBox9.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道9打开指令·····" )
    def btn10_event(self, event):
        event.Skip()
        _cmd = "10,"
        if self.m_checkBox10.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button10.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道10关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox10.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox10.FindString( self.m_comboBox10.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道10打开指令·····" )
    def btn11_event(self, event):
        event.Skip()
        _cmd = "11,"
        if self.m_checkBox11.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button11.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道11关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox11.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox11.FindString( self.m_comboBox11.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道11打开指令·····" )
    def btn12_event(self, event):
        event.Skip()
        _cmd = "12,"
        if self.m_checkBox12.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button12.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道12关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox12.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox12.FindString( self.m_comboBox12.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道12打开指令·····" )
    def btn13_event(self, event):
        event.Skip()
        _cmd = "13,"
        if self.m_checkBox13.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button13.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道13关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox13.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox13.FindString( self.m_comboBox13.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道13打开指令·····" )
    def btn14_event(self, event):
        event.Skip()
        _cmd = "14,"
        if self.m_checkBox14.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button14.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道14关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox14.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox14.FindString( self.m_comboBox14.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道14打开指令·····" )
    def btn15_event(self, event):
        event.Skip()
        _cmd = "15,"
        if self.m_checkBox15.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button15.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道15关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox15.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox15.FindString( self.m_comboBox15.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道15打开指令·····" )
    def btn16_event(self, event):
        event.Skip()
        _cmd = "16,"
        if self.m_checkBox16.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button16.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道16关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox16.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox16.FindString( self.m_comboBox16.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道16打开指令·····" )
    def btn17_event(self, event):
        event.Skip()
        _cmd = "17,"
        if self.m_checkBox17.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button17.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道17关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox17.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox17.FindString( self.m_comboBox17.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道17打开指令·····" )
    def btn18_event(self, event):
        event.Skip()
        _cmd = "18,"
        if self.m_checkBox18.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button18.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道18关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox18.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox18.FindString( self.m_comboBox18.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道18打开指令·····" )
    def btn19_event(self, event):
        event.Skip()
        _cmd = "19,"
        if self.m_checkBox19.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button19.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道19关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox19.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox19.FindString( self.m_comboBox19.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道19打开指令·····" )
    def btn20_event(self, event):
        event.Skip()
        _cmd = "20,"
        if self.m_checkBox20.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button20.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道20关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox20.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox20.FindString( self.m_comboBox20.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道20打开指令·····" )
    def btn21_event(self, event):
        event.Skip()
        _cmd = "21,"
        if self.m_checkBox20.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button21.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道21关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox21.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox21.FindString( self.m_comboBox21.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道21打开指令·····" )
    def btn22_event(self, event):
        event.Skip()
        _cmd = "22,"
        if self.m_checkBox22.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button22.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道22关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox22.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox22.FindString( self.m_comboBox22.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道22打开指令·····" )
    def btn23_event(self, event):
        event.Skip()
        _cmd = "23,"
        if self.m_checkBox23.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button23.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道23关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox23.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox23.FindString( self.m_comboBox23.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道23打开指令·····" )
    def btn24_event(self, event):
        event.Skip()
        _cmd = "24,"
        if self.m_checkBox24.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button24.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道24关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox24.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox24.FindString( self.m_comboBox24.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道24打开指令·····" )
    def btn25_event(self, event):
        event.Skip()
        _cmd = "25,"
        if self.m_checkBox25.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button25.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道25关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox25.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox25.FindString( self.m_comboBox25.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道25打开指令·····" )
    def btn26_event(self, event):
        event.Skip()
        _cmd = "26,"
        if self.m_checkBox26.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button26.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道26关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox26.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox26.FindString( self.m_comboBox26.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道26打开指令·····" )
    def btn27_event(self, event):
        event.Skip()
        _cmd = "27,"
        if self.m_checkBox27.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button27.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道27关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox27.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox27.FindString( self.m_comboBox27.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道27打开指令·····" )
    def btn28_event(self, event):
        event.Skip()
        _cmd = "28,"
        if self.m_checkBox28.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button28.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道28关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox28.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox28.FindString( self.m_comboBox28.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道28打开指令·····" )
    def btn29_event(self, event):
        event.Skip()
        _cmd = "29,"
        if self.m_checkBox29.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button29.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道29关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox29.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox29.FindString( self.m_comboBox29.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道29打开指令·····" )
    def btn30_event(self, event):
        event.Skip()
        _cmd = "30,"
        if self.m_checkBox30.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button30.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道30关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox30.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox30.FindString( self.m_comboBox30.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道30打开指令·····" )
    def btn31_event(self, event):
        event.Skip()
        _cmd = "31,"
        if self.m_checkBox31.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button31.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道31关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox31.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox31.FindString( self.m_comboBox31.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道31打开指令·····" )
    def btn32_event(self, event):
        event.Skip()
        _cmd = "32,"
        if self.m_checkBox32.IsChecked():  # 开启定时
            # number(1-32),timer_flag(定时标志，1定时，0非定时),key_flag(1打开状态，0关闭)，time(倒计时秒)
            _cmd = _cmd + "1,"
        else:
            _cmd = _cmd + "0,"
        if self.m_button32.GetValue() == False:  # 按键已被打开，现在关闭
            # print(u"红色")
            # 打开状态 Queue.put(item, [block[, timeout]])
            _cmd = _cmd + "0,0"
            # self.m_checkBox1.Enable( True )
            self.q_output.put( _cmd, block=False )
            # print(_cmd)
            self.display_debug_msg( u"正在发送通道32关闭指令·····" )
        else:  # 按键被关闭现在打开
            # print(u"其他色")
            # 关闭状态，现在要打开
            _cmd = _cmd + "1,"
            if self.m_checkBox32.IsChecked():
                # self.m_checkBox1.Enable(False)
                _temp = str( (1 + self.m_comboBox32.FindString( self.m_comboBox32.GetValue() )) * 30 * 60 )
                # 30m 30*2m 30*3m
                _cmd = _cmd + _temp
                # print(_temp)
            else:
                _cmd = _cmd + "0"
            self.q_output.put( _cmd, block=False )
            # print( _cmd )
            self.display_debug_msg( u"正在发送通道32打开指令·····" )

