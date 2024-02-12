
from tkinter import *
from tkinter import  filedialog, messagebox,font
from PIL import Image, ImageTk
from tkinter import ttk
global Note
import webbrowser
from datetime import datetime
import os
root=Tk()
root.geometry("1120x560")
root.title("*Untitled-Notepad")
path = "E:/python/image/note.png"
load = Image.open(path)
render = ImageTk.PhotoImage(load)
root.iconphoto(True, render)
frame=Frame()
frame.pack(side="top", fill="both", expand = True)
FILE=None
def show_options():
    def file():
        if text.get("1.0",END).strip(): 
            win=Tk()
            win.geometry("300x180")
            win.resizable(False,False)
            style = ttk.Style()
            style.configure("Rounded.TButton",padging=20)
           
            frame=Frame(win, bg="white", width=300, height=100)
            frame.place(x=0,y=0)
            label=Label(frame,font=("Helvitica",12),bg="white",text="Do you want to save changes to Utitiled?")
            label.place(x=10,y=40)
            def yes():
                save()
                win.destroy()
                root.destroy()
            butt=ttk.Button(win,style="Rounded.TButton",text="save",command=yes)
            butt.place(x=20,y=120)
            def dont():
                root.destroy()
                win.destroy()
            butt2=ttk.Button(win,style="Rounded.TButton",text="Don'tsave",command=dont)
            butt2.place(x=110,y=120)
            def close():
                win.destroy()
            butt3=ttk.Button(win,style="Rounded.TButton",text="close",command=close)
            butt3.place(x=200,y=120)
            
            
            win.mainloop
            

    def new():
        global file
        file=None
        text.delete(1.0,END)
        
    def openfile():
        file_path = filedialog.askopenfilename(defaultextension=".txt",filetypes=[("Text files", "*.txt"), ("All files", "*.*")],title="Select a File")
        if file_path:
            try:
                with open(file_path, 'r') as f:
                    file_content = f.read()
                    text.insert(END, file_content)
            except Exception as e:
                print(e)
                print("File can't be read")

    def save():
        file_path = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, "w") as f:
                f.write(text.get(1.0, "end"))
            root.title(os.path.basename(file_path) + " - Notepad")
  
    def saveas():
        file_path = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        f=open(file,"w")
        f.write(text.get(1.0,END))
        f.close()
    def paste():
        text.event_generate("<<Paste>>")
       
    # Create a new menu
    menu = Menu(root, tearoff=0)
    menu.add_command(label="New file",accelerator="ctr+n",command=file)
    menu.add_command(label="New window",accelerator="ctr+shift+n",command=new)
    menu.add_command(label="open",accelerator="ctr+o",command=openfile)
    menu.add_command(label="save",accelerator="ctr+s",command=save)
    menu.add_command(label="saveas",accelerator="ctr+shift+s",command=save)
    menu.add_command(label="paste",accelerator="ctrl+p",command=paste)
    menu.post(but.winfo_rootx(), but.winfo_rooty() + but.winfo_height())
    
    # Display the menu at the location of the button
    
def edit():
    def undo(): 
        pass
    def cut():
        text.event_generate("<<Cut>>")
    def copy():
        text.event_generate("<<Copy>>")
    def paste():
        text.event_generate("<<Paste>>")
    def delete():
        message = messagebox.askquestion('Notepad',"Do you want to Delete all")
        if message == "yes":
                text.delete('1.0','end')
        else:
               return "break"
    def select_all():
        text.tag_add('sel','1.0','end')
        return 'break'
    def time():
       d = datetime.now()
       text.insert('end',d)
        
            # Create a new menu
    menu = Menu(root, tearoff=0)
    menu.add_command(label="Undo",accelerator="Ctrl+Z",command=undo)
    menu.add_command(label="cut" , accelerator="ctr+x",command=cut)
    menu.add_command(label="copy",accelerator="ctr+c",command=copy)
    menu.add_command(label="paste ",accelerator="ctr+p",command=paste)
    menu.add_command(label="delete  ",accelerator= "Del",command=delete)
    menu.add_command(label="find ",command="paste")
    menu.add_command(label="findnext",accelerator="F3",command=paste)
    menu.add_command(label="findprevious",accelerator= "shift+F3",command=paste)
    menu.add_command(label="replace ",accelerator= "ctrl+H",command=paste)
    menu.add_command(label="Go To ",accelerator="ctrl+G",command=paste)
    menu.add_command(label="Select all",accelerator="ctrl+A",command=select_all)
    menu.add_command(label="Timne/Date",accelerator="F5",command=time)
    

    # Display the menu at the location of the button
    menu.post(but.winfo_rootx(), but.winfo_rooty() + but.winfo_height())
def view():
    def zoom():
        pass
    def status():
        pass
    def Wordwarp():
        pass
    menu = Menu(root, tearoff=0)
    menu.add_command(label="Zoom",command=zoom)
    menu.add_command(label="Status",command=status)
    menu.add_command(label="Wordwarp",command=Wordwarp)
     # Display the menu at the location of the button
    menu.post(but.winfo_rootx(), but.winfo_rooty() + but.winfo_height())

def formate():
    global fonts
    def fonts():
        root = Tk()
        root.geometry('350x200')
        root.title('Font')

        l1 = Label(root,text="Font:")
        l1.place(x=10,y=10)
        f = StringVar() 
        fonts = ttk.Combobox(root, width = 15, textvariable = f, state='readonly',font=('verdana',10,'bold'),) 
        fonts['values'] = font.families()
        fonts.place(x=10,y=30)
        fonts.current(0) 


        l2 = Label(root,text="Font Style:")
        l2.place(x=180,y=10)
        st = StringVar() 
        style = ttk.Combobox(root, width = 15, textvariable = st, state='readonly',font=('verdana',10,'bold'),) 
        style['values'] = ('bold','bold italic','italic')
        style.place(x=180,y=30)
        style.current(0) 

        l3 = Label(root,text="Size:")
        l3.place(x=350,y=10)
        sz = StringVar() 
        size = ttk.Combobox(root, width = 2, textvariable = sz, state='readonly',font=('verdana',10,'bold'),) 
        
        size['values'] = (8,9,10,12,15,20,23,25,27,30,35,40,43,47,50,55,65,76,80,90,100,150,200,255,300)
        size.place(x=350,y=30)
        size.current(0) 
        def OK():
            text['font'] = (fonts.get(),size.get(),style.get())
            root.destroy()
           
        
        ok = Button(root,text="OK",relief=RIDGE,borderwidth=2,padx=20,highlightcolor="blue",command=OK)
        ok.place(x=60,y=100)

        def Cnl():
                root.destroy()

        cancel = Button(root,text="Cancel",relief=RIDGE,borderwidth=2,padx=20,command=Cnl)
        cancel.place(x=150,y=100)
        root.mainloop()
   
    menu = Menu(root, tearoff=0)
    menu.add_command(label="fonts",command=fonts)
    menu.post(but.winfo_rootx(), but.winfo_rooty() + but.winfo_height())
def help():
    def view_help():
        messagebox.showinfo("HELP  SUPPORT","""Help & Support Note Pad

The Help & Support Note Pad app is your digital companion for efficient troubleshooting and problem-solving. Capture, categorize, and organize your technical notes with ease. From jotting down issues to documenting solutions, this app streamlines your support process, ensuring you never miss a beat. Simplify your troubleshooting efforts and stay organized with Help & Support Note Pad.""")
# feedbac
    def send_feedback():
        webbrowser.open('https://www.facebook.com/nabin.chaudhary.9862273')
    def about():
        messagebox.showinfo("note pad","Note pad by Nabin Tharu  v 1.0 BETA")
        
    
    menu = Menu(root, tearoff = 0)
    menu.add_command(label="View Help", command=view_help)
    menu.add_command(label="Send FeedBack",command=send_feedback)
    menu.add_command(label="About Notepad",command=about)
    menu.post(but.winfo_rootx(), but.winfo_rooty() + but.winfo_height())


def undo(): 
    pass
def cut():
       text.event_generate("<<Cut>>")
def copy():
    text.event_generate("<<Copy>>")
def paste():
    text.event_generate("<<Paste>>")
def delete():
    message = messagebox.askquestion('Notepad',"Do you want to Delete all")
    if message == "yes":
            text.delete('1.0','end')
    else:
           return "break"
def select_all():
    text.tag_add('sel','1.0','end')
    return 'break'
def time():
   d = datetime.now()
   text.insert('end',d)   
def auto_click3(event):
    but3.invoke()    
def auto_click1(event):
    but.invoke()
def auto_click5(event):
    but5.invoke()
but=Button(frame,font=("consolas",11),text="File",border=0,command=show_options)
but.place(x=0,y=0)
def auto_click(event):
    but2.invoke()
but2=Button(frame,font=("consolas",11),text="Edit",border=0,command=edit)
but2.place(x=45,y=0)
but3=Button(frame,font=("consolas",11),text="Format",border=0,command=formate)
but3.place(x=90,y=0)
def auto_click4(event):
    but4.invoke()   
but4=Button(frame,font=("consolas",11),text="View",border=0,command=view)
but4.place(x=150,y=0)
but5=Button(frame,font=("consolas",11),text="Help",border=0,command=help)
but5.place(x=200,y=0)
but2.bind('<Enter>', auto_click)
but.bind('<Enter>', auto_click1)
but4.bind('<Enter>',auto_click4)
but3.bind('<Enter>',auto_click3)
but5.bind('<Enter>',auto_click5)

global text
text=Text(frame,font=('consolas',12))
text.pack(fill="both",expand=True,pady=47)
scroll=Scrollbar(text)
scroll.pack(side=RIGHT,fill=Y)
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)



#  Right Click Menu

m = Menu(root, tearoff = 0)
m.add_command(label ="Select All",accelerator="Ctrl+A",command=select_all) 
m.add_command(label ="Cut",accelerator="Ctrl+X",command=cut) 
m.add_command(label ="Copy",accelerator="Ctrl+C",command=copy) 
m.add_command(label ="Paste",accelerator="Ctrl+V",command=paste) 
m.add_command(label ="Delete",accelerator="Del",command=delete) 
m.add_separator() 
m.add_command(label ="Undo",accelerator="Ctrl+Z",command=text.edit_undo)
m.add_command(label ="Redo",accelerator="Ctrl+Z",command=text.edit_redo) 
  
def do_popup(event): 
    try: 
        m.tk_popup(event.x_root, event.y_root) 
    finally: 
        m.grab_release() 
  
root.bind("<Button-3>", do_popup) 




root.mainloop()
