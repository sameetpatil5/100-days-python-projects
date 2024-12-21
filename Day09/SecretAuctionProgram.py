import os
from SecterAuctionProgram_art import logo

print(logo)

auction = {}

bidding = True

def highest_bidder(auction_list):
    highest_bid = 0
    highest_bidder = ""
    for bid in auction_list:
        if auction_list[bid] > highest_bid:
            highest_bid = auction_list[bid]
            highest_bidder = bid
            
    os.system("cls")
    print(f"{highest_bidder} won the Auction by the bid of ${highest_bid}")


while bidding:

    os.system("cls")
    print(logo)

    bidder_name = input("What is your name?\n")
    bid_value = int(input("What is your bid?\n$"))
    auction[bidder_name] = bid_value
    more_bidder = input("Are there more Bidders? Answer in 'yes' or 'no'\n")
    if more_bidder == "no":
        bidding = False
        highest_bidder(auction)