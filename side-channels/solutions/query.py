from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

class HTTPReqHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        query = urlparse(self.path)[4]
        print(f"GET query: {query}")

ip = "localhost"
port = 55555
addr = (ip, port)

server = HTTPServer(addr, HTTPReqHandler)
print(f'Server running on address: ip = {ip}, port = {port}')
server.serve_forever()

# 다른 방법은 임의의 웹사이트 링크를 입력하고 wireshark로 HTTP 패킷 캡쳐하기
# HTTP 연결이 생성되지 않으면 wireshark로 캡쳐할 수 없음
