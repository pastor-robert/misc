#!/usr/bin/env python
import wx

app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World") # A Frame is a top-level window.
#wx.TextCtrl(frame, style=wx.TE_MULTILINE)
s=wx.SearchCtrl(frame, name="BAR")
s.ShowCancelButton(True)
frame.Show(True)     # Show the frame.
app.MainLoop()
