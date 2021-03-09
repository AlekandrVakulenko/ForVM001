from socket import *
# HOST = '127.0.0.1'
HOST = '62.109.23.127'
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST, PORT)
uCliSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = input('>')
    if not data:
        break
    uCliSock.sendto(data.encode(), SOCKADDR)
    data, addr = uCliSock.recvfrom(BUFSIZE)
    if data == 'q':
        break
    print(data)

uCliSock.close()
