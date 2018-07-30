from queue import Queue


class GameTaskQueue(object):
    task_queue = Queue()

    def __init__(self):
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
