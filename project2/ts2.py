import threading
import time
import random

import socket
import sys

def server(table, ts2ListenPort):
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #server_binding = ("localhost", tsListenPort)
    ts2.bind( ('', ts2ListenPort) )
    print("[S]: Server bind created")
    
    ts2.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    # connect with ls server
    ls, addr = ts2.accept()
    print ("[S]: Got a connection request from a ls server at {}".format(addr))
        
    while True:
        # recieve ls input
        data = ls.recv(100)
        msg = ""

        # search for hostname
        for line in table:
            # splits the read in string into an array of its element
            node = line.split()

            if node[0] == data:
                msg = node[0]
                break

        # reply to ls
        if msg != "":
            #print(msg)
            ls.send(msg.encode('utf-8'))
        # server sends nothing on failure
    
    # close the server socket
    ts2.close()
    exit()

def main():
    if len(sys.argv) < 1:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    arg = sys.argv[1]
    ts2ListenPort = int(arg)
    
    # read in file
    f = open("PROJ2-DNSTS2.txt", "r")
    
    # set up DNS table
    table = []
    read = f.readlines()
    
    # populate the DNS table with values
    for line in read:
        table.append( line.strip() );
    
    # run the server
    server(table, ts2ListenPort)
    exit()
    
if __name__ == "__main__":
    main()
