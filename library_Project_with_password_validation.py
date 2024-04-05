import mysql.connector
import re
from tabulate import tabulate
con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Daniel2001",
    database="python_db"
    )
res=con.cursor()
class library:
    run=1
    #For Password Validation
    def __init__(self,User_Name,Password):
        sql="select User_Name from userDetails"
        res.execute(sql)
        result=res.fetchall()
        Name=[]
##            nested list into single list
        for i in result:
            if type(list(i)) is list:
                for j in i:
                    Name.append(j)
        if User_Name in Name:
            sql="select Password from userDetails"
            res.execute(sql)
            result=res.fetchall()
            vault=[]
    ##            nested list into single list
            for i in result:
                if type(list(i)) is list:
                    for j in i:
                        vault.append(j)
            if Password in vault:
                print("Log in Successfully")
                self.run+=-1
        else:
            print("User Name isn't Exist")
            request=input("Do you want to create New userName and Password? (yes/no/exit):")
            if request.lower()=="yes":
                User_Name=input("Enter your Name :")
                print("""
                        1.Minimum 8 characters.
                        2.The alphabet must be between [a-z]
                        3.At least one alphabet should be of Upper Case [A-Z]
                        4.At least 1 number or digit between [0-9].
                        5.At least 1 character from [ _ or @ or $ ].
                """)
                Password=input("Enter your Password :")
                flag=0
                """---paddword validation---"""
                while True:
                    if len(Password)<8:
                        flag=-1
                        print("Password minimum contain eight character")
                        break
                    elif not re.search("[a-z]",Password):
                        flag=-1
                        print("Password should contain alphabet")
                        break
                    elif not re.search("[A-Z]",Password):
                        flag=-1
                        print("Password should contain minimun one uppercase alphabet")
                        break
                    elif not re.search("[0-9]",Password):
                        flag=-1
                        print("Password should contain Numbers")
                        break
                    elif not re.search("[_@$]",Password):
                        flag=-1
                        print("password should contain special character _@$ only")
                        break
                    elif re.search("\s",Password):
                        flag=-1
                        print("Password shouldn't contain any space")
                        break
                    else:
                        flag=0
                        break
                if flag==0:
                    print("Valid password")
                else:
                    print("Invalid Password")
                    print("Try Again")
                    User_Name=input("Enter your Name :")
                    password=input("Enter your Password :")
                    library(User_Name,Password)
                sql="insert into userDetails (User_Name,Password) values (%s,%s)"
                user=(User_Name,Password)
                res.execute(sql,user)
                con.commit()
                print("YOur data has been added")
                print("Enter you data again")
                User_Name=input("Enter your Name :")
                Password=input("Enter your Password :")
                library(User_Name,Password)
            elif request.lower()=="no":
                print("Try Again")
                User_Name=input("Enter your Name :")
                Password=input("Enter your Password :")
                library(User_Name,Password)
            else:
                print("Thank you for your visit")
    def manage(self,sql):
        res.execute(sql)
        result=res.fetchall()
        print(tabulate(result,headers=["ID","bookName","authorName","borrowedBook"]))
    def insert_book(self,sql,user):
        res.execute(sql,user)
        con.commit()
        print("Book has been added in our Library")
    def borrow_book(self,sql,ID):
        user=(ID,)
        res.execute(sql,user)
        result=res.fetchone()
        list(result)
        rBook=result[0]
        user=(rBook,ID)
        sql="update books set borrowedBook=%s where ID=%s"
        res.execute(sql,user)
        con.commit()
        print(rBook,"book has been Borrowed")
    def delete_book(self,sql,user):
        res.execute(sql,user)
        con.commit()
    def returned_book(self,sql,user,ID):
        res.execute(sql,user)
        result=res.fetchone()
        list(result)
        book=result[0]
        user=(book,ID)
        sql="update books set bookName=%s where ID=%s"
        res.execute(sql,user)
        con.commit()
        print(book,"book has been returned")
User_Name=input("Enter your Name :")
Password=input("Enter your Password :")
person=library(User_Name,Password)
while True:
    if person.run==0:
        print("welcome")
        break
    else:
        print("no")
        User_Name=input("Enter your Name :")
        Password=input("Enter your Password :")
        person=library(User_Name,Password)
while True:
    print("""
        1.Show Available Books
        2.Insert New Books
        3.Borrow Book
        4.Return Book
        5.Exit
        """)
    ch=int(input("Enter Your choice :"))
    if ch==1:
        sql="select ID,bookName,authorName,borrowedBook from Books"        
        person.manage(sql)
    elif ch==2:
        bookName=input("Enter Book Name :")
        authorName=input("Enter Author Name :")
        sql="insert into Books (bookName,authorName) values (%s,%s)"
        user=(bookName,authorName)
        person.insert_book(sql,user)
    elif ch==3:
        ID=input("Enter ID of that Book : ")
        sql="select bookName from books where ID=%s"
        person.borrow_book(sql,ID)
        bookName="Not Available"
        sql="update books set bookName=%s where ID=%s"
        user=(bookName,ID)
        person.delete_book(sql,user)

    elif ch==4:
        ID=input("Enter ID of that Book : ")
        sql="select borrowedBook from books where ID=%s"
        user=(ID,)
        person.returned_book(sql,user,ID)
        bookName="received"
        sql="update books set borrowedBook=%s where ID=%s"
        user=(bookName,ID)
        person.delete_book(sql,user)
        
    elif ch==5:
        break;
    else:
        print("Invalid Input")
