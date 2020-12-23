import socket

target_host="10.9.95.21" #塩谷のIPアドレス
target_port=50000

client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))

while True:
    str=input()   #python3
    #str=raw_input()   #python2

    client.send(str.encode('utf-8'))
    print("waiting for server response...")
    response=client.recv(4096)
    print(">"+response.decode('utf-8'))