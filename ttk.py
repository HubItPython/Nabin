from tkinter import Tk, Canvas
from tkinter import ttk
from customtkinter import CTkScrollableFrame, CTkLabel,CTkFrame

root = Tk()
root.geometry("1350x700")

# Create a scrollable frame
frame1 = CTkScrollableFrame(root, width=1350, height=400, fg_color="#cdfefe").place(x=0,y=1)

style = ttk.Style()
style.configure('Rounded.TEntry', padding=45)
ttk.Label(frame1, text="Regi No:112123/075/076", background="#cdfefe", font=("Arial", 8), foreground="black").place(x=930, y=5)

label = ttk.Label(frame1, text="HUB IT GROUP PVT.LTD.", font=("Arial", 30, "bold"), background="#cdfefe", foreground="green")
label.place(x=460, y=20)
canvas = Canvas(frame1, width=90, height=120, bd=0)
canvas.place(x=350, y=9)
circle = canvas.create_oval(2, 2, 80, 80)
circle1 = canvas.create_oval(70, 9, 62, 16, fill="green")
circle2 = canvas.create_oval(61, 2, 54, 10, fill="green")

circle3 = canvas.create_oval(7, 60, 15, 70, fill="green")
circle4 = canvas.create_oval(70, 67, 60, 76, fill="green")
ttk.Label(frame1, background="#cdfefe", text="IT", font=("Arial", 12, "bold"), foreground="green", width=2).place(x=405, y=37)
label2 = ttk.Label(frame1, background="#cdfefe", text="Butwal-09 (Ganesh Path) Milanchowk", font=("Arial", 13, "bold"), foreground="black")
ttk.Label(frame1, background="#cdfefe", text="ph: 071-532805, 9827494116, 9827494119", font=("Arial", 13, "bold"), foreground="black").place(x=535, y=95)
label2.place(x=550, y=70)
head = CTkLabel(frame1, text="STUDENT ENROLLMENT REGISTRATION FORM",
                font=("Arial", 25, "bold"),
                text_color="white",
                fg_color="green",
                anchor="center",
                width=800,
                corner_radius=5)
head.place(x=245, y=125)
headl = CTkLabel(frame1, text="FULL NAME:",
                 font=("Arial", 18),
                 text_color="Black",
                 fg_color="#80ffff",
                 corner_radius=5)
headl.place(x=245, y=167)
headle = ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=55, font=("Arial", 13))
headle.place(x=363, y=167)

CTkLabel(frame1, text="ADDRESS:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=205)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=56, font=("Arial", 13)).place(x=354, y=205)
CTkLabel(frame1, text="CELL NO:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=250)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=25, font=("Arial", 13)).place(x=350, y=250)
CTkLabel(frame1, text="Date:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=595, y=250)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=23, font=("Arial", 13)).place(x=650, y=250)
CTkLabel(frame1, text="GUARDIAN's NAME:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=290)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=427, y=290)

CTkLabel(frame1, text="PHONE NO:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=325)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=75, font=("Arial", 13)).place(x=362, y=325)
CTkLabel(frame1, text="GENDER:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=360)
gen = ["Male", "Female"]
ttk.Combobox(frame1, values=gen, font=("Arial", 13)).place(x=342, y=360)
CTkLabel(frame1, text="DATE OF BIRTH:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=560, y=360)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=35, font=("Arial", 13)).place(x=720, y=360)
CTkLabel(frame1, text="EMAIL:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=400)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=79, font=("Arial", 13)).place(x=325, y=400)
CTkLabel(frame1, text="LEVEL OF EDUCATION:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=440)
lvl = ["see", +2, "Bachelor", "Masters"]
ttk.Combobox(frame1, values=lvl, font=("Arial", 13), width=62).place(x=465, y=440)
CTkLabel(frame1, text="NAME OF THE SCHOOL/COLLEGE:",
         font=("Arial", 18),
         text_color="Black",
         fg_color="#80ffff",
         corner_radius=5).place(x=245, y=480)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=52, font=("Arial", 13)).place(x=568, y=480)
CTkLabel(frame1, text="NAME OF COURSE/S TO ENROLL",
          font=("Arial", 25, "bold"),
          text_color="white",
          fg_color="green",
          anchor="center",
          width=800,
          corner_radius=5).place(x=245, y=520)

ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=262, y=560)
CTkLabel(frame1, text="1",
          font=("Arial", 25, "bold"),
          text_color="white",
          fg_color="#80ffff",
          anchor="center",
          corner_radius=5).place(x=245, y=560)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=262, y=600)
CTkLabel(frame1, text="2",
          font=("Arial", 25, "bold"),
          text_color="white",
          fg_color="#80ffff",
          anchor="center",
          corner_radius=5).place(x=245, y=600)
ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=262, y=640)
CTkLabel(frame1, text="3",
          font=("Arial", 25, "bold"),
          text_color="white",
          fg_color="#80ffff",
          anchor="center",
          corner_radius=5).place(x=245, y=640)

ttk.Entry(frame1, justify="center", style="Rounded.TButton", width=48, font=("Arial", 13)).place(x=262, y=640)
CTkLabel(frame1, text="OTHER COURSE PREVIOUSLY TAKEN",
          font=("Arial", 18, "bold"),
          text_color="white",
          fg_color="#80ffff",
          anchor="center",
          corner_radius=5).place(x=705, y=560)
a = ttk.Entry(frame1, justify="center", style="Rounded.TEntry", font=("Arial", 13))
a.place(x=710, y=590)

root.mainloop()
