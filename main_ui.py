from tkinter import *
def main():
    import tkinter
    r = Tk() 
    r.title('Sign Language Interpretor') 
    r.geometry('250x150')
    def open_rev_asl():
        window = Tk()        
        window.title("English to ASL")        
        window.geometry('350x200')        
        lbl = Label(window, text="Enter the text/Say Something")        
        lbl.grid(column=0, row=0)        
        txt = Entry(window,width=20)        
        txt.grid(column=1, row=0)        
        def clicked():        
            rev_asl(txt.get())
            # window.destroy()  # to exit after each ip    
        btn = Button(window, text="Click Me", command=clicked)        
        btn.grid(column=2, row=0)        
        window.mainloop()

    asl_button = tkinter.Button(r,text='ASL to English',width=25,command=asl)
    asl_button.pack()
    rev_button = tkinter.Button(r,text='English to ASL',width=25,command=open_rev_asl)
    rev_button.pack()
    quit_button = tkinter.Button(r, text='EXIT', width=25, command=r.destroy) 
    quit_button.pack() 
    r.mainloop() 
    
def asl():
    import ASL

def rev_asl(txt):
    from reverse import rev
    rev(txt)

main()