import tkinter as tk

# ↓↓↓ お約束のコード ↓↓↓
window = tk.Tk()
window.title("GUI App")
window.geometry("600x500")
bg_color = "#333333"  # ダークグレー
fg_color = "#FFFFFF"  # 白
window.configure(bg=bg_color)
# ↑↑↑ お約束のコード ↑↑↑


def button_action():  # 関数の定義 ※ボタンが押されたときの動き
  # 関数の定義 ※ボタンが押されたときの動き
    seireki = int(entry1.get())  # 入力値を取得
    label1.config(text=f"{seireki}")
 
    # 　西暦の判定と元号の計算
    if ():
        reiwa = seireki <=  2018
        print(f"{seireki}年は令和{(seireki - 2018)}です。") 
    elif ():
        heisei = seireki <= 1988
        print(f"{seireki}年は平成{(seireki - 1988)}です。") 
        shouwa = seireki <= 1925
        print(f"{seireki}年は昭和{(seireki - 1925)}です。") 
    elif ():
        taishou = seireki <= 1911
        print(seireki + "年は大正" + int(seireki - 1911) + "です。")
    else:
        meizi = seireki
        print(f"{seireki}年は明治{(seireki - 1967)}です。") 
    # 元号の計算
    

    

    




# 入力フィールドの作成
entry1 = tk.Entry(window, bg=fg_color, fg=bg_color)
entry1.pack(pady=10)

# ボタンの作成
button1 = tk.Button(window, text="Submit", command=button_action)
button1.pack(pady=10)

# 出力ラベルの作成
label1 = tk.Label(window, text="", bg=bg_color, fg=fg_color)
label1.pack(pady=10)

# ↓↓↓ お約束のコード ↓↓↓
window.mainloop()
# ↑↑↑ お約束のコード ↑↑↑
