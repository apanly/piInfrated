#!/usr/bin/python
# -*- coding: utf-8 -*-
import serial
class infrared():
    def __init__(self,port):
        self.init(port)
    def init(self,port):
        self.ser= serial.Serial()
        self.ser.baudrate=9600
        self.ser.port=port
        self.ser.timeout=1
        self.ser.open()
    def read(self):
        retval=''
        while 1:
            if self.ser.inWaiting():
                val = self.ser.read(self.ser.inWaiting())
                retval= val.encode('hex')
                break;
            else:
                pass
                #print 'wating'
        print "返回命令:%s"%retval
        return retval
        #print self.ser.read(5)
    #转化为16禁止

    def write(self,s):
        print "输入命令:%s"%s
        s=self.toHexStr(s)
        self.ser.write(s)
        #print s
        #print '---'
    def toHex(self,s):
        lst = []
        for ch in s:
            hv = hex(ord(ch)).replace('0x', '')
            if len(hv) == 1:
                hv = '0'+hv
            lst.append(hv)
        return reduce(lambda x,y:x+y, lst)
    #获取16进制字符串
    def toHexStr(self,s):
        if(len(s)%2!=0):
            s=s[0:-1]+'0'+s[-1]
        return s.decode("hex")