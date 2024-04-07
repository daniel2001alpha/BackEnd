##online shopping cart
class shop:
    def __init__(self):
        count=0
        while True:
            self.userName=input("Enter your userName : ")
            self.Password=input("Enter you Password :")
            if self.userName=="daniel@777" and self.Password=="1234":
                print("Login Successfully")
                break
            else:
                count+=1
                if count==3:
                    print("try again later")
                    break
                else:
                    print("you have ",3-count," choices")
class Mobile:
    def __init__(self):
        self.mobile_cart=[]
        self.available_brands=["Nokia","Samsung","apple","Realme","Motorola"]
        print("Available Brands:")
        i=1
        for item in self.available_brands:
            print("",i,item)
            i+=1
    def add_items(self):
        j=1
        i=int(input("How many brand do you want to select :"))
        while j<=i:
            self.add=input("Enter the Brand :")
            if self.add in self.available_brands:
                for item in range(1,self.qty+1):
                    self.mobile_cart.append(self.add)
                    j+=1
            else:
                print("Item not found")
            try:
                self.qty=int(input("Enter the quantity :"))
            except:
                print("try again")
        print(self.mobile_cart)
    def remove_items(self):
        self.new_item=[]
        brand_count=int(input("How many brand you want to remove :"))
        if brand_count>0:
            for i in range(brand_count):
                self.item=input("Enter the brand want to remove :")
                self.item_count=int(input("Enter count :"))
                for j in range(self.item_count):
                    for items in self.mobile_cart:
                        if self.item in self.mobile_cart:
                            self.mobile_cart.remove(self.item)
                            break
        print(self.mobile_cart)
    def bill(self):
        self.apple=12000
        self.Nokia=14000
        self.Samsung=15000
        self.Motorola=16000
        total=0
        for i in self.mobile_cart:
            if "Nokia" == i:
                total+=self.Nokia
            elif "Apple" == i:
                total+=self.Apple
            elif "Samsung" == i:
                total+=self.Samsung
            else:
                total+=self.Motorola
        print("Total Bill :",total)

o1=shop()
o=Mobile()
o.add_items()
o.remove_items()
o.bill()

""
