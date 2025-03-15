from datetime import datetime

clients = []
room = []
phone_number = []
enter = []
Exit = []
price = []
running = True

combined_data = []

print("### Welcome to the hotel managment system ###")
while running:
    print("1. book a room")
    print("2. update client")
    print("3. update room")
    print("4. update phone number")
    print("5. update exit time")
    print("6. update price")
    print("7. display clients")
    print("8. display all taken rooms")
    print("9. exit")

    choice = int(input("choose an option: "))

    if choice == 1:
        name = input("Enter client's name: ")
        rooms = int(input("Enter the room's number: "))

        while rooms in room:
            rooms = int(input("room already taken, re-enter the room number: "))

        phone = int(input("Enter client's phone number: "))

        x = input("schedule reservation? ").lower()
        if x == "yes":
            entry = input("enter date time: ")
        else:
            entry = datetime.now()
        exit_time = input("enter exit time: ")
        
        pricing = int(input("enter room's price: "))

        clients.append(name)
        room.append(rooms)
        phone_number.append(phone)
        enter.append(entry)
        Exit.append(exit_time)
        price.append(pricing)


        print('booking done successfully enjoy your day :)')

    elif choice == 2:
        if len(clients) != 0:
            for i in range(0, len(clients)):
                print((i+1), ".", clients[i],"(", room[i],")")
            
            user_n = int(input("enter clients you want to edit:  "))

            if 1 <= user_n <= len(clients):
                clients[user_n -1] = input("enter client name: ")
                print(clients)
            else:
                print("error")

        else:
            print("no record found!! ")

    elif choice == 3:
        if len(room) != 0:
            for iE in range(0, len(room)):
                print((iE+1), ".", clients[iE],"(", room[iE],")")
            
            user_nE = int(input("enter room's number you want to edit:  "))

            if 1 <= user_nE <= len(room):
                room[user_nE -1] = input("enter the room: ")
                print(room)
            else:
                print("error")

        else:
            print("no record found!! ")

    elif choice == 4:
        if len(phone_number) != 0:
            for D in range(0, len(phone_number)):
                print((D+1), ".", clients[D],"(", phone_number[D],")")
            
            user_nEC = int(input("enter   phone_number want to edit:  "))

            if 1 <= user_nEC <= len(phone_number):
                phone_number[user_nEC -1] = input("enter the phone number: ")
                print(phone_number)
            else:
                print("error")

        else:
            print("no record found!! ")

    elif choice == 5:
        if len(Exit) != 0:
            for j in range(0, len(Exit)):
                print((j+1), ".", clients[j],"(", room[j],")","(", Exit[j],")")
            
            user_nECt = int(input("enter exit time want to edit:  "))

            if 1 <= user_nECt <= len(Exit):
                Exit[user_nECt -1] = input("enter the exit time: ")
                print(Exit)
            else:
                print("error")

        else:
            print("no record found!! ")

    elif choice == 6:
        if len(price) != 0:
            for j in range(0, len(price)):
                print((j+1), ".", clients[j],"(", room[j],")(", price[j],")(", Exit[j],")")
            
            user_nECtr = int(input("enter price want to edit:  "))

            if 1 <= user_nECtr <= len(price):
                price[user_nECtr -1] = input("enter the price: ")
                print(price)
            else:
                print("error")

        else:
            print("no record found!! ")

    elif choice == 7:
        if len(clients) != 0:
            for z in range(0, len(clients)):
                print((z+1), ".", clients[z],"(",room[z],")(",Exit[z],")(",enter[z],")(",phone_number[z],")(",price[z],")")

    elif choice == 8:
        
        for i in range(len(room)):
            data = (room[i], clients[i], phone_number[i], enter[i], Exit[i], price[i])
            combined_data.append(data)  
        combined_data.sort()
        for data in combined_data:
            r = data[0]  
            c = data[1]  
            p = data[2]  
            e = data[3]  
            ex = data[4] 
            pr = data[5]

            print("Room: ", r, "Client: ",c," Phone Number: ",p,"Enter: ",e,"Exit:", ex," Price: ",pr)

    elif choice == 9:
        print("bye bye")
        running = False
    else:
        print("invalid option... please try again")
