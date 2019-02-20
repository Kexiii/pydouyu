from threading import Thread
import time
from . import packet_util


class HeartbeatWorker(Thread):
    def __init__(self, socket, heartbeat_interval=45):
        Thread.__init__(self)
        self.need_stop = False
        self.socket = socket
        self.heartbeat_interval = heartbeat_interval

    def set_stop(self, need_stop=True):
        self.need_stop = need_stop

    def run(self):
        while not self.need_stop:
            ori_str = packet_util.assemble_heartbeat_str()
            data = packet_util.assemble_transfer_data(ori_str)
            self.socket.send(data)
            time.sleep(self.heartbeat_interval)
