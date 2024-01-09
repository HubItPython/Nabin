from tkinter import Text, Tk, Canvas, Scrollbar, ttk
from customtkinter import CTkFrame

def on_mousewheel(event):
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

root = Tk()
root.geometry("1350x700")


# Create a scrollable frame
canvas = Canvas(root, bg="#cdfefe", width=1350, height=700, scrollregion=(0, -605, 0, 620))
canvas.pack(side="left", expand=True, fill="both")

scrollbar = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.place(relx=1, rely=0, relheight=1, anchor="ne")
canvas.configure(yscrollcommand=scrollbar.set)
frame1 = ttk.Frame(canvas,width=1200, height=1200, style='TFrame')
canvas.create_window((70, 600), window=frame1, anchor="sw")

# Bind mouse wheel event to canvas
canvas.bind_all("<MouseWheel>", on_mousewheel)

style = ttk.Style()
style.configure('Rounded.TEntry')


ttk.Label(frame1, text="Regi No:112123/075/076", font=("Arial", 8), foreground="black").place(x=930, y=5)

label = ttk.Label(frame1, text="HUB IT GROUP PVT.LTD.", font=("Arial", 30, "bold"), foreground="green")
label.place(x=460, y=20)
canvas_logo = Canvas(frame1, width=90, height=120, bd=0)
canvas_logo.place(x=350, y=9)
circle = canvas_logo.create_oval(2, 2, 80, 80)
circle1 = canvas_logo.create_oval(70, 9, 62, 16, fill="green")
circle2 = canvas_logo.create_oval(61, 2, 54, 10, fill="green")

circle3 = canvas_logo.create_oval(7, 60, 15, 70, fill="green")
circle4 = canvas_logo.create_oval(70, 67, 60, 76, fill="green")


label2 = ttk.Label(frame1, text="Butwal-09 (Ganesh Path) Milanchowk", font=("Arial", 13, "bold"), foreground="black")
ttk.Label(frame1, text="ph: 071-532805, 9827494116, 9827494119", font=("Arial", 13, "bold"), foreground="black").place(x=535, y=95)
label2.place(x=550, y=70)
head = ttk.Label(frame1, text="STUDENT ENROLLMENT REGISTRATION FORM",
                font=("Arial", 25, "bold"),
                background="green",
                width=45,
                anchor="center",
                foreground="white")
head.place(x=245, y=125)
headl = ttk.Label(frame1, text="FULL NAME:",
                 font=("Arial", 18),
                 background="#609f9f",
                 foreground="#80ffff")
headl.place(x=245, y=167)
headle = ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13))
headle.place(x=390, y=167)
frame2 = ttk.Frame(frame1, width=170, height=151, style='TFrame')
frame2.place(x=875, y=167)
ttk.Label(frame1, text="ADDRESS:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=205)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13)).place(x=370, y=205)
ttk.Label(frame1, text="CELL NO:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=250)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=25, font=("Arial", 13)).place(x=360, y=250)
ttk.Label(frame1, text="Date:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=595, y=250)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=23, font=("Arial", 13)).place(x=657, y=250)
ttk.Label(frame1, text="GUARDIAN's NAME:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=290)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=44, font=("Arial", 13)).place(x=469, y=290)

ttk.Label(frame1, text="PHONE NO:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=325)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=73, font=("Arial", 13)).place(x=382, y=325)
ttk.Label(frame1, text="GENDER:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=360)
gen = ["Male", "Female"]
ttk.Combobox(frame1, values=gen,width=18, font=("Arial", 13)).place(x=360, y=360)
ttk.Label(frame1, text="DATE OF BIRTH:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=560, y=360)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=32, font=("Arial", 13)).place(x=754, y=360)
ttk.Label(frame1, text="EMAIL:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=400)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=79, font=("Arial", 13)).place(x=326, y=400)
ttk.Label(frame1, text="LEVEL OF EDUCATION:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=440)
lvl = ["see", +2, "Bachelor", "Masters"]
ttk.Combobox(frame1, values=lvl, font=("Arial", 13), width=56).place(x=520, y=440)
ttk.Label(frame1, text="NAME OF THE SCHOOL/COLLEGE:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=480)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=44, font=("Arial", 13)).place(x=648, y=480)
ttk.Label(frame1, text="NAME OF COURSE/S TO ENROLL",
          font=("Arial", 25, "bold"),
         anchor="center",
         background="green",
         width=45,
         foreground="white").place(x=245, y=515)

ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13)).place(x=268, y=560)
ttk.Label(frame1, text="1",
          font=("Arial", 25, "bold"),
          background="#609f9f",
          foreground="#80ffff").place(x=245, y=560)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=262, y=600)
ttk.Label(frame1, text="2",
          font=("Arial", 25, "bold"),
          background="#609f9f",
          foreground="#80ffff").place(x=245, y=600)

ttk.Label(frame1, text="3",
          font=("Arial", 25, "bold"),
          background="#609f9f",
          foreground="#80ffff").place(x=245, y=640)

ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=47, font=("Arial", 13)).place(x=268, y=640)
ttk.Label(frame1, text="OTHER COURSE PREVIOUSLY TAKEN",
          font=("Arial", 14, "bold"),
          background="#609f9f",
          foreground="#80ffff").place(x=705, y=560)

frame = CTkFrame(frame1, width=170, height=151, fg_color="white")
frame.place(x=878, y=170)
ttk.Label(frame1, text="shift time",
          font=("Arial", 14, "bold"),
          background="#609f9f",
          foreground="#80ffff").place(x=708, y=640)
Text(frame1,width=39,height=2,font=("Arial", 13)).place(x=705, y=590)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=33, font=("Arial", 13)).place(x=754, y=640)
ttk.Label(frame1, text="RULES & REGULATIONS",
          font=("Arial", 25, "bold"),
         anchor="center",
         background="green",
         width=45,
         foreground="white").place(x=245,y=690)
ttk.Label(frame1,  wraplength=1200, justify="left",text="1.He/she should will be resposible for any damage done to the property owned by the institution and will be charged accordily\n2.Half of the fee should be paid within first week and remaing should be paid by the end scond week.Fees are not refundable\n3.Student should inform the institution if he/she will not be able to attend any class\n4.it is compulsory to attend any extra classes,seminars,field visits and internships and other programs that institution sees fit to\n deploy any student with respective to their course & field of the interest.\n5.certificate wil not be provided for incomplete courses.\nBy signing below, I hereby agree on all the terms and conditions mentioned above.  "
          ,
          font=("Arial", 10),
         width=150,

         foreground="black").place(x=245,y=730)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13)).place(x=255, y=850)
ttk.Label(frame1, text="COORDINATOR",
          font=("Arial", 15,"bold"),
          foreground="black").place(x=255,y=880)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13)).place(x=865, y=850)
ttk.Label(frame1, text="STUDENT",
          font=("Arial", 15,"bold"),
          foreground="black").place(x=955,y=880)

ttk.Label(frame1, text="FOR OFFICE USE ONLY",
          font=("Arial", 25, "bold"),
         anchor="center",
         background="green",
         width=45,
         foreground="white").place(x=245,y=920)
headl = ttk.Label(frame1, text="FULL NAME:",
                 font=("Arial", 18),
                 background="#609f9f",
                 foreground="#80ffff")
headl.place(x=245, y=980)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=73, font=("Arial", 13)).place(x=390, y=980)
ttk.Label(frame1, text="ADDRESS:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=1020)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=35, font=("Arial", 13)).place(x=370, y=1020)
ttk.Label(frame1, text="DATE OF BIRTH:",
         font=("Arial", 15),
         background="#609f9f",
         foreground="#80ffff").place(x=698, y=1020)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=20, font=("Arial", 13)).place(x=865, y=1020)
ttk.Label(frame1, text="REFERRED BY:",
         font=("Arial", 16),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=1060)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=24, font=("Arial", 13)).place(x=406, y=1060)
ttk.Label(frame1, text="REFFERAL CONTACT NO:",
         font=("Arial", 15),
         background="#609f9f",
         foreground="#80ffff").place(x=630, y=1060)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=19, font=("Arial", 13)).place(x=875, y=1060)
ttk.Label(frame1, text="DISCOUNT:",
         font=("Arial", 18),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=1100)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=74, font=("Arial", 13)).place(x=380, y=1100)
ttk.Label(frame1, text="SOURCES OF INFORMATION:",
         font=("Arial", 15),
         background="#609f9f",
         foreground="#80ffff").place(x=245, y=1140)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=57, font=("Arial", 13)).place(x=530, y=1140)
ttk.Label(frame1, text="HUB\n    IT", font=("Arial", 12, "bold"), foreground="green", width=4).place(x=370, y=37)
root.mainloop()
