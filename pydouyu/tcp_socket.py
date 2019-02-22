import socket
import logging
import time


class TCPSocket(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.closed = True

    def send(self, data):
        if self.closed:
            return
        try:
            self.socket.sendall(data)
        except Exception as e:
            self.close()
            logging.warning("Socket sendall failed. Exception: %s" % e)
        return

    def close(self):
        if not self.closed:
            self.socket.close()
            self.closed = True

    def connect(self):
        if self.closed:
            while True:
                try:
                    self.socket.connect((self.host, self.port))
                except Exception as e:
                    logging.warning("Socket connect failed with %s:%d. Exception: %s"
                          % (self.host, self.port, e))
                    self.socket.close()
                    self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    logging.warning("Try reconnect in 5 seconds")

                    time.sleep(5)
                    continue
                break
            self.closed = False

    def receive(self, target_size):
        data = b''
        while target_size:
            try:
                tmp = self.socket.recv(target_size)
            except Exception as e:
                self.close()
                logging.warning("Socket recv failed. Exception: %s" % e)
                return None
            if not tmp:
                self.close()
                return None
            target_size -= len(tmp)
            data += tmp
        return data
