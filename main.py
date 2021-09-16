#!/usr/bin/env python3
# coding=utf-8

import wx
import wx.xrc

from MyFrame import MyFrame


class Frame(MyFrame):

    # Virtual event handlers, override them in your derived class
    def solve(self, event):
        try:
            x = float(self.enter_x.GetValue())
            if x <= 5:
                a = float(self.enter_a.GetValue())
                b = float(self.enter_b.GetValue())
                c = float(self.enter_c.GetValue())
                d = float(self.enter_d.GetValue())
                y = (a ** 2 * c + b ** 2 - d) / x
            else:
                y = x ** 2 + 5
            self.label_answer.SetForegroundColour((0, 0, 0))
            self.label_answer.SetLabelText('Ответ: ' + str(format(y, '.2f')))
        except ValueError:
            self.label_answer.SetForegroundColour((255, 0, 0))
            self.label_answer.SetLabelText('Ошибка!')

    def clear(self, event):
        self.enter_x.Clear()
        self.enter_a.Clear()
        self.enter_b.Clear()
        self.enter_c.Clear()
        self.enter_d.Clear()
        self.label_answer.SetForegroundColour((0, 0, 0))
        self.label_answer.SetLabelText('Ответ: y =')


def main():
    app = wx.App(False)
    frame = Frame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
