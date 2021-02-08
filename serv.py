from socket import *

HOST = ''
PORT = 3000
BUFSIZE = 1024
SOCKADDR = (HOST, PORT)
uServSock = socket(AF_INET, SOCK_DGRAM)
uServSock.bind(SOCKADDR)

while True:
    print('waiting:')
    data, addr = uServSock.recvfrom(BUFSIZE)
    loc_data = data.decode('cp1251')
    print('recived from: ', addr, ' data: ', loc_data)
    answer = 'answer to ' + addr[0] + ' echo: ' + loc_data
    uServSock.sendto(answer.encode(), addr)

    if data == '1':
        break

uServSock.close()
