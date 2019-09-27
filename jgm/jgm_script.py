# _*_ coding:UTF-8 _*_
from time import sleep
from PIL import Image
from common.GameTaskQueue import GameTaskQueue
from common.GameWin import GameWin
from common.scripts_common import *
import pyautogui as pag


class JGMGame(GameWin, GameTaskQueue):
    def __init__(self):
        super().__init__(u"腾讯手游助手【极速傲引擎】")

    # 硬币坐标
    coin_pos = (
        (109, 278),
        (109, 368),
        (109, 457),
        (199, 229),
        (199, 319),
        (199, 413),
        (290, 184),
        (290, 275),
        (290, 365)
    )
    # 货物坐标
    cargo_pos = (
        (241, 611),
        (296, 589),
        (349, 550)
    )

    def ret_home(self):
        pass

    def collect_coin(self):
        for pos in self.coin_pos:
            super().click(pos[0], pos[1])

    train_not_come_count = 0

    flag_time = 0

    # 检查小火车
    def check_train(self):

        if self.flag_time != 0 and time.time() - self.flag_time > 3600:
            print("已经过了1小时,重新开始检查火车...")
            self.flag_time = 0

        if self.flag_time == 0:
            img = self.screen_img(279, 569, 304, 596)
            origin_img = Image.open('train.png')
            same_value = image_same_val(img, origin_img)
            if same_value < 9:
                print("火车来了....")
                sleep(Sleep.MIDDLE_LONG.value)
                self.train_not_come_count = 0
                self.freight()
                return
            self.train_not_come_count += 1
            if self.train_not_come_count > 30:
                print("火车长时间没来,过1小时再检查....")
                self.flag_time = time.time()
            return

    # 运货
    def freight(self):
        for pos1 in self.cargo_pos:
            for pos2 in self.coin_pos:
                self.draw(pos1[0], pos1[1], pos2[0], pos2[1])
                sleep(Sleep.SHORT.value)
                self.draw(pos1[0], pos1[1], pos2[0], pos2[1])
                sleep(Sleep.SHORT.value)
                self.draw(pos1[0], pos1[1], pos2[0], pos2[1])
                sleep(Sleep.SHORT.value)

    def up_build(self, pos):
        super().click(357, 429)
        sleep(Sleep.SHORT.value)
        super().click(pos[0], pos[1])
        sleep(Sleep.SHORT.value)
        super().click(313, 645)
        sleep(Sleep.SHORT.value)
        super().click(357, 429)
        sleep(Sleep.SHORT.value)

    def init_menu(self):
        # 点击次数
        count = 0
        # 建筑下标
        pos_idx = 0
        while True:
            count = count + 1
            self.collect_coin()
            if count == 30:
                self.up_build(self.coin_pos[pos_idx % len(self.coin_pos)])
                pos_idx = pos_idx + 1
                count = 0
            if count % 2 == 0:
                self.check_train()
            sleep(Sleep.MIDDLE.value)


if __name__ == "__main__":
    jgm = JGMGame()
    jgm.init_menu()
