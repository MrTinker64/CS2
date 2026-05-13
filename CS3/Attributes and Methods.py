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

class Pet:
    def __init__(self, name,person):       
        self.name = name
        self.person = person
        self.lives = 1

    def eat(self, thing):
        print(self.name+' ate'+thing+'!')

class Dog(Pet):
    def talk(self):
        print('Woof!')


    def eat(self,thing):
        if thing == 'chocolate':
            print(self.name + 'cannot eat' + thing + '!')
        else:
            super(Dog,self).eat(thing)
         
         
class Cat(Pet):
    def __init__(self, name,person):
        super(Cat,self)
        self.lives = 9
        
    def talk(self):
        print('Meow!')
        
    def lose_life(self):
        self.life -= 1
        
    # Implement the revive method for cats so that it resets a cat’s life to 9 only if the cat has no lives left. Otherwise, it prints, “This cat is still alive!” 
    def revive(self):
        if self.lives == 0:
            self.lives = 9
        else:
            print("This cat is still alive!")
            
class HungryCat(Cat):
    def eat(self,thing):
        super(HungryCat,self).eat(thing)
        super(HungryCat,self).eat(thing)
