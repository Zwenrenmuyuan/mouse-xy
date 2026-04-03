# mouse-xy

实时显示鼠标屏幕坐标的轻量小工具。

## 功能

- 置顶小窗口，实时刷新鼠标坐标（50ms 刷新率）
- 拖动标题栏可移动窗口位置
- `Ctrl+Alt+C` 全局快捷键复制当前坐标到剪贴板
- 复制成功后在鼠标旁弹出淡入淡出 toast 气泡提示
- 半透明深色主题，不遮挡工作区

## 使用

```bash
uv run main.py
```

> 注意：`keyboard` 库在 Windows 上可能需要管理员权限运行。

## 依赖

- Python 3.8+
- [pyautogui](https://pyautogui.readthedocs.io/)
- [keyboard](https://github.com/boppreh/keyboard)

依赖由 uv 自动管理。
