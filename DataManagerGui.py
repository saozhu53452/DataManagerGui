import tkinter as tk
from tkinter import messagebox

def show_message():
    messagebox.showinfo("提示", "Hello, 这是一个简单的 GUI！")

# 创建主窗口
root = tk.Tk()
root.title("Data Manager GUI")
root.geometry("300x200")

# 创建按钮
btn = tk.Button(root, text="点击我", command=show_message)
btn.pack(pady=50)

# 运行窗口
root.mainloop()
