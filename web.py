
from http.server import HTTPServer, BaseHTTPRequestHandler

content = """
<html>
<head>
    <title>My Simple Webserver</title>
</head>

<body>

    <h1>My Simple Website</h1>

    <h2>About Me</h2>

    <p>
        My name is Jagadeep, and I am a first-year Computer Science
        Engineering student at Saveetha Engineering College.
        I am passionate about technology, programming, and exploring
        how computers work. I enjoy learning new concepts, solving
        problems, and improving my technical skills. My interests
        include web development, Python programming, artificial
        intelligence, and cybersecurity. Apart from academics,
        I enjoy playing football, working out, and gaming.
        I believe in consistency, creativity, and continuous learning.
    
    </p>

    <h2>My Details</h2>

    <p>Name: Jagadeep</p>
    <p>College: Saveetha Engineering College</p>
    <p>Department: Computer Science Engineering</p>
    <p>Register Number: P JAGADEEP </p>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

server_address = ('', 8000)
httpd = HTTPServer(server_address, myhandler)

print("my webserver is running...")
print("Open http://127.0.0.1:8000")
httpd.serve_forever()