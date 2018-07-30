# _*_ coding:UTF-8 _*_
from common.GameTaskQueue import GameTaskQueue
from common.GameWin import GameWin
from common.scripts_common import *
from ysj.task.AgileRealm import AgileRealm
from ysj.task.EXP_STORE import *
from ysj.task.PowerRealm import PowerRealm
from ysj.task.SouChao import SouChao
from ysj.task.SpeedRealm import SpeedRealm
from ysj.task.ThePastDreamland import ThePastDreamland
from ysj.task.Fiesta import Fiesta
from ysj.task.XinHai import XinHai


class YSJGame(GameWin, GameTaskQueue):
    def __init__(self):
        super().__init__(u"腾讯手游助手【极速傲引擎】")
        self.__ROLE_TYPE = {
            1: '御者',
            2: '刺客',
            3: '炼丹师',
            4: '死士',
            5: '咒术师',
            6: '召唤师'
        }
        self.__PLAY_TYPE = {
            1: '天幻圣境',
            2: '前尘幻境',
            3: '限时祭典',
            4: '兽潮来袭',
            5: '心海试练',
            6: '每日一条龙!'
        }

    def get_role_type(self):
        return self.__ROLE_TYPE

    def get_play_type(self):
        return self.__PLAY_TYPE

    def continue_click(self):
        super().click(971, 550)

    def return_click(self):
        super().click(46, 75)

    def close_dialog_click(self):
        super().click(1012, 101)

    def ret_home(self):
        origin_img = Image.open('origin_home.png')
        same_val = 9
        while same_val > 8:
            sleep(Sleep.MIDDLE.value)
            img = ysj_game.screen_img(908, 491, 953, 532)
            same_val = image_same_val(img, origin_img)
            if same_val > 8:
                self.return_click()
                self.click(848, 98)
                self.close_dialog_click()

    def init_menu(self):
        play_type = common_input_switch(self.get_play_type())
        if play_type == 1:
            self.put_task(EXP_STORE(self))
            self.put_task(PowerRealm(self))
            self.put_task(SpeedRealm(self))
            self.put_task(AgileRealm(self))
        elif play_type == 2:
            self.put_task(ThePastDreamland(self))
        elif play_type == 3:
            self.put_task(Fiesta(self))
        elif play_type == 4:
            self.put_task(SouChao(self))
        elif play_type == 5:
            self.put_task(XinHai(self))
        elif play_type == 6:
            self.put_task(EXP_STORE(self))
            self.put_task(PowerRealm(self))
            self.put_task(SpeedRealm(self))
            self.put_task(AgileRealm(self))
            self.put_task(Fiesta(self))
            self.put_task(SouChao(self))
        self.exec_task()


if __name__ == "__main__":
    ysj_game = YSJGame()
    ysj_game.init_menu()

