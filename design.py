import socket
import time
import threading
from tkinter import*

root=Tk()
root.geometry("300x500")
root.config(bg="white")


def func():
    t1=threading.Thread(target=recv)
    t1.start()

def recv():
    listensocket=socket.socket()
    port=2090
    maxconnection=10
    ip=socket.gethostname()
    print(ip)
    print("connected")

    listensocket.bind(('',port))
    listensocket.listen(maxconnection)
    (clientsocket,address)=listensocket.accept()


    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbox.insert(0,"client : "+sendermessage)

x=0
def sendmsg():
    global x,s
    if x==0:
        s=socket.socket()
        hostname='DESKTOP-V4E1IG2'#your desktop name
        port=2090
        s.connect((hostname,port))
        msg=messagebox.get()
        lstbox.insert(0,"you :"+msg)
        s.send(msg.encode())
        x=x+1
    else:
        msg=messagebox.get()
        lstbox.insert(0,"you:"+msg)
        s.send(msg.encode())

        
def threadmsg():
    th=threading.Thread(target=sendmsg)
    th.start()


startimage=PhotoImage(file='startimg2.png')
b1=Button(root,image=startimage,command=func,borderwidth=0)
b1.place(x=90,y=10)

message=StringVar()
messagebox=Entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)

sendmessage=PhotoImage(file='send1.png')
sendbutton=Button(root,image=sendmessage,command=threadmsg,borderwidth=0)
sendbutton.place(x=260,y=440)

lstbox=Listbox(root,height=20,width=43)
lstbox.place(x=15,y=80)



root.mainloop()