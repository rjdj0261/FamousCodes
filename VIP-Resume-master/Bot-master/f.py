import time 
Name = input(" Enter your Name :")
#Why Have You Written This Print function???
print(" ..bot...")
Bot = (f"\n  Helo {Name} i am your BOT \n Nice to meet you")
print (Bot)
print (" \n What i can do for u Sir \nPlease selcet Choice Below")
print ("1. \n for Food")
print ("2.\n  for Journey ")
print ("3.\n for Favorites Flower ")
print ("4.\n  for favourite Colour ")
print(" 5. \n for Favourite Mobile Game")
print(" 6. \n For Sport Game ")
#It Should Be Hello(SPELLING MISTAKE)!!!
choice = input (" Helo Sir! Please select your choice ")
i = True
while True:
    if choice == '1':
        #Why is it restaurants???
          print( " \n welcome to our restraunts ")
          #food menu is of no need!!!
          print ("\n select your food menu sir ")
          #which type food of food???
          print (" \n which type food of food want sir \n There are two Type of Food available Sir ")
          #it should be a dict so the if statements would be shorter!!!
          print("1. for Vegeterian \n 2. Non - Vegetarian")
          #How will the person know that they have to write 1 or 2???
          choose = input (" Select your choice :")
          if choose == '1':
              print(" \n Here is your Vegeterian list")
              print (" 1.Masala Channa ,Paneer,\n 2. Makhani Biryani, Aamras Ki KadhiDahi, Kebab \n 3.Mushroom , Kofta \n 4.Tomato GravyStuffed ,BabyEggplant \n 5.Vegetarian Khao, SueyStuffed ,Masala Mushrooms ")
              select = input(" please select food Sir ;")
              if select == '1':
                  print(" \nYour Selcted Food is \n Masala , Chana , Paneer ")
              elif select == '2':
                  print(" \n Your Selcted Food is \nMakhani Biryani, Maras ki Kadhidahi, Kabab")
              elif select =='3':
                  print(" \n Your Selcted Food is \n Mushroom , Kofta  ")
              elif select == '4':
                  print(" \n Your Selcted Food is \nTomato GravyStuffed , BabyEggplant")
              elif select == '4':
                  print(" \n Your Selcted Food is \n Vegetarian Khao, SueyStuffed ,Masala Mushroom")
          if choose == '2':
              print(" \n Here is your Non - Vegetarian List \n choose from below Sir")
              print (" 1.Grilled Chicken Escalope with Fresh Salsa And Motton Korma \n 2.Pina Colada ribs And Tanduri Lambs Chop \n 3. Malabar Fish Biryani And Keema Samosa with Young heart dip \n 4. Curried Parmesan Fish Fingers And Chicken 65 \n 5. Goan Prawn Curry With Raw Mango And Nihari goshst \n 6. Butter Chicken ")
              select = input(" Select food item sir: ")
              if select =='1':
                  print(" \n Your selected Food is \n Grilled Chicken Escalope with Fresh Salsa And Motton Korma"  )
              elif select =='2':
                  print(" \n your selected Food is \n Pina Colada ribs And Tanduri Lambs Chop")
              elif select == '3':
                  print(" \n your selected Food is \n Malabar Fish Biryani And Keema Samosa with Young heart dip ")
              elif select =='4':
                  print(" \n your selected Food is \n Curried Parmesan Fish Fingers And Chicken 65 ")
              elif select == '5':
                  print(" \n your selected Food is \n Goan Prawn Curry With Raw Mango And Nihari goshst")
              elif select == '6':
                  print ("\n your selected Food is \n Butter Chicken")
    if choice == '2':
          print(" \n Welcome To  Journey ")
          print(" \n Where You want to go ")
          Balance = 5000.90
          #it is not compulsary that the person only wants to go a country it should be destination!!!
          Country = input (" Please Enter Journey country :")
          print(" \n Your Selected journey  Country is ", Country)
          #without writing how many tickets how can u write buying ticket???
          print(" \n ... Buying Ticket ....")
          print(" \n How many Tickets You want Sir :")
          Tickets = int(input(" \n Enter Tickets :"))
          print(" .\n . Ok ..")
          print(" \n Ticket price is 4500.89")
          print(" \n Are you want to buy ticket .. \n 1. Yes \n 2. No")
          select = input(" \n Confirm or Cancel ticket")
          if select == '1':
              print(" \n Ticket confirmation is Succes \n Please Pay money ")
              print (" \n Please Select payment Method ")
              print(" 1. Debit Card \n 2. Credit Card \n 3. Bank account")
              choose = input(" Select payment Type :")
              if choose == '1':
                  Name_on_card = input(" Enter Name as on  Debit card :")
                  #it should be debit card/credit card no. 
                  Debit_card_Number = int(input(" Enter 16 Digit Debit card number :"))
                  Expiry_date = input (" Enter expiry date :")
                  Cvv = int(input(" Enter 3 digit Cvv Number :"))
                  
                  print(" \n .... Verifying Card detail...")
                  print(" \n .. please wait for 4 sec ..")
                  time.sleep(3.5)
                  print( " \n Transaction succes")
                  ticket_price = 4500.89
                  print(" \n Transaction Succes Of 4500.89  ","\n  Remaing balance is " ,ticket_price - Balance )
                  print(" \n Happy Journey ")
              elif choose == '2':
                  #double n??
                  Name_on_card = input(" \nnEnter Name as on  credit card :")
                  credit_card_Number = int(input(" Enter 16 Digit credit card number :"))
                  Expiry_date = input (" Enter expiry date :")
                  Cvv = int(input(" Enter 3 digit Cvv Number :"))
                  print(" \n .... Verifying Card detail...")
                  print("\n  .. please wait for 4 sec ..")
                  time.sleep(3.5)
                  print( " \n Transaction succes")
                  ticket_price = 4500.89
                  print(" \n Transaction Succes Of 4500.89  ","\n  Remaing balance is " ,ticket_price - Balance )
                  print(" \n Happy Journey ")
              elif choose == '3':
                  #name and name on bank acc are compulsarily same -_-
                  Name = input("\n  Enter Name as on Bank ac:")
                  bank_account = int(input("\ Enter 11-Digit Bank account Number: "))
                  ifsc_code = input(" Enter Bank ifsc Code :")
                  print("\n  .... Verifying Card detail...")
                  print(" \n .. please wait for 4 sec ..")
                  time.sleep(3.5)
                  print( " \n Transaction succes")
                  ticket_price = 4500.89
                  print(" \n Transaction Succes Of 4500.89  ","\n  Remaing balance is " ,ticket_price - Balance )
                  print("\n  Happy Journey ")
          elif select == '2':
              print(" Transaction Cancel")
              print(" Thanks for using")
              break
          
    elif choice == '3':
        Flower = input(" \n Enter Your favourite flower name :")
        #it is the user's favourite flower not the bot's -_-
        print(" \n My Favourite Flower is : ",Flower)
    elif choice == '4':
        #it is the user's favourite colour not the bot's -_-
        Colour = input(" Enter Your Favourite Colour :")
        print (" My Favourite Colour is ", Colour)
    elif choice == '5':
        #its written favourite games not top mobile games in the list!!!
        print(" ... Top Mobile games ....")
        Game = { 1 : " Free Fire ", 2 : " Pubg", 3 : " Wcc3",4 : " Call of Duty"}
        get = Game.get(1)
        print(get)
        break
    elif choice == '6':
        #it is the user's favourite sport not the bot's -_-
        Sport = input(" Enter Your Sport game :")
        print(f"My Favourite Sport game is :{Sport}  ")
        break
#thx for watching, is this a bot or movie???
print(" \n Thanks for watching ")
#do bot show this message to users, if no then why u have written this in print???
print("If You want to add more things then u will try it")