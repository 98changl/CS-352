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

    def _str_(self):
        return str(self.hostname,self.address, self.flag)

def search(table, hostname):
    for item in table:
        if item.hostname == hostname:
            return item
    return -1


def server(table, rsListenPort):
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    #server_binding = ('', rsListenPort)
    rs.bind( ('', rsListenPort) )
    print("[S]: Server bind created")


    rs.listen(10)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    #csockid, addr = rs.accept()


    while True:
        csockid, addr = rs.accept()
        print ("[S]: Got a connection request from a client at {}".format(addr))


        data_from_client = csockid.recv(100)
        #print("print the data line 47"+ data_from_client)

        hostname = data_from_client
        #print("printing the host name line 50" + hostname)

        result = search(table, data_from_client)
        print(result)


        if result == -1:
            msg= socket.gethostname() +' '+ "- NS"
            print(msg)
            csockid.send(msg.encode('utf-8'))
        else:
            msg= result
            print(msg)
            csockid.send(msg.encode('utf-8'))


    #close the server socket    
    rs.close()
    exit()

def main():
    if len(sys.argv) < 1:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    arg = sys.argv[1]
    rsListenPort = int(arg)
    print (rsListenPort)
    
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
        #print(inputs)
        
        # set up variables
        hostname = inputs[0]
        address = inputs[1]
        flag = inputs[2]
        
        # add the variables into the DNS table 
        table.append( DNSnode(hostname, address, flag) )
        print(table)
    
    # run the server
    server(table, rsListenPort)
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
