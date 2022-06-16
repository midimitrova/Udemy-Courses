def blackjack(a, b, c):
    result = a + b + c
    if result <= 21:
        return result
    elif result > 21 and (a == 11 or b == 1 or c == 11):
        result -= 10
        if result > 21:
            return "BUST"
        return result
    elif result > 21:
        return "BUST"
print(blackjack(5, 6, 7))
print(blackjack(9, 9, 9))
print(blackjack(9, 9, 11))
print(blackjack(10, 12, 11))





