class student :

    def __init__(self,nm,r,marks):
        self.name=nm
        self.roll=r
        self.subjectsmarks=marks

    def display_per(self) :
        total_marks=sum(self.subjectsmarks.values())
        total_subject=len(self.subjectsmarks)
        per=(total_marks/(total_subject*100))*100

        print(f"student name={self.name}")
        print(f"student roll number={self.roll}")
        
        for subject, mark in self.subjectsmarks.items():
            print(f"  {subject:<15}  {mark}")
        
        print(f"total marks={total_marks}")
        print(f"percentge={per:.2f} %")
        print("---" * 20)

students=[]
marks1={ "python":87,"java":77,"html":99,"js":56,"cpp":87 }   
students.append(student("shruti jadhav","11",marks1)) 

marks2={ "python":33,"java":54,"html":48,"js":74,"cpp":83 }
students.append(student("swati chothe","12",marks2))

marks3={ "python":88,"java":65,"html":34,"js":65,"cpp":83 }
students.append(student("abhi godse","13",marks3))

for s in students:
    s.display_per()