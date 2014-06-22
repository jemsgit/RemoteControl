# -*- coding: utf-8 -*-

import socket, os, string
from Tkinter import *
from random import choice

PORT = 9092
if_run = False
TEXT_RUN = "Run Server"
TEXT_STOP = "Stop Server"

size = 5
passwd = ''.join([choice(string.letters + string.digits) for i in range(size)])
TextPrint = passwd

wind = Tk()
a = []
wind.title("Server")
wind.geometry("300x60")


l = Label(wind, fg = "red", justify = "right" , padx = 10, pady = 10, font = "Times", text = TextPrint)
l.pack(side="right")
wind.update()


def toggle_server():
    global if_run, conn, passwd
    if if_run == False:

        TextPrint = passwd + " : " "Waiting.."
        l[ "text" ] =  TextPrint
        wind.update()

        b.configure(text = TEXT_STOP)
        sock = socket.socket()
        sock.bind(('', 9092))
        sock.listen(1)
        conn, addr = sock.accept()
        addrnew = (addr[0:1], ":", addr[1:2])
        

        data = conn.recv(1024)
        a.append(data)
        print a[-1]
        if passwd != a[-1]:
            b.configure(text = TEXT_RUN)
            conn.send("Bad Password")
            conn.close();
            TextPrint = "Bad Password"
            l[ "text" ] =  TextPrint
            wind.update()
            if_run = False

        else:
           print 'connected:', addr
           conn.send(a[-1])
           TextPrint = addrnew
           l[ "text" ] =  TextPrint
           wind.update()
           if_run = True

           while True:
               data = conn.recv(1024)
               a.append(data)
               print a[-1]
               if not data:
                   break
               conn.send(data)
           if_run = True 

    else:
        b.configure(text = TEXT_RUN)
        conn.close();
        TextPrint = ""
        l[ "text" ] =  TextPrint
        wind.update()

        if_run = False
    return if_run

b = Button(wind, text = TEXT_RUN, command=toggle_server)
b.pack()
b.place(x = 10, y = 15)
wind.mainloop()

os.system(a[0])
