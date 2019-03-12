# 3/11/19 Final Project
# Brianna Rice

print('Pick a number between 1 and 30', "\n")
magic_number = 3
guess = int(input('Enter a number:', "\n"))

while guess != magic_number:
    print('Guess again', "\n")
    guess = int(input('Enter a number:', "\n"))
print('Now that you got the number I have another task for you.', "\n")

while True:
    Mystery = int(input("Enter random number"))
    if Mystery > 30:
        print("Nope to big of a number sorry", "\n")
    elif Mystery < 1:
        print("No lager number", "\n")
    else:
        print("Good choice", "\n")
        break





