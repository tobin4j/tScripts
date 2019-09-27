# 游戏窗口类 所有 pos 都已左上为参照
import win32gui
from common.scripts_common import *
import win32api
import win32con
from time import sleep
import pyautogui as pag
from PIL import ImageGrab


def init_pos(func):
    def wrapper(self, *args, **kw):
        try:
            self.left_px, self.up_px, self.right_px, self.down_px = win32gui.GetWindowRect(self.dlg)
        except:
            print("退出游戏..")
            exit()
        return func(self, *args, **kw)

    return wrapper


class GameWin(object):
    def __init__(self, title):
        dlg = win32gui.FindWindow(None, title)

        self.dlg = dlg
        win32gui.ShowWindow(dlg, win32con.SW_RESTORE)
        if dlg <= 0:
            print("未检测到游戏窗口..")
            exit()
        print("游戏窗口获取成功...")
        # 游戏窗口位置 已左上为参照
        self.left_px = None
        self.up_px = None
        self.right_px = None
        self.down_px = None
        print("初始化成功...")

    # 获得当前游戏窗口位置
    @init_pos
    def get_pos(self):
        return self.left_px, self.right_px, self.up_px, self.down_px

    # 游戏内点击
    @init_pos
    def click(self, x, y):
        x = self.left_px + x
        y = self.up_px + y
        # pag.click(x, y)

        pos = (x, y)
        handle = win32gui.WindowFromPoint(pos)
        client_pos = win32gui.ScreenToClient(handle, pos)
        tmp = win32api.MAKELONG(client_pos[0], client_pos[1])
        win32gui.SendMessage(handle, win32con.WM_ACTIVATE, win32con.WA_ACTIVE, 0)
        win32gui.SendMessage(handle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, tmp)
        win32gui.SendMessage(handle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, tmp)

    # 游戏内点对点拖拽
    @init_pos
    def draw(self, x, y, x1, y1):
        x = x + self.left_px
        y = y + self.up_px
        x1 = x1 + self.left_px
        y1 = y1 + self.up_px
        pag.mouseDown(x, y)
        pag.moveTo(x1, y1, 0.1)
        pag.mouseUp()

    # 游戏内点对点截图
    @init_pos
    def screen_img(self, x, y, x1, y1):
        x = x + self.left_px
        y = y + self.up_px
        x1 = x1 + self.left_px
        y1 = y1 + self.up_px
        bbox = (x, y, x1, y1)
        img = ImageGrab.grab(bbox)
        return img

    def ret_home(self):
        pass

    def init_menu(self):
        pass
