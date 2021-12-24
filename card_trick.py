import time
import random

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

    entered_row = int(
        input("\nChoose a card and enter its row number [1,2,3]: "))
    print()
    entered_row -= 1

    new_rows = []
    new_rows.extend(rows[(entered_row + 1) % 3])
    new_rows.extend(rows[entered_row])
    new_rows.extend(rows[(entered_row + 2) % 3])

    rows[0] = new_rows[::3]
    rows[1] = new_rows[1::3]
    rows[2] = new_rows[2::3]

    for i in range(3):
        print(f"Row {i+1}:", *rows[i], sep='\t')

    entered_row = int(
        input("\nEnter the row number of the chosen card [1,2,3]: "))
    print()
    entered_row -= 1

    new_rows = []
    new_rows.extend(rows[(entered_row + 1) % 3])
    new_rows.extend(rows[entered_row])
    new_rows.extend(rows[(entered_row + 2) % 3])

    rows[0] = new_rows[::3]
    rows[1] = new_rows[1::3]
    rows[2] = new_rows[2::3]

    for i in range(3):
        print(f"Row {i+1}:", *rows[i], sep='\t')

    entered_row = int(
        input("\nEnter the row number of the chosen card [1,2,3]: "))
    print()
    entered_row -= 1

    new_rows = []
    new_rows.extend(rows[(entered_row + 1) % 3])
    new_rows.extend(rows[entered_row])
    new_rows.extend(rows[(entered_row + 2) % 3])

    print("\nYour cards is ...")
    time.sleep(2)
    print("Wait for it ...")
    time.sleep(2)
    print("Wait for it ...")
    time.sleep(2)
    print("»  » ", new_rows[10], " «  «")

    play_again = input("Do you want to play again? [y/n]: ")
    if play_again not in ['y', 'Y']: break
