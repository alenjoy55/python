print("**********football management system**********")
football = []

while True:
    print("""
    1. Add player
    2. Display player Details
    3. Add coach
    4. Display coach Details
    5. coach mangement
    6. Player mangement
    7. Exit
    """)
    
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        pl_id=int(input("Enter player ID : "))
        pl_name = input("Enter a Name: ")
        pl_nation = input("enter player nation: ")
        pl_position = input("Enter position: ")
        pl_salary=int(input("Enter a salary: "))
        football.append({'pl_id':pl_id,'name': pl_name,'nation':pl_nation,'position':pl_position,'salary':pl_salary})
        print("Player added successfully!")
        
    elif choice == 2:
        print('_' * 70)
        print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format('pl_ID', 'Name','nation', 'Position', 'Salary'))
        print('*' * 70)
        for i in football:
                print('{:<10}{:<15}{:<15}{:<15}{:<15}'.format(i['pl_id'], i['name'],i['nation'],i['position'], i['salary']))
    
    elif choice== 3:
        print("ADDING A COACH ENTER THE DETAILES BELOW ")
        ch_id = int(input("Enter coach id: "))
        name = input("Enter a coach name: ")
        salary = int(input("Enter coach salary: "))
        football.append({ 'ch_id': ch_id,'name': name, 'salary': salary})
        print("coach added successfully!")
    
    elif choice== 4:
        print('_' * 30)
        print('{:<10}{:<10}{:<10}'.format('ch_id','name','salary'))
        print('*' * 30)
        for i in football:
            print('{:<10}{:<10}{:<10}'.format(i['ch_id'], i['name'], i['salary']))
   

