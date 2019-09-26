from time import sleep

from PIL import Image

from common.GameTask import GameTask
from common.scripts_common import Sleep, image_same_val


# 疾之境界
class SpeedRealm(GameTask):
    task_name = '疾之境界'

    def task_process(self):
        game = self.game_win
        game.click(820, 563)
        sleep(Sleep.SHORT.value)
        game.click(120, 272)
        sleep(Sleep.MIDDLE.value)
        # 冗余
        game.draw(879, 319, 10, 319)
        sleep(Sleep.SHORT.value)
        game.click(813, 297)

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
        while complete_count < 3:
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
            if same_value < 11:
                complete_count += 1
                print("--疾之境界--已刷:", complete_count, "次")
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
            sleep(Sleep.LONG.value)
