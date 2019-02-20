from .message_worker import MessageWorker
from .heartbeat_worker import HeartbeatWorker
from .tcp_socket import TCPSocket


class Client(object):
    def __init__(self, room_id=562590, heartbeat_interval=45,
                 barrage_host="openbarrage.douyutv.com",
                 barrage_port=8601):
        self.room_id = room_id
        self.heartbeat_interval = heartbeat_interval
        self.barrage_host = barrage_host
        self.barrage_port = barrage_port
        self.tcp_socket = TCPSocket(self.barrage_host, self.barrage_port)
        self.message_worker = MessageWorker(self.tcp_socket, self.room_id)
        self.heartbeat_worker = HeartbeatWorker(self.tcp_socket, self.heartbeat_interval)

    def add_handler(self, msg_type, handler):
        self.message_worker.add_handler(msg_type, handler)

    def set_heartbeat_interval(self, heartbeat_interval):
        self.heartbeat_interval = heartbeat_interval

    def refresh_object(self):
        self.tcp_socket = TCPSocket(self.barrage_host, self.barrage_port)
        self.message_worker = MessageWorker(self.tcp_socket, self.room_id)
        self.heartbeat_worker = HeartbeatWorker(self.tcp_socket, self.heartbeat_interval)

    def set_room_id(self, room_id):
        self.room_id = room_id

    def start(self):
        self.tcp_socket.connect()
        self.message_worker.start()
        self.heartbeat_worker.start()

    def stop(self):
        self.message_worker.set_stop()
        self.heartbeat_worker.set_stop()
        self.tcp_socket.close()
        self.refresh_object()

