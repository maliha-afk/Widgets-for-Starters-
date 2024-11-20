from tkinter import *

screen=Tk()
screen.title("Star Kebab")
screen.config(bg="lightgreen")
screen.geometry("500x400")

welcome=Label(screen,text="Welcome to Star Kebab",font=("Alice",20,"bold"),fg="black",bg="lightgreen")
welcome.grid(row=0,column=1)

pz_text=Label(screen,text="Pizza(10$)",font=("Alice",20,"bold"),fg="black",bg="lightgreen")
pz_text.grid(row=1,column=0,padx=5)
pz_q=Entry(screen,font=("Alice",10,"bold"))
pz_q.grid(row=1,column=1,padx=15)

burger_text=Label(screen,text="burger(5$)",font=("Alice",20,"bold"),fg="black",bg="lightgreen")
burger_text.grid(row=2,column=0,padx=5)
b_q=Entry(screen,font=("Alice",10,"bold"))
b_q.grid(row=2,column=1,padx=5)

momo_text=Label(screen,text="momo(3$)",font=("Alice",20,"bold"),fg="black",bg="lightgreen")
momo_text.grid(row=3,column=0,padx=5)
m_q=Entry(screen,font=("Alice",10,"bold"))
m_q.grid(row=3,column=1,padx=5)

noodles_text=Label(screen,text="noodles(3$)",font=("Alice",20,"bold"),fg="black",bg="lightgreen")
noodles_text.grid(row=4,column=0,padx=5)
n_q=Entry(screen,font=("Alice",10,"bold"))
n_q.grid(row=4,column=1,padx=5)

def generatebill():
    p_count=int(pz_q.get())
    b_count=int(b_q.get())
    m_count=int(m_q.get())
    n_count=int(n_q.get())
    price=(p_count*6)+(b_count*5)+(m_count*3)+(n_count*3)
    my_price.config(text=f"your total bill is {price} $ \n the items you have purchased: \n pizza:{p_count}\n burger:{b_count}\n noodles:{n_count}\n MOMO {m_count}")

bill=Button(screen,text=("Generate bill"),font=("Alice",10,"bold"),command=generatebill)
bill.grid(row=7,column=0,padx=5)

def refresh():
    my_price.config(text="")

reset=Button(screen,text="Reset",font=("Alice",10,"bold"),fg="black",bg="white",command=refresh)
reset.grid(row=7,column=1,padx=5)
my_price=Label(screen,font=("Alice",10,"bold"),fg="black",bg="lightgreen")
my_price.grid(row=8,column=1,padx=5)







screen.mainloop()