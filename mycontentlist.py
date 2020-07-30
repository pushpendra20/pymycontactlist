def ShowAllContacts():
     with open('E:\\project\\Python\\pymycontactlist\\contactlist.txt') as file:
        print(file.read())

def SearchContact():
    name = input("Enter name to search: ")
    with open('E:\\project\\Python\\pymycontactlist\\contactlist.txt') as file:
        lines = file.readlines()
        for line in lines:
            if line.__contains__(name):
                print("Your  contact data is: " + line)
                break

def AddNewContact():
    while True:
        name = input("plz enter name: ")
        contactno = input("enter contact no: ")

        contactline = name + "," + contactno

        with open("contactlist.txt", mode='a+') as f:
            f.write(contactline + "\n")

        confirmation = input("Are you want to add some more contact no(Y/N): ")

        if confirmation == "N" or confirmation == "n":
            break

def Editcontact():
    name = input("Enter name to search: ")
    newlines = ""
    with open('E:\\project\\Python\\pymycontactlist\\contactlist.txt', "r") as file:
        lines = file.readlines()
        for line in lines:
            if line.__contains__(name):
                print("Your  contact data is: " + line)
                newcontactno = input("enter new number: ")
                newlines = newlines + name + "," + newcontactno + "\n"
            else:
                newlines = newlines + line
    with open('E:\\project\\Python\\pymycontactlist\\contactlist.txt', "w") as file:
        file.write(newlines)

def Deletcontactlist():
    name = input("Enter name to search: ")
    newlines = ""
    with open('E:\\project\\Python\\pymycontactlist\\contactlist.txt') as file:
        lines = file.readlines()
        for line in lines:
            if not line.__contains__(name):
                newlines = newlines + line
    with open('E:\\project\\Python\\pymycontactlist\\contactlist.txt', "w") as file:
                file.write(newlines)



yourCondition = input("What you want to do:\n 1: Show all Contacts\n2: Search Contact\n3: Add new contact\n4: Edit new contact\n5: Delete new contact\n==> ")

if yourCondition == "1":
    ShowAllContacts()
if yourCondition == "2":
    SearchContact()
if yourCondition == "3":
    AddNewContact()
if yourCondition == "4":
    Editcontact()
if yourCondition == "5":
    Deletcontactlist()
