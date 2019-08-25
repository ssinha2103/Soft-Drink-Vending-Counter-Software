try:
    print("Hello User, This place is to buy soft-drinks.\n")
    print("Wow, Thanks for selecting us, let's select your choice of drink.\n")
    drink = int(input("Press the respective number assigned to the soft-drink of your choice :-\n"
                      "1 - Cocacola , 2 - Thumsup , 3 - Mazza , 4 - Sprite , 5 - Minute Maid Orange , 6 - Minute Maid Litchi\n"))
    if 0 < drink <= 1:
        print("Wow!!! Great choice .")
        quantity = int(input("Please enter the no. of bottles you want :-\n"))
        price = quantity * 12
        print(f" So the total price of {quantity} Coca-Cola bottles is {price}.")
    elif 1 < drink <= 2:
        print("Wow!!! Great choice .")
        quantity = int(input("Please enter the no. of bottles you want :-\n"))
        price = quantity * 12
        print(f" So the total price of {quantity} Thumsup bottles is {price}.")
    elif 2 < drink <= 3:
        print("Wow!!! Great choice .")
        quantity = int(input("Please enter the no. of bottles you want :-\n"))
        price = quantity * 12
        print(f" So the total price of {quantity} Mazza bottles is {price}.")
    elif 3 < drink <= 4:
        print("Wow!!! Great choice .")
        quantity = int(input("Please enter the no. of bottles you want :-\n"))
        price = quantity * 12
        print(f" So the total price of {quantity} Sprite bottles is {price}.")
    elif 4 < drink <= 5:
        print("Wow!!! Great choice .")
        quantity = int(input("Please enter the no. of bottles you want :-\n"))
        price = quantity * 20
        print(f" So the total price of {quantity} Minute Maid Orange bottles is {price}.")
    elif 5 < drink <= 6:
        print("Wow!!! Great choice .")
        quantity = int(input("Please enter the no. of bottles you want :-\n"))
        price = quantity * 20
        print(f" So the total price of {quantity} Minute Maid Litchi bottles is {price}.")
    else:
        print("Invalid input. Please try again.")

    again = int(input("\nDo you want anything else, if yes please press 1 if no press any other number.\n"))
    if 0 < again <= 1:
        print("Wow great !\n")
        drink = int(input("Press the respective number assigned to the soft-drink of your choice :-\n"
                          "1 - Cocacola , 2 - Thumsup , 3 - Mazza , 4 - Sprite , 5 - Minute Maid Orange , 6 - Minute Maid Litchi\n"))
        if 0 < drink <= 1:
            print("Wow!!! Great choice .")
            quantity = int(input("Please enter the no. of bottles you want :-\n"))
            price2 = quantity * 12
            print(f" So the total price of {quantity} Coca-Cola bottles is {price2}.")
        elif 1 < drink <= 2:
            print("Wow!!! Great choice .")
            quantity = int(input("Please enter the no. of bottles you want :-\n"))
            price2 = quantity * 12
            print(f" So the total price of {quantity} Thumsup bottles is {price2}.")
        elif 2 < drink <= 3:
            print("Wow!!! Great choice .")
            quantity = int(input("Please enter the no. of bottles you want :-\n"))
            price2 = quantity * 12
            print(f" So the total price of {quantity} Mazza bottles is {price2}.")
        elif 3 < drink <= 4:
            print("Wow!!! Great choice .")
            quantity = int(input("Please enter the no. of bottles you want :-\n"))
            price2 = quantity * 12
            print(f" So the total price of {quantity} Sprite bottles is {price2}.")
        elif 4 < drink <= 5:
            print("Wow!!! Great choice .")
            quantity = int(input("Please enter the no. of bottles you want :-\n"))
            price2 = quantity * 20
            print(f" So the total price of {quantity} Minute Maid Orange bottles is {price2}.")
        elif 5 < drink <= 6:
            print("Wow!!! Great choice .")
            quantity = int(input("Please enter the no. of bottles you want :-\n"))
            price2 = quantity * 20
            print(f" So the total price of {quantity} Minute Maid Litchi bottles is {price2}.")
        else:
            print("Invalid input. Please try again.")
    else:
            print ("\nFine. No issues. \n")
            TotalPrice = price
            print (f"So the final price to be paid by you is Rs.({price}) = Rs.{TotalPrice}")
            print ("\n What is your payment method :-\n")
            payment = int (input ("If Cash press 1...\n"
                          "If Card press 2\n"
                          "If UPI press 3\n"))
            if 0 < payment <= 1:
                    cash = int (input ("Cash amount given by Buyer\n"))
                    refund = cash - TotalPrice
                    print (f"Please refund Rs.{refund} to the user\n.")
                    yes = int (input ("Press 1 if refunded or 2 if not :-\n"))
                    if yes <= 1:
                           print ("\nThanks for Shopping with us.")
                    elif yes <= 2:
                        print ("Sorry no change, so you have to pay via any other method,\n")
                        payment = int (input ("If Card press 2\n"
                                                 "If UPI press 3\n"))

                        if 1 < payment <= 2:
                                 UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
                                 print ("Thank you for Shopping..!!!!!!!")
                        elif 2 < payment <= 3:
                                 UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
                                 print ("Thank you for Shopping..!!!!!!!")
                        else:
                                 print ("Payment Unfinished. Regret for the in-convenience caused.")

            elif 1 < payment <= 2:
                UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
                print ("Thank you for Shopping..!!!!!!!")
            elif 2 < payment <= 3:
                UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
                print ("Thank you for Shopping..!!!!!!!")
            else:
                print ("Payment Unfinished. Regret for the in-convenience caused.")
            exit()

    again = int(input("\nDo you want anything else, if yes please press 1 ,if not press any other number. .\n"))
    if 0 < again <= 1:
            print("Wow Awesome !\n")
            drink = int(input("Press the respective number assigned to the soft-drink of your choice :-\n"
                              "1 - Cocacola , 2 - Thumsup , 3 - Mazza , 4 - Sprite , 5 - Minute Maid Orange , 6 - Minute Maid Litchi\n"))
            if 0 < drink <= 1:
                print("Wow!!! Great choice .")
                quantity = int(input("Please enter the no. of bottles you want :-\n"))
                price3 = quantity * 12
                print(f" So the total price of {quantity} Coca-Cola bottles is {price3}.")
            elif 1 < drink <= 2:
                print("Wow!!! Great choice .")
                quantity = int(input("Please enter the no. of bottles you want :-\n"))
                price3 = quantity * 12
                print(f" So the total price of {quantity} Thumsup bottles is {price3}.")
            elif 2 < drink <= 3:
                print("Wow!!! Great choice .")
                quantity = int(input("Please enter the no. of bottles you want :-\n"))
                price3 = quantity * 12
                print(f" So the total price of {quantity} Mazza bottles is {price3}.")
            elif 3 < drink <= 4:
                print("Wow!!! Great choice .")
                quantity = int(input("Please enter the no. of bottles you want :-\n"))
                price3 = quantity * 12
                print(f" So the total price of {quantity} Sprite bottles is {price3}.")
            elif 4 < drink <= 5:
                print("Wow!!! Great choice .")
                quantity = int(input("Please enter the no. of bottles you want :-\n"))
                price3 = quantity * 20
                print(f" So the total price of {quantity} Minute Maid Orange bottles is {price3}.")
            elif 5 < drink <= 6:
                print("Wow!!! Great choice .")
                quantity = int(input("Please enter the no. of bottles you want :-\n"))
                price3 = quantity * 20
                print(f" So the total price of {quantity} Minute Maid Litchi bottles is {price3}.")
            else:
                print("Invalid input. Please try again.")


    else:
                print("\nFine. No issues. \n")
                TotalPrice = price + price2
                print(f"So the final price to be paid by you is Rs.({price} + {price2}) = Rs.{TotalPrice}")
                print("\n What is your payment method :-\n")
                payment = int(input("If Cash press 1...\n"
                        "If Card press 2\n"
                        "If UPI press 3\n"))
                if 0 < payment <= 1:
                    cash = int(input("Cash amount given by Buyer\n"))
                    refund = cash - TotalPrice
                    print(f"Please refund Rs.{refund} to the user\n.")
                    yes = int(input("Press 1 if refunded or 2 if not :-\n"))
                    if yes <= 1:
                        print("\nThanks for Shopping with us.")
                    elif yes <= 2:
                        print("Sorry no change, so you have to pay via any other method,\n")
                        payment = int(input(
                                "If Card press 2\n"
                                "If UPI press 3\n"))

                        if 1 < payment <= 2:
                             UTRno = input("Please enter the UTR / reference no. of the Tranxaction ")
                             print("Thank you for Shopping..!!!!!!!")
                        elif 2 < payment <= 3:
                             UTRno = input("Please enter the UTR / reference no. of the Tranxaction ")
                             print("Thank you for Shopping..!!!!!!!")
                        else:
                             print("Payment Unfinished. Regret for the in-convenience caused.")
                    else:
                             print("Sorry Invalid input.")
                elif 1 < payment <= 2:
                    UTRno = input("Please enter the UTR / reference no. of the Tranxaction ")
                    print("Thank you for Shopping..!!!!!!!")
                elif 2 < payment <= 3:
                    UTRno = input("Please enter the UTR / reference no. of the Tranxaction ")
                    print("Thank you for Shopping..!!!!!!!")
                else:
                    print("Payment Unfinished. Regret for the in-convenience caused.")
                exit()

    print ("\nGood Lets Finalize the bill. \n")
    TotalPrice = price + price2 + price3
    print (f"So the final price to be paid by you is Rs.({price} + {price2} + {price3}) = Rs.{TotalPrice}")
    print ("\n What is your payment method :-\n")
    payment = int (input ("If Cash press 1...\n"
                          "If Card press 2\n"
                          "If UPI press 3\n"))
    if 0 < payment <= 1:
        cash = int (input ("Cash amount given by Buyer\n"))
        refund = cash - TotalPrice
        print (f"Please refund Rs.{refund} to the user\n.")
        yes = int (input ("Press 1 if refunded or 2 if not :-\n"))
        if yes <= 1:
            print ("\nThanks for Shopping with us.")
        elif yes <= 2:
            print ("Sorry no change, so you have to pay via any other method,\n")
            payment = int (input (
                "If Card press 2\n"
                "If UPI press 3\n"))

            if 1 < payment <= 2:
                UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
                print ("Thank you for Shopping..!!!!!!!")
            elif 2 < payment <= 3:
                UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
                print ("Thank you for Shopping..!!!!!!!")
            else:
                print ("Payment Unfinished. Regret for the in-convenience caused.")
        else:
            print ("Sorry Invalid input.")
    elif 1 < payment <= 2:
        UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
        print ("Thank you for Shopping..!!!!!!!")
    elif 2 < payment <= 3:
        UTRno = input ("Please enter the UTR / reference no. of the Tranxaction ")
        print ("Thank you for Shopping..!!!!!!!")
    else:
        print ("Payment Unfinished. Regret for the in-convenience caused.")
    exit()
except(ValueError):
        print("Sorry, Invalid Input !!!!!!!!!!!!!")
exit()        