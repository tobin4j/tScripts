from time import sleep

from PIL import Image

from common.GameTask import LoopGameTask
from common.scripts_common import Sleep, image_same_val


# 心海试练
class XinHai(LoopGameTask):
    task_name = '心海试练'

    def __init__(self, game_win):
        super().__init__(game_win)
        level = 0
        while level not in range(1, 11):
            print("请选择试练level(1-10):")
            try:
                level = int(input())
                if level not in range(1, 11):
                    print('输入错误..')
            except:
                print('输入错误..')
        print('已选择:', level)
        self.level = level

    def task_process(self):
        game = self.game_win
        level = self.level
        pre_val = 0
        count = 0
        complete_count = 0
        # 前置点击
        game.click(820, 563)
        sleep(Sleep.SHORT.value)
        game.click(967, 285)
        sleep(Sleep.SHORT.value)

        if level in range(1, 10, 2):
            level_pos_x = 200
        else:
            level_pos_x = 471

        if level in (1, 2):
            level_pos_y = 192
        elif level in (3, 4):
            level_pos_y = 283
        elif level in (5, 6):
            level_pos_y = 372
        else:
            level_pos_y = 463

        if level in (9, 10):
            game.draw(204, 451, 204, 90)
        game.click(level_pos_x, level_pos_y)
        sleep(Sleep.SHORT.value)
        game.click(882, 493)
        sleep(Sleep.LONG.value)
        game.continue_click()
        # 开始循环
        while complete_count < self.loop_count:
            img = game.screen_img(749, 155, 852, 230)
            origin_img = Image.open('origin_qianchen.png')
            same_value = image_same_val(img, origin_img)
            if pre_val == same_value:
                count += 1
            else:
                count = 0
            pre_val = same_value
            if count > 3:
                game.continue_click()
            if same_value < 5:
                complete_count += 1
                print(self.task_name, "--已刷:", complete_count, "次")
                game.continue_click()
                if complete_count == self.loop_count:
                    return

                sleep(Sleep.MIDDLE.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE_LONG.value)
                game.continue_click()
                sleep(Sleep.MIDDLE.value)
            sleep(Sleep.LONG.value)
