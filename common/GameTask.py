import time

from common.scripts_common import get_str_time, get_time_diff


class GameTask(object):
    task_name = None
    start_time = None
    end_time = None

    def __init__(self, game_win=None):
        self.game_win = game_win

    def start_task(self):
        self.game_win.ret_home()
        self.start_time = time.time()
        print('--', self.task_name, '--', '开始')
        self.task_process()
        self.end_time = time.time()
        print('--', self.task_name, '--', '已完成', '耗时:', get_time_diff(self.end_time, self.start_time), "秒")

    def task_process(self):
        pass


# 循环任务类
class LoopGameTask(GameTask):
    def __init__(self, game_win):
        super().__init__(game_win)
        loop_count = 0
        while loop_count == 0:
            print("请输入循环次数:")
            try:
                loop_count = int(input())
                if loop_count <= 0:
                    print('输入错误..')
            except:
                print('输入错误..')
        print(self.task_name, '循环次数:', loop_count, '次')
        self.loop_count = loop_count
