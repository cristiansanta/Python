class Phone11:

    def __init__(self, name, major, gpa, is_on_probation):#This is the phone DATA TYPE - I passed in a name,major,etc to file classesAndObjects
        #STUDENT CLASS DEFINED, I can use this class inside of my other file
        self.name = name           #AttributeOfPhoneObject = name that WE passed in
        self.major = major  #Those are getting passed into this init FUNCTION
        self.gpa = gpa
        self.is_on_probation = is_on_probation

        '''
        SELF=It's the actual object
        '''