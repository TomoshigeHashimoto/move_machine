import socket

bind_host="0.0.0.0"
bind_port=50000

#AF_INETで、IPv4,   SOCK_STREAMで、TCP プロトコルを利用
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_host, bind_port))
server.listen(5)
print("host: "+bind_host)
print("port: "+str(bind_port))

while True:
    client, addr=server.accept()
    print("from:"+ addr[0]+" "+str(addr[1]))
    while True:
        print("waiting for client response...")
        rec=client.recv(1024)
        print(">"+rec.decode('utf-8'))

        res=input()  #python3
        #res=raw_input()  #python2

        client.send(res.encode('utf-8'))
        if len(rec)==0:
            client.close()
            break