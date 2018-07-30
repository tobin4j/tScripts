from time import sleep

from PIL import Image

from common.GameTask import GameTask
from common.scripts_common import Sleep, image_same_val, common_input_switch


# 兽潮来袭
class SouChao(GameTask):
    task_name = '兽潮来袭'

    def __init__(self, game_win):
        super().__init__(game_win)

    def task_process(self):
        game = self.game_win
        print(self.task_name, "start...")
        pre_val = 0
        count = 0
        complete_count = 0
        # 前置点击
        game.click(820, 563)
        sleep(Sleep.SHORT.value)
        game.draw(963, 265, 10, 265)
        game.click(553, 276)
        sleep(Sleep.SHORT.value)
        game.click(880, 537)
        sleep(Sleep.LONG.value)
        game.continue_click()

        while complete_count < 9:
            img = game.screen_img(759, 169, 834, 207)
            origin_img = Image.open('shouchao.png')
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
                print(self.task_name, "--已刷:", complete_count, "次")
                game.continue_click()
                sleep(Sleep.SHORT.value)
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
                if complete_count % 3 == 0:
                    game.click(458, 327)
                    sleep(Sleep.SHORT.value)
                game.click(882, 538)
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
            sleep(Sleep.LONG.value)
