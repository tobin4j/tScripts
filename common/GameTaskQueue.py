from queue import Queue

from common.mail_utils import send_mail
from common.scripts_common import get_str_time, get_str_datetime, get_time_diff


class GameTaskQueue(object):
    task_queue = Queue()
    complete_task_list = []

    def __init__(self):
        pass

    def put_task(self, game_task):
        self.task_queue.put(game_task)

    def exec_task(self):
        if self.task_queue.empty():
            print("任务全部执行完毕...")
            self.send_task_end_mail()
            exit()
        task = self.task_queue.get()
        task.start_task()
        self.complete_task_list.append(task)
        self.exec_task()

    def send_task_end_mail(self):
        content = "完成清单:\n"
        for task in self.complete_task_list:
            content = content + "玩法名称:" + task.task_name + \
                      " 开始时间:" + get_str_datetime(task.start_time) + " 结束时间:" + \
                      get_str_datetime(task.end_time) + " 耗时: " + get_time_diff(task.end_time, task.start_time) + "秒\n"
        title = "报告长官!任务完成!"
        send_mail(content, title=title)
