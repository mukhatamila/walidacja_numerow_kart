def luhn_formula(card):
    # Drop the last digit
    last_digit = card[-1:]
    card = card[:-1]
    print(last_digit)
    print(card)

    # Reverse the digits
    card = card[::-1]
    print(card)
    list_card = [int(x) for x in card]

    # Multiple odd digits by 2
    multiple_odd_card = []
    for i in range(len(list_card)):
        digit = int(list_card[i])
        if digit % 2 == 0:
            digit *= 2
        multiple_odd_card.append(digit)
    print(multiple_odd_card)
    list_card = multiple_odd_card
    print(list_card)

    # Subtract 9 to numbers over 9
    subtract_nine_card = []
    for num in list_card:
        if num > 9:
            num -= 9
        subtract_nine_card.append(num)
    print(subtract_nine_card)
    list_card = subtract_nine_card

    # Add all numbers
    add_all_card = 0
    for num in list_card:
        add_all_card += num
    
    # Mod 10
    if add_all_card % 10 == last_digit:
        return True
    else:
        return False

luhn_formula("4556737586899855")