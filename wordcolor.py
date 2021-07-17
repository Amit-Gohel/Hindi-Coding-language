import tkinter as tk


class colorcode:
    def __init__(self, code, editor):
        self.code = code
        self.editor = editor

    def findver(self):
        s = self.code
        if s:
            idx = '1.0'
            while 1:
                idx = self.editor.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx:
                    break
                    # last index sum of current index and
                    # length of text
                lastidx = '%s+%dc' % (idx, len(s))
                self.editor.tag_add('found', idx, lastidx)
                idx = lastidx
            self.editor.tag_config('found', foreground='#0000FF')
            return self.editor

    def findimpter(self):
        s = self.code
        if s:
            idx = '1.0'
            while 1:
                idx = self.editor.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx:
                    break
                    # last index sum of current index and
                    # length of text
                lastidx = '%s+%dc' % (idx, len(s))
                self.editor.tag_add('found1', idx, lastidx)
                idx = lastidx
            self.editor.tag_config('found1', foreground='#00FF00')
            return self.editor
