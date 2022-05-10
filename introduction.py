""""
phrase= "idris"
print(len(phrase))
print(phrase.upper)L
print(phrase.upper().isupper())
                                                 #VARIABLE AND DATA TYPES AND STRINGS
print(len(phrase))
print(phrase[1])
print(phrase.index("i"))
print(phrase.replace("id", "ID"))
"""
#----------------------------------------------------------------------------------------------------------------------
"""
    
#REMAINDER
#print(10%3)                

my_num = 5

#TOSTRİNG
print(str(my_num) + ": My favorite number")

#(abs)ABSOLUTE VALUE
number = -5
print(abs(number))          


#POWER OF NUMBER
print(pow(2,3)) 
             
                                                      #WORKING WITH NUMBER
                                 
#WHICH İS MAX
print(max(25,43))     

#IN ORDER TO RUN MATH PROBLEM
from math import *

#NUMBER DOWN
print(floor(3.7))

#NUMBER UP
print(ceil(3.7))


#SQUARE ROOT
print(sqrt(25))
"""
#----------------------------------------------------------------------------------------------------------------------


""""
ID = input("Enter your ID: ")

age= input("Sumbit your age: ")                            #GETTING INPUT FROM USER

print("welcome " + ID + " you are" +  age)
"""

#----------------------------------------------------------------------------------------------------------------------




"""
num1=5
num2=3
result=num1*num2
print(result)

num1=input("First number:")                            #BASIC CALCULATOR
num2=input("Second number:")

result=int(num1)*int(num2)
print(result)
"""

#----------------------------------------------------------------------------------------------------------------------



"""
color = input("Enter a color: ")
plural_noun = input("Enter plural noun: ")
celebrity = input("Enter celebrity name: ")
                                                    #MAD LIBS GAME
print("Roses are "+ color)
print(plural_noun + " are blue")
print("I love "+ celebrity)
"""
#----------------------------------------------------------------------------------------------------------------------


"""
numbers = [1,2,3,4]
friends = ["AVRİN", "Huseyn", "Huseyn" ,"Ahmet"]


#MERGE 2 LIST
friends.extend(numbers)
print(friends)

#ADDING ELEMENT END OF THE LIST
friends.append("Ramin")
print(friends)

#ADDING ELEMENT TO MIDDLE OF THE LIST
friends.insert(1, "Nahid")
print(friends)

#REMOVE THE ELEMENT FRROM THE LIST
friends.remove("Nahid")
print(friends)                                                  #LISTS
                                                                                                          
#INDEX OF ELEMENT
print(friends.index("AVRİN"))

#COUNTING ELEMENTS IN LIST
print(friends.count("Huseyn"))

#SORTING LIST
dosiler = ["s","d","f"]
dosiler.sort()
print(dosiler)

#REVERSE
numbers.reverse()
print(numbers)

#COPY LIST
dosiler= friends.copy()
print(dosiler)
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
def say_hi(name):
    print("welcome "+ name)
say_hi("idris")

                                             #FUNCITON
                                             
def cube(num):
   return num*num*num
print(cube(4))
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
#IF AND ELSE STATEMENTS
is_male = True
is_tall = True

if is_male:
    print("You are a Male")
else:
    print("You are a Female")

#İF_OR
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a Male or tall or both")
else:                                                                    #IF, ELSE, ELIF
    print("You are Neither")


#İF_AND
is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall Male")
else:
    print("You are either male or not tall or both")

#IF_NOT
is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a tall Male")

elif is_male and not(is_tall):
    print("You are a short male")

elif not(is_male) and is_tall:
    print("You are not a  malevbut yoo are tall")

else:
    print("You are either male or not tall or both")
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
def max_num(num1,num2,num3):

    if num1>=num2 and num1>=num3:
        return num1    
    elif num2>=num1 and num2>=num3:                    #IF STATEMENTS AND COMPARISONS
        return num2                                  
    else:
        return num3

print (max(3,4,6))
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
num1= float(input("Enter first number: "))
op = input("Enter operator: ")
num2= float(input("Enter first number: "))
if op== "+":
    print(num1+num2)

elif op== "-":
    print(num1-num2)

elif op=="*":                                         #CALCULATOR
    print(num1*num2)
    
elif op=="/":
    print(num1/num2)

else:
    print("invalid operator")      
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar                             #SMALLEST
    else:
        print("Loop:", itervar, smallest)
print("Smallest:", smallest)
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
monthConversion ={
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",                                      #DICTIONARIES
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
print(monthConversion["Apr"])
print(monthConversion.get("Jul"))
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
i = 0
while i<=15:
    i+=1                                               # WHILE
    print(i)
    print("DOne with loop")
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
a = ["banana", "apple", "orange"]
for fruits in a:
    #print(fruits)

b = [1,2,3,4,5,6,7,8,9,10,11]
total = 0
for numbers in b :
    #total = total+ numbers
    #print(total)


c = (list(range(1,10)))
print(c)
total = 0
for list in range(1,10):
    #total = total+ list
    #print(total)

b = list(range(1,10))
total = 0
for a in range(1,10):
    if a %2==0:
        total = total+a
        print(total)

"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------



"""
secret_word = "idris"
guess=""
guess_count = 0
guess_limit = 3
out_of_guesses=False

while guess != secret_word and not(out_of_guesses):
    if guess_count<guess_limit:
        guess=input("Enter guess: ")
        guess_count+=1
    else:
        out_of_guesses=True                                   #GUESSING GAME
if out_of_guesses:
    print ("YOU LOST")
else:
    print("You win")
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

"""
for my_name in ("İdris"):
    print(my_name)

friends=["Huseyn","Avrin","Ahmet"]
for friend in friends:
    print(friend)
"""
  
#--------------------------------------------------------------------------------------------------------------------------------------------------------------


"""
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
        return translation
print(translate(input("Enter a phrase to translate: ")))            
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
try:
    number = int(input("Number: "))
    value= 10/0
    print(value)
except ValueError:                                             #TRY & EXCEPT
    print("Invalid Number")
except ZeroDivisionError:
    print("Zero Division Error")
"""
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
programmer= open("Untitled1.exe","r")
print(programmer.readline())
programmer.close()
"""

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
class Student:

    def __init__(self, name, major, gpa,is_on_probation):
        self.name=name
        self.major=major
        self.gpa=gpa
        self.is_on_probation=is_on_probation
"""
import openai

openai.Completion.create(
  engine="davinci",
  prompt="Make a list of astronomical observatories:"
)