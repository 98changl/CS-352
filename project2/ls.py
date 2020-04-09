import threading
import time
import random

import socket
import sys

def server(lsListenPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort):
    try:
        ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    # server_binding = ('', rsListenPort)
    ls.bind( ('', lsListenPort) )
    print("[S]: Server bind created")
    
    ls.listen(10)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))

    
    # create socket connections with ts1
    try:
        ts1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    
    ts1.bind( (ts1Hostname, ts1ListenPort) )
    print("[S]: ts1 server bind created")
    
    # create socket connections with ts2
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    
    ts2.bind( (ts2Hostname, ts2ListenPort) )
    print("[S]: ts2 server bind created")

    # accept all socket requests
    csockid, addr = ls.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))
    ts1sockid, addr = ts1.accept()
    print ("[S]: Got a connection request from a ts server at {}".format(addr))
    ts2sockid, addr = ts2.accept()
    print ("[S]: Got a connection request from a ts server at {}".format(addr))
    
    # loop for processing data
    while true:
        # recieve a node from client
        data_from_client = csockid.recv(100)
        
        # client needs to send something to indicate end, or implement a timer mechanic 
        if data_from_client == ""
            break;

        ts1sockid.settimeout(5)
        ts2sockid.settimeout(5)
        
        # send data to servers
        ts1sockid.send( data_from_client ) 
        ts2sockid.send( data_from_client )


        
        data_from_ts1 = ts1sockid.recv(100)
        # need to implement time delay function here
        data_from_ts2 = ts2sockid.recv(100)
        
        # check server results and reply to client
        if data_from_ts1 != "":
            # forward response to client
            msg = data_from_ts1
            print (msg)
            csockid.send(msg.encode('utf-8'))
         
        if data_from_ts2 != "":
            # forward response to client
            msg = data_from_ts2
            print (msg)
            csockid.send(msg.encode('utf-8'))
        else:
            # send an error message
            msg = data_from_client + " - ERROR: HOST NOT FOUND"
            print (msg)
            csockid.send(msg.encode('utf-8'))

    # close all sockets    
    ls.close()
    ts1.close()
    ts2.close()
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
