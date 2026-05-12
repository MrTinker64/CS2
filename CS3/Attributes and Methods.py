class Student:
    def __init__(self, student_name):       
      self.name = student_name
      self.year = 0
      self.courses = []
      self.pref_name = student_name

    def add_course(self, course):
        self.courses += [course]
        if self not in course.roster:
            course.roster.append(self)
        return(self.courses)
    
    def teachers(self):
        return [course.instructor for course in self.courses]

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print('Cannot drop '+ course)
        return(self.courses)
    
class Course:
    def __init__(self, name, instructor, term):       
      self.name = name
      self.instructor = instructor
      self.term = term
      self.roster = []
      
bob = Student('Bob')
john = Student('John')
john.year = 2029
CS3 = Course('CS3', 'Parisa','Spring')
French_5 = Course('French 5','Arnaud','Spring')
CS2 = Course('CS2', 'Parisa','Winter')

print(CS3.roster)