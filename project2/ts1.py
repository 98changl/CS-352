import threading
import time
import random

import socket
import sys

def search(table, hostname):
    for line in table:
        # splits the read in string into an array of its elements
        node = line.split()
        
        # check to see if the split is valid
        #print(inputs)
        
        # set up variables
        name = node[0]
        
        if name == hostname:
            return line
    return ""

def server(table, ts1ListenPort):
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #server_binding = ("localhost", tsListenPort)
    ts1.bind( ('', ts1ListenPort) )
    print("[S]: Server bind created")
    
    ts1.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    # connect with ls server
    ls, addr = ts1.accept()
    print ("[S]: Got a connection request from a ls server at {}".format(addr))
        
    while true:
        # recieve ls input
        data = ls.recv(100)
        
        # search for hostname
        msg = search(table, data)
    
        # reply to ls
        if msg == "":
            # send error message to client
            break
        else:
            # send node data as a string to client
            print(msg)
            ls.send(msg.encode('utf-8'))
    
    # close the server socket
    ts1.close()
    exit()

def main():
    if len(sys.argv) < 1:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    arg = sys.argv[1]
    tsListenPort = int(arg)
    
    # read in file
    f = open("PROJ2-DNSTS1.txt", "r")
    
    # set up DNS table
    table = []
    read = f.readlines()
    
    # populate the DNS table with values
    for line in read:
        table.append(line);
    
    # run the server
    server(table, ts1ListenPort)
    exit()
    
if __name__ == "__main__":
    main()
    #t1 = threading.Thread(name='server', target=server)
    #t1.start()

    #time.sleep(random.random() * 5)
    #t2 = threading.Thread(name='client', target=client)
    #t2.start()

    #time.sleep(5)
    print("Done.")
