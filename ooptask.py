#employee has name,salary and phone,email id and employee has one opertion which displays salary,email and name of employee

class employee :
    def __init__(e,name,salary,phone,email):
      e.name=name
      e.salary=salary
      e.phone=phone
      e.email=email

    def display(e):
        print("details of employee is:")
        print("Name:",e.name)  
        print("Salary:",e.salary)
        print("Phone:",e.phone)    
        print("Email:",e.email)  

emp1=employee("shruti jadhav",50000,"9863254356","shruu123@gmail.com") 
emp1.display()