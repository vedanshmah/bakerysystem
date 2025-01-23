# CS PROJECT:BAKERY MANAGEMENT SYSTEM
import mysql.connector

con=mysql.connector.connect(host='localhost',user='root',password='ss',charset='utf8')

cur=con.cursor()

cur.execute("create database if not exists items" )
cur.execute("use items")
cur.execute("create table if not exists cs(sno int,products varchar(20),cost int)")
cur.execute("select*from cs")
res=cur.fetchall()
if res==[]:
   cur.execute("insert into cs values(1,'Cake',50)")
   cur.execute("insert into cs values(2,'Pastry',20)")
   cur.execute("insert into cs values(3,'Milk',60)")
   cur.execute("insert into cs values(4,'Butter',20)")
   cur.execute("insert into cs values(5,'Cheese',30)")
   con.commit()

cur.execute("create table if not exists  vip(sno int,varieties varchar(20))")
cur.execute("select*from vip")
res=cur.fetchall()
if res==[]:
   cur.execute("insert into vip values(1,'Vaniella')")
   cur.execute("insert into vip values(2,'Chocalate')")
   cur.execute("insert into vip values(3,'Strawberry')")
   cur.execute("insert into vip values(4,'Butter_scotch')")
   con.commit()
   
cur.execute("create table if not exists worker(Sno int,Name varchar(20),Salary int)")
cur.execute("select*from worker")
res=cur.fetchall()
if res==[]:
   cur.execute("insert into worker values(1,'Mukesh',12364)")
   cur.execute("insert into worker values(2,'Ram',1234)")
   cur.execute("insert into worker values(3,'Suresh',23459)")
   cur.execute("insert into worker values(4,'Raju',8987)")
   con.commit()



   
from datetime import datetime
print("_________________________________________________________________________")
print("__________________##CLASS 12 th CS PROJECT(083)##__________________")
print("________________________________________________________________________")
print("|..........@@@@@@@@@@ WELCOME @@@@@@@@@@..........|")
print("|............@@@@@@@@@@ TO @@@@@@@@@@............|")
print("|..............BAKERY MANAGEMENT SYSTEM...........|")
print('|Made BY: VEDANSH MAHENDROO,SHAURYA SACHDEVA,SHAUYRYA NARANG|')
print('|Submitted To:MS-SONIKA GUPTA(P.G.T Computer Science)|')
print("|Session :2022-2023|")
print("_________________________________________________________________________")

ch=' '
while ch!='N' or ch!='n':
   print("\n\nPLEASE CHOOSE \n 1 FOR ADMIN \n 2 FOR COSTUMER\n 3 for EXIT\n")

   choice=int(input("Enter your choice:"))
   if choice==3:
           break
   if choice==1:
      admin=input("USERNAME:")
      password=int(input("ENTER PASSWORD:"))
      if password==1234:
         print("**********HELLO SIR, You logged in as Admin successfully**********")
         print('______________________________________________________________________________________________________________________________________________________________________')
         print("Press 1 To See Items in the shop....")
         print("Press 2 To Add Item in the shop....")
         print("Print 3 to update cost of any item.... ")
         print("Press 4 to See varieties of cake in the shop....")
         print("Press 5 to add varieties of cake in the shop....")
         print("Print 6 to see workers....")
         print("Press 7 to Add worker in the shop....")
         
       
         c=int(input('Enter your choice:'))
         if c==1:
            def items():
               print("Items in the shop:")
               sql="select*from cs"
               cur.execute(sql)
               res=cur.fetchall()
               t=(['serial_no','products','cost'])
               for serial_no,products,cost in res:
                  print(serial_no,":",products,":\t",'cost',cost)
            items()
            
         elif c==2:
            
            def add():
               print("Items already in the shop:")
               sql="select*from cs"
               cur.execute(sql)
               res=cur.fetchall()
               t=(['serial_no','products','cost'])
               for serial_no,products,cost in res:
                  print(serial_no,":",products,":\t",'cost',cost)
               
               sno=int(input("Enter sno:"))
               product1=input("Enter product name:")
               cost=int(input("Enter the cost:"))
               d1=(sno,product1,cost)
               s1='insert into cs values (%s,%s,%s)'
               cur.execute(s1,d1)
               con.commit()
               print('................ITEM ADDED SUCCESSFULLY................')
            add()
         
         elif c==3:
            def money():
               print("Items in the shop:")
               sql="select*from cs"
               cur.execute(sql)
               res=cur.fetchall()
               t=(['serial_no','products','cost'])
               for serial_no,products,cost in res:
                  print(serial_no,":",products,":\t",'cost',cost)

               
               sno=input("Enter the sno of product:")
               n_cost=input("Enter the new cost:")
               cur.execute("update cs  set cost="+n_cost+" where sno="+sno+';')
               con.commit()
               print("TABLE AFTER UPDATION:")
               sq="select*from cs"
               cur.execute(sq)
               res=cur.fetchall()
               t=(['sno','products','cost'])
               for sno,products,cost in res:
                  print(sno,":","\t",products,":","\t",'Cost',cost)
            money()

         elif c==4:
            def svariety():
               print("Varieties of cake in the shop:")
               sql="select*from vip"
               cur.execute(sql)
               res=cur.fetchall()
               t=(['sno','varieties'])
               for sno,varieties in res:                
                  print(sno,":",varieties,)
            svariety()
            
         elif c==5:
            def variety():
               

               print("Varieties of cake in the shop:")
               sql="select*from vip"
               cur.execute(sql)
               res=cur.fetchall()
               t=(['sno','varieties'])
               for sno,varieties in res:                
                  print(sno,":",varieties,)
               sno=input("Enter sno:") 
               varieties=input("Enter variety:")
               d2=(sno,varieties)
               s2='insert into vip values (%s,%s)'
               cur.execute(s2,d2)
               con.commit()
             
            variety()

         
         elif c==6:
            def workers():
               print("Workers in the shop:")
               sql="select*from worker"
               cur.execute(sql)
               res=cur.fetchall()
               t=('serial_no','name','salary')
               for serial_no,name,salary in res:
                  print(serial_no,":","\t",name,":","\t",'salary',salary)
            workers()
         elif c==7:
            def ad():
               print("Workers in the shop:")
               sql="select*from worker"
               cur.execute(sql)
               res=cur.fetchall()
               t=('serial_no','name','salary')
               for serial_no,name,salary in res:
                  print(serial_no,":","\t",name,":","\t",'salary',salary)

                  
               sno=int(input("Enter sno:"))
               emp=input("Enter  name:")
               salary=int(input("Enter the salary:"))
               dx=(sno,emp,salary)
               sy='insert into worker values (%s,%s,%s)'
               cur.execute(sy,dx)
               con.commit()
               print('................................................................................................................////////////////////////WORKER ADDED SUCCESSFULLY/////////////////////////.........................................................................................................')
            ad()
         
            
         
         else:
            print("SORRY..You have entered the  Wrong Input, Input From 1 to 8")
         
         
         
      else:
         print("Wrong password")

   elif choice==2:
      name=input("Enter your name:")
      phone=int(input("Enter your phone number:"))
      print('Press 1 to see the MENU ',sep='......')
      print('Press 2 to order an item')
      c=int(input('Enter your choice:'))
      if c==1:
         def items():
            print("Items in the shop:")
            cur.execute("select*from cs")
            res=cur.fetchall()
            t=('serial_no','products','cost')
            for serial_no,products,cost in res:
               print(serial_no,":","\t",products,":","\t",'cost',cost)
         items()
      elif c==2:
         print("What do you want to order?")
         cur.execute("select*from cs")
         res=cur.fetchall()
         t=('serial_no','products','cost')
         for serial_no,products,cost in res:
                 print(serial_no,":","\t",products,":","\t",'cost',cost)

         res=cur.fetchall()
         print(res)
         l=[]
         for i in range(len(res)):
                 l.append(res[i][0])

         d=int(input("Enter your Serial No of the Item to Buy:"))
         if d==1:
            def items():
               print("Which cake do you want?")
               cur.execute("select*from vip")
               srh=cur.fetchall()
               f=('sno','varieties')
               for sno,varieties in srh:
                  print(sno,":","\t",varieties)
               print("Choose which cake do you want?")
               ck=int(input("Enter choice:"))
               if ck==1:
                  print("How much Quantity of  Vaniella cake do you want?")
                  qty=int(input("Enter Qty."))
                  print("You have succesfully ordered your cake!!!\t:")
                  cur.execute("select*from cs where products='cake'"';')
                  for i in cur:
                     c=i[2]
                     con.commit()
                  print("Total amount:",qty*c)
                  print("\n")
                  print("...........................................................................................................................................................................................................................................................................................................................")
                  print("YOUR BILL")
                  print("___________________________________________________________________________________________________________________________________________________________________")
                  print("Costumer's name:",name)
                  print("Contact no.:",phone)
                  print("Cake type:Vaniella")
                  print("No. of cakes:",qty)
                  print("Total amount:",qty*c)
                  print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
                  print("\t\t\tDate:",datetime.now())
               if ck==2:
                  print("How much Quantity of Chocalate cake do you want?")
                  qty=int(input("Enter Qty."))
                  print("You have succesfully ordered your cake!!!\t:")
                  cur.execute("select*from cs where products='cake'"';')
                  for i in cur:
                     L=i[2]
                  print("Total amount",qty*L)
                  print("\n")
                  print("...........................................................................................................................................................................................................................................................................................................................")
                  print("YOUR BILL")
                  print("___________________________________________________________________________________________________________________________________________________________________")
                  print("Costumer's name:",name)
                  print("Contact no.:",phone)
                  print("Cake type:Chocalate")
                  print("No. of cakes:",qty)
                  print("Total amount:",qty*L)
                  print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
                  print("\t\t\tDate:",datetime.now())
               if ck==3:
                  print("How much Quantity of  Strawberry cake do you want?")
                  qty=int(input("Enter Qty."))
                  print("You have succesfully ordered your cake!!!\t:")
                  cur.execute("select*from cs where products='cake'"';')
                  for i in cur:
                     N=i[2]
                  print("Total amount",qty*N)
                  print("\n")
                  print("...........................................................................................................................................................................................................................................................................................................................")
                  print("YOUR BILL")
                  print("___________________________________________________________________________________________________________________________________________________________________")
                  print("Costumer's name:",name)
                  print("Contact no.:",phone)
                  print("Cake type:Strawberry")
                  print("No. of cakes:",qty)
                  print("Total amount:",qty*N)
                  print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
                  print("\t\t\tDate:",datetime.now())
               if ck==4:
                  print("How much Quantity of Butter_scotch cake do you want?")
                  qty=int(input("Enter Qty."))
                  print("You have succesfully ordered your cake!!!\t:")
                  cur.execute("select*from cs where products='cake'"';')
                  for i in cur:
                     M=i[2]
                  print("Total amount",qty*M)
                  print("\n")
                  print("...........................................................................................................................................................................................................................................................................................................................")
                  print("YOUR BILL")
                  print("___________________________________________________________________________________________________________________________________________________________________")
                  print("Costumer's name:",name)
                  print("Contact no.:",phone)
                  print("Cake type:Butter_scotch")
                  print("No. of cakes:",qty)
                  print("Total amount:",qty*M)
                  print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
                  print("\t\t\tjDate:",datetime.now())
            items()
         elif d==2:
            print("How much pastry do you want:")
            past=int(input("enter your choice:"))
            print("You have successfully ordered",past," pastry")
            cur.execute("select*from cs where products='pastry'"';')
            for i in cur:
               c=i[2]
            print("Total amount =",past*c)
            print("\n")
            print(".................................................................................................................................................................................................................................................................................................................................")
            print("YOUR BILL")
            print("___________________________________________________________________________________________________________________________________________________________________")
            print("Costumer's name:",name)
            print("Contact no.:",phone)
            print("No. of pastry:",past)
            print("Total amount:",past*c)
            print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
            print("\t\t\tDate:",datetime.now())
         elif d==3:
            print("How much litres of milk do you want?")
            mlk=int(input("Enter your choice:"))
            print("You have successfully ordered", mlk,"L of milk.")
            cur.execute("select*from cs where products='milk'"';')
            for i in cur:
               c=i[2]
           
            print("Total amount=",mlk*c)
            print("\n")
            print(".................................................................................................................................................................................................................................................................................................................................")
            print("YOUR BILL")
            print("___________________________________________________________________________________________________________________________________________________________________")
            print("Costumer's name:",name)
            print("Contact no.:",phone)
            print("Quantity of milk:",mlk)
            print("Total amount:",mlk*c)
            print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
            print("\t\t\tDate:",datetime.now())
         elif d==4:
            print("How many packets(20gm) of butter do you want?")
            but=int(input("Enter your choice:"))
            print("You have successfully ordered", but,"packets of butter.")
            cur.execute("select*from cs where products='butter'"';')
            for i in cur:
               c=i[2]
            print("Total amount:",but*c)
            print("\n")
            print(".................................................................................................................................................................................................................................................................................................................................")
            print("YOUR BILL")
            print("___________________________________________________________________________________________________________________________________________________________________")
            print("Costumer's name:",name)
            print("Contact no.:",phone)
            print("Quantity of butter:",but)
            print("Total amount:",but*c)
            print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
            print("\t\t\tDate:",datetime.now())
         elif d==5:
            print("How much cheese(in Kg)do you want?")
            chs=int(input("Enter your choice:"))
            print("You have successfully ordered", chs,"Kg of cheese.")
            cur.execute("select*from cs where products='cheese'"';')
            for i in cur:
               c=i[2]
            print("Total amount:",chs*c)
            print("\n")
            print(".................................................................................................................................................................................................................................................................................................................................")
            print("YOUR BILL")
            print("___________________________________________________________________________________________________________________________________________________________________")
            print("Costumer's name:",name)
            print("Contact no.:",phone)
            print("Quantity of cheese:",chs)
            print("Total amount:",chs*c)
            print("@@@@@@@@@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@@@@@@")
            print("\t\t\tDate:",datetime.now())
         elif d in l:
            qty=int(input("Enter Qty."))
            print("You have succesfully ordered your Selected Item!!!\t:")
            cur.execute("select*from cs where sno="+str(d))
            for i in cur:
                    L=i[2]
            print("Total amount",qty*L)
            print("\n")
            print("...........................................................................................................................................................................................................................................................................................................................")
            print("YOUR BILL")
            print("___________________________________________________________________________________________________________________________________________________________________")
            print("Costumer's name:",name)
            print("Contact no.:",phone)
            print("Quantity:",qty)
            print("Total amount:",qty*L)
            print("@@@@@@@@@@@@THANK_YOU FOR ORDERING THE ITEM@@@@@@@@@@@@")
            print("\t\t\tDate:",datetime.now())
         else:
                 print("Wrong Input")
                 
      else:
              print("\t\t\t\t\t\t\t***Wrong Password!!****")
ch=input("DO YOU WANT TO CONTINUE (Y/N)?")
if ch=='n' or ch=="N":
        exit()
