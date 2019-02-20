from threading import Thread
from . import packet_util
import logging


class MessageConsumer(Thread):
    def __init__(self, msg_queue):
        Thread.__init__(self)
        self.need_stop = False
        self.msg_queue = msg_queue
        self.handlers = {}

    def add_handler(self, msg_type, handler):
        if msg_type not in self.handlers:
            self.handlers[msg_type] = []
        self.handlers[msg_type].append(handler)

    def set_stop(self, need_stop=True):
        self.need_stop = need_stop

    def run(self):
        while not self.need_stop:
            data = self.msg_queue.get()
            ori_str = packet_util.extract_str_from_data(data)
            msg = packet_util.parse_str_to_dict(ori_str)
            try:
                msg_type = msg['type']
                if msg_type in self.handlers:
                    for handler in self.handlers[msg_type]:
                        handler(msg)
            except Exception as e:
                logging.warning("Invalid msg received. Exception: %s"
                                % e)
            self.msg_queue.task_done()

