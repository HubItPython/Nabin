from tkinter import *
def hub():
    from tkinter import  Tk, Canvas, ttk,Entry,Label
    from customtkinter import CTkFrame
    from tkinter import filedialog
    from tkinter import messagebox
    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    root = Tk()
    height = 700
    width = 1000
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 4) - (height // 4)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    root.resizable(False,False)
################database##########
    def database():
        db=Tk()
        db.title("Linkto your database")
        data_frame = LabelFrame(db, text="",height=200)
        data_frame.pack(fill="x", expand="yes", padx=20)
        hs_label = Label(data_frame, text="Host")
        hs_label.grid(row=0, column=0, padx=10, pady=10)
        hs_entry = Entry(data_frame)
        hs_entry.grid(row=0, column=1, padx=10, pady=10)
        
        u_label = Label(data_frame, text="User")
        u_label.grid(row=0, column=2, padx=10, pady=10)
        u_entry = Entry(data_frame)
        u_entry.grid(row=0, column=3, padx=10, pady=10)
        
        pasw_label = Label(data_frame, text="Password")
        pasw_label.grid(row=0, column=4, padx=10, pady=10)
        pasw_entry = Entry(data_frame)
        pasw_entry.grid(row=0, column=5, padx=10, pady=10)


        def link():
            global host1
            global user1
            global password1
            host1=hs_entry.get()
            user1=u_entry.get()
            password1=pasw_entry.get()
            try:
                import mysql.connector
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}")
                cur = con.cursor()
                #Execute a SELECT query
                database_name="student"
                create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
                cur.execute(create_database_query)  
                cur.close()
                con.commit()
                con.close()
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                cur = con.cursor()
                #Execute a SELECT query
                create_database_query = ("""create table if not exists form (
                                        id int auto_increment primary key,FullName varchar(225),Address varchar(225),Cellno int,Date varchar(50),GaurdiansName varchar(225),PhoneNo int,Email varchar(225),Gender varchar(225),DateOfBirth varchar(255),LevelOfEducation varchar(50),Schoolorcollege varchar(225))
		                                """)
                cur.execute(create_database_query)
                con.commit()
                con.close() 
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                cur = con.cursor()
                #Execute a SELECT query
                create_database_query = ("""CREATE TABLE if not exists enroll(
                                        id int auto_increment primary key,course1 varchar(225),course2 varchar(225),course3 varchar(225),shifttime int,codinator varchar(225),student varchar(225),other varchar(225))
		                                """)
                cur.execute(create_database_query)
                con.commit()
                con.close() 
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                cur = con.cursor()
                #Execute a SELECT query
                create_database_query = ("""CREATE TABLE if not exists office(
                                        id int auto_increment primary key,Fullname varchar(225),Address varchar(225),DateOfBirth varchar(50),Refrence varchar(225),Refrencecontact int,Discount int,SourcesOfInformation varchar(225))
		                                """)
                cur.execute(create_database_query)
                con.commit()
                con.close() 
            except:
                messagebox.showinfo("cant connetc","unable to connect to the data base")
            db.destroy()
        



        button= ttk.Button(data_frame,text="connect",style="Rounded.TButton",command=link)
        button.grid(row=1, column=0, padx=10, pady=10)
        
     
        db.mainloop()
    def photo():
       from PIL import Image, ImageTk
       file_path = filedialog.askopenfilename(title="Select a File")
       if file_path:
        # Load and resize the image
           img = Image.open(file_path)
           img = img.resize((169, 150))

        # Convert the image to Tkinter PhotoImage format
           tk_img = ImageTk.PhotoImage(img)

        # Create a label in the frame and set the image
           label = Label(frame1, image=tk_img)
           label.image = tk_img  # Keep a reference to the image
           label.place(x=878, y=170)
       else:
            label.configure(text="image not found") 

    def sub():
################values###########
        try:
            import re
            import mysql.connector 
            fullname =headle.get()
            address=addrs.get()
            cell=cel.get()
            datee=date.get()
            gaurd=gaur.get()
            phohe=phon.get()
            Email= email.get()
            gend=genn.get()
            dateofb=dateb.get()
            educ=edu.get()
            cllz=clz.get()
            pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@gmail\.com$'
            if re.match(pattern,Email):
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            # Create a cursor object to execute SQL queries
                cursor = con.cursor()            
                # Execute an INSERT query
                query = "INSERT INTO form(FullName,Address,Cellno,Date,GaurdiansName,PhoneNo,Email,Gender,DateOfBirth,LevelOfEducation,Schoolorcollege) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                values = (fullname,address,cell,datee,gaurd,phohe,Email,gend,dateofb,educ,cllz)
                cursor.execute(query, values)
                # Commit the transaction
                con.commit()
                con.close()
            elif Email is not None and Email != "":
                messagebox.showinfo("Invalid Email", "Email is not valid")
            else:
                pass
       
#======    =   ======NAME OF COURSE/S TO ENROLL=============
            course1=cour1.get()
            course2 = cour2.get()
            course3 = cour3.get()
            shift1=shift.get()
            codinator=cod.get()
            student = stud.get()
            other = o.get()
            con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            # Create a cursor object to execute SQL queries
            cursor = con.cursor()
            query = "INSERT INTO enroll(course1,course2,course3,shifttime,codinator,student,other) VALUES (%s, %s, %s,%s, %s, %s,%s)"
            values = (course1,course2,course3,shift1,codinator,student,other)
            cursor.execute(query, values)
            # Commit the transaction
            con.commit()
            con.close()
            fulln=full.get()
            add=ad.get()
            dob1=dob.get()
            ref1=ref.get()
            refc1=refc.get()
            dis1=dis.get()
            sof1=sof.get()
            con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            # Create a cursor object to execute SQL queries
            cursor = con.cursor()
        
            query = "INSERT INTO office(Fullname,Address,DateOfBirth,Refrence,Refrencecontact,Discount,SourcesOfInformation) VALUES (%s, %s, %s,%s, %s, %s,%s)"
            values = (fulln,add,dob1,ref1,refc1,dis1,sof1)
            cursor.execute(query, values)
            con.commit()
            con.close()
            messagebox.showinfo("Success", "Record successfully saved.")
        except:
            messagebox.showerror('Error!', 'Please check all fields')


#==================detial=================
    def detial():
        root.destroy()
        def on_mousewheel_main(event):
            canvas_main.yview_scroll(int(-1 * (event.delta / 120)), "units")
        
        # Create the main window
        win = Tk()
        win.title("Nested Scrollable Frames")
        
        # Create the main scrollable canvas
        canvas_main = Canvas(win, bg="#cdfefe", width=1000, height=700, scrollregion=(0, 0, 1500, 1500))
        canvas_main.pack(side="left", fill="both", expand=True)
        
        # Add a vertical scrollbar for the main canvas
        scrollbar_main = ttk.Scrollbar(win, orient="vertical", command=canvas_main.yview)
        scrollbar_main.pack(side="right", fill="y")
        canvas_main.configure(yscrollcommand=scrollbar_main.set)
        
        # Create a frame inside the main canvas
        frame_main = ttk.Frame(canvas_main, width=1500, height=1500)
        canvas_main.create_window((0, 0), window=frame_main, anchor="nw")
        
        # Bind mouse wheel event to the main canvas
        canvas_main.bind_all("<MouseWheel>", on_mousewheel_main)

#=============================label===================================
        

        head = ttk.Label(frame_main, text="STUDENT ENROLLMENT REGISTRATION FORM",
                    font=("Arial", 25, "bold"),
                    background="#A1056A",
                    width=45,
                    anchor="center",
                    foreground="white")
        head.place(x=245, y=20)
#================================label2=====================================
        ttk.Label(frame_main, text="NAME OF COURSE/S TO ENROLL",
              font=("Arial", 25, "bold"),
             anchor="center",
             background="#A1056A",
             width=45,
             foreground="white").place(x=245, y=520)
        
#================================label3=====================================
        ttk.Label(frame_main, text="FOR OFFICE USE ONLY",
              font=("Arial", 25, "bold"),
             anchor="center",
             background="#A1056A",
             width=45,
             foreground="white").place(x=245,y=1000)

#--------------------create table if not exist--------------------
        


 #===================inner scrollable frame========================

     
#===================fetching============================================
        def data():
            import mysql.connector
            con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            cur = con.cursor()
            #Execute a SELECT query
            query = "SELECT * FROM form"
            cur.execute(query)  
            records = cur.fetchall()
            for ro in records:
                tree.insert(parent='',index='end',text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7],ro[8],ro[9],ro[10],ro[11]))
           # Create a Treeview Scrollbar
        #Fetch the result
        tree=ttk.Treeview(frame_main)
        tree.column("#0", width=0, stretch=NO)
        tree["column"]=("id","FullName","Address","Cellno","Date","GaurdiansName","PhoneNo","Email","Gender","DateOfBirth","LevelOfEducation","Schoolorcollege")
        tree.column("id",width=50,minwidth=50,anchor="center")
        tree.column("FullName",width=100,minwidth=50,anchor="center")
        tree.column("Address",width=100,minwidth=50,anchor="center")
        tree.column("Cellno",width=100,minwidth=70,anchor="center")
        tree.column("Date",width=80,minwidth=70,anchor="center")
        tree.column("GaurdiansName",width=105,minwidth=70,anchor="center")
        tree.column("PhoneNo",width=90,minwidth=70,anchor="center")
        tree.column("Gender",width=150,minwidth=150,anchor="center")
        tree.column("DateOfBirth",width=90,minwidth=70,anchor="center")
        tree.column("Email",width=150,minwidth=150,anchor="center")
        tree.column("LevelOfEducation",width=150,minwidth=150,anchor="center")
        tree.column("Schoolorcollege",width=140,minwidth=150,anchor="center")
        
        #===================heading=================================
        tree.heading("#0", text="", anchor=W)
        tree.heading("id",text="ID",anchor="center")
        tree.heading("FullName",text="FULLNAME",anchor="center")
        tree.heading("Address",text="ADDRESS",anchor="center")
        tree.heading("Cellno",text="CELLNO",anchor="center")
        tree.heading("Date",text="DATE",anchor="center")
        tree.heading("GaurdiansName",text="GAURDIAN'S NAME",anchor="center")
        tree.heading("PhoneNo",text="PHONENO",anchor="center")
        tree.heading("Gender",text="DATE OF BIRTH",anchor="center")
        tree.heading("DateOfBirth",text="EMAIL",anchor="center")
        tree.heading("Email",text="GENDER",anchor="center")
        tree.heading("LevelOfEducation",text="LEVELOFEDUCATION",anchor="center")
        tree.heading("Schoolorcollege",text="SCHOOL/COLLEGE",anchor="center")
        tree_scroll = ttk.Scrollbar(frame_main,orient="vertical")
        tree_scroll.configure(command=tree.yview)
        tree.configure(yscrollcommand=tree_scroll.set)
        tree_scroll.place(x=1330,y=70,height=250)
        tree.place(x=15,y=75)

   
        
#======================= 1st entry section ================================


        data_frame = LabelFrame(frame_main, text="Record",height=200)
        data_frame.place(x=25,y=320)
        fl_label = Label(data_frame, text="Full NAME")
        fl_label.grid(row=0, column=0, padx=10, pady=10)
        fl_entry = Entry(data_frame)
        fl_entry.grid(row=0, column=1, padx=10, pady=10)
        
        A_label = Label(data_frame, text="Address")
        A_label.grid(row=0, column=2, padx=10, pady=10)
        A_entry = Entry(data_frame)
        A_entry.grid(row=0, column=3, padx=10, pady=10)
        
        celllabel = Label(data_frame, text="cellno")
        celllabel.grid(row=0, column=4, padx=10, pady=10)
        cellentry = Entry(data_frame)
        cellentry.grid(row=0, column=5, padx=10, pady=10)
        
        date_label = Label(data_frame, text="Date")
        date_label.grid(row=1, column=0, padx=10, pady=10)
        date_entry = Entry(data_frame)
        date_entry.grid(row=1, column=1, padx=10, pady=10)
        
        gaurd_label = Label(data_frame, text="Gaurdiansname")
        gaurd_label.grid(row=1, column=2, padx=10, pady=10)
        gaurd_entry = Entry(data_frame)
        gaurd_entry.grid(row=1, column=3, padx=10, pady=10)
        
        phon = Label(data_frame, text="phoneno")
        phon.grid(row=1, column=4, padx=10, pady=10)
        phon_entry = Entry(data_frame)
        phon_entry.grid(row=1, column=5, padx=10, pady=10)
                
        gender_label = Label(data_frame, text="gender")
        gender_label.grid(row=1, column=6, padx=10, pady=10)
        gender_entry = Entry(data_frame)
        gender_entry.grid(row=1, column=7, padx=10, pady=10)
        
        DOB_label = Label(data_frame, text="DOB")
        DOB_label.grid(row=1, column=8, padx=10, pady=10)
        DOB_entry = Entry(data_frame)
        DOB_entry.grid(row=1, column=9, padx=10, pady=10)

        emaillabel = Label(data_frame, text="Email")
        emaillabel.grid(row=0, column=6, padx=10, pady=10)
        emailentry = Entry(data_frame)
        emailentry.grid(row=0, column=7, padx=10, pady=10)
        
        edu_label = Label(data_frame, text="LVL EDU")
        edu_label.grid(row=1, column=10, padx=10, pady=10)
        edu_entry = Entry(data_frame)
        edu_entry.grid(row=1, column=11, padx=10, pady=10)

        clzlabel = Label(data_frame, text="Scl/clz")
        clzlabel.grid(row=0, column=8, padx=10, pady=10)
        clzentry = Entry(data_frame)
        clzentry.grid(row=0, column=9, padx=10, pady=10)



#=============================funcationality==================================
        def clear_entries():
            fl_entry.delete(0, END)
            A_entry.delete(0, END)
            cellentry.delete(0, END)
            date_entry.delete(0, END)
            gaurd_entry.delete(0, END)
            phon_entry.delete(0, END)
            gender_entry.delete(0, END)
            edu_entry.delete(0, END)
            DOB_entry.delete(0,END)
            clzentry.delete(0,END)
            emailentry.delete(0,END)

        def add_():
            try:
                import re
                import mysql.connector
                a=fl_entry.get()
                b=A_entry.get()
                c=cellentry.get()
                d=date_entry.get()
                e=gaurd_entry.get()
                f=phon_entry.get()
                g=gender_entry.get()
                h=edu_entry.get()
                i=DOB_entry.get()
                j=emailentry.get()
                k= clzentry.get()
                if not all([a, b, c, d, e, f, g,h,i,k]):
                    messagebox.showinfo("Error", "All input fields must be filled")
                pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)*@gmail\.com$'
                if re.match(pattern,j):
                    con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                    # Create a cursor object to execute SQL queries
                    cursor = con.cursor()
                
                    # Execute an INSERT query
                    query = "INSERT INTO form(FullName,Address,Cellno,Date,GaurdiansName,PhoneNo,Email,Gender,DateOfBirth,LevelOfEducation,Schoolorcollege) VALUES (%s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s)"
                    values = (a,b,c,d,e,f,g,h,i,j,k)
                    cursor.execute(query, values)
                    # Commit the transaction
                    con.commit()
                    con.close()
                    # Clear entry boxes
        
	               # Clear The Treeview Table
                    fl_entry.delete(0, END)
                    A_entry.delete(0, END)
                    cellentry.delete(0, END)
                    date_entry.delete(0, END)
                    gaurd_entry.delete(0, END)
                    phon_entry.delete(0, END)
                    gender_entry.delete(0, END)
                    edu_entry.delete(0, END)
                    DOB_entry.delete(0,END)
                    clzentry.delete(0,END)
                    emailentry.delete(0,END)
                    tree.delete(*tree.get_children())
        
	            # Run to pull data from database on start
                    data()
                elif j is not None and j != "":
                    messagebox.showinfo("Invalid Email", "Email is not valid")
                else:
                    pass
            except:
                messagebox.showinfo("error","invalid input")        
        def select_record(e):
            clear_entries()
            selected = tree.focus()
	# Grab record values
            values = tree.item(selected, 'values')

            fl_entry.insert(0, values[1])
            A_entry.insert(0, values[2])
            cellentry.insert(0, values[3])
            date_entry.insert(0, values[4])
            gaurd_entry.insert(0, values[5])
            phon_entry.insert(0, values[6])
            gender_entry.insert(0, values[7])
            DOB_entry.insert(0, values[8])
            emailentry.insert(0, values[9])
            edu_entry.insert(0, values[10])
            clzentry.insert(0, values[11])
    
        #========================updatingg==========================
# ... (previous code)
        def update():
            try:
                selected = tree.focus()
                id = tree.item(selected, 'values')[0]
            
                # Update record in Treeview
                tree.item(selected, text="", values=(id, fl_entry.get(), A_entry.get(), cellentry.get(), date_entry.get(),
                                                      gaurd_entry.get(), phon_entry.get(), gender_entry.get(), edu_entry.get(),
                                                      DOB_entry.get(), emailentry.get(), clzentry.get()))
            
                import mysql.connector
                con = mysql.connector.connect(host="localhost", user="root", password="Nabin(123)", database="student")
            
                # Create a cursor object to execute SQL queries
                cursor = con.cursor()
            
                cursor.execute("""
                    UPDATE form SET
                    Address = %s,
                    Cellno = %s,
                    Date = %s,
                    GaurdiansName = %s,
                    PhoneNo = %s,
                    Email = %s,
                    Gender = %s,
                    DateOfBirth = %s,
                    LevelOfEducation = %s,
                    Schoolorcollege = %s,
                    FullName = %s
                    WHERE id = %s
                """, (
                    A_entry.get(),
                    cellentry.get(),
                    date_entry.get(),
                    gaurd_entry.get(),
                    phon_entry.get(),
                    emailentry.get(),
                    gender_entry.get(),
                    DOB_entry.get(),
                    edu_entry.get(),
                    clzentry.get(),
                    fl_entry.get(),
                    id,  # Pass the ID as a single-element tuple
                ))
            
                con.commit()
                con.close()
            
# ... (rest     of the code)
    
                	# Clear entry boxes
    
                fl_entry.delete(0, END)
                A_entry.delete(0, END)
                cellentry.delete(0, END)
                date_entry.delete(0, END)
                gaurd_entry.delete(0, END)
                phon_entry.delete(0, END)
                gender_entry.delete(0, END)
                edu_entry.delete(0, END)
                DOB_entry.delete(0,END)
                clzentry.delete(0,END)
                emailentry.delete(0,END)
                tree.delete(*tree.get_children())
    
	# Run to     pull data from database on start
                data()
            except:
                messagebox.showinfo("error","invalid input")
    
        def remove_many():
            try:
                import mysql.connector
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            # Create a cursor object to execute SQL queries
                cursor = con.cursor()
	# Add a     little message box for fun
                response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")
                if response == 1:
	            	# Designate selections
                    x = tree.selection()
            
	            	# Create List of ID's
                    ids_to_delete = []
	            	
	            	# Add selections to ids_to_delete list
                    for record in x:
                        ids_to_delete.append(tree.item(record, 'values')[0])
            
	            	# Delete From Treeview
                    for record in x:
                        tree.delete(record)
            
            
	            	# Delete Everything From The Table
                    cursor.executemany("DELETE FROM form WHERE id = %s", [(a,) for a in ids_to_delete])
                    ids_to_delete = []
                    con.commit()
                    con.close()
                    clear_entries()
            except:
                messagebox.showinfo("error","unable to delete")
    
                
        

        #===================command section========================================
        button_frame = LabelFrame(frame_main, text="Commands")
        button_frame.place(x=25,y=430)
        
        update_button = Button(button_frame, text="Update Record",command=update)
        update_button.grid(row=0, column=0, padx=10, pady=10)
        
        add_button = Button(button_frame, text="Add Record",command=add_)
        add_button.grid(row=0, column=1, padx=10, pady=10)
        
        remove_many_button = Button(button_frame, text="Delete",command=remove_many)
        remove_many_button.grid(row=0, column=4, padx=10, pady=10)
        
        
        clear = Button(button_frame, text="Clear Entry Boxes",command=clear_entries)
        clear.grid(row=0, column=5, padx=10, pady=10)

#=======================innner frame 2 =================================
 

        #===================fetching============================================
        def data2():
            import mysql.connector
            con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            cur = con.cursor()
            #Execute a SELECT query
            query = "SELECT * FROM enroll"
            cur.execute(query)   
            #Fetch the result
            records2= cur.fetchall()
            for ro in records2:
                tree2.insert(parent='',index='end',text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))

        tree2=ttk.Treeview(frame_main)
        tree2['show']='headings'
        tree2["column"]=("id","course1","course2","course3","shifttime","codinator","student","other")
        tree2.column("id",width=50,minwidth=50,anchor="center")
        tree2.column("course1",width=200,minwidth=150,anchor="center")
        tree2.column("course2",width=200,minwidth=150,anchor="center")
        tree2.column("course3",width=200,minwidth=150,anchor="center")
        tree2.column("shifttime",width=150,minwidth=100,anchor="center")
        tree2.column("student",width=150,minwidth=100,anchor="center")
        tree2.column("codinator",width=150,minwidth=100,anchor="center")
        tree2.column("other",width=150,minwidth=100,anchor="center")
        
        #===================heading=================================
        tree2.heading("id",text="ID",anchor="center")
        tree2.heading("course1",text="course1",anchor="center")
        tree2.heading("course2",text="Course2",anchor="center")
        tree2.heading("course3",text="Course3",anchor="center")
        tree2.heading("shifttime",text="ShiftTime",anchor="center")
        tree2.heading("student",text="Student",anchor="center")
        tree2.heading("codinator",text="Codinator",anchor="center")
        tree2.heading("other",text="Other",anchor="center")
        tree_scroll2 = ttk.Scrollbar(frame_main,orient="vertical")
        tree_scroll2.configure(command=tree2.yview)
        tree2.configure(yscrollcommand=tree_scroll2.set)
        tree_scroll2.place(x=1300,y=590,height=250)
        tree2.place(x=40,y=595)


#=================================enroll section=================================
        
        data_frame = LabelFrame(frame_main, text="Record",height=200)
        data_frame.place(x=25,y=830)
        c_label = Label(data_frame, text="Course1")
        c_label.grid(row=0, column=0, padx=10, pady=10)
        c_entry = Entry(data_frame)
        c_entry.grid(row=0, column=1, padx=10, pady=10)
        
        c2_label = Label(data_frame, text="Course2")
        c2_label.grid(row=0, column=2, padx=10, pady=10)
        c2_entry = Entry(data_frame)
        c2_entry.grid(row=0, column=3, padx=10, pady=10)
        
        c3abel = Label(data_frame, text="Course3")
        c3abel.grid(row=0, column=4, padx=10, pady=10)
        c3entry = Entry(data_frame)
        c3entry.grid(row=0, column=5, padx=10, pady=10)
        
        shift_label = Label(data_frame, text="shift time")
        shift_label.grid(row=1, column=0, padx=10, pady=10)
        shift_entry = Entry(data_frame)
        shift_entry.grid(row=1, column=1, padx=10, pady=10)
        
        co_label = Label(data_frame, text="cordinator")
        co_label.grid(row=1, column=2, padx=10, pady=10)
        cc_entry = Entry(data_frame)
        cc_entry.grid(row=1, column=3, padx=10, pady=10)
        
        stu = Label(data_frame, text="student")
        stu.grid(row=1, column=4, padx=10, pady=10)
        stu_entry = Entry(data_frame)
        stu_entry.grid(row=1, column=5, padx=10, pady=10)
                
        oth_label = Label(data_frame, text="other")
        oth_label.grid(row=1, column=6, padx=10, pady=10)
        oth_entry = Entry(data_frame)
        oth_entry.grid(row=1, column=7, padx=10, pady=10)


        #=============================funcationality==================================
        def clear_entries2():
            c_entry.delete(0, END)
            c2_entry.delete(0, END)
            c3entry.delete(0, END)
            shift_entry.delete(0, END)
            cc_entry.delete(0, END)
            stu_entry.delete(0, END)
            oth_entry.delete(0,END)
        def select_records(e):
            clear_entries2()
            selected = tree2.focus()
	# Grab record values
            values = tree2.item(selected, 'values')
            c_entry.insert(0, values[1])
            c2_entry.insert(0, values[2])
            c3entry.insert(0, values[3])
            shift_entry.insert(0, values[4])
            cc_entry.insert(0, values[5])
            stu_entry.insert(0, values[6])
            oth_entry.insert(0, values[7])


        def add():
            try:
                import mysql.connector
                a=c_entry.get()
                b=c2_entry.get()
                c=c3entry.get()
                d=shift_entry.get()
                e=cc_entry.get()
                f=stu_entry.get()
                g=oth_entry.get()
                if not all([a, b, c, d, e, f, g]):
                    messagebox.showinfo("Error", "All input fields must be filled")
                else:
                    con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                    cur = con.cursor()
                    # Create a cursor object to execute SQL queries
                    cursor = con.cursor()
                    query = "INSERT INTO enroll(course1,course2,course3,shifttime,codinator,student,other) VALUES (%s, %s, %s,%s, %s, %s,%s)"
                    values = (a,b,c,d,e,f,g)
                    cursor.execute(query, values)
                    con.commit()
                    con.close()
                    c_entry.delete(0, END)
                    c2_entry.delete(0, END)
                    c3entry.delete(0, END)
                    shift_entry.delete(0, END)
                    cc_entry.delete(0, END)
                    stu_entry.delete(0, END)
                    oth_entry.delete(0,END)
                    tree.delete(*tree2.get_children())
                    data2()
            except:
                messagebox.showinfo("error","invalid input")


        def update_record():
            try:
                selected = tree2.focus()
                id=tree2.item(selected,'values')[0]
	# Update     record
                tree2.item(selected, text="", values=(id,c_entry.get(),c2_entry.get(),c3entry.get(),shift_entry.get(),cc_entry.get(),stu_entry.get(),oth_entry.get(),))
                import mysql.connector
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                # Create a cursor object to execute SQL queries
                cursor = con.cursor()
                cursor.execute( """
                               UPDATE enroll SET
                               course1= %s,                           
                               course2=%s,
                               course3=%s,
                               shifttime=%s,
                               codinator=%s,
                               student=%s,
                               other=%s
                               WHERE id = %s
                            """, (c_entry.get(),
                                  c2_entry.get(),
                                  c3entry.get(),
                                  shift_entry.get(),
                                  cc_entry.get(),
                                  stu_entry.get(),
                                  oth_entry.get(),
                                  id,
                                ))
    
                # Commit the transaction
                con.commit()
                con.close()
                tree2.delete(*tree2.get_children())
                data2()
            except:
                messagebox.showinfo("error","invalid input")




        def remove():
            try:
                import mysql.connector
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                # Create a cursor object to execute SQL queries
                cursor = con.cursor()
                response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")
                if response == 1:
                	# Designate selections
                    x = tree2.selection()
                
                	# Create List of ID's
                    ids_to_delete = []
                	
                	# Add selections to ids_to_delete list
                    for record in x:
                        ids_to_delete.append(tree2.item(record, 'values')[0])
                
                	# Delete From Treeview
                    for record in x:
                        tree2.delete(record)
                
                
                	# Delete Everything From The Table
                    cursor.executemany("DELETE FROM enroll WHERE id = %s", [(a,) for a in ids_to_delete])
                    ids_to_delete = []
                    con.commit()
                    con.close()
                    clear_entries()
            except:
                messagebox.showinfo("error","unable to delete")
                
    
#===================command section========================================
        button_frame2 = LabelFrame(frame_main, text="Commands")
        button_frame2.place(x=25,y=930)
        
        update_button = Button(button_frame2, text="Update Record",command=update_record)
        update_button.grid(row=0, column=0, padx=10, pady=10)
        
        add_button = Button(button_frame2, text="Add Record",command=add)
        add_button.grid(row=0, column=1, padx=10, pady=10)
        
        
        remove_many_button = Button(button_frame2, text="Delete",command=remove)
        remove_many_button.grid(row=0, column=4, padx=10, pady=10)
        
        
        select_record_button = Button(button_frame2, text="Clear Entry Boxes", command=clear_entries2)
        select_record_button.grid(row=0, column=7, padx=10, pady=10)
        
 #================inner frame 3 ===================================


        #===================fetching============================================
        def data3():
            import mysql.connector
            con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
            cur = con.cursor()
            #Execute a SELECT query
            query = "SELECT * FROM office"
            cur.execute(query)   
            #Fetch the result
            records3=cur.fetchall()
            for ro in records3:
                tree3.insert(parent='',index='end',text='',values=(ro[0],ro[1],ro[2],ro[3],ro[4],ro[5],ro[6],ro[7]))


        tree3=ttk.Treeview(frame_main)
        tree3['show']='headings'
        tree3["column"]=("id","Fullname","Address","DateOfBirth","Refrence","Refrencecontact","Discount","SourcesOfInformation")
        tree3.column("id",width=50,minwidth=50,anchor="center")
        tree3.column("Fullname",width=200,minwidth=150,anchor="center")
        tree3.column("Address",width=200,minwidth=150,anchor="center")
        tree3.column("DateOfBirth",width=200,minwidth=150,anchor="center")
        tree3.column("Refrence",width=150,minwidth=100,anchor="center")
        tree3.column("Refrencecontact",width=150,minwidth=100,anchor="center")
        tree3.column("Discount",width=160,minwidth=100,anchor="center")
        tree3.column("SourcesOfInformation",width=160,minwidth=100,anchor="center")
        
        #===================heading=================================
        tree3.heading("id",text="ID",anchor="center")
        tree3.heading("Fullname",text="FullName",anchor="center")
        tree3.heading("Address",text="Address",anchor="center")
        tree3.heading("DateOfBirth",text="Date Of Birth",anchor="center")
        tree3.heading("Refrence",text="Refrence",anchor="center")
        tree3.heading("Refrencecontact",text="RefrenceContact",anchor="center")
        tree3.heading("Discount",text="discount",anchor="center")
        tree3.heading("SourcesOfInformation",text="Sources Of Information",anchor="center")
        tree_scroll3 = ttk.Scrollbar(frame_main,orient="vertical")
        tree_scroll3.configure(command=tree3.yview)
        tree3.configure(yscrollcommand=tree_scroll3.set)
        tree_scroll3.place(x=1300,y=1055,height=250)
        tree3.place(x=20,y=1060)
        
#=====================office section=======================================



        data_frame = LabelFrame(frame_main, text="Record",height=200)
        data_frame.place(x=25,y=1310)
        fn_label = Label(data_frame, text="fullname")
        fn_label.grid(row=0, column=0, padx=10, pady=10)
        fn_entry = Entry(data_frame)
        fn_entry.grid(row=0, column=1, padx=10, pady=10)
        
        a_label = Label(data_frame, text="Address")
        a_label.grid(row=0, column=2, padx=10, pady=10)
        a_entry = Entry(data_frame)
        a_entry.grid(row=0, column=3, padx=10, pady=10)
        
        Dob_label = Label(data_frame, text="DOB")
        Dob_label.grid(row=0, column=4, padx=10, pady=10)
        Dob_entry = Entry(data_frame)
        Dob_entry.grid(row=0, column=5, padx=10, pady=10)
        
        r3_label = Label(data_frame, text="refrences")
        r3_label.grid(row=1, column=0, padx=10, pady=10)
        r3_entry = Entry(data_frame)
        r3_entry.grid(row=1, column=1, padx=10, pady=10)
        
        rf_label = Label(data_frame, text="refrences con")
        rf_label.grid(row=1, column=2, padx=10, pady=10)
        rf_entry = Entry(data_frame)
        rf_entry.grid(row=1, column=3, padx=10, pady=10)
        
        dis = Label(data_frame, text="Discount")
        dis.grid(row=1, column=4, padx=10, pady=10)
        dis_entry = Entry(data_frame)
        dis_entry.grid(row=1, column=5, padx=10, pady=10)
                
        so_label = Label(data_frame, text="Sources of information")
        so_label.grid(row=1, column=6, padx=10, pady=10)
        so_entry = Entry(data_frame)
        so_entry.grid(row=1, column=7, padx=10, pady=10)
#====================function============================================
        def clear_entries3():
            fn_entry.delete(0, END)
            a_entry.delete(0, END)
            r3_entry.delete(0, END)
            Dob_entry.delete(0, END)
            rf_entry.delete(0, END)
            dis_entry.delete(0, END)
            so_entry.delete(0, END)

        def add_record():
            try:
                import mysql.connector
                a=fn_entry.get()
                b=a_entry.get()
                c=Dob_entry.get()
                d=r3_entry.get()
                e=rf_entry.get()
                f=dis_entry.get()
                g=so_entry.get()
                
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                cur = con.cursor()
                # Create a cursor object to execute SQL queries
                cursor = con.cursor()
        
                query = "INSERT INTO office(Fullname,Address,DateOfBirth,Refrence,Refrencecontact,Discount,SourcesOfInformation) VALUES (%s, %s, %s,%s, %s, %s,%s)"
                values = (a,b,c,d,e,f,g)
                cursor.execute(query, values)
                con.commit()
                con.close()
    
                fn_entry.delete(0, END)
                a_entry.delete(0, END)
                r3_entry.delete(0, END)
                Dob_entry.delete(0, END)
                rf_entry.delete(0, END)
                dis_entry.delete(0, END)
                so_entry.delete(0, END)
                tree3.delete(*tree3.get_children())
    
                data3()
            except:
                messagebox.showinfo("error","invalid input")

        def select_recor(e):
            clear_entries3()
            selected = tree3.focus()
	# Grab record values
            values = tree3.item(selected, 'values')
            fn_entry.insert(0, values[1])
            a_entry.insert(0, values[2])
            r3_entry.insert(0, values[4])
            Dob_entry.insert(0, values[3])
            rf_entry.insert(0, values[5])
            dis_entry.insert(0, values[6])
            so_entry.insert(0, values[7])
        

        def remove():
            try:
                import mysql.connector
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                # Create a cursor object to execute SQL queries
                cursor = con.cursor()
                response = messagebox.askyesno("WOAH!!!!", "This Will Delete EVERYTHING SELECTED From The Table\nAre You Sure?!")
                if response == 1:
                	# Designate selections
                    x = tree3.selection()
                
                	# Create List of ID's
                    ids_to_delete = []
                	
                	# Add selections to ids_to_delete list
                    for record in x:
                        ids_to_delete.append(tree3.item(record, 'values')[0])
                
                	# Delete From Treeview
                    for record in x:
                        tree3.delete(record)
                
                
                	# Delete Everything From The Table
                    cursor.executemany("DELETE FROM office WHERE id = %s", [(a,) for a in ids_to_delete])
                    ids_to_delete = []
                    con.commit()
                    con.close()
                    clear_entries()
            except:
                messagebox.showinfo("error","unable to delete")
                
            

        def update_():
            try:
                selected = tree3.focus()
                id=tree3.item(selected, 'values')[0]
	# Update     record
                tree3.item(selected, text="", values=(id,fn_entry.get(),a_entry.get(),Dob_entry.get(),r3_entry.get(),rf_entry.get(),dis_entry.get(),so_entry.get(),))
                import mysql.connector
                con = mysql.connector.connect(host=f"{host1}",user=f"{user1}",password=f"{password1}",database="student")
                # Create a cursor object to execute SQL queries
                cursor = con.cursor()
                cursor.execute( """
                               UPDATE office SET
                               Fullname= %s,
                               Address= %s,
                               DateOfBirth = %s,
                               Refrence = %s,
                               Refrencecontact=%s,
                               Discount=%s,
                               SourcesOfInformation=%s
                               WHERE id = %s
                            """, (fn_entry.get(),
                                  a_entry.get(),
                                  Dob_entry.get(),
                                  r3_entry.get(),
                                  rf_entry.get(),
                                  dis_entry.get(),
                                  so_entry.get(),
                                  id,
                                ))
    
                # Commit the transaction
                con.commit()
                con.close()
                tree3.delete(*tree3.get_children())
                data3()
            except:
                messagebox.showinfo("error","invalid input")








#===================command section========================================
        button_frame3 = LabelFrame(frame_main, text="Commands")
        button_frame3.place(x=25,y=1420)
        
        update_button = Button(button_frame3, text="Update Record",command=update_)
        update_button.grid(row=0, column=0, padx=10, pady=10)
        
        add_button = Button(button_frame3, text="Add Record",command=add_record)
        add_button.grid(row=0, column=1, padx=10, pady=10)
        
        remove_many_button = Button(button_frame3, text="delete",command=remove)
        remove_many_button.grid(row=0, column=4, padx=10, pady=10)
        
        
        select_record_button = Button(button_frame3, text="Clear Entry Boxes",command=clear_entries3)
        select_record_button.grid(row=0, column=7, padx=10, pady=10)
        


        


        tree3.bind("<ButtonRelease-1>", select_recor)
        tree.bind("<ButtonRelease-1>", select_record)
        tree2.bind("<ButtonRelease-1>", select_records)
        data()
        data2()
        data3()
        win.mainloop()
        


        
    
        
        
    # Create a scrollable frame
    canvas = Canvas(root, bg="#cdfefe", width=1280, height=700, scrollregion=(0, -605, 0, 700))
    canvas.pack(side="left", expand=True, fill="both")
    
    scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
    canvas.configure(yscrollcommand=scrollbar.set)
    frame1 = ttk.Frame(canvas,width=1350, height=1210, style='TFrame')
    canvas.create_window((-150, 600), window=frame1, anchor="sw")
    
    # Bind mouse wheel event to canvas
    canvas.bind_all("<MouseWheel>", on_mousewheel)
    
    style = ttk.Style()
    style.configure("Rounded.TButton"
                    , font=("Arial", 13, "bold"),
                    width=20
                    ,background='#ffcce6')
    
    
    ttk.Label(frame1, text="Regi No:112123/075/076", font=("Arial", 8), foreground='black').place(x=930, y=5)
    
    label = ttk.Label(frame1, text="HUB IT GROUP PVT.LTD.", font=("Arial", 30, "bold"), foreground="#A1056A")
    label.place(x=460, y=20)
    canvas_logo = Canvas(frame1, width=90, height=120, bd=0)
    canvas_logo.place(x=350, y=9)
    circle = canvas_logo.create_oval(2, 2, 80, 80)
    circle1 = canvas_logo.create_oval(70, 9, 62, 16, fill="#A1056A")
    circle2 = canvas_logo.create_oval(61, 2, 54, 10, fill="#A1056A")
    
    circle3 = canvas_logo.create_oval(7, 60, 15, 70, fill="#A1056A")
    circle4 = canvas_logo.create_oval(70, 67, 60, 76, fill="#A1056A")
    
    
    label2 = ttk.Label(frame1, text="Butwal-09 (Ganesh Path) Milanchowk", font=("Arial", 13, "bold"), foreground="Black")
    ttk.Label(frame1, text="ph: 071-532805, 9827494116, 9827494119", font=("Arial", 13, "bold"), foreground="black").place(x=535, y=95)
    label2.place(x=550, y=70)
    head = ttk.Label(frame1, text="STUDENT ENROLLMENT REGISTRATION FORM",
                    font=("Arial", 25, "bold"),
                    background="#A1056A",
                    width=45,
                    anchor="center",
                    foreground="white")
    head.place(x=245, y=125)
    headl = ttk.Label(frame1, text="FULL NAME:",
                     font=("Arial", 18),
                     background="#ffcce6",
                     foreground="black")
    headl.place(x=245, y=167)
    headle = ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13))
    headle.place(x=390, y=167)
    ttk.Label(frame1, text="ADDRESS:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=205)
    addrs=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13))
    addrs.place(x=370, y=205)
    ttk.Label(frame1, text="CELL NO:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=250)
    cel=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=25, font=("Arial", 13))
    cel.place(x=360, y=250)
    ttk.Label(frame1, text="Date:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=595, y=250)
    date=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=23, font=("Arial", 13))
    date.place(x=657, y=250)
    ttk.Label(frame1, text="GUARDIAN's NAME:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=290)
    gaur=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=44, font=("Arial", 13))
    gaur.place(x=469, y=290)
    
    ttk.Label(frame1, text="PHONE NO:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=325)
    phon=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=73, font=("Arial", 13))
    phon.place(x=382, y=325)
    ttk.Label(frame1, text="GENDER:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=360)
    gen = ["Male", "Female"]
    genn=ttk.Combobox(frame1, values=gen,width=18, font=("Arial", 13))
    genn.place(x=360, y=360)
    ttk.Label(frame1, text="DATE OF BIRTH:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=560, y=360)
    dateb=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=32, font=("Arial", 13))
    dateb.place(x=754, y=360)
    ttk.Label(frame1, text="EMAIL:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=400)
    email=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=79, font=("Arial", 13))
    email.place(x=326, y=400)
    ttk.Label(frame1, text="LEVEL OF EDUCATION:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=440)
    lvl = ["see", +2, "Bachelor", "Masters"]
    edu=ttk.Combobox(frame1, values=lvl, font=("Arial", 13), width=56)
    edu.place(x=520, y=440)
    ttk.Label(frame1, text="NAME OF THE SCHOOL/COLLEGE:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=480)
    clz=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=44, font=("Arial", 13))
    clz.place(x=648, y=480)
    ttk.Label(frame1, text="NAME OF COURSE/S TO ENROLL",
              font=("Arial", 25, "bold"),
             anchor="center",
             background="#A1056A",
             width=45,
             foreground="white").place(x=245, y=515)
    
    cour1=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13))
    cour1.place(x=268, y=560)
    ttk.Label(frame1, text="1",
              font=("Arial", 25, "bold"),
              background="#ffcce6",
              foreground="Black").place(x=245, y=560)
    cour3=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13))
    cour3.place(x=270, y=640)
    ttk.Label(frame1, text="2",
              font=("Arial", 25, "bold"),
              background="#ffcce6",
              foreground="Black").place(x=245, y=600)
    
    ttk.Label(frame1, text="3",
              font=("Arial", 25, "bold"),
              background="#ffcce6",
              foreground="Black").place(x=245, y=640)
    
    cour2=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13))
    cour2.place(x=270, y=600)
    ttk.Label(frame1, text="OTHER COURSE PREVIOUSLY TAKEN",
              font=("Arial", 14, "bold"),
              background="#ffcce6",
              foreground="Black").place(x=705, y=560)

    
    frame = CTkFrame(frame1, width=170, height=151, fg_color="white")
    frame.place(x=878, y=170)

    ttk.Label(frame1, text="shift time",
              font=("Arial", 14, "bold"),
              background="#ffcce6",
              foreground="Black").place(x=708, y=640)
    o=Entry(frame1,width=39,font=("Arial", 13))
    o.place(x=705, y=590)
    shift=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=33, font=("Arial", 13))
    shift.place(x=754, y=640)
    ttk.Label(frame1, text="RULES & REGULATIONS",
              font=("Arial", 25, "bold"),
             anchor="center",
             background="#A1056A",
             width=45,
             foreground="white").place(x=245,y=690)
    ttk.Label(frame1,  wraplength=1200, justify="left",text="1.He/she should will be resposible for any damage done to the property owned by the institution and will be charged accordily\n2.Half of the fee should be paid within first week and remaing should be paid by the end scond week.Fees are not refundable\n3.Student should inform the institution if he/she will not be able to attend any class\n4.it is compulsory to attend any extra classes,seminars,field visits and internships and other programs that institution sees fit to\n deploy any student with respective to their course & field of the interest.\n5.certificate wil not be provided for incomplete courses.\nBy signing below, I hereby agree on all the terms and conditions mentioned above.  "
              ,
              font=("Arial", 10),
             width=150,
    
             foreground="Black").place(x=245,y=730)
    cod=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13))
    cod.place(x=255, y=850)
    ttk.Label(frame1, text="COORDINATOR",
              font=("Arial", 15,"bold"),
              foreground="Black").place(x=255,y=880)
    stud=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13))
    stud.place(x=865, y=850)
    ttk.Label(frame1, text="STUDENT",
              font=("Arial", 15,"bold"),
              foreground="Black").place(x=955,y=880)
    
    ttk.Label(frame1, text="FOR OFFICE USE ONLY",
              font=("Arial", 25, "bold"),
             anchor="center",
             background="#A1056A",
             width=45,
             foreground="white").place(x=245,y=920)
    headl = ttk.Label(frame1, text="FULL NAME:",
                     font=("Arial", 18),
                     background="#ffcce6",
                     foreground="Black")
    headl.place(x=245, y=980)
    full=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=73, font=("Arial", 13))
    full.place(x=390, y=980)
    ttk.Label(frame1, text="ADDRESS:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=1020)
    ad=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=35, font=("Arial", 13))
    ad.place(x=370, y=1020)
    ttk.Label(frame1, text="DATE OF BIRTH:",
             font=("Arial", 15),
             background="#ffcce6",
             foreground="Black").place(x=698, y=1020)
    dob=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13))
    dob.place(x=865, y=1020)
    ttk.Label(frame1, text="REFERRED BY:",
             font=("Arial", 16),
             background="#ffcce6",
             foreground="Black").place(x=245, y=1060)
    ref=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=24, font=("Arial", 13))
    ref.place(x=406, y=1060)
    ttk.Label(frame1, text="REFFERAL CONTACT NO:",
             font=("Arial", 15),
             background="#ffcce6",
             foreground="Black").place(x=630, y=1060)
    refc=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=19, font=("Arial", 13))
    refc.place(x=875, y=1060)
    ttk.Label(frame1, text="DISCOUNT:",
             font=("Arial", 18),
             background="#ffcce6",
             foreground="Black").place(x=245, y=1100)
    dis=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=74, font=("Arial", 13))
    dis.place(x=380, y=1100)
    ttk.Label(frame1, text="SOURCES OF INFORMATION:",
             font=("Arial", 15),
             background="#ffcce6",
             foreground="Black").place(x=245, y=1140)
    sof=ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=57, font=("Arial", 13))
    sof.place(x=530, y=1140)
    ttk.Label(frame1, text="HUB\n    IT", font=("Arial", 12, "bold"), foreground="#A1056A", width=4).place(x=370, y=37)
    button = ttk.Button(frame1,text="SUBMIT",style="Rounded.TButton",command=sub)
    button.place(x=550,y=1180)
    button = ttk.Button(frame,text="upload photo",command=photo)
    button.place(x=50, y=126)
    button = ttk.Button(frame1,text="detial",style="Rounded.TButton",command=detial)
    button.place(x=350,y=1180)
    button = ttk.Button(frame1,text="Link To Database",style="Rounded.TButton",command=database)
    button.place(x=750,y=1180)
    root.mainloop()
hub()
