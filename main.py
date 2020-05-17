import tkinter
from tkinter import *
import os
import pymysql
from tkinter import messagebox

db = pymysql.connect('localhost', 'user1', 'password', 'data')

cursor = db.cursor()


def optionSelected():
    if QueryVar.get() == '**Please select an option**':
        Label(screen3, text="Please select a valid operation!", fg="red").pack()
    if QueryVar.get() == 'Enter a new SUPPLIER-NO with SUPPLIER-ADDRESS and SUPPLIER-NAME.':
        query1()
    elif QueryVar.get() == 'Enter a new ITEM-NO with ITEM-DESCRIPTION.':
        query2()
    elif QueryVar.get() == 'Enter a new PROJECT-NO with PROJECT-DATA.':
        query3()
    elif QueryVar.get() == 'Enter a new CONTRACT-NO with DATE-OF-CONTRACT together with the ITEM-NO,CONTRACT-PRICE, and CONTRACT-AMOUNT for all items in the contract':
        query4()
    elif QueryVar.get() == 'Enter a new order':
        query5()
    elif QueryVar.get() == 'Find the items in an order':
        query6()
    elif QueryVar.get() == 'Find the price of an item in an order.':
        query7()
    elif QueryVar.get() == 'Find the orders in which a particular item appears':
        query8()
    elif QueryVar.get() == 'Find the price for a given item in a contract':
        query9()
    elif QueryVar.get() == 'Find a particular contract together with its supplier':
        query10()
    elif QueryVar.get() == 'Find the quantity of a given item still available under a given contract':
        query11()


def query1():
    global screen4

    global supplier_num
    global supplier_add
    global supplier_name
    supplier_num = IntVar()
    supplier_add = StringVar()
    supplier_name = StringVar()
    screen4 = Toplevel(screen)
    screen4.geometry("700x550")
    screen4.title("Insert Suppliers")
    Label(screen4, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen4, text="Insert Suppliers", font=("Callibri", 18)).pack()
    Label(screen4, text="").pack()
    Label(screen4, text="").pack()
    Label(screen4, text="Supplier Number:").pack()
    Entry(screen4, textvariable=supplier_num).pack()
    Label(screen4, text="Supplier Name:").pack()
    Entry(screen4, textvariable=supplier_name).pack()
    Label(screen4, text="Supplier Address:").pack()
    Entry(screen4, textvariable=supplier_add).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="INSERT", height="2", width="20", bg="grey", command=query1exec).pack()


def query1exec():
    sup_num = int(supplier_num.get())
    sup_add = str(supplier_add.get())
    sup_name = str(supplier_name.get())

    count = cursor.execute(
        "insert into suppliers(supplier_no,supplier_name,supplier_address) values('%d','%s','%s')" % (
        sup_num, sup_name, sup_add))
    Label(screen4, text="inserted successfully " + str(count)).pack()
    db.commit()


def query2():
    global screen5
    global item_no
    global item_desc
    item_desc = StringVar()
    item_no = IntVar()
    screen5 = Toplevel(screen)
    screen5.geometry("700x550")
    screen5.title("Insert Item")
    Label(screen5, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen5, text="Insert Item", font=("Callibri", 18)).pack()
    Label(screen5, text="").pack()
    Label(screen5, text="").pack()
    Label(screen5, text="Item Number:").pack()
    Entry(screen5, textvariable=item_no).pack()
    Label(screen5, text="Item Description").pack()
    Entry(screen5, textvariable=item_desc).pack()
    Label(screen5, text="").pack()
    Button(screen5, text="INSERT", height="2", width="20", bg="grey", command=query2exec).pack()


def query2exec():
    itemN = int(item_no.get())
    itemD = str(item_desc.get())
    count = cursor.execute("INSERT INTO ITEMS(ITEM_NO,ITEM_DESC) VALUES('%d','%s')" % (itemN, itemD))
    Label(screen5, text="inserted successfully " + str(count)).pack()
    db.commit()


def query3():
    global screen6
    global proj_no
    global proj_data
    proj_no = IntVar()
    proj_data = StringVar()
    screen6 = Toplevel(screen)
    screen6.geometry("700x550")
    screen6.title("Projects")
    Label(screen6, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen6, text="Project", font=("Callibri", 18)).pack()
    Label(screen6, text="").pack()
    Label(screen6, text="").pack()
    Label(screen6, text="Project Number:").pack()
    Entry(screen6, textvariable=proj_no).pack()
    Label(screen6, text="Project Data").pack()
    Entry(screen6, textvariable=proj_data).pack()
    Label(screen6, text="").pack()
    Button(screen6, text="INSERT", height="2", width="20", bg="grey", command=query3exec).pack()


def query3exec():
    proj_n = int(proj_no.get())
    proj_d = str(proj_data.get())
    count = cursor.execute("INSERT INTO PROJECTS(PROJECT_NO,PROJECT_DATA)VALUES('%d','%s')" % (proj_n, proj_d))
    Label(screen6, text="inserted successfully" + str(count)).pack()
    db.commit()


def query4():
    global screen7
    global contract_no
    global supplier_no
    global date_of_contract
    global item_number
    global price
    global quantity
    contract_no = IntVar()
    supplier_no = IntVar()
    date_of_contract = StringVar()
    item_number = IntVar()
    price = IntVar()
    quantity = IntVar()
    screen7 = Toplevel(screen)
    screen7.geometry("700x550")
    screen7.title("Contracts")
    Label(screen7, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen7, text="Contracts", font=("Callibri", 18)).pack()
    Label(screen7, text="").pack()
    Label(screen7, text="Contract Number:").pack()
    Entry(screen7, textvariable=contract_no).pack()
    Label(screen7, text="Supplier Number:").place(x=30, y=230)
    Entry(screen7, textvariable=supplier_no).place(x=150, y=230)
    Label(screen7, text="Date of contract:").place(x=30, y=300)
    Entry(screen7, textvariable=date_of_contract).place(x=150, y=300)
    Label(screen7, text="Item Number:").place(x=350, y=230)
    Entry(screen7, textvariable=item_number).place(x=450, y=230)
    Label(screen7, text="Price:").place(x=350, y=300)
    Entry(screen7, textvariable=price).place(x=450, y=300)
    Label(screen7, text="Quantity:").place(x=350, y=370)
    Entry(screen7, textvariable=quantity).place(x=450, y=370)
    Button(screen7, text="Add item", height="1", width="10", bg="grey", command=query4exec).place(x=300, y=420)


def query4exec():
    con_no = int(contract_no.get())
    sup_num = int(supplier_no.get())
    doc = str(date_of_contract.get())
    itemN = int(item_number.get())
    quant = int(quantity.get())
    p = int(price.get())
    cursor.execute("insert into contracts(contract_no,supplier_no,date_of_contract) values('%d','%d','%s')" % (
    con_no, sup_num, doc))
    cursor.execute(
        "INSERT INTO TOSUPPLY(contract_no,item_no,contract_amt,contract_price) values('%d','%d','%d','%d')" % (
        con_no, itemN, quant, p))
    messagebox.showinfo('Success!', 'Successfully Inserted')
    db.commit()


def query5():
    global screen8
    global order_no
    order_no = IntVar()
    global date_reqd
    date_reqd = StringVar()
    global proj_no
    proj_no = IntVar()
    global contract_no
    contract_no = IntVar()
    global item_no
    item_no = IntVar()
    global item_quant
    item_quant = IntVar()
    global date_of_comp
    date_of_comp = StringVar()
    screen8 = Toplevel(screen)
    screen8.geometry("700x550")
    screen8.title("Insert Orders")
    Label(screen8, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen8, text="Order", font=("Callibri", 18)).pack()
    Label(screen8, text="Order Number:").pack()
    Entry(screen8, textvariable=order_no).pack()
    Label(screen8, text="Date required:").place(x=30, y=180)
    Entry(screen8, textvariable=date_reqd).place(x=160, y=180)
    Label(screen8, text="Date of completion:").place(x=30, y=220)
    Entry(screen8, textvariable=date_of_comp).place(x=160, y=220)
    Label(screen8, text="Project Number:").place(x=30, y=260)
    Entry(screen8, textvariable=proj_no).place(x=160, y=260)
    Label(screen8, text="Contract Number:").place(x=30, y=300)
    Entry(screen8, textvariable=contract_no).place(x=160, y=300)
    Label(screen8, text="Item Number:").place(x=380, y=180)
    Entry(screen8, textvariable=item_no).place(x=480, y=180)
    Label(screen8, text="Item Quantity:").place(x=380, y=260)
    Entry(screen8, textvariable=item_quant).place(x=480, y=260)
    Button(screen8, text="INSERT", height="2", width="20", bg="grey", command=query5exec).place(x=300, y=350)


def query5exec():
    global orderN
    orderN = int(order_no.get())
    contractN = int(contract_no.get())
    projN = int(proj_no.get())
    dateReqd = str(date_reqd.get())
    dateCom = str(date_of_comp.get())
    itemN = int(item_no.get())
    quant = int(item_quant.get())
    cursor.execute(
        "INSERT INTO ORDERS(order_no,date_req,date_comp,contract_no,project_no) VALUES('%d','%s','%s','%d','%d')" % (
        orderN, dateReqd, dateCom, contractN, projN))
    cursor.execute(
        "INSERT INTO MADEOF(order_no,item_no,order_quantity) VALUES('%d','%d','%d')" % (orderN, itemN, quant))
    messagebox.showinfo("SUCCESS!", "SUCCESSFULLY INSERTED")
    db.commit()


def query6():
    global screen9
    global order_no
    order_no = IntVar()
    screen9 = Toplevel(screen)
    screen9.geometry("700x550")
    screen9.title("Search Item")
    Label(screen9, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen9, text="Search Item", font=("Callibri", 18)).pack()
    Label(screen9, text="").pack()
    Label(screen9, text="Order Number:").pack()
    Entry(screen9, textvariable=order_no).pack()
    Label(screen9, text="").pack()
    Button(screen9, text="Search", height="2", width="20", bg="grey", command=query6exec).pack()


def query6exec():
    or_no = int(order_no.get())
    cursor.execute(
        "SELECT i.item_no,item_desc from items as i, madeof as m where i.item_no=m.item_no and m.order_no=%d" % (or_no))
    print('executed')
    rows = cursor.fetchall()
    for row in rows:
        Label(screen9, text="Item number").pack()
        Label(screen9, text=row[0]).pack()
        Label(screen9, text="Item description : ").pack()
        Label(screen9, text=row[1]).pack()
        Label(screen9, text=cursor.fetchone()).pack()


def query7():
    global screen10
    global order_no
    order_no = IntVar()
    screen10 = Toplevel(screen)
    screen10.geometry("700x550")
    screen10.title("Search Price of an Item")
    Label(screen10, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen10, text="Search Price of an Item", font=("Callibri", 18)).pack()
    Label(screen10, text="").pack()
    Label(screen10, text="Order Number:").pack()
    Entry(screen10, textvariable=order_no).pack()
    Label(screen10, text="").pack()
    Button(screen10, text="Search", height="2", width="20", bg="grey", command=query7exec).pack()


def query7exec():
    or_no = int(order_no.get())
    cursor.execute(
        "select p.contract_price from tosupply as p, orders as o where p.contract_no=o.contract_no and order_no=%d" % (
            or_no))
    rows = cursor.fetchall()
    for row in rows:
        Label(screen10, text="PRICE : ").pack()
        Label(screen10, text=row[0]).pack()
        Label(screen10, text=cursor.fetchone()).pack()


def query8():
    global screen11
    global item_no
    item_no = IntVar()
    screen11 = Toplevel(screen)
    screen11.geometry("700x550")
    screen11.title("Order Search")
    Label(screen11, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen11, text="Search an order for an item", font=("Callibri", 18)).pack()
    Label(screen11, text="").pack()
    Label(screen11, text="Item Number:").pack()
    Entry(screen11, textvariable=item_no).pack()
    Label(screen11, text="").pack()
    Button(screen11, text="Search", height="2", width="20", bg="grey", command=query8exec).pack()


def query8exec():
    itemN = int(item_no.get())
    cursor.execute(
        "select o.order_no, o.date_req, o.contract_no, o.project_no from orders as o, madeof as m where o.order_no=m.order_no and m.item_no=%d" % (
            itemN))
    rows = cursor.fetchall()
    for row in rows:
        Label(screen11, text="ORDER NUMBER : ").pack()
        Label(screen11, text=row[0]).pack()
        Label(screen11, text="DATE REQUIRED : ").pack()
        Label(screen11, text=row[1]).pack()
        Label(screen11, text="CONTRACT NUMBER : ").pack()
        Label(screen11, text=row[2]).pack()
        Label(screen11, text="PROJECT NUMBER : ").pack()
        Label(screen11, text=row[3]).pack()
        Label(screen11, text=cursor.fetchone()).pack()


def query9():
    global screen12
    global item_no
    item_no = IntVar()
    screen12 = Toplevel(screen)
    screen12.geometry("700x550")
    screen12.title("Search Item Price")
    Label(screen12, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen12, text="Search Item Price in contract", font=("Callibri", 18)).pack()
    Label(screen12, text="").pack()
    Label(screen12, text="Item Number : ").pack()
    Entry(screen12, textvariable=item_no).pack()
    Label(screen12, text="").pack()
    Button(screen12, text="Search", height="2", width="20", bg="grey", command=query9exec).pack()


def query9exec():
    itemN = int(item_no.get())
    cursor.execute(
        "SELECT TS.CONTRACT_PRICE FROM TOSUPPLY AS TS, ITEMS AS I WHERE TS.ITEM_NO = I.ITEM_NO AND I.ITEM_NO=%d" % (
            itemN))
    rows = cursor.fetchall()
    for row in rows:
        Label(screen12, text="CONTRACT PRICE : ").pack()
        Label(screen12, text=row[0]).pack()
        Label(screen12, text=cursor.fetchone()).pack()


def query10():
    global screen13
    global contract_no
    contract_no = IntVar()
    screen13 = Toplevel(screen)
    screen13.geometry("700x550")
    screen13.title("Search Supplier")
    Label(screen13, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen13, text="Search Supplier for a contract", font=("Callibri", 18)).pack()
    Label(screen13, text="").pack()
    Label(screen13, text="Contract Number : ").pack()
    Entry(screen13, textvariable=contract_no).pack()
    Label(screen13, text="").pack()
    Button(screen13, text="Search", height="2", width="20", bg="grey", command=query10exec).pack()


def query10exec():
    con_no = int(contract_no.get())
    cursor.execute(
        "SELECT S.SUPPLIER_NO, S.SUPPLIER_ADDRESS, S.SUPPLIER_NAME FROM SUPPLIERS AS S, CONTRACTS AS C WHERE C.SUPPLIER_NO = S. SUPPLIER_NO AND C.CONTRACT_NO = %d" % (
            con_no))
    rows = cursor.fetchall()
    for row in rows:
        Label(screen13, text="SUPPLIER NUMBER : ").pack()
        Label(screen13, text=row[0]).pack()
        Label(screen13, text="SUPPLIER ADDRESS : ").pack()
        Label(screen13, text=row[1]).pack()
        Label(screen13, text="SUPPLIER NAME : ").pack()
        Label(screen13, text=row[2]).pack()
        Label(screen13, text=cursor.fetchone()).pack()


def query11():
    global screen14
    global item_no
    item_no = IntVar()
    screen14 = Toplevel(screen)
    screen14.geometry("700x550")
    screen14.title("Search Supplier")
    Label(screen14, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen14, text="Search ITEM NUMBER", font=("Callibri", 18)).pack()
    Label(screen14, text="").pack()
    Label(screen14, text="Item Number : ").pack()
    Entry(screen14, textvariable=item_no).pack()
    Label(screen14, text="").pack()
    Button(screen14, text="Search", height="2", width="20", bg="grey", command=query11exec).pack()


def query11exec():
    itemN = int(item_no.get())
    cursor.execute("SELECT CONTRACT_AMT FROM TOSUPPLY WHERE ITEM_NO = %d" % (itemN))
    row1 = cursor.fetchall()
    amount_available = sum(list(map(sum,list(row1))))
    print(amount_available)
    cursor.execute("SELECT ORDER_NO FROM MADEOF WHERE ITEM_NO = %d" % (itemN))
    rows = cursor.fetchall()
    rows = list(rows)
    print(rows)
    for row in rows:
        cursor.execute("SELECT ORDER_QuantitY FROM MADEOF AS MO, TOSUPPLY AS TS WHERE TS.ITEM_NO = MO.ITEM_NO AND MO.ORDER_NO = %d" % row)
        pro = sum(list(map(sum,list(cursor.fetchall()))))
        print(pro)
    amount_available = amount_available - pro
    Label(screen14, text="Amount Available: " + str(amount_available)).pack()


def login_success():
    global screen3
    screen3 = Toplevel(screen)
    screen3.title("WELCOME TO TURNER CONSTRUCTIONS")
    screen3.geometry("700x550")
    Label(screen3, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen3, text="What do you want to do?", font=("Callibri", 18)).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    Label(screen3, text="").pack()
    QueryOption = ['Enter a new SUPPLIER-NO with SUPPLIER-ADDRESS and SUPPLIER-NAME.',
                   'Enter a new ITEM-NO with ITEM-DESCRIPTION.',
                   'Enter a new PROJECT-NO with PROJECT-DATA.',
                   'Enter a new CONTRACT-NO with DATE-OF-CONTRACT together with the ITEM-NO,CONTRACT-PRICE, and CONTRACT-AMOUNT for all items in the contract',
                   'Enter a new order',
                   'Find the items in an order',
                   'Find the price of an item in an order.',
                   'Find the orders in which a particular item appears',
                   'Find the price for a given item in a contract',
                   'Find a particular contract together with its supplier',
                   'Find the quantity of a given item still available under a given contract']
    global QueryVar
    QueryVar = StringVar(screen3)
    QueryVar.set("**Please select an option**")
    OptionMenu(screen3, QueryVar, *QueryOption).pack()
    Button(screen3, text='Execute', command=optionSelected).place(x=310, y=280)


def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info + "\n")
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(screen1, text="Registration Successful", fg="green").pack()


def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_entry1.delete(0, END)
    password_entry1.delete(0, END)
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            Label(screen2, text="Login Successful", fg="green").pack()
            login_success()
        else:
            Label(screen2, text="Password Wrong!", fg="Red").pack()
    else:
        Label(screen2, text="User Not Found!!", fg="Red").pack()


def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title('New User Registration')
    screen1.geometry("700x550")
    Label(screen1, text="TURNER CONSTRUCTION", bg="grey", width="300", height="3", font=("Calibri", 18)).pack()
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(screen1, text="Please enter the details below:").pack()
    Label(screen1, text="").pack()
    Label(screen1, text="Username *").pack()
    username_entry = Entry(screen1, textvariable=username)
    username_entry.pack()
    Label(screen1, text="Password *").pack()
    password_entry = Entry(screen1, textvariable=password)
    password_entry.pack()
    Label(screen1, text="").pack()
    Button(screen1, text="Register", height="3", width="40", command=register_user).pack()


def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("700x550")
    Label(screen2, text="TURNER CONSTRUCTION", bg="gray", width="300", height="3", font=("Calibri", 18)).pack()
    Label(screen2, text="Please enter the details below to login:").pack()
    Label(screen2, text="").pack()
    global username_verify
    global password_verify
    username_verify = StringVar()
    password_verify = StringVar()
    global username_entry1
    global password_entry1
    Label(screen2, text="Username *").pack()
    username_entry1 = Entry(screen2, textvariable=username_verify)
    username_entry1.pack()
    Label(screen2, text="")
    Label(screen2, text="Password *").pack()
    password_entry1 = Entry(screen2, textvariable=password_verify)
    password_entry1.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Login", height="3", width="40", command=login_verify).pack()


def main_screen():
    global screen
    screen = Tk()
    screen.geometry("700x550")
    background_image = PhotoImage(file='C:/Users/darsh/Desktop/img.png')
    screen.title("TURNER CONSTRUCTION")
    Label(image=background_image).place(x=0, y=-200, relwidth=1, relheight=1)
    Button(text="Login", height="3", width="40", command=login).place(x=150, y=150)
    Label(text="").pack()
    Button(text="Register", height="3", width="40", command=register).place(x=150, y=250)
    screen.mainloop()


main_screen()
