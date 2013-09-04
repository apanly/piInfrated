#!/usr/bin/python
# -*- coding: utf-8 -*-
import zmq
from infraredTh import infrared
from mapping import codemapping
if __name__=="__main__":
    PORT='/dev/ttyUSB0'
    target=infrared(PORT)
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    codemap=codemapping()
    while True:
        cmd = socket.recv()#cmd=raw_input('Enter Command:');
        if(len(cmd)>0):
            if(cmd=='quit'):
                socket.disconnect("tcp://*:5555")
                exit(0)
            else:
                target.write(cmd)
                response=target.read()
                socket.send(codemap.codetomsg(response))
        else:
            socket.send("fail")



