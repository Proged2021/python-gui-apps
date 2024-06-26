import tkinter as tk
import random

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x500")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑

name_list = []


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
    # 関数の定義 ※ボタンが押されたときの動き
    name = str(entry1.get())  # 入力値を取得
    name_list.append(name)
    # display_string = ""
    # # \n (option + ¥)
    # for n in name_list:
    #     display_string = display_string + n + "\n"

    label1.config(text=f"{"\n".join(name_list)}")


def random_action():
    random.shuffle(name_list)
    index = random.randint(0, len(name_list))
    label2.config(text=name_list[index])


# 入力フィールドの作成
entry1 = tk.Entry(window, text="名前を入力してください", bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="追加", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ボタンの作成
button2 = tk.Button(window, text="ランダム選択", command=random_action)
button2.pack(pady=10)

# 出力ラベルの作成
label2 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label2.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
