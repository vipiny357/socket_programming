import socket 
import sys

def create_socket():
    try:
        global host
        global port
        global s
        host=""
        port=9999
        s=socket.socket()
    except socket.error as e:
        print("socket error"+str(e))

def bind_socket():
    try:
        global host
        global port
        global s

        print("Binding Port: "+str(port))

        s.bind((host,port))
        s.listen(5)

    except socket.error as e:
        print("socket bind error"+str(e)+"\n"+"Retrying...")
        bind_socket()

def  socket_accept():
    conn,addr=s.accept()
    print("connection with: "+str(addr[0])+" :IP"+" and "+str(addr[1])+" :port")
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd=input()
        if cmd=="quit":
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_reesponse =str(conn.recv(1024),'utf-8')
            print(client_reesponse,end="")


def main():
    create_socket()
    bind_socket()
    socket_accept()

main()



