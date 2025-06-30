class A:
    def m1(self):
        print("THIS IS CLASS A")

class B(A):        
    def m2(self):
        print('THIS IS CLASS B')

class C(A):
    def m3(self):
        print('THIS IS CLASS C')     

class D:
    def m4(self):
        print('THIS IS CLASS D')

class E(B,A):      
    def m5(self):
        print('THIS IS CLASS E') 

class F(C,D):     
    def m6(self):
        print('THIS IS CLASS F')       

jay=E()
viru=F()

print("methods accesible by jay")
jay.m1()
jay.m2()
jay.m5()   

print("methods accesible by viru")
viru.m1()
viru.m4()      
viru.m3()
viru.m6()
