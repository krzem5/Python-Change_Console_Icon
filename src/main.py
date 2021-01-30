import ctypes
import ctypes.wintypes



WM_SETICON=0x80
ICON_SMALL=0
ICON_BIG=1
NULL=0
IMAGE_ICON=1
LR_LOADFROMFILE=0x10



hwnd=ctypes.windll.kernel32.GetConsoleWindow()
ctypes.windll.user32.SendMessageW(hwnd,WM_SETICON,ICON_SMALL,ctypes.windll.user32.LoadImageW(NULL,"rsrc/icon.ico",IMAGE_ICON,16,16,LR_LOADFROMFILE))
ctypes.windll.user32.SendMessageW(hwnd,WM_SETICON,ICON_BIG,ctypes.windll.user32.LoadImageW(NULL,"rsrc/icon.ico",IMAGE_ICON,32,32,LR_LOADFROMFILE))
