from time import sleep

from PIL import Image

from common.GameTask import GameTask
from common.scripts_common import Sleep, image_same_val


# 经验宝库
class EXP_STORE(GameTask):
    task_name = '经验宝库'

    def task_process(self):
        game = self.game_win
        game.click(820, 563)
        sleep(Sleep.SHORT.value)
        game.click(120, 272)
        sleep(Sleep.MIDDLE.value)
        game.click(187, 315)
        sleep(Sleep.MIDDLE.value)
        game.draw(707, 435, 707, 50)
        sleep(Sleep.MIDDLE.value)
        game.click(700, 425)
        game.click(750, 533)
        sleep(Sleep.LONG.value)
        game.continue_click()
        # 开始循环
        pre_val = 0
        count = 0
        complete_count = 0
        while complete_count < 1:
            img = game.screen_img(749, 155, 852, 230)
            origin_img = Image.open('origin_qianchen.png')
            same_value = image_same_val(img, origin_img)
            if pre_val == same_value:
                count += 1
            else:
                count = 0
            pre_val = same_value
            if count > 2:
                game.continue_click()
            if same_value < 5:
                complete_count += 1
                print("--经验宝库--已刷:", complete_count, "次")
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
            sleep(Sleep.LONG.value)
