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

"cas test de c_i"

game.piles[Green]=2
game.piles[yellow]=3