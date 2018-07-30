from queue import Queue


class GameTaskQueue(object):
    task_queue = Queue()

    def __init__(self):
        # 询问任务结束是否需要发送邮件
        # 加一个完成清单 ,发邮件过去
        # 游戏任务类增加任务具体信息相关字段
        pass

    def put_task(self, game_task):
        self.task_queue.put(game_task)

    def exec_task(self):
        if self.task_queue.empty():
            print("任务全部执行完毕,脚本退出")
            exit()
        task = self.task_queue.get()
        task.start_task()
        self.exec_task()
