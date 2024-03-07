from tkinter import Tk,Button,Entry
from math import sin,cos,tan
def append_to_entry(val):
    try:
        curren=inp.get()
        inp.delete(0, 'end')
        inp.insert('end', curren + str(val))
    except:
        inp.delete(0, 'end')
        inp.insert('end', 'Error')

    

def equal(event=None):
    try:

        curren=inp.get()
        result=eval(curren)
        inp.delete(0, 'end')
        inp.insert('end', f'{result}')
    except:
        inp.delete(0, 'end')
        inp.insert('end', 'Error')


def clear_func():
    try:
        inp.delete(len(inp.get()) - 1, 'end')
    except:
        inp.delete(0, 'end')
        inp.insert('end', 'Error')

r= Tk()
screen_width = r.winfo_screenwidth()
screen_height = r.winfo_screenheight()
x = (screen_width - 480) // 2
y = (screen_height - 480) // 2
r.geometry(f'380x450+{x}+{y}')
r.title('Calculator')
r.configure(bg='#f9f1ff')
inp=Entry(r,justify='right')
inp.place(x=10,y=10,width=360,height=60)
inp.config(bg='#ebebe0',font=('Sans Serif',18))

sin_btn=Button(r,font=('Sans Serif',18),text='sin',command=lambda: append_to_entry('sin('))
sin_btn.place(x=13,y=90,width=55,height=55)

cos_btn=Button(r,font=('Sans Serif',18),text='cos',command=lambda: append_to_entry('cos('))
cos_btn.place(x=74,y=90,width=55,height=55)

tan_btn=Button(r,font=('Sans Serif',18),text='tan',command=lambda: append_to_entry('tan('))
tan_btn.place(x=136,y=90,width=55,height=55)

openbracket_btn=Button(r,font=('Sans Serif',18),text='(',command=lambda: append_to_entry('('))
openbracket_btn.place(x=196,y=90,width=55,height=55)

bracket_btn=Button(r,font=('Sans Serif',18),text=')',command=lambda: append_to_entry(')'))
bracket_btn.place(x=259,y=90,width=55,height=55)


backspace_btn = Button(r,font=('Sans Serif',18), text='←', command=clear_func)
backspace_btn.place(x=320, y=90, width=55, height=55)

b1=Button(r,font=('Sans Serif',18),text='1', command=lambda: append_to_entry('1'))
b1.place(x=13,y=160,width=75,height=55)

b2=Button(r,font=('Sans Serif',18),text='2', command=lambda: append_to_entry('2'))
b2.place(x=110,y=160,width=75,height=55)

b3=Button(r,font=('Sans Serif',18),text='3', command=lambda: append_to_entry('3'))
b3.place(x=207,y=160,width=75,height=55)

add_btn=Button(r,font=('Sans Serif',18),text='+',command=lambda: append_to_entry('+'))
add_btn.place(x=304,y=160,width=75,height=55)

b4=Button(r,font=('Sans Serif',18),text='4', command=lambda: append_to_entry('4'))
b4.place(x=13,y=230,width=75,height=55)

b5=Button(r,font=('Sans Serif',18),text='5', command=lambda: append_to_entry('5'))
b5.place(x=110,y=230,width=75,height=55)

b6=Button(r,font=('Sans Serif',18),text='6', command=lambda: append_to_entry('6'))
b6.place(x=207,y=230,width=75,height=55)

sub_btn=Button(r,font=('Sans Serif',18),text='-',command=lambda: append_to_entry('-'))
sub_btn.place(x=304,y=230,width=75,height=55)


b7=Button(r,font=('Sans Serif',18),text='7', command=lambda: append_to_entry('7'))
b7.place(x=13,y=300,width=75,height=55)

b8=Button(r,font=('Sans Serif',18),text='8', command=lambda: append_to_entry('8'))
b8.place(x=110,y=300,width=75,height=55)

b9=Button(r,font=('Sans Serif',18),text='9', command=lambda: append_to_entry('9'))
b9.place(x=207,y=300,width=75,height=55)


mul_btn=Button(r,font=('Sans Serif',18),text='',command=lambda: append_to_entry(''))
mul_btn.place(x=304,y=300,width=75,height=55)


clear_btn=Button(r,font=('Sans Serif',18),text='CE',command=lambda: (inp.delete(0,'end'),inp.insert('end','')))
clear_btn.place(x=13,y=365,width=75,height=55)

b0=Button(r,font=('Sans Serif',18),text='0', command=lambda: append_to_entry('0'))
b0.place(x=110,y=365,width=75,height=55)

equal_btn=Button(r,font=('Sans Serif',18),text='=',command=equal)
equal_btn.place(x=207,y=365,width=75,height=55)



div_btn=Button(r,font=('Sans Serif',18),text='/',command=lambda: append_to_entry('/'))
div_btn.place(x=304,y=365,width=75,height=55)

r.bind('<Return>', equal)

r.mainloop()