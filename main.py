# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random # mporting the random package
number_ofnames = len(names) #getting the actual number of items

chosen_name = random.randint(0, number_ofnames-1) #obtaining the item positiion
print(names[chosen_name],"will be the one to take care of the bill!") #printing the result


