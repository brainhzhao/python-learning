#!/usr/bin/python
# -*-coding:utf-8 -*-

from socket import *
import time


class SendMessage(object):
    """
       send network message to remote server
    """
    def __init__(self,host,port):
        self.inet_address=(host,port)

    """
      send message by udp
      data send message
      count 发送次数
      batch_count 发送总次数
    """
    def send_by_udp(self,data,count,batch_count):
        udp_sock_cli = socket(AF_INET,SOCK_DGRAM)
        while count:
            for i in range(0,batch_count):
                udp_sock_cli.sendto(data.encode("utf-8"),self.inet_address)
            count=count-1
            time.sleep(5)
            print("send to server success %s",count)