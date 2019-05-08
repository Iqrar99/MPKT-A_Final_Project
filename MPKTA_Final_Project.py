#project akhir mpkta
#semoga lancar
#aminnn

from tkinter import *

class DirektoriMakanan():
	def __init__(self, master=Tk()):
		self.master = master
		master.minsize(width = 500, height = 550)
		master.maxsize(width = 500, height = 550)


		self.master.title("Direktori Makanan Tradisional Nusantara")
		self.master.judul = Label(self.master, text = "Direktori Makanan Tradisional Nusantara", font = "Arial 16 bold")

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
		pass
	def __prov2(self):
		pass	
	def __prov3(self):
		pass
	def __prov4(self):
		pass
	def __prov5(self):
		pass
	def __prov6(self):
		pass
	def __prov7(self):
		pass
	def __prov8(self):
		pass	
	def __prov9(self):
		pass
	def __prov10(self):
		pass
	def __prov11(self):
		pass
	def __prov12(self):
		pass
	def __prov13(self):
		pass
	def __prov14(self):
		pass	
	def __prov15(self):
		pass
	def __prov16(self):
		pass
	def __prov17(self):
		pass
	def __prov18(self):
		pass
	def __prov19(self):
		pass
	def __prov20(self):
		pass	
	def __prov21(self):
		pass
	def __prov22(self):
		pass
	def __prov23(self):
		pass
	def __prov24(self):
		pass
	def __prov25(self):
		pass
	def __prov26(self):
		pass	
	def __prov27(self):
		pass
	def __prov28(self):
		pass
	def __prov29(self):
		pass
	def __prov30(self):
		pass
	def __prov31(self):
		pass
	def __prov32(self):
		pass	
	def __prov33(self):
		pass
	def __prov34(self):
		pass




if __name__ == "__main__":
	DirektoriMakanan()
