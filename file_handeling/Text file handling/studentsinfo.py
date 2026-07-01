def storestudentsdetails():
    
  i=1
  f=open('studentsdetails.txt','a')
  while True:
      name=input(f"Enter Student {i} name: ")
      age=int(input(f"Enter Student {i} age: "))
      id=int(input(f"Enter Student {i} id: "))
      email=input(f"Enter Student {i} email: ")
      contact=int(input(f"Enter Student {i} contact: "))
      fees=float(input(f"Enter Student {i} fees: "))
      print()

      f.write(f'{id} | {name} | {age} | {email} | {contact} |{fees}\n')
      i=i+1

      option = input("Do you want to add more? [yes/no]: ")
      if option.lower()=='no':
          break
  f.close()

def readstudentdetails():
  f=open('studentsdetails.txt')
  data=f.readlines()
  for line in data:
    print(line, end='')
    f.close()


def search_by_id():
  f=open('studentsdetails.txt')
  data=f.readlines()

  ids=int(input("Enter students id for search: "))
  for line in data:
    id,name,age,email,contact,fees=line.split('|')
  
    if int(id)==ids:
        print(f'Student name: {name}')
        print(f'Student ID: {id}')
        print(f'Student Age: {age}')
        print(f'Student Contact: {contact}')
        print(f'Student Email: {email}')
        print(f'Student Fees: {fees}')

        break
  else:
       print("Student Record not Found")

  f.close()

print("Student Information CRUD Operation")
print("--"*50)
print()

while True:
   print('1. Insert Student details')
   print('2. Display all students details')
   print('3. Search students details by id')
   print('4. Edit students details by id')
   print('5. Delete students details by id')
   print('6. exit')
   print()
   ch= int(input("Enter your choice: "))
   if ch==1:
    storestudentsdetails()
   elif ch==2:
    readstudentdetails()
   elif ch ==3:
    search_by_id()
   elif ch==6:
    print("Thanks for using our application !!")
    exit()
   else:
    print("Invalid choice!! plz enter valid choice")
  
  
   
