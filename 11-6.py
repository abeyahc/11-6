# Abeyah Calpatura
# 11/21/22
# pg 593 #6 Phone Book Program

# displays menu
def menu():
    print(""" 
    -------------------
    1. Add a new record
    2. Search for a name.
    3. Modify a phone number.
    4. Delete a record.
    5. Exit the program.
    -------------------
    """)
    userInput = int(input('Enter your selection: '))
    return userInput

def addRecord():
    print()
    print('Enter the name and number to add.')
    addfile = open('records.txt', 'a')
    username = input('Name: ')
    usernumber = int(input('Number: '))

    # open file
    

    #write name and number to the file
    addfile.write(str(username) + '\n')           
    addfile.write(str(usernumber) + '\n')

    # close file
    addfile.close()
    print('Name and number were added to records.txt.')
    return username

def searchName():
  name = input("Enter the name you wish to search for: ")
  with open('records.txt') as f:
    if name.capitalize() in f.read():
      print('found')
    else:
      print('not found')
    
def modifyNumber():
    original_number = input("Enter the number you wish to replace: ")
    new_number = input("Enter number to replace with: ")

    with open("records.txt", 'r+') as newtxt:
        string = newtxt.read()
        string = string.replace(original_number, new_number)
        newtxt.truncate(0)
        newtxt.seek(0)
        newtxt.write(string)


def deleteRecord():
    delete_value = input("Enter the record you wish to delete: ")
  
    with open("records.txt", "r") as f:
      file = f.readlines()
    with open("records.txt", "w") as f:
        for line in file:
          words = line.strip("\n").lower().split(' ')
          if delete_value.lower() not in words:
            f.write(line)
    
            
# main module
def main():
    userInput = 2
    while not (userInput < 1 or userInput > 5):
        userInput = menu()
        if userInput == 1:
            addRecord()
        elif userInput == 2:
            searchName()
        elif userInput == 3:
            modifyNumber()
        elif userInput == 4:
            deleteRecord()
        elif userInput == 5:
          exit()

        while userInput < 1 or userInput > 5:
          print()
          print('Invalid. Enter a number between 1 - 5. ')

            

main()

