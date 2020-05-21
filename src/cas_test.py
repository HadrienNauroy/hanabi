'''cas tests'''


Red = 31
Blue = 34
Green = 32
White = 37
Yellow = 33


import hanabi
game=hanabi.Game(5)
ai=hanabi.ai.Strat1_ai(game)
a=hanabi.deck.Card(Red,1)
b=hanabi.deck.Card(Red,1)
c=hanabi.deck.Card(Blue,4)
d=hanabi.deck.Card(Yellow,2)
e=hanabi.deck.Card(White,2)
f=hanabi.deck.Card(White,2)
g=hanabi.deck.Card(White,3)

L=[a,b,c,d,e,f,g]
game.discard_pile.cards=L
t1=hanabi.deck.Card(Red,1)
t2=hanabi.deck.Card(Yellow,3)
t3=hanabi.deck.Card(Green,5)
t4=hanabi.deck.Card(Red,5)
t5=hanabi.deck.Card(White,3)
t6=hanabi.deck.Card(White,5)
t7=hanabi.deck.Card(Blue, 5)


"cas test de is_indispensable2"

if ai.is_indispensable2(t1) : print("test 1 OK")
else: print("test 1 not OK ")
if not(ai.is_indispensable2(t2)) : print("test 2 OK")
else: print("test 2 not OK ")
if ai.is_indispensable2(t3) : print("test 3 OK")
else: print("test 3 not OK ")
if ai.is_indispensable2(t4) : print("test 4 OK")
else: print("test 4 not OK ")
if not(ai.is_indispensable2(t5)) : print("test 5 OK")
else: print("test 5 not OK ")
if not(ai.is_indispensable2(t6)) : print("test 6 OK")
else: print("test 6 not OK ")
if not(ai.is_indispensable2(t6)) : print("test 6bis OK")
else: print("test 6bis not OK ")

"cas test de c_i"

game.piles[Green]=2
game.piles[Yellow]=4
game.piles[White] = 1
game.piles[Red]= 4
game.piles[Blue] = 0

card1 = hanabi.deck.Card(Red, 5)
card2 = hanabi.deck.Card(Yellow, 5)
card3 = hanabi.deck.Card(Red, 2)
card4 = hanabi.deck.Card(Blue, 5)
L = [card1, card2, card3, card4]

card6 = hanabi.deck.Card(Red, 4)
card7 = hanabi.deck.Card(Yellow, 4)
card8 = hanabi.deck.Card(Green, 3)
card9 = hanabi.deck.Card(Blue, 1)
L2 = [card6, card7, card8, card9]

card11 = hanabi.deck.Card(Blue, 2)
card12 = hanabi.deck.Card(Yellow, 2)
card13 = hanabi.deck.Card(Red, 2)
card14 = hanabi.deck.Card(Blue, 5)
L3 = [card11, card12, card13, card14]

card15 = hanabi.deck.Card(Blue, 2)
card16 = hanabi.deck.Card(White, 5)
card17 = hanabi.deck.Card(White, 4)
card18 = hanabi.deck.Card(Blue, 5)
L4 = [card15, card16, card17, card18]


if ai.c_i(L) == 0: print("test 7 ok <3 (play le 5 avec l'indice le plus bas)")
else:
     print("test 7 not ok :(")
     print(ai.c_i(L))

if ai.c_i(L2) == 3: print("test 8 ok <3 (play le plus petit nombre de plus petit indice jouable)")
else:
    print("test 8 not ok :(")
    print(ai.c_i(L2))
if ai.c_i(L3) == 5: print("test 9 ok <3 (discard la dead card d'incide le plus faible )")
else:
    print("test 9 not ok :(")
    print(ai.c_i(L3))
if ai.c_i(L4) == 5: print("test 10 ok <3 (discard la carte de plus haut nombre pas indispensable) ")
else:
    print("test 10 not ok :(")
    print(ai.c_i(L4))

print("Test clue ")
print(L)
ai.other_hands[0].cards = L
ai.other_hands[1].cards = L2
ai.other_hands[2].cards = L3
ai.other_hands[3].cards = L4
c = ai.clue()

print(L[1].color)

if c != 'cR2':
    print("Test clue faux, on trouve:")
    print(c)
else:
    print("Test clue réussi")


'''cas test clue to play'''

ai.actions+=['cR2']
ai.from_clue_to_play()
for k in range(4):
	print(ai.other_hands[k].recommendation)

#cas test 1 ok ...


'''cas test situation reel'''

card1 = hanabi.deck.Card(White,3)
card2 = hanabi.deck.Card(Yellow,4)
card3 = hanabi.deck.Card(White,1)
card4 = hanabi.deck.Card(Red,1)

card5 = hanabi.deck.Card(Blue,5)
card6 = hanabi.deck.Card(Red,4)
card7 = hanabi.deck.Card(Red ,2)
card8 = hanabi.deck.Card(White,4)

card9 = hanabi.deck.Card(Yellow,1)
card10 = hanabi.deck.Card(Red,2)
card11 = hanabi.deck.Card(Blue,4)
card12 = hanabi.deck.Card(Red,3)

card13 = hanabi.deck.Card(Red,4)
card14 = hanabi.deck.Card(Blue,1)
card15 = hanabi.deck.Card(Green,4)
card16 = hanabi.deck.Card(Green,1)


clara = [card1, card2, card3, card4]
Dante = [card5, card6, card7, card8]
elric= [card9, card10, card11, card12]
Alice = [card13, card14, card15, card16]

game.piles[Green]=3
game.piles[Yellow]=3
game.piles[White] = 1
game.piles[Red]= 0
game.piles[Blue] = 3

D=[hanabi.deck.Card(Blue,1),hanabi.deck.Card(White,1),hanabi.deck.Card(White,2),hanabi.deck.Card(Yellow,1),hanabi.deck.Card(Yellow,4),hanabi.deck.Card(White,4)]
'''B1 W1 W2 Y1 Y4 W4'''

if ai.c_i(clara) == 3: print("test A ok <3 (play le 5 avec l'indice le plus bas)")
else:
     print("test A not ok :(")
     print(ai.c_i(L))

if ai.c_i(Dante) == 5: print("test B ok <3 (play le plus petit nombre de plus petit indice jouable)")
else:
    print("test B8 not ok :(")
    print(ai.c_i(L2))
if ai.c_i(elric) == 2: print("test C ok <3 (discard la dead card d'incide le plus faible )")
else:
    print("test C not ok :(")
    print(ai.c_i(L3))
if ai.c_i(Alice) == 2 :print("test D ok <3 (discard la carte de plus haut nombre pas indispensable) ")
else:
    print("test Dnot ok :(")
    print(ai.c_i(L4))

card17=hanabi.deck.Card(Green,5)
card18=hanabi.deck.Card(Yellow,5)
card19=hanabi.deck.Card(White,4)
card20=hanabi.deck.Card(White,5)

Benji=[card17,card18,card19,card20]

ai.game.hands[0].cards=Alice
ai.other_hands[0].cards=Benji
ai.other_hands[1].cards=clara
ai.other_hands[2].cards=Dante
ai.other_hands[3].cards=elric
ai.game.hands[0].recomemndation=[]
ai.game.hands[1].recommendation=[]
ai.game.hands[2].recommendation=[]
ai.game.hands[3].recommendation=[]
ai.game.hands[4].recommendation=[]

if ai.clue()=='c51' : print('test E OK')
else : print('test E not OK', ai.clue())


ai.actions=[ai.clue()]+ai.actions
ai.from_clue_to_play()
for k in range(5):
	print(game.hands[k].recommendation)