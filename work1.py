import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x500")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action1():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry1.get()  # 入力値を取得3
    num3 = int(num1) + int(num2)
    num4 = int(num1) - int(num2)
    num5 = int(num1) * int(num2)
    num6 = int(num1) / int(num2)
     # 画面に出力
    label1.config(text=f"{num1} + {num2} = {num3}")
    


def button_action2():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry1.get()  # 入力値を取得3
    num3 = int(num1) + int(num2)
    num4 = int(num1) - int(num2)
    num5 = int(num1) * int(num2)
    num6 = int(num1) / int(num2)
     # 画面に出力
    label2.config(text=f"{num1} - {num2} = {num4}")

def button_action3():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry1.get()  # 入力値を取得3
    num3 = int(num1) + int(num2)
    num4 = int(num1) - int(num2)
    num5 = int(num1) * int(num2)
    num6 = int(num1) / int(num2)
     # 画面に出力
    label3.config(text=f"{num1} * {num2} = {num5}")

def button_action4():  # 関数の定義 ※ボタンが押されたときの動き
    num1 = entry1.get()  # 入力値を取得
    num2 = entry1.get()  # 入力値を取得3
    num3 = int(num1) + int(num2)
    num4 = int(num1) - int(num2)
    num5 = int(num1) * int(num2)
    num6 = int(num1) / int(num2)
     # 画面に出力
    label4.config(text=f"{num1} / {num2} = {num6}")





# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)
entry2 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry2.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="+", command=button_action1)
button1.pack(pady=10)
button2 = tk.Button(window, text="-", command=button_action2)
button2.pack(pady=10)
button3 = tk.Button(window, text="*", command=button_action3)
button3.pack(pady=10)
button4 = tk.Button(window, text="/", command=button_action4)
button4.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)
label3 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label3.pack(pady=10)
label4 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label4.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
