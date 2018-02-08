#!/usr/bin/env python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello World")
sizer = wx.BoxSizer(wx.HORIZONTAL)

menu = wx.Menu()
menu.Append(wx.ID_ABOUT, 'About')

search = wx.SearchCtrl(frame)
search.ShowCancelButton(True)
search.SetMenu(menu)

sizer.Add(search, 0)
frame.SetSizer(sizer)
frame.SetAutoLayout(1)
sizer.Fit(frame)
frame.Show()
app.MainLoop()
