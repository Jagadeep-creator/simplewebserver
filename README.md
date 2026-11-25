# EX01 Developing a Simple Webserver
## Date:25-11-26

## AIM:
To develop a simple webserver to serve html pages and display the Windows Specifications of your Laptop.

## DESIGN STEPS:
### Step 1: 
HTML content creation.

### Step 2:
Design of webserver workflow.

### Step 3:
Implementation using Python code.

### Step 4:
Import the necessary modules.

### Step 5:
Define a custom request handler.

### Step 6:
Start an HTTP server on a specific port.

### Step 7:
Run the Python script to serve web pages.

### Step 8:
Serve the HTML pages.

### Step 9:
Start the server script and check for errors.

### Step 10:
Open a browser and navigate to http://127.0.0.1:8000 (or the assigned port).

## PROGRAM:
```
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
httpd.serve_forever()
```

## OUTPUT:
![alt text](<../Screenshot 2026-11-25 095527.png>)

![alt text](<../Screenshot 2026-11-25 095534.png>)
## RESULT:
The program for implementing simple webserver is executed successfully.
