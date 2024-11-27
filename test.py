import tkinter as tk

def open_second_window():
    # 두 번째 윈도우 생성
    second_window = tk.Toplevel(root)
    second_window.title("Second Window")
    second_window.geometry("300x200")
    label = tk.Label(second_window, text="This is the second window!")
    label.pack(pady=20)

# 메인 윈도우 생성
root = tk.Tk()
root.title("Main Window")
root.geometry("400x300")

button = tk.Button(root, text="Open Second Window", command=open_second_window)
button.pack(pady=20)

root.mainloop()
