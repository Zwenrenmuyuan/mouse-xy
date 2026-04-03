import tkinter as tk


class Toast:
    def __init__(self, parent: tk.Tk, x: int, y: int, text: str):
        self._win = tk.Toplevel(parent)
        self._win.overrideredirect(True)
        self._win.attributes("-topmost", True)
        self._win.attributes("-alpha", 0.0)
        self._win.geometry(f"+{x + 18}+{y + 18}")
        self._build_ui(text)
        self._fade_in(0.0)
        self._win.after(1000, self._fade_out)

    def _build_ui(self, text: str):
        outer = tk.Frame(self._win, bg="#45475a", bd=0)
        outer.pack()

        tk.Frame(outer, bg="#a6e3a1", width=4).pack(side="left", fill="y")

        inner = tk.Frame(outer, bg="#313244", padx=12, pady=8)
        inner.pack(side="left")

        tk.Label(
            inner,
            text="✔  已复制",
            bg="#313244",
            fg="#a6e3a1",
            font=("Segoe UI", 9, "bold"),
            anchor="w",
        ).pack(anchor="w")

        tk.Label(
            inner,
            text=text,
            bg="#313244",
            fg="#cdd6f4",
            font=("Consolas", 11),
            anchor="w",
        ).pack(anchor="w")

    def _fade_in(self, alpha: float):
        alpha = min(alpha + 0.1, 0.95)
        try:
            self._win.attributes("-alpha", alpha)
            if alpha < 0.95:
                self._win.after(20, lambda: self._fade_in(alpha))
        except tk.TclError:
            pass

    def _fade_out(self):
        try:
            alpha = self._win.attributes("-alpha") - 0.08
            if alpha <= 0:
                self._win.destroy()
            else:
                self._win.attributes("-alpha", alpha)
                self._win.after(30, self._fade_out)
        except tk.TclError:
            pass
