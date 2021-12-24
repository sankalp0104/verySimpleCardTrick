import time
import random


def update_rows(rows, entered_row):
    new_list = []
    new_list.extend(rows[(entered_row + 1) % 3])
    new_list.extend(rows[entered_row])
    new_list.extend(rows[(entered_row + 2) % 3])

    new_rows = []
    new_rows.append(new_list[::3])
    new_rows.append(new_list[1::3])
    new_rows.append(new_list[2::3])

    for i in range(3):
        print(f"Row {i+1}:", *new_rows[i], sep='\t')
    return new_rows, new_list


suits = ['♦', '♥', '♠', '♣']
card_numbers = [str(i) for i in range(2, 11)]
card_numbers.extend(['K', 'Q', 'J', 'A'])
cards = []
for suit in suits:
    for card_number in card_numbers:
        cards.append(card_number + suit)

while 1:
    random.shuffle(cards)
    used_cards = cards[:21]

    rows = [None for _ in range(3)]

    rows[0] = used_cards[:7]
    rows[1] = used_cards[7:14]
    rows[2] = used_cards[14:]

    print()
    for i in range(3):
        print(f"Row {i+1}:", *rows[i], sep='\t')

    m1 = "\nChoose a card and enter its row number [1,2,3]: "
    m2 = "\nEnter the row number of the chosen card [1,2,3]: "

    for i in range(3):
        message = m1 if i == 0 else m2
        entered_row = int(input(message))
        entered_row -= 1
        print()
        rows, new_list = update_rows(rows, entered_row)

    print("\nYour cards is ...")
    time.sleep(2)
    print("Wait for it ...")
    time.sleep(2)
    print("Wait for it ...")
    time.sleep(2)
    print("»  » ", new_list[10], " «  «")

    play_again = input("Do you want to play again? [y/n]: ")
    if play_again not in ['y', 'Y']: break
