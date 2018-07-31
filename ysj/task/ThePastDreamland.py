from time import sleep

from PIL import Image

from common.GameTask import GameTask, LoopGameTask
from common.scripts_common import Sleep, image_same_val, common_input_switch


# 前尘幻境
class ThePastDreamland(LoopGameTask):
    task_name = '前尘幻境'

    def __init__(self, game_win):
        super().__init__(game_win)
        role_type = common_input_switch(game_win.get_role_type())
        self.role_type = role_type

    def task_process(self):
        game = self.game_win
        role_type = self.role_type
        pre_val = 0
        count = 0
        complete_count = 0
        # 前置点击
        game.click(820, 563)
        sleep(Sleep.SHORT.value)
        game.draw(963, 265, 10, 265)
        game.click(830, 280)
        if role_type in (1, 2, 3):
            role_pos_x = 280
        else:
            role_pos_x = 640
        if role_type in (1, 4):
            role_pos_y = 200
        elif role_type in (2, 5):
            role_pos_y = 334
        else:
            role_pos_y = 453
        sleep(Sleep.SHORT.value)
        game.click(role_pos_x, role_pos_y)
        sleep(Sleep.MIDDLE.value)
        game.draw(727, 450, 727, 30)
        sleep(Sleep.MIDDLE.value)
        game.click(727, 430)
        game.click(800, 550)
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
                print("--前尘幻境--已刷:", complete_count, "次")
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
