from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import fuctions
import sys
from io import StringIO
import contextlib
import os
import wordcolor

compiler = Tk()
compiler.title('My Fantastic IDE')
compiler.resizable(False,False)
#compiler.attributes('-fullscreen',True)


#લખો("કેમ છો")
#લખો("ક ખ ગ ચ મ બ ")
def myfuc(event):
    list1=['$દોરવાનું દાખલ કરો$','દોરો.આગળ','દોરો.પાછળ','દોરો.જમણીબાજુ','દોરો.ડાબીબાજુ','દોરો.પેનનોરંગ','લાલ','કાળો','વાદળી','લીલો','દોરો.વર્તુળ','દોરો.રદકરો','દોરો.પેનબંધ','દોરો.પેનચાલુ','દોરો.રંગપૂરો']           
    list2 = ['લખો','ફરીથી','જો','અથવાજો','નહીતો','જ્યાંસુધી','ની','શ્રેણી']  #00ff00
    for i in range(len(list1)):
        p1=wordcolor.colorcode(list1[i],editor);p1.findver()
    
    for i in range(len(list2)):
        p1=wordcolor.colorcode(list2[i],editor);p1.findimpter()

def helper():
    print("help")
    h1 = Tk()
    h1.title("helper")
    l1 = Label(h1,text="enter fuction")
    l1.pack(side=LEFT)
    e1 = Entry(h1,bd=5)
    e1.pack(side=RIGHT)
    h1.mainloop()

def run():
    code_output.delete("1.0",END)
    a=editor.get("1.0",END)
    p1 = fuctions.frist1(a)
    p2 = p1.frist()
    p2=p1.maths()
    p2=p1.olp()
    p2=p1.drowing()
    #print(p2)
    @contextlib.contextmanager
    def stdoutIO(stdout=None):
        old=sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout=stdout
        yield stdout
        sys.stdout = old
    #print(p2)
    with stdoutIO() as s:
        try:
            exec(p2)
        except SyntaxError as err:
            editor.tag_add("tag1",f'{err.lineno}.0',f'{err.lineno}.100')
            editor.tag_config("tag1",background="red")
            print(f'લાઈન નંબર {err.lineno} માં કઈક ભૂલ છે.')

    p=(s.getvalue())
    #print(p)
    code_output.insert(INSERT,p)
    

manubar = Menu(compiler)
compiler.config(menu=manubar)

comand=Menu(manubar)
manubar.add_cascade(label='commands',menu=comand)
comand.add_command(label='run',command=run)
comand.add_command(label='fuctions',command=helper)

editor = Text(background="#454545",foreground="#07040A",font=('Century schoolbook',13,'italic'))
editor.pack()

code_output = Text(height=10,background="#388F72",foreground="#07040A",font=('Century schoolbook',13,'italic'))
code_output.pack()



compiler.bind('<Key>',myfuc)


compiler.mainloop()