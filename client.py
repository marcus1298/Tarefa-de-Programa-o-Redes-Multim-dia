import socket

class RTSPClient:
    def __init__(self, server_host, server_port, rtp_port, video_file):
        self.server_host = server_host
        self.server_port = server_port
        self.rtp_port = rtp_port
        self.video_file = video_file
        self.rtsp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.rtsp_socket.connect((self.server_host, self.server_port))
        self.session_id = None

    def send_request(self, request):
        self.rtsp_socket.sendall(request.encode())

    def receive_response(self):
        response = self.rtsp_socket.recv(1024)
        return response.decode()

    def setup(self):
        request = f'SETUP {self.video_file} RTSP/1.0\r\nCSeq: 1\r\nTransport: RTP/UDP; client_port={self.rtp_port}\r\n'
        self.send_request(request)
        response = self.receive_response()
        self.session_id = response.split('Session: ')[1].split('\r\n')[0]

    def play(self):
        request = f'PLAY {self.video_file} RTSP/1.0\r\nCSeq: 2\r\nSession: {self.session_id}\r\n'
        self.send_request(request)
        response = self.receive_response()
        print(response)

    def pause(self):
        request = f'PAUSE {self.video_file} RTSP/1.0\r\nCSeq: 3\r\nSession: {self.session_id}\r\n'
        self.send_request(request)
        response = self.receive_response()
        print(response)

    def teardown(self):
        request = f'TEARDOWN {self.video_file} RTSP/1.0\r\nCSeq: 4\r\nSession: {self.session_id}\r\n'
        self.send_request(request)
        response = self.receive_response()
        print(response)

# Exemplo de uso do cliente
client = RTSPClient('localhost', 554, 1234, 'movie.Mjpeg')
client.setup()
client.play()
client.pause()
client.teardown()
