# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jan 23 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc


###########################################################################
## Class netDialog1
###########################################################################

class netDialog( wx.Dialog ):
    def __init__(self, parent):
        wx.Dialog.__init__( self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                            size=wx.Size( 330, 221 ), style=wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.Size( 330, 221 ) )

        sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"网络参数配置：" ), wx.VERTICAL )

        self.m_staticText1 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"设备ID：", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        sbSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.DefaultSize, 0 )
        sbSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        self.m_staticText2 = wx.StaticText( sbSizer1.GetStaticBox(), wx.ID_ANY, u"APIKEY：", wx.DefaultPosition,
                                            wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        sbSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( sbSizer1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition,
                                        wx.Size( 250, -1 ), 0 )
        sbSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button_save = wx.Button( sbSizer1.GetStaticBox(), wx.ID_OK, u"保存", wx.DefaultPosition, wx.DefaultSize,
                                        0 )
        bSizer2.Add( self.m_button_save, 0, wx.ALL, 5 )

        self.m_button_back = wx.Button( sbSizer1.GetStaticBox(), wx.ID_CANCEL, u"取消", wx.DefaultPosition, wx.DefaultSize,
                                        0 )
        bSizer2.Add( self.m_button_back, 0, wx.ALL, 5 )

        sbSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        self.SetSizer( sbSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

        # Connect Events
       # self.m_button_save.Bind( wx.EVT_BUTTON, self.save_msg )
       # self.m_button_back.Bind( wx.EVT_BUTTON, self.cancal_msg )

    def __del__(self):
        pass
    def GetText(self):
        return (self.m_textCtrl1.GetValue()+"|"+self.m_textCtrl2.GetValue())
    # Virtual event handlers, overide them in your derived class
   # def save_msg(self, event):
     #   event.Skip()


   # def cancal_msg(self, event):
    #    event.Skip()


