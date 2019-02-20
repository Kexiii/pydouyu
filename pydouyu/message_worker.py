from threading import Thread
import queue
from . import packet_util
from .message_consumer import MessageConsumer
import logging


class MessageWorker(Thread):
    def __init__(self, socket, room_id):
        Thread.__init__(self)
        self.need_stop = False
        self.socket = socket
        self.room_id = room_id
        self.msg_queue = queue.Queue()
        self.message_consumer = MessageConsumer(self.msg_queue)

    def add_handler(self, msg_type, handler):
        self.message_consumer.add_handler(msg_type, handler)

    def set_stop(self, need_stop=True):
        self.need_stop = need_stop
        self.message_consumer.set_stop(need_stop)

    def prepare(self):
        self.message_consumer.start()
        self.enter_room()

    def enter_room(self):
        ori_str = packet_util.assemble_login_str(self.room_id)
        data = packet_util.assemble_transfer_data(ori_str)
        self.socket.send(data)
        ori_str = packet_util.assemble_join_group_str(self.room_id)
        data = packet_util.assemble_transfer_data(ori_str)
        self.socket.send(data)

    def run(self):
        self.prepare()
        while not self.need_stop:
            packet_size = self.socket.receive(4)
            if packet_size is None:
                logging.warning("Socket closed")
                self.socket.connect()
                self.enter_room()
                continue
            packet_size = int.from_bytes(packet_size, byteorder='little')
            data = self.socket.receive(packet_size)
            if data is None:
                logging.warning("Socket closed")
                self.socket.connect()
                self.enter_room()
                continue
            self.msg_queue.put(data)
