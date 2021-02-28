import socket
import threading


class SimpleChatClient:
    """Client for the Simple Chat Server"""

    def __init__(self, *, port_no: int = 5000, buf_size: int = 1024):
        self.port_no = port_no
        self.buf_size = buf_size
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def _connect_local(self):
        """Connect to the server"""
        self.client.connect((socket.gethostbyname(socket.gethostname()), self.port_no))
        # TODO: Update to use supplied IP addr

    def _start_threads(self):
        """Start the Threads to receive and send messages"""

        def recv_thread_func():
            """Message Receiver"""
            while True:
                print(self.client.recv(self.buf_size).decode('utf-8'))

        def send_thread_func():
            """Message Sender"""
            while True:
                msg = input("Enter Message : ").encode()
                self.client.send(msg)

        threading.Thread(target=recv_thread_func, args=()).start()
        threading.Thread(target=send_thread_func, args=()).start()

    def start_client(self):
        """Start the client"""
        self._connect_local()
        self._start_threads()
