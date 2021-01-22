from tkinter import *
from tkinter import ttk
import tkinter
import webbrowser as wb
import mlModel as mm

class Application(object):

    def __init__(self,master):
        """
        tkinter ui
        """
        self.master = master

        #frames
        self.lvl1 = Frame(master,height=100,bg='white')
        self.lvl1.pack(fill=X)
        self.lvl2 = Frame(master,height=100,bg='#B577E4')
        self.lvl2.pack(fill=X)
        self.lvl3 = Frame(master,height=100,bg='#B577E4')
        self.lvl3.pack(fill=X)
        self.lvl4 = Frame(master,height=100,bg='#B577E4')
        self.lvl4.pack(fill=X)
        self.lvl5 = Frame(master,height=186,bg='#B577E4')
        self.lvl5.pack(fill=BOTH)
        self.lvl6 = Frame(master,height=15,bg='#B577E4')
        self.lvl6.pack(fill=X)

        #widgets
        self.heading = ttk.Label(self.lvl1,text='Iris Flower Specific Epithet Predictor',background='white',font=(('Gothic Medium'),35),foreground='#210934')
        self.heading.pack()

        self.insImg = PhotoImage(file='src/head.png')
        self.imgLbl = Label(self.lvl1,image=self.insImg,background='white')
        self.imgLbl.pack(pady=(10,5))

        self.fLbl1 = ttk.Label(self.lvl2,text='Sepal Length:',background='#B577E4',foreground='white')
        self.fLbl1.pack(side=LEFT,pady=(15,15))
        self.sLength = ttk.Entry(self.lvl2,width=17)
        self.sLength.insert(0,'Sepal Length in cm')
        self.sLength.pack(side=LEFT,padx=(0,10),pady=(15,15))

        self.fLbl2 = ttk.Label(self.lvl2,text='Sepal Width:',background='#B577E4',foreground='white')
        self.fLbl2.pack(side=LEFT,pady=(15,15))
        self.sWidth = ttk.Entry(self.lvl2,width=17)
        self.sWidth.insert(0,'Sepal Width in cm')
        self.sWidth.pack(side=LEFT,padx=(0,10),pady=(15,15))

        self.fLbl3 = ttk.Label(self.lvl2,text='Petal Length:',background='#B577E4',foreground='white')
        self.fLbl3.pack(side=LEFT,pady=(15,15))
        self.pLength = ttk.Entry(self.lvl2,width=17)
        self.pLength.insert(0,'Petal Length in cm')
        self.pLength.pack(side=LEFT,padx=(0,10),pady=(15,15))

        self.fLbl4 = ttk.Label(self.lvl2,text='Petal Width:',background='#B577E4',foreground='white')
        self.fLbl4.pack(side=LEFT,pady=(15,15))
        self.pWidth = ttk.Entry(self.lvl2,width=17)
        self.pWidth.insert(0,'Petal Length in cm')
        self.pWidth.pack(side=LEFT,pady=(15,15))

        self.pBtn = Button(self.lvl3,text='Predict!',fg='red',bg='white',font=(('Ariel'),30),command=self.changeImgaVal)
        self.pBtn.pack(side=LEFT,pady=(0,15),padx=(170,30))
        #self.cBtn = Button(self.lvl3,text='Clear Prediction',fg='black',bg='white',font=(('Ariel'),20),command=self.clearPrediction)
        #self.cBtn.pack(side=LEFT,pady=(0,15))

        self.pLbl = ttk.Label(self.lvl4,text='Prediction:',font=(('Ariel'),20),foreground='white',background='#B577E4')
        self.pLbl.pack(side=LEFT,pady=(15,15))

        self.about = Label(self.lvl6,text='About Developer',fg='blue',bg='#B577E4',cursor='hand2')
        self.about.pack(side=RIGHT)
        self.about.bind("<Button-1>", lambda e: self.new_window())

    def changeImgaVal(self):
        """
        Change Image and Name according to Prediction 
        5.2 1.2 4.2 0.5
        """
        data = [[float(self.sLength.get()),float(self.sWidth.get()),float(self.pLength.get()),float(self.pWidth.get())]]
        print(data)
        f1 = mm.modelM(data)
        val = f1.useModel()
        path = StringVar
        sName = StringVar

        if val == [0.]:
            path = 'src/setosa.png'
            sName = 'Iris Setosa'
        elif val == [1.]:
            path = 'src/virginica.png'
            sName = 'Iris Virginica'
        elif val == [2.]:
            path = 'src/versicolor.png'
            sName = 'Iris Versicolor'
        
        self.pImg = PhotoImage(file=path)
        self.pName = ttk.Label(self.lvl4,text=sName,font=(('Ariel'),20),foreground='red',background='#B577E4')
        self.pImgLbl = Label(self.lvl5,image=self.pImg)
        self.pImgLbl.pack()
        self.pName.pack(side=LEFT)

    def callback(self,url):
        """
        Label Hyperlinks
        """
        wb.open_new(url)


    def new_window(self):
        self.new = tkinter.Toplevel()
        self.new.title('About Developer')
        self.new.iconbitmap('src/aboutdev.ico')
        self.new.geometry('500x300+50+50')

        #frames
        self.leftF = Frame(self.new,width=150,bg='white')
        self.leftF.pack(side=LEFT,fill=Y)
        self.rightF = Frame(self.new,width=350,bg='#92A8D1')
        self.rightF.pack(side=RIGHT,fill=Y)

        #widgets
        self.devImg = PhotoImage(file='src/dev.png')
        self.devImgLbl = Label(self.leftF,image=self.devImg,background='white')
        self.devImgLbl.pack(padx=(10,10),pady=(10,0))

        self.nmeLbl = ttk.Label(self.rightF,text='Pasindu Akalpa',font=(('Adobe Devanagari'),20),background='#92A8D1')
        self.nmeLbl.place(x=20,y=20)
        self.github = ttk.Label(self.rightF,text='GitHub',font=(('Adobe Devanagari'),15),background='#92A8D1',cursor='hand2')
        self.github.place(x=20,y=70)
        self.github.bind("<Button-1>", lambda e: self.callback('https://github.com/pAkalpa'))
        self.twitter = ttk.Label(self.rightF,text='Twitter',font=(('Adobe Devanagari'),15),background='#92A8D1',cursor='hand2')
        self.twitter.place(x=20,y=90)
        self.twitter.bind("<Button-1>", lambda e: self.callback('http://twitter.com/AkalpaPasindu'))


def main():
    """
    main method
    """
    win = Tk()
    app = Application(win)
    win.wm_iconbitmap('src/f.ico')
    win.wm_title('Specific Predictor')
    win.geometry('763x650+10+20')
    win.mainloop()

if __name__ == '__main__':
    main()