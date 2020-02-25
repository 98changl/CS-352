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
    return NULL

def server(table, tsListenPort):
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', tsListenPort)
    ts.bind(server_binding)
    
    ts.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    
    # connect with client
    csockid, addr = ts.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    
    # recieve client input
    data_from_client = cssockid.recv(100)
    
    # translate client message into DNS table format
    hostname = data_from_client

    # search for hostname
    result = search(table, hostname)
    
    # reply to client
    if result == NULL:
        # send error message to client
        msg = data_from_client + " - ERROR: HOST NOT FOUND"
        csockid.send(msg.encode('utf-8'))
    else:
        # send node data as a string to client
        msg = result.hostname + " " + result.address + " " + result.flag
        csockid.send(msg.encode('utf-8'))
    
    # close the server socket
    ts.close()
    exit()

def main():
    if len(sys.argv) < 1:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    args = str(sys.argv)
    print args
    tsListenPort = args[0]
    
    # read in file
    f = open ("PROJI-DNSTS.txt", "r")
    
    # set up DNS table
    table = []
    read = f.readlines()
    
    
    # populate the DNS table with values
    for line in read:
        # splits the read in string into an array of its elements
        inputs = line.split()
        
        # check to see if the split is valid
        print(inputs)
        
        # set up variables
        hostname = inputs[0]
        address = inputs[1]
        flag = inputs[2]
        
        # add the variables into the DNS table 
        table.append( DNSnode(hostname, address, flag) )
    
    # run the server
    server(table, tsListenPort)
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
