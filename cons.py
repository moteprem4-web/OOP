class Employee:
    def __init__(self):
        print("started executing attributes and data")
        self.id=123
        self.name="Prem D Mote"
        self.salary=10000
        self.designation="AI Engineer"
        print("attributes/data have been initiated")


#we need to call it manually it is 
    def travel(self,destination):
        print("this travel method was called manually")
        print(f"Employee is now travelling to {destination}")
       

sam=Employee()
print(type(sam))
# sam.travel("Pune")

#what is speciality of __init__ or constructor 
#all the data and attributes and automatucally called when the 
#object is created

#Q) what was the need
#if we developing the meaning of software
#we need to intialize the data and attributes of the object
#then can connect  to the database and fetch the data and attributes of the objec
#ex

#facebook then internet connect and also connected with the database and fetch the data and attributes of the object


