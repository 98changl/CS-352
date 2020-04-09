
import threading
import time
import random

import socket
import sys

# object to store three variables
class DNSnode:
    def __init__(self, hostname, address, flag):
        self.hostname = hostname
        self.address = address 
        self.flag = flag

def search(table, hostname):
    for node in table:
        if node.hostname == hostname:
            return node
    return -1

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


    
    while True:
        # connect with client
        csockid, addr = ts2.accept()
        print ("[S]: Got a connection request from a client at {}".format(addr))
    
        # recieve client input
        data_from_client = csockid.recv(100)
    
        # translate client message into DNS table format
        hostname = data_from_client

        # search for hostname
        result = search(table, hostname)
    
        # reply to client
        if result == -1:
            # send error message to client
            break
        else:
            # send node data as a string to client
            msg = result.hostname + " " + result.address + " " + result.flag
            print(msg)
            csockid.send(msg.encode('utf-8'))
    
    # close the server socket
    ts2.close()
    exit()

def main():
    if len(sys.argv) < 1:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    arg = sys.argv[1]
    ts2ListenPort = int( arg )
    
    
    # read in file
    f = open("PROJ2-DNSTS2.txt", "r")
    
    # set up DNS table
    table = []
    
    read = f.readlines()
    
    # populate the DNS table with values
    for line in read:
        # splits the read in string into an array of its elements
        inputs = line.split()
        
        # check to see if the split is valid
        #print(inputs)
        
        # set up variables
        hostname = inputs[0]
        address = inputs[1]
        flag = inputs[2]
        
        # add the variables into the DNS table 
        table.append( DNSnode(hostname, address, flag) )
    
    # run the server
    server(table, ts2ListenPort)
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
