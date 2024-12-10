from tkinter import*
root=Tk()
root.title("login page")
root.geometry('300x200')


snap_logo = PhotoImage(file="c:/spectrum/snapchat_logo.gif.png")


logo_label =Label(root, image=snap_logo)
logo_label.pack(pady=70) 

lbl=Label(root,text="Log in",font=("arial",20))
lbl.place(x=725,y=300)

lbl=Label(root,text="username or Email",font=("normal",10))
lbl.place(x=630,y=360)


entry=Entry(bg="white",fg="black",width=42)
entry.place(x=635,y=390)

lbl=Label(root,text="password",font=("normal",10))
lbl.place(x=630,y=410)

entry=Entry(bg="white",fg="black",width=42)
entry.place(x=635,y=440)

lbl=Label(root,text="Forgot password",font=("normal",10))
lbl.place(x=790,y=460)

btn=Button(root,text="Login",font=("ariel",10),bg=("yellow"), fg=("black"))
btn.place(x=730,y=520)



root.mainloop()

