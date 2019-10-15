import socket
import time


class Client:
    def __init__(self, host, port, timeout):
        self.host = str(host)
        self.port = int(port)
        self.timeout = int(timeout)
        self.error_answer = 'ClientError'
        self.data = None

    def server_connection(self, req_2, req):
        with socket.create_connection((self.host, self.port)) as sock:
            sock.settimeout(self.timeout)
            try:
                if req.split()[0] is 'put':
                    sock.sendall(req_2)
                else:
                    sock.sendall(req_2)
                    self.data = sock.recv(1024)
            except socket.timeout():
                print('TIMEOUT')
            except socket.error as err:
                print('Send data error', err)
            sock.close()

    def put(self, name, value, timestamp=str(int(time.time()))):
        req = f'put {name} {value} {timestamp}\n'
        req_2 = req.encode('utf-8')
        try:
            self.server_connection(req_2, req)
        except:
            print(self.error_answer)

    def get(self, name):
        req = f'get {name}\n'
        req_2 = req.encode('utf-8')
        try:
            self.server_connection(req_2, req)
            if self.data is 'ok\n\n':
                dict_ = {}
                return dict_
            elif name is not '*':
                for element in self.data:
                    dict_ = {name: sorted(self.data, key=None)}
        except:
            print(self.error_answer)
