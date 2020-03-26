import wx
import wikipedia
import wolframalpha

class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None,
            pos=wx.DefaultPosition, size=wx.Size(450, 100),
            style=wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |
             wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title="Assistant Project")
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText(panel,
        label="Hello I am here to help you. How can I help you?")
        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER,size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        user_input = self.txt.GetValue()
        user_input = user_input.lower()
        try:
            app_id = "77QEU8-G37HX8LK6V"
            client = wolframalpha.Client(app_id)
            result = client.query(user_input)
            answer = next(result.results).text
            print (answer)
        except:
            user_input = user_input.split(" ")
            user_input = " ".join(user_input[:])
            answer = wikipedia.summary(user_input)
            print (answer)

if __name__ == "__main__":
    app = wx.App(True)
    frame = MyFrame()
    app.MainLoop()
