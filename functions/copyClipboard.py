def copyClipboard(self):
        content = self.textbox.get("0.0", "end")
        self.clipboard_clear()
        self.clipboard_append(content)
        self.update()