"""
Artificial Intelligence to play Hanabi.
"""

import itertools
from random import *

class AI:
    """
    AI base class: some basic functions, game analysis.
    """
    def __init__(self, game):
        self.game = game

    @property
    def other_hands(self):
        "The list of other players' hands."
        return self.game.hands[1:]

    @property
    def other_players_cards(self):
        "All of other players's cards, concatenated in a single list."
        # return sum([x.cards for x in self.other_hands], [])
        return list(itertools.chain.from_iterable([hand.cards for hand in self.other_hands]))


class Cheater(AI):
    """
    This player can see his own cards!

    Algorithm:
      * if 1-or-more card is playable: play the lowest one, then newest one
      * if blue_coin<8 and an unnecessary card present: discard it.
      * if blue_coin>0: give a clue on precious card (so a human can play with a Cheater)
      * if blue_coin<8: discard the largest one, except if it's the last of its kind or in chop position in his opponent.
    """

    def play(self):
        "Return the best cheater action."
        game = self.game
        playable = [ (i+1, card.number) for (i, card) in
                     enumerate(game.current_hand.cards)
                     if game.piles[card.color]+1 == card.number ]

        if playable:
            # sort by ascending number, then newest
            playable.sort(key=lambda p: (p[1], -p[0]))
            print('Cheater would play:', "p%d"%playable[0][0], end=' ')
            if (len(playable) > 1):
                print('but could also pick:', playable[1:])
            else:
                print()

            return "p%d"%playable[0][0]

        #
        discardable = [ i+1 for (i, card) in
                        enumerate(game.current_hand.cards)
                        if ( (card.number <= game.piles[card.color])
                             or (game.current_hand.cards.count(card) > 1)
                        ) ]
        # discard already played cards, doubles in my hand
        # fixme: discard doubles, if I see it in partner's hand
        # fixme: il me manque les cartes sup d'une pile morte

        if discardable and (game.blue_coins < 8):
            print('Cheater would discard:', "d%d"%discardable[0], discardable)
            return "d%d"%discardable[0]

        ## 2nd type of discard: I have a card, and my partner too

        discardable2 = [ i+1 for (i, card) in enumerate(game.current_hand.cards)
                         if card in self.other_players_cards
                       ]
        if discardable2 and (game.blue_coins < 8):
            print('Cheater would discard2:', "d%d"%discardable2[0], discardable2)
            return "d%d"%discardable2[0]


        ## Look at precious cards in other hand, to clue them
        precious = [ card for card in
                     self.other_players_cards
                     if (1+game.discard_pile.cards.count(card))
                         == game.deck.card_count[card.number]
                   ]
        if precious:
            clue = False
            # this loop is such that we prefer to clue an card close to chop
            # would be nice to clue an unclued first, instead of a already clued
            for p in precious:
                # print(p, p.number_clue, p.color_clue)
                if p.number_clue is False:
                    clue = "c%d"%p.number
                    break
                if p.color_clue is False:
                    clue = "c%s"%p.color
                    clue = clue[:2]   # quick fix, with 3+ players, can't clue cRed anymore, only cR
                    break
                # this one was tricky:
                # don't want to give twice the same clue
            if clue:
                print('Cheater would clue a precious:',
                       clue, precious)
                if game.blue_coins > 0:
                    return clue
                print("... but there's no blue coin left!")


        # if reach here, can't play, can't discard safely, no card to clue-save
        # Let's give a random clue, to see if partner can unblock me
        if game.blue_coins > 0:
            print('Cheater would clue randomly: cW')
            return 'cw'

        # If reach here, can't play, can't discard safely
        # No blue-coin left.
        # Must discard a card. Let's choose a non-precious one (preferably a 4)
        mynotprecious = [ (card.number, i+1) for (i, card) in
                          enumerate(game.current_hand.cards)
                          if not (
                                  (1+game.discard_pile.cards.count(card))
                                  == game.deck.card_count[card.number])
                     ]
        mynotprecious.sort(key=lambda p: (-p[0], p[1]))
        if mynotprecious:
            act = 'd%d'%mynotprecious[0][1]
            print('Cheater is trapped and must discard:', act, mynotprecious)
            return act

        # Oh boy, not even a safe discard, this is gonna hurt!
        # it's a loss. Discard the biggest
        myprecious = [ (card.number, i+1) for (i, card) in enumerate(game.current_hand.cards) ]
        myprecious.sort(key=lambda p: (-p[0], p[1]))
        act = 'd%d'%myprecious[0][1]
        print('Cheater is doomed and must discard:', act, myprecious)
        return act




class Stupid_ai(AI):
    """
    let's start with a simple AI

    Algorithm :
        *play a random card
    """

    def play(self):
        game = self.game
        a=randint(0,4)
        return"p%d"%a

"""It seems like it's working"""

class Basic_ai(AI):
    """
    let's do something better

    Algorithm:
        *if we got two clue on a card play it
        *if blue_coin>0 give cW clue
        *if blue_coin<0 discard a card

    """

    def play(self):
        game=self.game


        for k in range(5):
            if game.current_hand.cards[k].color_clue and game.current_hand.cards[k].number_clue :
                return"p%d"%k+1 #retour à des indices rééls !


        if game.blue_coins > 0:
            return"cW"

        if game.blue_coins==0 :
            return"d1"

"""it seems ok too but not really efficient"""

class Smarter_ai(AI):
    """
    let's do something better

    Algorithm:
        *if we got two clue on a card and the card is playable play it
        *if we got two clue on a card and the card is disacrdable : discard it
        *if blue_coin>0 give a new clue
        *else discard a random card

    """
    def play(self):
        game=self.game

        for k in range(5):
            if game.current_hand.cards[k].color_clue and game.current_hand.cards[k].number_clue :
                if game.piles[game.current_hand.cards[k].color]+1 == game.current_hand.cards[k].number :
                    return"p%d"%(k+1) #retour à des indices rééls !
                if game.piles[game.current_hand.cards[k].color] >= game.current_hand.cards[k].number :
                    return"d%d"%(k+1) #idem

        if game.blue_coins > 0 :
            I_see = [ card for card in self.other_players_cards ]
            print(I_see)
            for c in I_see :
                #print(c.color)

                if  not c.color_clue:
                    clue = "c%s"%c.color
                    clue = clue[:2] # quick fix, with 3+ players, can't clue cRed anymore, only cR
                    return clue
                if not c.number_clue:
                    return"c%d"%c.number

        else :
            return"d1"
"""it seems ok too but not really efficient : average score is 2 """

class Strat1_ai(AI)

    """ Algorithm:
    1) If the most recent recommendation was to play a card
    and no card has been playedsince the last hint, play the recommended card.
    2) If the most recent recommendation was to play a card, one card has been
    playedsince the hint was given, and the players have made fewer than two errors, play therecommended card
    3) If the players have a hint token, give a hint.
        cf recommendation algo
    4) If the most recent recommendation was to discard a card, discard the requestedcard.
    5) Discard card c1

    """

    actions=[]  #liste des actions jouées pendant la partie
                #variable de classe mise à jour à chaque utilisation de play
                #on saura ce que les autres ont fait avant
                #liste de chaines de carctères


    def from_clue_to_play(self,I_see,clue):
        '''
        la fonction prend en entréé le jeu (au cas où) les cartes des autres et un indice (chaine de caractère) 
        la fonction renvoie une chaine de caractère renvoyant l'action correspondant à l'indice donné
        ''' 
    





    def play(self):
        game=self.game

        if actions[-1][0] == 'c': #si la dernière action était un indice
            if from_clue_to_play(I_see,actions[-1])[0] == p : 

            


