# -*- coding: utf-8 -*-

import socket, os, string, subprocess, Image, ImageTk
from Tkinter import *
from random import choice


a = []
PORT = 9092
if_run = False
TEXT_RUN = "Run Server"
TEXT_STOP = "Stop Server"
passwd = '1234'
#passwd = ''.join([choice(string.letters + string.digits) for i in range(5)])

# ----- Make window
wind = Tk()
wind.title("Server")
wind.geometry("300x80")
img = PhotoImage(file='/usr/share/remjem/icon.gif')
wind.tk.call('wm', 'iconphoto', wind._w, img)


# ----- Get IP Host

sock = socket.socket()
sock.connect(("google.com",80))
TextPrint2 = "Host IP : " + sock.getsockname()[0]
TextPrint = "Passwod is : " + passwd
sock.close()


# ----- Print Info

l = Label(wind, fg = "red", justify = "right" , padx = 10, font = "Times", text = TextPrint)
l.pack()
wind.update()

lal = Label(wind, fg = "blue", padx = 10,  font = "Times", text = TextPrint2)
lal.pack()
wind.update()


def toggle_server():
    global if_run, conn, passwd, sock
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
               os.system(a[-1])
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
b.place(x = 100, y = 50)

wind.mainloop()

        

