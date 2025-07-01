class book:
     def __init__(self,name,p):
         self.name=name
         self.price=p

     def __str__(self): 
        return f"book name is {self.name}"


     def __add__(self,other):
         return self.price + other.price

     def __sub__(self,other):
         return self.price - other.price
     
     def __mul__(self,other):
         return self.price * other.price
     
     def __truediv__(self,other):
         return self.price / other.price
     
     def __floordiv__(self,other):
         return self.price // other.price
     
     def __mod__(self,other):
         return self.price % other.price
     
     def __pow__(self,other):
        return self.price ** other.price  #power
     
     def __eq__(self,other):
         return self.price == other.price
     
     def __ne__(self,other):
         return self.price != other.price
     
     def __lt__(self,other):
         return self.price < other.price
     
     def __gt__(self,other):
         return self.price > other.price
     
     def __le__(self,other):
         return self.price <= other.price
     
     def __ge__(self,other):
         return self.price >= other.price
     
     def __getitem__(self, index):
        return self.p[index]


     def __len__(self):  
        return len(self.items)         

     def __str__(self): 
        return f"book name is {self.name}"         


b1=book("core python",200)
b2=book("adv python",400) 

print("Addition : ",b1+b2)
print("Substraction : ",b1-b2)
print("Multiplication : ",b1*b2)
print("True Division : ",b1/b2)
print("Floor Division : ",b1//b2)
print("Modulo : ",b1%b2)
print("power",b1**b2)
print("is equal?",b1==b2)  
print("is not equal?",b1!=b2)  
print("is less then?",b1<b2) 
print("is greater then?",b1>b2) 
print("is less then or equal?",b1<=b2) 
print("is greater then or equal?",b1>=b2) 

shelf =(["Python", "C++", "Java"])  #for indexing
print(shelf[1])

print(len(shelf))   #length

b=("java")   #string represention
print(b)     

