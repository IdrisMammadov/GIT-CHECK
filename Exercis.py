"""
number = [75,55,155,200,20,10]
for i in number:
    if i > 500:
        break
    elif i>150:
        continue
    elif i % 5==0:
        print(i)
"""

"""
word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
        print(count )
  """
"""
word = "Idris Mammadov"
print(word[0:3])
print(word[6:10])
"""
"""
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
index = 0
for e in b:                                                #LIST
    index += e
    print(index)
"""
""
"""
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b.append(14)
print(b)
                                                         #LIST
print(b.count(1))
"""
"""
name = {"Idris", "Huseyn", "Ahmet", " Avrin"}
name2 = {"Ahmet", "Esma", "Huseyn","Ali"}
print(name.intersection(name2))                             #SETS
print(name.difference(name2))
print(name.union(name2))
"""


"""
a = [1,2,3,4,5,6,7,8,9,10]
print(a[0:5])
""" 

"""
idris = {
    "Name": "Idris",
    "Phone" : {
        "type": "init",
        "number": "054323223"
    }
}
print(idris["Phone"])
"""


"""
def cube (x):
 return x*x*x
a=cube(3)
print(a)
"""


"""
name1= "YK"
height_m1=2
weight_kg1 = 90
          
name2 = "YK's sister"
height_m2 = 1.8
weight_kg2 = 70

name3 = "YK's brother"
height_m3 = 2.5
weight_kg3 = 160


def bmi_calculator(name, height_m, weight_kg):
 bmi= weight_kg /(height_m ** 2)
 print("BMI: ")
 print(bmi)

 if bmi< 25:
    return name + " is not overweight"
 else :
        return name + " is  overweight"

result1 = bmi_calculator(name1, height_m1, weight_kg1)
result2 = bmi_calculator(name2, height_m2, weight_kg2)
result3 = bmi_calculator(name3, height_m3, weight_kg3)

print(result1)
print(result2)
print(result3)
"""


"""
def conver (miles):
    return 1.6 * miles 
a=  conver(3)
print(a)
"""    
"""
class Robot:
    def introduce_self(self):
     print("My name is "+ self.name )

     r1=Robot()
     r1.name = "Idris"
     r1.color = "Red"
     r1.heigt = 1.90
     r1.weight = 90

     r1.introduce_self()
"""      
                                                                        #CLASS
"""
class student:
         def __init__(self, name, surname, age):
             self.name = name
             self.surname = surname
             self.age = age
student1 = student("Idris", "Mammadov", 18)
print(student1.name)
"""
"""
class Person :
    def __init__(self, name):
     self.name = name

     def __repr__(self):
         return f"Person({self.name})"

     def __mul__(self, x):
         self.neme = self.name*x
         if type(x) is not int:
          raise Exception("invaldi")

p = Person("Idris")
p * "idris"
print(p)
"""

"""
def square_number(nums):
 for i in range(nums):
     yield (i*i)

my_nums =square_number (10)
for i in my_nums:
 print(i)
 
 #print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
"""

"""
import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


computer_guess(100)
"""
"""
import random

def play():
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a tie'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!'

    return 'You lost!'

def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
"""
from re import I


i = input('what is your name? ')
print(len(i))