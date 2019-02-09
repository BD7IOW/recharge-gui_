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
## Class MyDialog1
###########################################################################

class DebugView( wx.Dialog ):
    def __init__(self, parent):
        wx.Dialog.__init__( self, parent, id=wx.ID_ANY, title=wx.EmptyString, pos=wx.DefaultPosition,
                            size=wx.Size( 500, 569 ), style=wx.DEFAULT_DIALOG_STYLE )

        self.SetSizeHints( wx.DefaultSize, wx.Size( 500, 600 ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, style=wx.TE_MULTILINE|wx.TE_RICH|wx.TE_PROCESS_ENTER )
        self.m_textCtrl1.SetMinSize( wx.Size( 500, 500 ) )

        bSizer1.Add( self.m_textCtrl1, 0, wx.ALL, 5 )

        bSizer2 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button3 = wx.Button( self, wx.ID_OK, u"清除", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button3, 0, wx.ALL, 5 )

        self.m_button4 = wx.Button( self, wx.ID_CANCEL, u"返回", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer2.Add( self.m_button4, 0, wx.ALL, 5 )

        bSizer1.Add( bSizer2, 1, wx.EXPAND, 5 )

        self.SetSizer( bSizer1 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__(self):
        pass

    def Set_Text(self,msg):
        t=msg.split( 'LOG:' )
        for i in t:
           self.m_textCtrl1.write(i+"\n")

