import tkinter as tk
import pyautogui
import keyboard

from toast import Toast


class MouseTrackerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("鼠标坐标")
        self.root.attributes("-topmost", True)
        self.root.attributes("-alpha", 0.92)
        self.root.resizable(False, False)
        self.root.overrideredirect(True)

        self._drag_x = 0
        self._drag_y = 0
        self._build_ui()
        self._update_coords()
        keyboard.add_hotkey("ctrl+alt+c", lambda: self.root.after(0, self._copy_coords))

    def _build_ui(self):
        outer = tk.Frame(self.root, bg="#1e1e2e", bd=1, relief="solid")
        outer.pack(fill="both", expand=True)

        title_bar = tk.Frame(outer, bg="#313244", cursor="fleur")
        title_bar.pack(fill="x")

        title_label = tk.Label(
            title_bar,
            text="📍 Mouse XY",
            bg="#313244",
            fg="#cdd6f4",
            font=("Segoe UI", 9, "bold"),
            pady=4,
            padx=8,
            cursor="fleur",
        )
        title_label.pack(side="left")

        close_btn = tk.Label(
            title_bar,
            text=" × ",
            bg="#313244",
            fg="#f38ba8",
            font=("Segoe UI", 11, "bold"),
            cursor="hand2",
        )
        close_btn.pack(side="right", padx=4)
        close_btn.bind("<Button-1>", lambda e: self.root.destroy())

        for w in (title_bar, title_label):
            w.bind("<ButtonPress-1>", self._on_drag_start)
            w.bind("<B1-Motion>", self._on_drag_move)

        body = tk.Frame(outer, bg="#1e1e2e", padx=16, pady=10)
        body.pack(fill="both")

        self.x_var = tk.StringVar(value="X:     0")
        self.y_var = tk.StringVar(value="Y:     0")

        for var in (self.x_var, self.y_var):
            lbl = tk.Label(
                body,
                textvariable=var,
                bg="#1e1e2e",
                fg="#a6e3a1",
                font=("Consolas", 18, "bold"),
                anchor="w",
            )
            lbl.pack(fill="x")

        self.hint_var = tk.StringVar(value="Ctrl+Alt+C 复制")
        tk.Label(
            body,
            textvariable=self.hint_var,
            bg="#1e1e2e",
            fg="#6c7086",
            font=("Segoe UI", 8),
        ).pack(pady=(2, 0))

        self.root.geometry("200x140+100+100")

    def _update_coords(self):
        x, y = pyautogui.position()
        self.x_var.set(f"X: {x:5d}")
        self.y_var.set(f"Y: {y:5d}")
        self.root.after(50, self._update_coords)

    def _copy_coords(self):
        x, y = pyautogui.position()
        text = f"{x}, {y}"
        self.root.clipboard_clear()
        self.root.clipboard_append(text)
        self.hint_var.set(f"已复制: {text}")
        self.root.after(1500, lambda: self.hint_var.set("Ctrl+Alt+C 复制"))
        Toast(self.root, x, y, text)

    def _on_drag_start(self, event):
        self._drag_x = event.x_root - self.root.winfo_x()
        self._drag_y = event.y_root - self.root.winfo_y()

    def _on_drag_move(self, event):
        x = event.x_root - self._drag_x
        y = event.y_root - self._drag_y
        self.root.geometry(f"+{x}+{y}")
