import http.server
import socketserver

ACCOUNT_ID = "444455556666"
PORT = 14571

class STSHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        if content_length > 0:
            self.rfile.read(content_length)
        response = (
            '<GetCallerIdentityResponse xmlns="https://sts.amazonaws.com/doc/2011-06-15/">'
            '<GetCallerIdentityResult>'
            '<Arn>arn:aws:iam::' + ACCOUNT_ID + ':user/test-user</Arn>'
            '<UserId>AKIAIOSFODNN7SESSION</UserId>'
            '<Account>' + ACCOUNT_ID + '</Account>'
            '</GetCallerIdentityResult>'
            '<ResponseMetadata>'
            '<RequestId>01234567-89ab-cdef-0123-456789abcdef</RequestId>'
            '</ResponseMetadata>'
            '</GetCallerIdentityResponse>'
        )
        encoded = response.encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'text/xml; charset=utf-8')
        self.send_header('Content-Length', str(len(encoded)))
        self.send_header('x-amzn-requestid', '01234567-89ab-cdef-0123-456789abcdef')
        self.end_headers()
        self.wfile.write(encoded)
    def do_GET(self):
        self.do_POST()
    def log_message(self, format, *args):
        pass

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(('127.0.0.1', PORT), STSHandler) as httpd:
    httpd.serve_forever()
