bitcoin_price = input("Would you know the bitcoin price? Yes/No ")
btc_price = 20360

if bitcoin_price == ("yes"):
    print (f"The prise of Bitcoin for today is {btc_price} ")
    amount_of_money = int(input("How much do you have in USD? "))
    amount_of_bitcoin = amount_of_money / btc_price
    print (f"you can get {amount_of_bitcoin} BTS")
    question = input("Want to buy more? yes/no ")
if question == ("yes"):
    amount_of_money = int(input("How much do you have in USD? "))
    amount_of_bitcoin = amount_of_money / btc_price
    print (f"you can get {amount_of_bitcoin} BTS")
else: 
    print ("GoodBye")








