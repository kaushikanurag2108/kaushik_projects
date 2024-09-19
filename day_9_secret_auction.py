logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)


def bidders():
    name = input("Enter you name?: ")
    bid = int(input("Enter your bid?: $"))
    conti = input("Are there any other bidders? Type 'Yes' or 'No'").lower()
    return name, bid, conti


def max_bidder(bid_dict):
    max = 0
    max_key = ''
    for key in bid_dict:
        if bid_dict[key] > max:
            max_key = key
            max = bid_dict[key]

    print(f"Bid is won by {max_key}. Bid amount placed was {max}")


bid_dict = {}
flag = True
while flag:
    name, bid, conti = bidders()
    print("\n" * 100)
    bid_dict[name] = bid
    if conti == 'no':
        flag = False
        max_bidder(bid_dict)
