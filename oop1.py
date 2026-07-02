class Employee:
    def __init__(self):
        self.id=123
        self.name="Prem D Mote"
        self.salary=10000
        self.designation="AI Engineer"

    def travel(self,destination):
        print(f"Employee is now travelling to {destination}")

sam=Employee()
sam.travel("Pune")