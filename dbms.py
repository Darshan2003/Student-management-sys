
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import *
from sqlite3 import *
from tkinter .scrolledtext import*
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import requests
import socket
import bs4
import lxml



def f1():
	addst.deiconify()
	root.withdraw()
	entrno.focus()

def f2():
	con=None
	try:
		con=connect("stundetails.db")

		cur=con.cursor()
		sql="insert into student values('%d','%s','%s','%s','%d','%d')"
		rno=entrno.get()
		name=entname.get()
		lname=entlname.get()
		address=entaddress.get()
		phone=entnumber.get()
		marks=entmarks.get()


		if len(name)==0:
			showerror("Mistake","Name should not be empty")
			return
		if (len(phone)!=10):
			showerror("Mistake","Phone must of 10 digit only. ")
			return	
		if len(rno)==0:
			showerror("Mistake","roll no. should not be empty")
			return
		if len(address)==0:
			showerror("Mistake","Address should not be empty")
			return
		if not rno.isdigit():
			showerror("Mistake","rno should contain integers only")
			return
		if not phone.isdigit():
			showerror("Mistake","Phone no. should contain integers only")
			return
		srno=int(rno)
		pnumber=int(phone)
		
		if not name.isalpha():
			showerror("Mistake","first name should contain alphabets only")
			return
		if not lname.isalpha():
			showerror("Mistake","last name should contain alphabets only")
			return
	
		
		
		if len(marks)==0:
			showerror("Mistake","marks should not be empty")
			return
		
		if not marks.isdigit():
			showerror("Mistake","marks should contain integers only")
			return
		mark=int(marks)
		if (mark>100 or mark<0):
			showerror("Mistake","marks should be in the range of 0 to 100")
			return
			
		cur.execute(sql%(srno,name,lname,address,pnumber,mark))
		con.commit()
		showinfo("Success","Data Saved")
	except Exception as e:
		con.rollback()
		showerror("Error",e)


	finally:
		if con is not None:
			con.close()
		entlname.delete(0,END)
		entnumber.delete(0,END)
		entaddress.delete(0,END)
		entmarks.delete(0,END)
		entrno.delete(0,END)
		entname.delete(0,END)
		entrno.focus()


def f3():
    root.deiconify()
    addst.withdraw()

def f4():
	
	vist.deiconify()
	root.withdraw()
	con=None
	try:
		con=connect("stundetails.db")
		for i in tv.get_children():
    			tv.delete(i)
		cur=con.cursor()
		sql="select * from student"
		cur.execute(sql)
		data=cur.fetchall()
		for i in data:
			tv.insert('','end',values=i)

	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()


def f5():
	root.deiconify()
	vist.withdraw()

def f6():
	upst.deiconify()
	root.withdraw()
	upstentrno.focus()

def f7():
	con=None
	try:
		con=connect("stundetails.db")
		rno=upstentrno.get()
		name=upstentname.get()
		lname=upstentlname.get()
		address=upstentaddress.get()
		phone=upstentnumber.get()
		marks=upstentmarks.get()
		cur=con.cursor()
		sql="update student set marks='%d',name='%s',lname='%s',address='%s',pnumber='%d' where srno='%d'"
		
		if len(name)==0:
			showerror("Mistake","Name should not be empty")
			return
		if (len(phone)!=10):
			showerror("Mistake","Phone must of 10 digit only. ")
			return	
		if len(rno)==0:
			showerror("Mistake","roll no. should not be empty")
			return
		if len(address)==0:
			showerror("Mistake","Address should not be empty")
			return
		if not rno.isdigit():
			showerror("Mistake","rno should contain integers only")
			return
		if not phone.isdigit():
			showerror("Mistake","Phone no. should contain integers only")
			return
		srno=int(rno)
		pnumber=int(phone)
		
		if not name.isalpha():
			showerror("Mistake","first name should contain alphabets only")
			return
		if not lname.isalpha():
			showerror("Mistake","last name should contain alphabets only")
			return
	
		
		
		if len(marks)==0:
			showerror("Mistake","marks should not be empty")
			return
		
		if not marks.isdigit():
			showerror("Mistake","marks should contain integers only")
			return
		mark=int(marks)
		if (mark>100 or mark<0):
			showerror("Mistake","marks should be in the range of 0 to 100")
			return
			
		
		cur.execute(sql%(mark,name,lname,address,pnumber,srno))
		con.commit()
		if cur.rowcount>0:
			showinfo("Success","Data Updated")
		else:
			showerror("Error","Record does not exist")
	except Exception as e:
		con.rollback()
		showerror("Error",e)


	finally:
		if con is not None:
			con.close()
		upstentlname.delete(0,END)
		upstentaddress.delete(0,END)
		upstentnumber.delete(0,END)	
		upstentmarks.delete(0,END)
		upstentrno.delete(0,END)
		upstentname.delete(0,END)
		upstentrno.focus()

def f8():
	root.deiconify()
	upst.withdraw()

def f9():
	dlt.deiconify()
	root.withdraw()
	dlt_entrno.focus()

def f10():
	con=None
	try:
		con=connect("stundetails.db")

		cur=con.cursor()
		sql="delete from student where srno='%d'"
		rno=dlt_entrno.get()
		if len(rno)==0:
			showerror("Mistake","roll no. should not be empty")
			return
		srno=int(rno)
		cur.execute(sql%(srno))
		con.commit()
		if cur.rowcount>0:
			showinfo("Error","Record deleted")
		else:
			showerror("Error","Record does not exists")
	except ValueError:
		con.rollback()
		showerror("Error","please enter integer only")
	except Exception as e:
		con.rollback()
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()

		dlt_entrno.delete(0,END)
		dlt_entrno.focus()

def f11():
	root.deiconify()
	dlt.withdraw()

def f12():
	con=None
	student_list=[]
	marks_list=[]
	try:
		con=connect("stundetails.db")
		cur=con.cursor()
		sql="select * from student"
		cur.execute(sql)
		table=cur.fetchall()
		for rno,name,lname,address,phone,marks in table:
			student_list.append(name)
			marks_list.append(marks)
		plt.title("Batch Details!")
		plt.bar(student_list,marks_list,linewidth=5,width=0.65,alpha=0.45)
		plt.xlabel("Names")
		plt.ylabel("Marks")
		plt.show()

	except Exception as e:
		showerror("Error",e)
	finally:
		if con is not None:
			con.close()	

def f13():
	name=loginname.get()
	Pass=loginpass.get()
	if name=="Vidyalankar" and Pass=="vidyalankar": 
		login.withdraw()
		root.deiconify()

	else:
		showerror("Error","Invalid Login Credentials")
def on_close():
	if askokcancel("Quit","Do you want to exit ?"):
		login.destroy()

login =Tk()
login.geometry("420x390+600+200")
login.title("S M S by Darshan & Soham ")
login.resizable(False,False)
login.protocol("WM_DELETE_WINDOW",on_close)

LOGINname=Label(login,text="Enter Name:",font=('arial',15,'bold'),bg="#82e0bd")
loginname=Entry(login,bd=3,font=('arial',19,'bold'))
LOGINpass=Label(login,text="Enter Password:",font=('arial',15,'bold'),bg="#82e0bd")
loginpass=Entry(login,bd=3,font=('arial',19,'bold'),show='*')
LOGIN=Button(login,text="Login",font=('arial',13,'bold'),width=10,command=f13)

LOGINname.pack(pady=(20,5))
loginname.pack()
LOGINpass.pack(pady=5)
loginpass.pack()
LOGIN.pack(pady=(30,0))
loginname.focus()
login.configure(background='#82e0bd')
root=Toplevel(login)
root.geometry("420x390+600+200")
root.title("S M S by Darshan & Soham ")
root.resizable(False,False)
root.protocol("WM_DELETE_WINDOW",on_close)


btnAdd=Button(root,text="Insert",font=('arial',13,'bold'),width=10,command=f1)
btnView=Button(root,text="View",font=('arial',13,'bold'),width=10,command=f4)
btnUpdate=Button(root,text="Update",font=('arial',13,'bold'),width=10,command=f6)
btnDelete=Button(root,text="Delete",font=('arial',13,'bold'),width=10,command=f9)
btnCharts=Button(root,text="Charts",font=('arial',13,'bold'),width=10,command=f12)

btnAdd.place(x=155,y=20)
btnView.place(x=155,y=60)
btnUpdate.place(x=155,y=100)
btnDelete.place(x=155,y=140)
btnCharts.place(x=155,y=180)

root.configure(background='#82e0bd')
root.withdraw()
addst=Toplevel(root)
addst.geometry("500x365+600+200")
addst.title("Add St.")
addst.resizable(False,False)
addst.protocol("WM_DELETE_WINDOW",on_close)
lblrno=Label(addst,text="Enter Roll no:",font=('arial',15,'bold'),bg="#d1e3ff")
entrno=Entry(addst,bd=3,font=('arial',19,'bold'))

lblname=Label(addst,text="Enter First Name:",font=('arial',15,'bold'),bg="#d1e3ff")
entname=Entry(addst,bd=3,font=('arial',19,'bold'))

lbllname=Label(addst,text="Enter Last Name:",font=('arial',15,'bold'),bg="#d1e3ff")
entlname=Entry(addst,bd=3,font=('arial',19,'bold'))

lbladdress=Label(addst,text="Enter Address:",font=('arial',15,'bold'),bg="#d1e3ff")
entaddress=Entry(addst,bd=3,font=('arial',19,'bold'))

lblnumber=Label(addst,text="Enter Phone no:",font=('arial',15,'bold'),bg="#d1e3ff")
entnumber=Entry(addst,bd=3,font=('arial',19,'bold'))

lblmarks=Label(addst,text="Enter Marks:",font=('arial',15,'bold'),bg="#d1e3ff")
entmarks=Entry(addst,bd=3,font=('arial',19,'bold'))
btnsave=Button(addst,text="Save",font=('arial',13,'bold'),width=10,command=f2)
btnback=Button(addst,text="Back",font=('arial',13,'bold'),width=10,command=f3)

lblrno.place(x=5,y=10)
entrno.place(x=200,y=10)
lblname.place(x=5,y=55)
entname.place(x=200,y=55)
lbllname.place(x=5,y=100)
entlname.place(x=200,y=100)
lbladdress.place(x=5,y=145)
entaddress.place(x=200,y=145)
lblnumber.place(x=5,y=190)
entnumber.place(x=200,y=190)
lblmarks.place(x=5,y=235)
entmarks.place(x=200,y=235)
btnsave.place(x=200,y=285)
btnback.place(x=200,y=325)

addst.configure(background="#d1e3ff")
addst.withdraw()

vist=Toplevel(root)
vist.title("View stu")
vist.geometry("612x250+600+200")
vist.resizable(False,False)
vist.protocol("WM_DELETE_WINDOW",on_close)
frm=Frame(vist)
frm.pack(padx=5,pady=10)

tv=ttk.Treeview(frm,columns=(1,2,3,4,5,6),show="headings",height="8")
tv.pack()
style=ttk.Style()

tv.heading(1,text="Roll no")
tv.heading(2,text="First Name")
tv.heading(3,text="Last Name")
tv.heading(4,text="Address")
tv.heading(5,text="Phone no")
tv.heading(6,text="Marks")

tv.column(1,width=100, stretch=NO)
tv.column(2,width=100, stretch=NO)
tv.column(3,width=100, stretch=NO)
tv.column(4,width=100, stretch=NO)
tv.column(5,width=100, stretch=NO)
tv.column(6,width=100, stretch=NO)
style.configure("Custom.Treeview.Heading",background="green")

vist_btnback=Button(vist,text="Back",font=('arial',13,'bold'),width=10,command=f5)

vist_btnback.place(x=260,y=205)
vist.configure(background="#fff3c4")
vist.withdraw()

upst=Toplevel(root)
upst.title("Update stu")
upst.geometry("500x365+600+200")
upst.resizable(False,False)
upst.protocol("WM_DELETE_WINDOW",on_close)
upstrno=Label(upst,text="Enter Roll no:",font=('arial',15,'bold'),bg="#ffd1d6")
upstentrno=Entry(upst,bd=3,font=('arial',19,'bold'))

upstname=Label(upst,text="Enter First Name:",font=('arial',15,'bold'),bg="#ffd1d6")
upstentname=Entry(upst,bd=3,font=('arial',19,'bold'))

upstlname=Label(upst,text="Enter Last Name:",font=('arial',15,'bold'),bg="#ffd1d6")
upstentlname=Entry(upst,bd=3,font=('arial',19,'bold'))

upstaddress=Label(upst,text="Enter Address:",font=('arial',15,'bold'),bg="#ffd1d6")
upstentaddress=Entry(upst,bd=3,font=('arial',19,'bold'))

upstnumber=Label(upst,text="Enter Phone no:",font=('arial',15,'bold'),bg="#ffd1d6")
upstentnumber=Entry(upst,bd=3,font=('arial',19,'bold'))

upstmarks=Label(upst,text="Enter Marks:",font=('arial',15,'bold'),bg="#ffd1d6")
upstentmarks=Entry(upst,bd=3,font=('arial',19,'bold'))

upstsave=Button(upst,text="Update",font=('arial',13,'bold'),width=10,command=f7)
upstback=Button(upst,text="Back",font=('arial',13,'bold'),width=10,command=f8)


upstrno.place(x=5,y=10)
upstentrno.place(x=200,y=10)
upstname.place(x=5,y=55)
upstentname.place(x=200,y=55)
upstlname.place(x=5,y=100)
upstentlname.place(x=200,y=100)
upstaddress.place(x=5,y=145)
upstentaddress.place(x=200,y=145)
upstnumber.place(x=5,y=190)
upstentnumber.place(x=200,y=190)
upstmarks.place(x=5,y=235)
upstentmarks.place(x=200,y=235)
upstsave.place(x=200,y=285)
upstback.place(x=200,y=325)

upst.configure(background="#ffd1d6")
upst.withdraw()

dlt=Toplevel(root)
dlt.title("Delete stu")
dlt.geometry("420x330+600+200")
dlt.resizable(False,False)
dlt.protocol("WM_DELETE_WINDOW",on_close)
dlt_lblrno=Label(dlt,text="Enter Roll no:",font=('arial',15,'bold'),bg="#d1e3ff")
dlt_entrno=Entry(dlt,bd=3,font=('arial',18,'bold'))
dlt_btnsave=Button(dlt,text="Delete",font=('arial',13,'bold'),width=10,command=f10)
dlt_btnback=Button(dlt,text="Back",font=('arial',13,'bold'),width=10,command=f11)
dlt_lblrno.pack(pady=(12,6))
dlt_entrno.pack()
dlt_btnsave.pack(pady=(12,6))
dlt_btnback.pack()
dlt.configure(background="#d1e3ff")
dlt.withdraw()


login.mainloop()