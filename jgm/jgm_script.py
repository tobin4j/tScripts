# _*_ coding:UTF-8 _*_
from time import sleep

from common.GameTaskQueue import GameTaskQueue
from common.GameWin import GameWin
from common.scripts_common import *


class JGMGame(GameWin, GameTaskQueue):
    def __init__(self):
        super().__init__(u"腾讯手游助手【极速傲引擎】")

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

    def ret_home(self):
        pass

    def collect_coin(self):
        for pos in self.coin_pos:
            super().click(pos[0], pos[1])

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
        count = 0
        pos_idx = 0
        while True:
            count = count + 1
            self.collect_coin()
            if count == 10:
                self.up_build(self.coin_pos[pos_idx % len(self.coin_pos)])
                pos_idx = pos_idx + 1
                count = 0
            sleep(Sleep.MIDDLE.value)


if __name__ == "__main__":
    jgm = JGMGame()
    jgm.init_menu()
