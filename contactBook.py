print('                 CONTACT BOOK          ')
print("      -----------------------------------    ")

print("--ENTER--")
print("1.ADD CONTACT")
print("2.EDIT CONTACT")
print("3.VIEW CONTACT")
print("4.DELETE CONTACT")
print("5.EXIT")
dict1={}
option=0
while option<=5:
    try:
        option=int(input("choose an option:"))
    except:
        print("Invalid input. Please enter a valid numeric option.")
    if option==1:
        x=input("Enter the name:")
        y=int(input("Enter the number:"))
        dict1[x]=y
        print("contact saved successfully")
    elif option==2:
        print("1.Change Name")
        print("2.Change Number")
        try:
            opt=int(input("choose an option:"))
        except:
             print("Invalid input. Please enter a valid numeric option.")
        if opt==1:
            old_name=input("Enter contact name to be edited: ")
            if old_name in dict1:
                new_name=input("Enter new name:")
                dict1[new_name]=dict1[old_name]
                dict1.pop(old_name)
                print("contact has been updated")
                print(name,dict1[name])
            else:
                print("contact not found")
        elif opt==2:
            name=input("Enter contact name to be edited:")
            if name in dict1:
                new_num=int(input("Enter the new number:"))
                dict1[name]=new_num
                print("contact has been edited succesfully")
                print(name,dict1[name])
            else:
                print("contact not found")
        for i,j in dict1.items():
                print(i,j)
    elif option==3:
        for i,j in dict1.items():
            print(i,j)
    elif option==4:
        name=input("Enter contact name to be deleted:")
        if name in dict1:
            dict1.pop(name)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")   
    elif option==5:
        print("exiting........") 
        break
