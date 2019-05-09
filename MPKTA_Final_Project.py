#project akhir mpkta
#semoga lancar
#aminnn

from tkinter import *

lst = []

def readf():
    with open('all.txt', 'r') as f:
        line = ''
        for i in range(68):
            while('<deskripsi>' not in line):
                line = f.readline()
            cmp = ''
            txt = ''
            while('<end>' not in cmp):
                txt += cmp
                cmp = f.readline()
            lst.append(txt)

            line = f.readline()

class DirektoriMakanan():
    
    def __init__(self, master=Tk()):

        self.master = master
        master.minsize(width = 500, height = 600)
        master.maxsize(width = 500, height = 600)

        self.master.title("Selamat Datang di McDones (Direktori Macanan Tradisional)")
        self.master.judul = Label(self.master, text = "Pilih provinsi yang ingin anda ketahui", font = "Arial 16 bold")
        self.master.judul.grid(row = 0, column = 3, columnspan = 8)
        
        self.bprov1 = Button(self.master, text='Aceh', command=self.__prov1, width = 25)
        self.bprov1.grid(row = 1, column = 3, columnspan = 4)
        self.bprov2 = Button(self.master, text='Sumatera Utara', command=self.__prov2, width = 25)
        self.bprov2.grid(row = 2, column = 3, columnspan = 4)
        self.bprov3 = Button(self.master, text='Sumatera Barat', command=self.__prov3, width = 25)
        self.bprov3.grid(row = 3, column = 3, columnspan = 4)
        self.bprov4 = Button(self.master, text='Riau', command=self.__prov4, width = 25)
        self.bprov4.grid(row = 4, column = 3, columnspan = 4)
        self.bprov5 = Button(self.master, text='Kepulauan Riau', command=self.__prov5, width = 25)
        self.bprov5.grid(row = 5, column = 3, columnspan = 4)
        self.bprov6 = Button(self.master, text='Jambi', command=self.__prov6, width = 25)
        self.bprov6.grid(row = 6, column = 3, columnspan = 4)
        self.bprov7 = Button(self.master, text='Bengukulu', command=self.__prov7, width = 25)
        self.bprov7.grid(row = 7, column = 3, columnspan = 4)
        self.bprov8 = Button(self.master, text='Sumatera Selatan', command=self.__prov8, width = 25)
        self.bprov8.grid(row = 8, column = 3, columnspan = 4)
        self.bprov9 = Button(self.master, text='Kepulauan Bangka Belitung', command=self.__prov9, width = 25)
        self.bprov9.grid(row = 9, column = 3, columnspan = 4)
        self.bprov10 = Button(self.master, text='Lampung', command=self.__prov10, width = 25)
        self.bprov10.grid(row = 10, column = 3, columnspan = 4)
        self.bprov11 = Button(self.master, text='Banten', command=self.__prov11, width = 25)
        self.bprov11.grid(row = 11, column = 3, columnspan = 4)
        self.bprov12 = Button(self.master, text='Jawa Barat', command=self.__prov12, width = 25)
        self.bprov12.grid(row = 12, column = 3, columnspan = 4)
        self.bprov13 = Button(self.master, text='DKI Jakarta', command=self.__prov13, width = 25)
        self.bprov13.grid(row = 13, column = 3, columnspan = 4)
        self.bprov14 = Button(self.master, text='Jawa Tengah', command=self.__prov14, width = 25)
        self.bprov14.grid(row = 14, column = 3, columnspan = 4)
        self.bprov15 = Button(self.master, text='DI Yogyakarta', command=self.__prov15, width = 25)
        self.bprov15.grid(row = 15, column = 3, columnspan = 4)
        self.bprov16 = Button(self.master, text='Jawa Timur', command=self.__prov16, width = 25)
        self.bprov16.grid(row = 16, column = 3, columnspan = 4)
        self.bprov17 = Button(self.master, text='Bali', command=self.__prov17, width = 25)
        self.bprov17.grid(row = 17, column = 3, columnspan = 4)
        self.bprov18 = Button(self.master, text='NTB', command=self.__prov18, width = 25)
        self.bprov18.grid(row = 1, column = 7, columnspan = 4)
        self.bprov19 = Button(self.master, text='NTT', command=self.__prov19, width = 25)
        self.bprov19.grid(row = 2, column = 7, columnspan = 4)
        self.bprov20 = Button(self.master, text='Kalimantan Utara', command=self.__prov20, width = 25)
        self.bprov20.grid(row = 3, column = 7, columnspan = 4)
        self.bprov21 = Button(self.master, text='Kalimantan Barat', command=self.__prov21, width = 25)
        self.bprov21.grid(row = 4, column = 7, columnspan = 4)
        self.bprov22 = Button(self.master, text='Kalimantan Tengah', command=self.__prov22, width = 25)
        self.bprov22.grid(row = 5, column = 7, columnspan = 4)
        self.bprov23 = Button(self.master, text='Kalimantan Selatan', command=self.__prov23, width = 25)
        self.bprov23.grid(row = 6, column = 7, columnspan = 4)
        self.bprov24 = Button(self.master, text='Kalimantan Timur', command=self.__prov24, width = 25)
        self.bprov24.grid(row = 7, column = 7, columnspan = 4)
        self.bprov25 = Button(self.master, text='Gorontalo', command=self.__prov25, width = 25)
        self.bprov25.grid(row = 8, column = 7, columnspan = 4)
        self.bprov26 = Button(self.master, text='Sulawesi Utara', command=self.__prov26, width = 25)
        self.bprov26.grid(row = 9, column = 7, columnspan = 4)
        self.bprov27 = Button(self.master, text='Sulawesi Barat', command=self.__prov27, width = 25)
        self.bprov27.grid(row = 10, column = 7, columnspan = 4)
        self.bprov28 = Button(self.master, text='Sulawesi Tengah', command=self.__prov28, width = 25)
        self.bprov28.grid(row = 11, column = 7, columnspan = 4)
        self.bprov29 = Button(self.master, text='Sulawesi Selatan', command=self.__prov29, width = 25)
        self.bprov29.grid(row = 12, column = 7, columnspan = 4)
        self.bprov30 = Button(self.master, text='Sulawesi Tenggara', command=self.__prov30, width = 25)
        self.bprov30.grid(row = 13, column = 7, columnspan = 4)
        self.bprov31 = Button(self.master, text='Maluku Utara', command=self.__prov31, width = 25)
        self.bprov31.grid(row = 14, column = 7, columnspan = 4)
        self.bprov32 = Button(self.master, text='Maluku', command=self.__prov32, width = 25)
        self.bprov32.grid(row = 15, column = 7, columnspan = 4)
        self.bprov33 = Button(self.master, text='Papua Barat', command=self.__prov33, width = 25)
        self.bprov33.grid(row = 16, column = 7, columnspan = 4)
        self.bprov34 = Button(self.master, text='Papua', command=self.__prov34, width = 25)
        self.bprov34.grid(row = 17, column = 7, columnspan = 4)

        self.master.mainloop()

    def __prov1(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Mie Aceh', command=self.aceh1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Kue Timpan', command=self.aceh2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()

    def aceh1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Aceh")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Mie Aceh.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[0]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def aceh2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Aceh")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Kue Timpan.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[1]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()


    def __prov2(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Dekke Na Niura', command=self.sumut1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Bika Ambon', command=self.sumut2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()

    def sumut1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sumatera Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Dekke Na Niura.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[2]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sumut2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sumatera Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Bika Ambon.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[3]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()


    def __prov3(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Rendang', command=self.sumbar1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Ampiang Dadiah', command=self.sumbar2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    
    def sumbar1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sumatera Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Rendang.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[4]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sumbar2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sumatera Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Ampiang Dadiah.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[5]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()


    def __prov4(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Bolu Kemojo', command=self.riau1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Asidah', command=self.riau2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()

    def riau1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Riau")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Bolu Kemojo.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[6]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def riau2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Riau")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Asidah.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[7]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()

    def __prov5(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Luti Gendang', command=self.kriau1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Gong gong', command=self.kriau2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    
    def kriau1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kepulauan Riau")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Luti Gendang.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[8]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kriau2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kepulauan Riau")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Gong Gong.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[9]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()

    def __prov6(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Tempoyak', command=self.jambi1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Kue Padamaran', command=self.jambi2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def jambi1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jambi")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Tempoyak.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[10]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def jambi2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jambi")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Padamaran.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[11]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()

        
    def __prov7(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Lepek Binti', command=self.beng1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Bagar Hiu', command=self.beng2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def beng1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Bengkulu")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Lepek Binti.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[12]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def beng2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Bengkulu")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Bagar Hiu.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[13]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov8(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Pempek Palembang', command=self.sumsel1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Tekwan Palembang', command=self.sumsel2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def sumsel1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sumatera Selatan")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Pempek Palembang.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[14]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sumsel2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sumatera Selatan")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Tekwan Palembang.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[15]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
            
    def __prov9(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Martabak Bangka', command=self.kbang1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Belacan Belitung', command=self.kbang2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def kbang1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Bangka Belitung")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Martabak Bangka.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[16]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kbang2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Bangka Belitung")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Belaca Belitung.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[17]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov10(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Seruit Lampung', command=self.lamp1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Gulai Taboh', command=self.lamp2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def lamp1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Lampung")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Seruit Lampung.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[18]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def lamp2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Lampung")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Gulai Taboh.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[19]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov11(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Soto Betawi', command=self.dki1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Sayur Babanci', command=self.dki2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def dki1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional DKI Jakarta")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Soto Betawi.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[20]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def dki2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional DKI Jakarta")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sayur Babanci.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[21]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov12(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Nasi Sumsum', command=self.ban1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Sate Bandeng', command=self.ban2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def ban1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional BAnten")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Nasi Sumsum.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[22]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def ban2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Banten")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sate Bandeng.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[23]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov13(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Nasi Jamblang Daun Jati', command=self.jabar1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Dorokdok', command=self.jabar2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def jabar1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jawa Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Nasi Jamblang Daun Jati.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[24]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def jabar2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jawa Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Dorokdok.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[25]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()


    def __prov14(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Tiwul', command=self.diy1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Jadah Tempe', command=self.diy2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def diy1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional DI Yogyakarta")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Tiwul.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[26]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def diy2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional DI Yogyakarta")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Jadah Tempe.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[27]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
            
    def __prov15(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Soto Kudus', command=self.jateng1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Nasi Gerombyang', command=self.jateng2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def jateng1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jawa TEngah")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Soto Kudus.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[28]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def jateng2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jawa TEngah")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Nasi Grombyang.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[29]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov16(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Rujak Cingur', command=self.jatim1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Rawon', command=self.jatim2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def jatim1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jawa Timur")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Rujak Cingur.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[30]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def jatim2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Jawa Timur")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Rawon.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[31]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov17(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Sate Lilit', command=self.bali1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Ayam Betutu', command=self.bali2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def bali1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Bali")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sate Lilit.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[32]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def bali2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Bali")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Ayam Betutu.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[33]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov18(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Ayam Taliwang', command=self.ntb1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Sate Bulayak', command=self.ntb2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def ntb1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional NTB")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Ayam Taliwang.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[34]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def ntb2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional NTB")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sate Bulayak.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[35]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov19(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text="Se'i", command=self.ntt1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Tapa Kolo', command=self.ntt2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def ntt1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional NTT")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sei.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[36]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def ntt2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional NTT")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Tapa Kolo.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[37]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov20(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Lawa', command=self.kalut1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Kepiting Soka', command=self.kalut2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def kalut1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Lawa.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[38]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kalut2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Kepiting Soka.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[39]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
            
    def __prov21(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Bubur Paddas Sambas', command=self.kalbar1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Asam Padas Tempoyak', command=self.kalbar2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop() 
    def kalbar1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Bubur Paddas Sambas.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[40]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kalbar2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Asam Pedas Tempoyak.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[41]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov22(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Kalumpe', command=self.kalteng1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Wadi Patin', command=self.kalteng2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def kalteng1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Tengha")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Kalumpe.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[42]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kalteng2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Tengah")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Wadi Patin.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[43]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov23(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Manday', command=self.kalsel1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Gangan Asam Banjar', command=self.kalsel2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def kalsel1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Selatan")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Manday.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[44]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kalsel2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Selatan")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Gangan Asam Banjar.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[45]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov24(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Ayam Cincane', command=self.kaltim1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Nasi Bekekpor', command=self.kaltim2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def kaltim1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimnantan Timur")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Ayam Cincane.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[46]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def kaltim2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Kalimantan Timur")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Nasi Bekepor.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[47]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov25(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Binte Biluhuta', command=self.goron1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Bilenthango', command=self.goron2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def goron1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Gorontalo")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Binte Biluhuta.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[48]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def goron2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Gorontalo")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Bilenthango.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[49]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov26(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Kelapertaar', command=self.sulut1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Tinutuan', command=self.sulut2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def sulut1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Klapertaart.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[50]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sulut2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Tinutuan.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[51]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
            
    def __prov27(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Apang Bugis', command=self.sulbar1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Jepa', command=self.sulbar2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def sulbar1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Barat ")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Apang Bugis.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[52]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sulbar2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Jepa.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[53]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov28(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Uta Kelo', command=self.sulteng1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Kaledo', command=self.sulteng2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def sulteng1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Tengah")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Uta Kelo.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[54]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sulteng2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Tengah")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Kaledo.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[55]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov29(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Sop Konro', command=self.sulsel1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Coto Makassar', command=self.sulsel2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def sulsel1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Selatan")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sop Konro.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[56]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sulsel2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Selatan")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Coto Makassar.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[57]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov30(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Sinonggi', command=self.sulgar1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Kasoami', command=self.sulgar2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def sulgar1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Tenggara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sinonggi.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[58]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def sulgar2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Sulawesi Tenggara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Kasoami.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[59]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov31(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Gatang Kenari', command=self.malut1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Nasi Lapola', command=self.malut2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def malut1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Maluku Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Gatang Kenari.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[60]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def malut2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Maluku Utara")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Nasi Lapola.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[61]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov32(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Sambal Colo-colo', command=self.malu1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Kohu-kohu', command=self.malu2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def malu1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Maluku")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sambal Colo Colo.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[62]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def malu2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Maluku")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Kohu Kohu.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[63]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
            
    def __prov33(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Ikan Bakar Manokwari', command=self.pabar1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Sate Ulat Sagu', command=self.pabar2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def pabar1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Papua Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Ikan Bakar Manokwari.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[64]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def pabar2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Papua Barat")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Sate Ulat Sagu.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[65]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        
    def __prov34(self):
        master0 = Tk()
        
        master0.minsize(width = 450, height = 100)
        master0.maxsize(width = 450, height = 100)

        master0.title("Direktori Makanan Tradisional Nusantara")
        master0.judul = Label(master0, text = "Pilih makanan :)", font = "Arial 16 bold")
        master0.judul.grid(row = 0, column = 2, columnspan = 4)
        
        master0.bprov1 = Button(master0, text='Udang Salingkuh', command=self.papua1, width = 25, height=3)
        master0.bprov1.grid(row = 1, column = 2, columnspan = 4)
        master0.bprov2 = Button(master0, text='Papeda', command=self.papua2, width = 25, height=3)
        master0.bprov2.grid(row = 1, column = 6, columnspan = 4) 
        master0.mainloop()
    def papua1(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Papua")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Udang Selingkuh.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[66]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
    def papua2(self):
        master2 = Tk()
        master2.minsize(width = 800, height = 600)
        master2.maxsize(width = 800, height = 600)
        master2.title("Makanan tradisional Papua")
        
        canvas = Canvas(master2, width = 300, height = 300)      
        canvas.pack()      
        img = PhotoImage(master = canvas,file="Papeda.png")      
        canvas.create_image(5,5, anchor=NW, image=img) 
  
        text1 = lst[67]
        text2 = Text(master2, font = "Arial 12")
        text2.insert(INSERT, text1)
        text2.pack()
        master2.mainloop()
        



if __name__ == "__main__":
    readf()
    DirektoriMakanan()
