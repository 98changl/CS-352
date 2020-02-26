import threading
import time
import random

import socket
import sys


class DNSnode:
    def __init__(self, hostname, address, flag):
        self.hostname = hostname
        self.address = address
        self.flag = flag

def search(table, hostname):
    for node in table:
        if node.hostname == hostname:
            return node.hostname, node.address, node.flag
    return -1

def server(table, rsListenPort):
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', rsListenPort)
    rs.bind(server_binding)

    rs.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))


    while True:
        csockid, addr = rs.accept(100)
        print ("[S]: Got a connection request from a client at {}".format(addr))


        data_from_client = csockid.recv(100)

        hostname = data_from_client

        result = search(table, hostname)


        if result =-1:
            msg= 'TS' + hostname +' '+ "- NS"
            print(msg)
            csockid.send(msg.encode('utf-8'))
        else:
            msg= result
            csockid.send(msg.encode('utf-8'))


    #closś the server socket    
    rs.Close()
    exit()

    def main():
    if len(sys.argv) < 1:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    args = str(sys.argv)
    print args ("Argument:" + args)
    rsListenPort = args[0]
    
    # read in file
    f = open ("PROJI-DNSRS.txt", "r")
    
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
