'''
I already started before I knew that they all had to go together
so some of it makes sense the rest doesn't
'''
# 3/11/19 Final Project
# Brianna Rice

print('Pick a number between 1 and 30', "\n")
magic_number = 3
guess = int(input('Enter a number:', ))

while guess != magic_number:
    print('Guess again', "\n")
    guess = int(input('Enter a number:'))
print('Now that you got the number I have another task for you.', "\n")

# I'm getting them to guess the numb

while True:
    Mystery = int(input("Enter number: "))
    if Mystery > 100:
        print("Nope to big of a number sorry", "\n")
    elif Mystery < 20:
        print("No lager number", "\n")
    else:
        print("Good choice", "\n")
        break
print('Ok your next task is .... ', "\n")

# I am hoping I can attach this code so it can work with my for loop, functions and so on.

def print_multiple_times(string, times):
   for i in range(times):
       print(string)

print_multiple_times('money', 5)

scan = str('Im hungry')

def print_something():
    scan_van = str('This is confusing')
    print('\r\n',scan_van)

print('\r\n', scan)
print_something()

for i in range(1,3):
   for j in range(7,10):
    print(i,j)


    


