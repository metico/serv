import socket

s = socket.socket(
    socket.AF_UNIX, socket.SOCK_STREAM)
s.bind(('0.0.0.0', 2222))
s.listen(1)
while True:
    conn, addr = s.accept()
    while True:
            data = conn.recv(1024)
            if data=='close' or data=='Close':
                break
            if not data: 
                break
            conn.send(data)
    conn.close()

	
