types_of_people = 10
# create variable x and set it to a string with types of variable people inserted into string
x = f"There are {types_of_people} typles of people"

#create a variable called binary and set it to the string "binary"
binary = "binary"

#create a variable do_not and set it to the string "don't"
do_not = "don't"

#create a variable y and set it to the a string with the variable "binary" inserted into the string
y = f"Those who know {binary} and those who do not"

#print variable x, which is a string with types of people inserted into that string
print(x)

#print variable why which is a string with binary inserted into the string
print(y)

#print variable x which is more strings with the variable x inserted into the string
print(f" I said : {x}")

#print variable y which is more strings with the variable y inserted into it
print(f"I also said '{y}'")

#create a variable called hilarious and set it to the boolean false
hilarious = True

#create a variable called joke_evaluation and set it to isn't that joke funny
joke_evaluation = "Isn't that joke so funny?! {}"

#print joke evaluation variable and pass in the variable boolean, which is set to false
print(joke_evaluation.format(hilarious))

#create a variable called w and set it to string
w = "This is the left side of ..."

#create a variable e and set it to a string
e = "a string with a right side"

#This is string concatenation 
print(w +e)