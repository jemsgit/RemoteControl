# -*- coding: utf-8 -*-

import socket, os
from Tkinter import *

wind = Tk()
a = []
wind.title("Server")
wind.geometry("300x50")



def runserv():
    sock = socket.socket()
    sock.bind(('', 9092))
    sock.listen(1)
    conn, addr = sock.accept()
#    addr = str(addr)
    addrnew = (addr[0:1], ":", addr[1:2])

    print 'connected:', addr
    w1 = Label(wind, fg = "red", justify = "right" , padx = 10, pady = 10, font = "Times", text = addrnew).pack(side="right")

    while True:
        data = conn.recv(1024)
        a.append(data)
        print a[-1]
        if not data:
            break
        conn.send(data)




b = Button(wind, text = "Run Server", command=runserv).place(x = 10, y = 10)


wind.mainloop()

os.system(a[0])
