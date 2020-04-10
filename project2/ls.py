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
        ts1.settimeout(5)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
    
    ts1.bind( (ts1Hostname, ts1ListenPort) )
    print("[S]: ts1 server bind created")
    
    # create socket connections with ts2
    try:
        ts2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ts2.settimeout(5)
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
            print ("Data from client ended")
            break;

        # send data to servers
        ts1sockid.send( data_from_client ) 
        ts2sockid.send( data_from_client )
        
        try:
            data_from_ts1 = ts1sockid.recv(100)
        
            # check server results and reply to client
            if data_from_ts1 != "":
                # forward response to client
                msg = data_from_ts1
                print (msg)
                csockid.send(msg.encode('utf-8'))
                continue
              
        except ts1sockid.timeout:
            print ("timeout 1")
            data_from_ts1 = ""
        
        try:
            data_from_ts2 = ts2sockid.recv(100)
            
            # check server results and reply to client
            if data_from_ts2 != "":
                # forward response to client
                msg = data_from_ts2
                print (msg)
                csockid.send(msg.encode('utf-8'))
                continue
              
	    except ts2sockid.timeout:
            print ("timeout 2")
            data_from_ts2 = ""
            
        if data_from_ts1 = ""
            if data_from_ts2 = ""
                msg = data_from_client + " - ERROR: HOST NOT FOUND"
                print(msg)
                csockid.send(msg.encode('utf-8'))
            
    # close all sockets    
    ls.close()
    ts1.close()
    ts2.close()
    exit()

def main():
    if len(sys.argv) < 5:
        print('not enough arguments error: {} \n'.format(err))
        exit()
    
    # read in arguments from command
    lsListenPort = int(sys.argv[1])
    print (lsListenPort)
    
    ts1Hostname = str(sys.argv[2])
    print (ts1Hostname)
    
    ts1ListenPort = int(sys.argv[3])
    print (ts1ListenPort)
    
    ts2Hostname = str(sys.argv[4])
    print (ts2Hostname)
    
    ts2ListenPort = int(sys.argv[5])
    print (ts2ListenPort)
    
    # run the server
    server(lsListenPort, ts1Hostname, ts1ListenPort, ts2Hostname, ts2ListenPort)
    exit()

if __name__ == "__main__":
    main()
