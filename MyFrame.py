#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import wx
import wx.xrc


class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Визуальная программа wxPython", pos=wx.DefaultPosition,
                          size=wx.Size(796, 330), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)
        self.SetIcon(wx.Icon("logo.jpg"))
        self.SetSizeHints(wx.Size(796, 330), wx.Size(796, 330))
        style = self.GetWindowStyle()
        self.SetWindowStyle(style & (~wx.CLOSE_BOX) & (~wx.MAXIMIZE_BOX))
        self.Refresh()

        Form = wx.BoxSizer(wx.VERTICAL)

        Variables = wx.GridBagSizer()
        Variables.SetFlexibleDirection(wx.BOTH)
        Variables.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.label_info = wx.StaticText(self, wx.ID_ANY, u"BMK01\n___________\nPython 3.9\n+\nwxPython",
                                        wx.Point(-1, -1), wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL)
        self.label_info.Wrap(-1)

        self.label_info.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                        "Cascadia Mono SemiLight"))

        Variables.Add(self.label_info, wx.GBPosition(0, 2), wx.GBSpan(5, 1),
                      wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.label_x = wx.StaticText(self, wx.ID_ANY, u"X =", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_x.Wrap(-1)

        self.label_x.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.label_x, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.ALL, 9)

        self.enter_x = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.enter_x.SetMaxLength(15)
        self.enter_x.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.enter_x, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.TOP, 5)

        self.label_a = wx.StaticText(self, wx.ID_ANY, u"A =", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_a.Wrap(-1)

        self.label_a.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.label_a, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.ALL, 9)

        self.enter_a = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.enter_a.SetMaxLength(15)
        self.enter_a.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.enter_a, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.TOP, 5)

        self.label_b = wx.StaticText(self, wx.ID_ANY, u"B =", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_b.Wrap(-1)

        self.label_b.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.label_b, wx.GBPosition(2, 0), wx.GBSpan(1, 1), wx.ALL, 9)

        self.enter_b = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.enter_b.SetMaxLength(15)
        self.enter_b.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.enter_b, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.TOP, 5)

        self.label_c = wx.StaticText(self, wx.ID_ANY, u"C =", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_c.Wrap(-1)

        self.label_c.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.label_c, wx.GBPosition(3, 0), wx.GBSpan(1, 1), wx.ALL, 9)

        self.enter_c = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.enter_c.SetMaxLength(15)
        self.enter_c.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.enter_c, wx.GBPosition(3, 1), wx.GBSpan(1, 1), wx.TOP, 5)

        self.label_d = wx.StaticText(self, wx.ID_ANY, u"D =", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_d.Wrap(-1)

        self.label_d.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.label_d, wx.GBPosition(4, 0), wx.GBSpan(1, 1), wx.ALL, 9)

        self.enter_d = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER)
        self.enter_d.SetMaxLength(15)
        self.enter_d.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                     "Cascadia Mono SemiLight"))

        Variables.Add(self.enter_d, wx.GBPosition(4, 1), wx.GBSpan(1, 1), wx.TOP, 5)

        self.image_variant = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap(u"1variant.png", wx.BITMAP_TYPE_ANY),
                                             wx.Point(0, 0), wx.Size(-1, -1), 0)
        self.image_variant.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
        self.image_variant.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))

        Variables.Add(self.image_variant, wx.GBPosition(0, 3), wx.GBSpan(5, 1), wx.ALL, 5)

        Form.Add(Variables, 1, wx.ALL, 5)

        Buttons = wx.BoxSizer()

        self.Solve = wx.Button(self, wx.ID_ANY, u"Решить", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Solve.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                   "Cascadia Mono SemiLight"))

        Buttons.Add(self.Solve, 0, wx.ALL, 5)

        self.Clear = wx.Button(self, wx.ID_ANY, u"Очистить", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Clear.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                   "Cascadia Mono SemiLight"))

        Buttons.Add(self.Clear, 0, wx.ALL, 5)

        self.Exit = wx.Button(self, wx.ID_ANY, u"Выйти", wx.DefaultPosition, wx.DefaultSize, 0)
        self.Exit.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                  "Cascadia Mono SemiLight"))

        Buttons.Add(self.Exit, 0, wx.ALL, 5)

        Form.Add(Buttons, 1, wx.ALIGN_CENTER_HORIZONTAL | wx.ALL, 5)

        self.label_answer = wx.StaticText(self, wx.ID_ANY, u"Ответ: y =", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_answer.Wrap(-1)

        self.label_answer.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False,
                                          "Cascadia Mono SemiLight"))

        Form.Add(self.label_answer, 0, wx.ALL, 10)

        self.SetSizer(Form)
        self.Layout()

        self.Centre()

        # Connect Events
        self.Solve.Bind(wx.EVT_BUTTON, self.solve)
        self.Clear.Bind(wx.EVT_BUTTON, self.clear)
        self.Exit.Bind(wx.EVT_BUTTON, exit)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def solve(self, event):
        event.Skip()

    def clear(self, event):
        event.Skip()
