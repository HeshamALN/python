print("Welcome to the special recruitment program, please answer the following questions:")
print("")

name = input("What's your name? ")
age = int(input("How old are you? "))
experience = int(input("How many years of experience do you have? "))

skills = ["Python", "C++", "Javascript", "Juggling","Running","Eating"] #1

cv = {} #2
cv = {
	"name":name,#3
	"age":age,#4
	"experience":experience,#5
	"skills":[]#6
} 
# cv["skills"] =[] #6


for x in skills:#7
	i = 1 + skills.index(x)
	print(i,x)


add = int(input("Choose a skill from above by entering its number: "))#8
cv["skills"].append(skills[add-1])#8

add = int(input("Choose another skill from above by entering its number: "))#9

cv["skills"].append(skills[add-1])#9


if cv["age"] > 25 and cv["experience"] > 2 and "Python" in cv["skills"]:
		print("You have been accepted! %s" % name.title())
else:
	print("you're not accepted, get out!")


#print(cv)


