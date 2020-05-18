"""
Artificial Intelligence to play Hanabi.
"""

import itertools
import random as random

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
            game.log('Cheater would play:', "p%d"%playable[0][0], end=' ')
            if (len(playable) > 1):
                game.log('but could also pick:', playable[1:])
            else:
                game.log()

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
            game.log('Cheater would discard:', "d%d"%discardable[0], discardable)
            return "d%d"%discardable[0]

        ## 2nd type of discard: I have a card, and my partner too

        discardable2 = [ i+1 for (i, card) in enumerate(game.current_hand.cards)
                         if card in self.other_players_cards
                       ]
        if discardable2 and (game.blue_coins < 8):
            game.log('Cheater would discard2:', "d%d"%discardable2[0], discardable2)
            return "d%d"%discardable2[0]


        ## Look at precious cards in other hand, to clue them
        precious = [ card for card in
                     self.other_players_cards
                     if (1+game.discard_pile.cards.count(card))
                         == game.deck.card_count[card.number]
                   ]
        precious = []  # FIXME : temporarily disable this feature, it doesn't work for 3+ players (save clue is given to the wrong player)
        if precious:
            clue = False
            # this loop is such that we prefer to clue a card close to chop
            # would be nice to clue an unclued first, instead of an already clued
            for p in precious:
                # game.log(p, p.number_clue, p.color_clue)
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
                game.log('Cheater would clue a precious:',
                       clue, precious)
                if game.blue_coins > 0:
                    return clue
                game.log("... but there's no blue coin left!")


        # if reach here, can't play, can't discard safely, no card to clue-save
        # Let's give a random clue, to see if partner can unblock me
        if game.blue_coins >0:
            game.log ('Cheater would clue randomly:')
            return 'c'+random.choice('12345RGBWY')

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
            game.log('Cheater is trapped and must discard:', act, mynotprecious)
            return act

        # Oh boy, not even a safe discard, this is gonna hurt!
        # it's a loss. Discard the biggest
        myprecious = [ (card.number, i+1) for (i, card) in enumerate(game.current_hand.cards) ]
        myprecious.sort(key=lambda p: (-p[0], p[1]))
        act = 'd%d'%myprecious[0][1]
        game.log('Cheater is doomed and must discard:', act, myprecious)
        return act




class Stupid_ai(AI):
    """
    let's start with a simple AI

    Algorithm :
        *play a random card
    """

    def play(self):
        game = self.game
        a=random.randint(0,4)
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

class Strat1_ai(AI):
    """"
    Algorithm:
    1) If the most recent recommendation was to play a card
    and no card has been playedsince the last hint, play the recommended card.
    2) If the most recent recommendation was to play a card, one card has been
    playedsince the hint was given, and the players have made fewer than two errors, play therecommended card
    3) If the players have a hint token, give a hint.
        cf recommendation algo
    4) If the most recent recommendation was to discard a card, discard the requestedcard.
    5) Discard card c1 """

    nb_cards= 4
    nb_players=5
    actions=[]  #liste des actions jouées pendant la partie la derniere action vient en premier
                     #variable de classe mise à jour à chaque utilisation de play
                     #on saura ce que les autres ont fait avant
                     #liste de chaines de carctères

    def is_indispensables(self,card):
        '''la fonction determine si une carte est indispensable'''
        if card.number == 5:
            #On ajoute le cas des deux n-1 défaussés pour ajouter de la précision.
            i=0
            for c in self.game.discard_pile.cards :
                if c.color == card.color and c.number == card.number-1 :
                    i+=1
            if i>= 2:
                return False
            else:
                return True
        if card.number == 1 :
            i=0
            for c in self.game.discard_pile.cards :
                if c.color == card.color and c.number == card.number :
                    i+=1
            if i>=2 :
                return True
            else :
                return False
        else  :
            i=0
            j = 0
            for c in self.game.discard_pile.cards :
                if c.color == card.color and c.number == card.number :
                    i+=1
                if c.color == card.color and c.number == card.number-1 :
                    j+=1
            if i>=1:
                if j<=1 :
                    return True
                if j==2 and c.number == 2:
                    return(True)
                else:
                    return(False)
            else :
                return False

    def is_indispensable2(self,card):
        L = [0 for k in range(card.number)] #On construit L la liste du nombre de cartes
        #de numéro inférieur ou égale à la carte testée présentes dans la défausse.
        #Avec k+1 le numéro de la carte
        saturation = [3, 2, 2, 2, 1] #saturation[k] = nombre de carte de numero k+1 en tout
        for c in self.game.discard_pile.cards :
            for k in range(card.number):
                if c.color == card.color and c.number == card.number-k :
                    L[card.number-k-1] += 1
        s = card.number-1

        #premier test: si elle n'est pas la dernière carte existante elle n'est pas indispensable
        if L[s] == saturation[card.number - 1]-1:
            A = True
        else:
            return(False)
        #ensuite on teste un par un les cas de nombre inférieur
        while s>0:
            s-=1
            if L[s] == saturation[s]:
                A = False
        return(A)

    def c_i(self, L ):
       #on joue le 5 playable du plus petit indice en premier
        for k in range(len(L)):
            if L[k].number == 5 and self.game.piles[L[k].color] == 4: #si le 5 est jouable
                return(k)

        #si pas de 5 on met le plus petit numéro playable de plus petit indice
        m,l = 6, len(L)+1
        for k in range(len(L)):
            if (self.game.piles[L[k].color] == L[k].number +1) and (L[k].number <m) :  #si jouable et meilleur
                m = L[k].number
                l = k
        if m!=6 and l != len(L)+1:  #FIXME je comprends pas bien cette double condition !
            return(k)

        #si y'a une dead card (déjà jouée), on a discard celle de plus petit indice
        for k in range(len(L)):
            if L[k].number <= self.game.piles[L[k].color]:
                return(4+k)

        #on discard la carte de plus haut numéro de plus petit indice et non indispensable
        m, l = 0 , len(L)+1 #FIXME : j 'ai rien compris à celui la
        for k in range(len(L)):
            if L[k].number > m and not self.is_indispensables(L[k]):  #si on a une carte plus grand non indispensable
                                                                       #la condition indice plus grand est implicite avec la boucle
                m = L[k].number
                l = k
        if m!= 0 and l!= len(L)+1:
            return(k+4)

        #On discard c1
        return(4)

    def from_clue_to_play(self):
        '''
        la fonction est lancée au moment où le joueur donne l'indice.
        elle doit mettre à jour hand.recommendation pour tous les autres joueurs cad traduire l'indice pour chaque joueur
        FIXME : il faut se mettre a la place de chaque joueurs.
        '''
        c = self.actions[0]
        I_see = self.other_players_cards
        # si c est un clue on peut continuer sinon on ne fait rien
        if c[0] == 'c':
            #On explicite g_1 on repasse d'une chaine de charactères à un chiffre entre 0 et 7
            #Si on a donné un numéro c'est que g_1 est entre 0 et 3
            if c[1] in ['1','2','3','4']:
                g_1 = int(c[2]) -1
            #Si on a donné une lettre alors g_1 est entre 4 et 7
            else:
                g_1 = int(c[2]) +3
            #maintenant qu'on a g_1 on peut faire le tour des joueurs pour leur donner leur indice
            for k in range(self.nb_players -1):
                g_p = 0
                #il faut exclure le joueur k à qui on explicite l'indice car il ne voit pas ses cartes
                #et exclure celui qui a donné l'indice
                #On cherche g_p = g_1 - \sum_{i!=1, i!=p}c_i[8]
                for i in range(1,k):
                    L = I_see[self.nb_cards*i:self.nb_cards*(i+1)-1]
                    g_p += self.c_i(L)
                for i in range(k+1, self.nb_players-1):
                    L = I_see[self.nb_cards*i:self.nb_cards*(i+1)-1]
                    g_p += self.c_i(L)
                c_p = (g_1-g_p)%8
                #maintenant on le transforme en chaine de charactères
                if c_p <= 3:
                    self.other_hands[k].recommendation = ["p%d"%(c_p+1)] + self.other_hands[k].recommendation
                else:
                    self.other_hands[k].recommendation = ["d%d"%(c_p-3)] + self.other_hands[k].recommendation

        #return "p1"

    def clue(self):
        '''la fonction renvoie l'indice à donner sous forme de chaine de carctère'''
        g_1 = 0
        I_see = self.other_players_cards

        #pour chaque joueur
        for k in range(self.nb_players-1):
            L=I_see[self.nb_cards*k : self.nb_cards*(k+1)-1]
            g_1+= self.c_i(L) #on calcul ci
        indice = g_1%8

        if indice<4:
            #On donne comme indice la valeur de la première carte du joueur numero (indice)
            return("c%d%d"%(self.other_players_cards[(indice)*(self.nb_cards)].number, (indice+1)))
        else:
            #On donne la couleur de la première carte du joueur numero (indice-4)
            clue ="c%s%d" %(self.other_players_cards[(indice-4)*(self.nb_cards)].color ,(indice-3))  #C = Donner une couleur celle de la première carte à
            #clue = clue[:2]+clue[-1]  quick fix, with 3+ players, can't clue cRed2 anymore, only cR2
            return(clue)


    def played_since_hint(self):
        if self.actions == [] :
            raise liste_vide(" actions list is empty ")


        i,n=0,0
        while self.actions[i][0] != 'c':
            if self.actions[i][0] == 'p':
                n+=1
            i+=1
        return n


    def play(self):
        game=self.game
        """oui """

        #I_see = self.other_players_cards
        #print("\n self.pile : ", game.piles, "\n")
        #print("I_see : ", I_see , "\n")

        if game.current_hand.recommendation[0][0] == 'p': #si la dernière recommendation est de jouer
            if self.played_since_hint() == 0 : #si personne n'a joué depuis l'indice  1)
                self.actions=[game.current_hand.recommendation[0]] + self.actions  #maj de actions avant le return
                return game.current_hand.recommendation[0]

            if self.played_since_hint() == 1 : #si 1 personne a joué depuis l'indices   2)
                if self.game.red_coins<2:
                    self.actions=[game.current_hand.recommendation[0]] + self.actions  #maj de actions avant le return
                    return game.current_hand.recommendation[0]



        if game.blue_coins > 0 :  # 3)
            c=self.clue()         #give a clue
            self.actions = [c] + self.actions
            self.from_clue_to_play()     #met a jour les hands.recommendation
            return c

        if game.current_hand.recommendation[0][0] == 'd': #si la dernière recommendation est de defausser 4)
            actions = [game.current_hand.recommendation[0]] + actions
            return game.current_hand.recommendation[0]

        self.actions = ["d1"] + self.actions  # 5)
        return "d1"
