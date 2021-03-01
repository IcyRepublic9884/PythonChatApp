import socket
import threading
from typing import List


# TODO: Add option to connect to external machine

def send_messages(client_sock: socket.socket, msg: str):
    """Encode a string and send to the client"""
    client_sock.send(msg.encode())


class SimpleChatServer:
    """A Simple Chat Server"""

    def __init__(self, *, port_no, max_clients: int = 5, buf_size: int = 1024, host: str = None):
        self.port_no = port_no
        self.max_clients = max_clients
        self.buf_size = buf_size
        self.client_list: List[socket.socket] = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if host is None:
            self._host = socket.gethostbyname(socket.gethostname())
        else:
            self._host = host

    def recv_and_send_messages(self, client_sock: socket.socket):
        """Send and receive the message to clients"""
        while True:
            msg = client_sock.recv(self.buf_size).decode('utf-8')
            send_messages(client_sock, msg)

    def close_all_clients(self):
        """Close all the clients connected to the server"""
        for client in self.client_list:
            client.close()

    def __del__(self):
        """Delete the Object, make sure to have a clean exit"""
        for client in self.client_list:
            client.close()
        self.server_socket.close()
        del self

    def _bind_local(self):
        """Bind the Server to the Local Machine"""
        self.server_socket.bind((self._host, self.port_no))

    def _start_acceptor_thread(self):
        """Accept connection and add the client to the client list"""

        def thread_func():
            """Thread for accepting connections"""
            sock, _ = self.server_socket.accept()
            self.client_list.append(sock)

        threading.Thread(target=thread_func, args=()).start()

    def _start_main_thread(self):
        """Thread for reading and sending messages to clients"""

        def thread_func():
            while True:
                for client in self.client_list:
                    self.recv_and_send_messages(client_sock=client)

        threading.Thread(target=thread_func, args=()).start()

    def stop(self):
        """Close all the clients and close the server"""
        for client in self.client_list:
            client.close()
        self.server_socket.close()

    def start_server(self):
        """Start the server"""
        try:
            self._bind_local()
            self.server_socket.listen(self.max_clients)
            self._start_acceptor_thread()
            self._start_main_thread()
        except ConnectionRefusedError:
            raise ConnectionRefusedError(f"Error: Connection Refused at {self._host} at port {self.port_no}")
