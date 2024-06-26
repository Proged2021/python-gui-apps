import tkinter as tk
import random


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("マルバツゲーム")
        self.root.geometry("400x450")
        self.root.configure(bg="#333333")
        self.reset_game()

        # リセットボタン
        reset_button = tk.Button(
            self.root,
            text="リセット",
            command=self.reset_game,
            bg="#FF5722",
            fg="#FFFFFF",
        )
        reset_button.pack(pady=20)

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "◯" if random.choice([True, False]) else "✕"
        self.buttons = []
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget.cget("text") != "リセット":
                widget.destroy()

        self.create_board()

        if self.current_player == "✕":
            self.computer_move()

    def create_board(self):
        frame = tk.Frame(self.root, bg="#333333")
        frame.pack()
        for i in range(9):
            button = tk.Button(
                frame,
                text="",
                font=("Helvetica", 20),
                height=3,
                width=6,
                command=lambda i=i: self.player_move(i),
                bg="#555555",
                fg="#FFFFFF",
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)
        self.status_label = tk.Label(
            self.root, text=f"{self.current_player}の番です", bg="#333333", fg="#FFFFFF"
        )
        self.status_label.pack(pady=10)

    def player_move(self, index):
        if self.board[index] == "" and self.current_player == "◯":
            self.board[index] = "◯"
            self.buttons[index].config(text="◯", fg="red")
            if self.check_winner("◯"):
                self.status_label.config(text="あなたの勝ちです！")
                self.disable_buttons()
            elif self.is_draw():
                self.status_label.config(text="引き分けです！")
            else:
                self.current_player = "✕"
                self.computer_move()

    def computer_move(self):
        best_score = -float("inf")
        best_move = None
        for i in range(9):
            if self.board[i] == "":
                self.board[i] = "✕"
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""
                if score > best_score:
                    best_score = score
                    best_move = i

        self.board[best_move] = "✕"
        self.buttons[best_move].config(text="✕", fg="blue")
        if self.check_winner("✕"):
            self.status_label.config(text="コンピュータの勝ちです！")
            self.disable_buttons()
        elif self.is_draw():
            self.status_label.config(text="引き分けです！")
        else:
            self.current_player = "◯"
            self.status_label.config(text=f"{self.current_player}の番です")

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner("✕"):
            return 1
        elif self.check_winner("◯"):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "✕"
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(9):
                if board[i] == "":
                    board[i] = "◯"
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def check_winner(self, player):
        win_conditions = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),
            (0, 4, 8),
            (2, 4, 6),
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def is_draw(self):
        return all(self.board[i] != "" for i in range(9))


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
