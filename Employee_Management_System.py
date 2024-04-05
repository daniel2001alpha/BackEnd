"""
Employee Management System
"""
import mysql.connector
con=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Daniel2001",
        database="emp"
    );
class checkEmployee:
    def __init__(self,employee_id):
        self.employee_id=employee_id
        sql="select employee_id from EmployeeDetails"
        res=con.cursor()
        res.execute(sql)
        result=res.fetchall()
        result_1=[]
        for item in result:
            if type(item)==tuple:
                for element in item:
                   result_1.append(element)
        count=0
        for item in result_1:
            if employee_id==item:
                    count+=1     
        if count==1:
            #Invoking promote class
            print("Your id is been in our Database")
            promoteEmployee()
        else:
            #Invoke AddEmployee  class
            print("id isn't existed you gave")
            addEmployee()
            
class addEmployee(checkEmployee):
    def __init__(self):
        Name=input("Enter Your Name : ")
        Post=input("Enter Your Post you want : ")
        Salary=int(input("Enter Your Salary : "))
        sql="insert into EmployeeDetails (Name,Post,Salary) values (%s,%s,%s)"
        data=(Name,Post,Salary)
        res=con.cursor()
        res.execute(sql,data)
        con.commit()
        """
        Show the Employee New Id
        """
        sql="select employee_id from EmployeeDetails where Name=%s"
        res=con.cursor()
        data=(Name,)
        res.execute(sql,data)
        Id=res.fetchone()
        employee_id=Id[0]
        print("You're Id is ,",Id[0])
        super().__init__(employee_id)
class promoteEmployee:
    def __init__(self):
        employee_id=int(input("Enter your Employee ID : "))
        self.employee_id=employee_id
        sql="select employee_id from EmployeeDetails"
        res=con.cursor()
        res.execute(sql)
        result=res.fetchall()
        result_1=[]
        for item in result:
            if type(item)==tuple:
                for element in item:
                   result_1.append(element)
        for element in result_1:
            if employee_id==element:
                sql="update EmployeeDetails set Salary=Salary+1000 where employee_id=%s"
                data=(employee_id,)
                res=con.cursor()
                res.execute(sql,data)
                con.commit()
                print("you're salary appraisal has been raised by RS.1000")
                DisplayEmployee()
class DisplayEmployee(promoteEmployee):
    """
        Display Particular Employee Detail
    """
    def __init__(self):
        sql="select * from EmployeeDetails where employee_id=%s"
        employee_id=int(input("Enter your Employee ID : "))
        data=(employee_id,)
        res=con.cursor()
        res.execute(sql,data)
        result=res.fetchall()
        print(result)
        print("Employee ID %0.1f : "%(result[0][0]))
        print("Name %s : "%(result[0][1]))
        print("Post %s : "%(result[0][2]))
        print("Salary %0.1f : "%(result[0][3]))
class Employee(checkEmployee):
    def __init__(self,employee_id):
        self.employee_id=employee_id
        super().__init__(employee_id)
employee_id=int(input("Enter your Employee ID : "))
emp1=Employee(employee_id)
