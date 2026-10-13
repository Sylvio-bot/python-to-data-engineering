import socket
'''
  AF_INET → IPv4
  SOCK_STREAM → protocole TCP (fiable, orienté connexion)'
  
'''
mysock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd = "GET /romeo.txt HTTP/1.1\r\nHost: data.pr4e.org\r\n\r\n".encode()
mysock.sendall(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysock.close()
