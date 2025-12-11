def highest_bidder(bidding_dict):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bidding_dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

#max(bidding_dict, key=bidding_dict.get)

bids = {}
continue_bidding = True
while continue_bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if other_bidders == "no":
        continue_bidding == False
        highest_bidder(bids)
    elif other_bidders == "yes":
        print("\n" * 20)
