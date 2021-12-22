# Very Simple Card Trick
The old-school game where you choose a card and I guess it.

Run the following command on your terminal:

```bash
python card_trick.py
```

Then you will be shown with the following rows containing various cards

```
Row 1:	3♦	3♥	3♣	4♥	3♠	4♠	10♦
Row 2:	8♠	4♦	6♠	J♠	9♣	J♥	7♠
Row 3:	2♣	5♥	2♥	5♦	K♦	Q♦	8♥
```

You will have to choose a card (in your mind) and stick with it for the entire game. When prompted to enter the row number of the chosen card, just enter 1, 2 or 3. Let us say you select `5♥` , then just type `3`.

```
Choose a card and enter its row number [1,2,3]: 3
```

 The cards will then be shuffled and shown again, you have to remember your card and pick the new row of the card.  

```
Row 1:	3♦	4♥	10♦	2♥	Q♦	4♦	9♣
Row 2:	3♥	3♠	2♣	5♦	8♥	6♠	J♥
Row 3:	3♣	4♠	5♥	K♦	8♠	J♠	7♠
```

Since the chosen card `5♥` is still in row `3`, I will enter that when prompted.

```
Enter the row number of the chosen card [1,2,3]: 3
```

You will be asked this one last time. 

```
Row 1:	3♦	2♥	9♣	5♥	J♠	3♠	8♥
Row 2:	4♥	Q♦	3♣	K♦	7♠	2♣	6♠
Row 3:	10♦	4♦	4♠	8♠	3♥	5♦	J♥

Enter the row number of the chosen card [1,2,3]: 1
```

After this I will  try to guess your card.
