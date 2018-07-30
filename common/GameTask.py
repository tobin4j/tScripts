import datetime


class GameTask(object):
    task_name = None

    def __init__(self, game_win):
        self.game_win = game_win

    def start_task(self):
        self.game_win.ret_home()
        current_time = datetime.datetime.now()
        print('--', self.task_name, '--', '开始')
        self.task_process()
        print('--', self.task_name, '--', '已完成', '耗时:', str(datetime.datetime.now() - current_time))

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
