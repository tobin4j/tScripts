from time import sleep

from PIL import Image

from common.GameTask import GameTask
from common.scripts_common import Sleep, image_same_val


# 限时祭典
class Fiesta(GameTask):
    task_name = '限时祭典'

    def task_process(self):
        game = self.game_win
        game.click(820, 563)
        sleep(Sleep.SHORT.value)
        game.click(412, 272)
        sleep(Sleep.MIDDLE.value)
        game.click(775, 287)
        sleep(Sleep.MIDDLE_LONG.value)
        game.click(775, 287)
        game.draw(761, 479, 750, 47)
        sleep(Sleep.SHORT.value)
        game.draw(761, 479, 750, 47)
        sleep(Sleep.SHORT.value)
        game.draw(761, 479, 750, 47)
        sleep(Sleep.SHORT.value)
        game.click(776, 507)
        sleep(Sleep.LONG.value)
        game.continue_click()
        # 开始循环
        pre_val = 0
        count = 0
        complete_count = 0
        while complete_count < 30:
            img = game.screen_img(425, 182, 600, 197)
            origin_img = Image.open('origin_jidian.png')
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
                print(self.task_name, "--已刷:", complete_count, "次")
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.SHORT.value)
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
                game.continue_click()
            sleep(Sleep.LONG.value)
