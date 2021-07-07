import tkinter as tk
from bbscode import converter
import bbscode

root = tk.Tk()

root.title("bbscode转换器")
# 输入框
inputText = tk.Text(root,height=20,width=100)
inputText.pack()

# 转换按钮
def md_to_bbscode():
    md_str = inputText.get('1.0',tk.END)
    bbscode = converter.md_to_bbscode(md_str)
    inputText.delete('1.0', tk.END)
    inputText.insert('1.0',bbscode)

convertBtn = tk.Button(root,text="markdown转换为bbscode",command=md_to_bbscode)
convertBtn.pack()


root.mainloop()
