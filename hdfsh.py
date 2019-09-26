x = 0
count = 0
user = ""
# allows the code to run until the user inputs exit
while user != "EXIT":
    user_input = input("enter number ").upper()
    if user_input.isnumeric():
        count += 1
        x += float(user_input)
    else:
        break
# prints out the average after the user has entered exit
print("Your average is " + str(x / count))




