var = input("please enter a value:")
char_count=(len(var))


print (var.upper())
print ("no of characters = ",char_count)


result=(any(char.isdigit() for char in var))
if result==True:
    print("contains number")
else:
    print("no number")

