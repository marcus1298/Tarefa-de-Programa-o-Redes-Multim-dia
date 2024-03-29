import socket

class RTSPServer:
    def __init__(self, server_port, video_file):
        self.server_port = server_port
        self.video_file = video_file
        self.rtsp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rtsp_socket.bind(('localhost', self.server_port))
        self.rtsp_socket.listen(5)
        print('Server listening on port', self.server_port)
        self.session_id = '123456'

    def send_response(self, client_socket, response):
        client_socket.sendall(response.encode())

    def handle_client(self, client_socket):
        while True:
            request = client_socket.recv(1024).decode()
            if not request:
                break
            if 'SETUP' in request:
                self.send_response(client_socket, f'RTSP/1.0 200 OK\r\nCSeq: 1\r\nSession: {self.session_id}\r\n')
            elif 'PLAY' in request:
                self.send_response(client_socket, f'RTSP/1.0 200 OK\r\nCSeq: 2\r\nSession: {self.session_id}\r\n')
                # Iniciar a transmissão de vídeo RTP
            elif 'PAUSE' in request:
                self.send_response(client_socket, f'RTSP/1.0 200 OK\r\nCSeq: 3\r\nSession: {self.session_id}\r\n')
                # Pausar a transmissão de vídeo RTP
            elif 'TEARDOWN' in request:
                self.send_response(client_socket, f'RTSP/1.0 200 OK\r\nCSeq: 4\r\nSession: {self.session_id}\r\n')
                break

    def start(self):
        while True:
            client_socket, _ = self.rtsp_socket.accept()
            self.handle_client(client_socket)

# Exemplo de uso do servidor
server = RTSPServer(554, 'movie.Mjpeg')
server.start()
