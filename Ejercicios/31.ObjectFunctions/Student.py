class Student:
    def __init__(self, name, major, gpa):
        self.name = name     #I KNOW
        self.major = major
        self.gpa = gpa
#Putting Function Inside of Class
    def on_honor_roll(self): #The student win or not
        if self.gpa >= 3.5:#This student is on the honor roll
            return True
        else:
            return False
