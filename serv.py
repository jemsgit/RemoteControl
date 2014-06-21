# -*- coding: utf-8 -*-

import socket, os
from Tkinter import *

PORT = 9092
if_run = False
TEXT_RUN = "Run Server"
TEXT_STOP = "Stop Server"


wind = Tk()
a = []
wind.title("Server")
wind.geometry("300x50")



def toggle_server():
    global if_run, sock, conn
    if if_run == False:
        b.configure(text = TEXT_STOP)
        sock = socket.socket()
        sock.bind(('', 9092))
        sock.listen(1)
        conn, addr = sock.accept()
        addrnew = (addr[0:1], ":", addr[1:2])

        print 'connected:', addr
        print conn
        w1 = Label(wind, fg = "red", justify = "right" , padx = 10, pady = 10, font = "Times", text = addrnew).pack(side="right")

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
        if_run = False
    return if_run

b = Button(wind, text = TEXT_RUN, command=toggle_server)
b.pack()
b.place(x = 10, y = 10)
wind.mainloop()

os.system(a[0])
