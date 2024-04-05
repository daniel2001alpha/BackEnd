#library management system
class Member:
    def __init__(self,Id):
        Id=input("Enter your id :")
        self.member_id=Id
class Library(Member):
    def __init__(self):
        self.__members_id=["daniel2001","michael2002","david2003","nova2020"]
        self.members_id=self.__members_id
    def check_member(self):
        super().__init__(self)
        for person in self.members_id:
            if self.member_id in self.members_id:
                print("Your Member id accepted")
                break
            else:
                print("you're new member here")
                print("Create your ID")
                self.Name=input("Enter your name :")
                self.Year=input("Enter your year of birth :")
                Id=self.Name+self.Year
                self.members_id.append(Id)
                Library.check_member(self)
    def listOfBooks(self,Book):
        self.Book=Book
        print("Available Books")
        for i in self.Book:
            print(i)
    def borrow_book(self):
        self.count=int(input("How many book do you need :"))
        self.borrow_book=[]
        for i in range(self.count):
            a=input("Enter The Book :")
            self.borrow_book.append(a)
            self.Book.remove(a)
        print("Available Book :",self.Book)
        print("Borrowed Book :",self.borrow_book)
    def return_book(self):
        self.return_count=int(input("Enter No of Book return :"))
        for i in range(self.return_count):
            self.return_book=input("Enter return Books :")
            self.Book.append(self.return_book)
            self.borrow_book.remove(self.return_book)
        print("Available Books After Return :")
        print(self.Book)
        print("You have to return ",self.borrow_book," book")
o=Library()
o.check_member()
Book=["c","c++","python",".net","java"]
o.listOfBooks(Book)
o.borrow_book()
o.return_book()
