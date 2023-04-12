import http.server
import socketserver
from http import HTTPStatus

# Handler class for get
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        print('Request Received')
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        self.wfile.write(b'Hello world')


httpserver = socketserver.TCPServer(('0.0.0.0', 9000), Handler)
httpserver.serve_forever()
