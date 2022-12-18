def get_name():
    user_name = input("What's your name?: ").strip().title()
    return user_name


def get_bid():
    user_bid = input("What's your bid?: $").strip()
    user_bid = int(user_bid)
    return user_bid


def clear():
    print('\n' * 100)


bidder_information = {}
max_bid = 0
winner = ''
while True:
    name = get_name()
    bid = get_bid()
    bidder_information[name] = bid
    question = input("Are there any other bidders? Type 'yes' or 'no'.\n").strip().lower()
    if question == 'yes':
        clear()
        continue
    else:
        for name, bid in bidder_information.items():
            if bid > max_bid:
                max_bid = bid
                winner = name
        print(f"The winner is {winner} with a bid of ${max_bid}.")
        break
