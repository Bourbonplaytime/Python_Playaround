SERVICE_CHARGE = 2

TICKET_PRICE = 10

tickets_remaining = 100

def calculate_price(number_of_tickets):
    return number_of_tickets * TICKET_PRICE + SERVICE_CHARGE

while tickets_remaining > 0:
    print("There are {} tickets left.".format(tickets_remaining))

    name = input("What is your name? ")

    num_tickets = input("Greetings {}, how many tickets would you like to buy? ".format(name))

    try:
        num_tickets = int(num_tickets)
        if num_tickets > tickets_remaining:
            raise ValueError("There are only {} tickets remaining".format(tickets_remaining))
    except ValueError as err:
        print("Oh no, we ran into an issue. {}. Please try again.".format(err))
    else:   
        total_cost = calculate_price(num_tickets)

        print("The total cost of your tickets will be ${}".format(total_cost))

        buy_tix = input("Do you want to buy these tickets? press Y if yes. ")

        if(buy_tix.upper() == "Y"):
            print("SOLD!")
            tickets_remaining = tickets_remaining - num_tickets
        else:
            print("Thank you for considering attending the show {}.".format(name))

print("Sorry the tickets are sold out.")