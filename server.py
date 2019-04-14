'''

    py-chatroom
    server.py

'''

import socket, datetime
from _thread import *

ipv4 = "0.0.0.0"
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ipv4, port))
s.listen(5)

users = []


def prefix(): print("<%s> " % datetime.datetime.now().strftime("%H:%M:%S"), end="")


def client_thread(conn, addr):
    while True:
        data = conn.recv(4096)
        if not data:
            break
        else:
            prefix()
            print(data.decode("utf-8"))

            for user in users: # send message to all of our users
                user.send(str.encode(data.decode("utf-8")))
    prefix()
    print("client disconnected: %s:%s" % (addr[0], addr[1]))
    conn.close()


def main():
    prefix()
    print("server listening on port: %s" % port)

    while True:
        conn, addr = s.accept()
        users.append(conn)
        prefix()
        print("client connected: %s:%s" % (addr[0], addr[1]))

        start_new_thread(client_thread, (conn, addr))


main()
