print("----------------------------")
print('Welcome to Josue\'s Chatbot')
print("----------------------------")

name = input("What is your name? ")
while True:
  try:
    age = int(input(("What is your age? ")))
    break
  except ValueError:
    print("Please enter a valid age")

print("\nHello " + name + ". Dang " + str(age) + " years old?, back problems already?")
print("How may I help you today?")
print("----------------------------")


def display_menu():#this is the menu
  print('----------------------------')
  print('Please choose a number between 1-4')
  print('1. Placeholder 1')
  print('2. Placeholder 2')
  print('3. Placeholder 3')
  print('4. Exit ')
  print('----------------------------')

def user_selection():#how user selects
  in_use = True
  while True:
    try:
      print('----------------------------')
      number = int(input('Enter A number 1-4: '))
      if 1 <= number <= 4:
        if number == 1:
          print('Placeholder 1')
        elif number == 2:
          print('Placeholder 2')
        elif number == 3:
          print('Placeholder 3')
        elif number == 4:
          while True:
            print('Are You Sure You Want To Exit?')
            exit_program = input('Y or N: ').lower()
            if exit_program == 'y':
              in_use = False
              print("Thank You For using my chatbot\nUntil Next Time!")
              break
            elif exit_program == 'n':
              break
        if not in_use:
          break
      else:
        print('Pleae enter a number between 1-4')
    except ValueError:
      print('Please enter a number between 1-4')
  return in_use
    
display_menu()
user_selection()