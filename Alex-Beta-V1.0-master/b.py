i = True
name = input("Hello my name is Alex(Beta Version)! I am your new personal A.I! Please Tell me your name! -> ")
print(f'Nice to meet you {name}!')
while i == True:
            print("How May I Help You?:-\n1.Order Pizzas!\n2.Make a sentence on favourite colour\n3.Call Someone\n4.Book A Cab\n5.Message Someone\n6.Activate Car Service Reminders\n7.Book A Movie Ticket\n8.Add a Reminder\n9.What is today's Date?\n10.Quit")
    a = input("Please Write The Task!!! (1/2/3/4/5/6/7/8/9/10) -> )
    if a == "1":
            print("Please Write The Pizza You Want To Order!!!\nPlease Write Only The Pizza's Name. Don't End It With The Word Pizza!!!"))
            pizza = input()
        print(f"Ordering A {pizza} Pizza!!!")
    if a == '2':
        color = input("Please Write Your Favourite Colour!!!")
        print(f"{name} likes the colour {color}!!!")
    if a == '3':
        call = input(f"Please tell me who you want to call {name}!!!")
        print(f"Calling {call}!!!")
    if a == '4':
        cab = input("Please write what Cab service would you prefer?")
            print("1.Jugnoo | 4.Meru")
            print("2.Ola    | 5.Carzonrent")
            print("3.Uber   | 6.Savvari")
            print ("Please choose the service by writing (1/2/3/4/5/6)")
        if cab == '1':
            print("Booking A Jugnoo Cab For You It Will Reach Home In 5 Mins!!!")
        if cab == '2':
            print("Booking A Ola Cab For You It Will Reach Home In 5 Mins!!!")
        if cab == '3':
            print("Booking A Uber Cab For You It Will Reach Home In 5 Mins!!!")
        if cab == '4':
            print("Booking A Meru Cab For You It Will Reach Home In 5 Mins!!!")
        if cab == '5':
            print("Booking A Carzonrent Cab For You It Will Reach Home In 5 Mins!!!")
        if cab == '6':
            print("Booking A Savaari Cab For You It Will Reach Home In 5 Mins!!!")
    if a == '5':
        reciever = input("Please Write Whom You Want To Send The Message !!! -> ")
        message = input("Please Write Your Message!!! -> ")
        print("Sending Message to ", reciever, "!!!")
    if a == '6':
        print("Car Reminders Activated!!!")
    if a == '7':
        movie = input("Please Write Which Movie You Want To See!!!")
        timing = input("Please Write The Time You Want To Book The Show!!!")
        tickets = input("Please Write How Many Tickets You Want To Buy!!!")
        print("Booked ",  tickets, "for ", movie, "at ", timing, "!!!")
    if a == '8':
        note = input("Please Write Your Note!!! -> ")
        date = input("Please Set The Date Of The Reminder!!! -> ")
        time = input("Please Set Time Of The Reminder!!! -> ")
        print("Reminder Set For Date: {date} And Time: ", time)
    if a == '10'
        print("Thank You For Trying Alex(Beta Version)!!! -Reyaansh Jhaveri")
        i == False
else:
    print("Sorry I Don't Understand That!!! Please Try Again!!!")