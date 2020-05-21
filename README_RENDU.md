# Stratégie retenue

Nous avons fait le choix de nous intéresser au document sur le  [hat guessing](https://d0474d97-a-62cb3a1a-s-sites.googlegroups.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attachauth=ANoY7coMzpFRtLM4k0xQFM5uHV6_UW4qjYf5C8FRXvHy0NDu8d82FC8cK7Up3O2EhV64LSXjWuFUPUBg5NqQdXyli6nmdMelkYIhgqJlN1v8Gt94H9BJjQmYpiJSPaVfueaxEeqdr70QNzejFypRwhcEw3EGT2FcH0E4WnmQ-LL49xHzV-DIL_O1kCZ12Dq2KIrjElFK-RgkRR1qoM20dsjxFYIweSsDmIlBAMvAX2kAntIKHMHfddk%3D&attredirects=0). Le document étant extrêmement bien fait nous décidons de coder pas à pas la stratégie de recommendation. 

# Points techniques

Pour simplifier la lecture du code et pour se repartir aisément le travail nous avons decider de fragmenter le plus possible le code en sous fonctions. La fonction `play`se réduit alors à quelques lignes qui appellent les autres fonctions.

## Hand.recommendation

La stratégie de hat guessing que l'on a retenu necessite que chaque joueur retienne la dernière recommandation qui lui a été donné plus que l'indice puisque ce dernier ne correspond à rien. Nous avons donc ajouté un élément à la classe `Hand` : l'argument `hand.recommendation` qui contient la dernière recommandation. 

## Actions

La strategie que nous avons retenu necessite aussi que les joueurs se souviennent des actions précédentes pour modeliser ce souvenir nous avons créé une variable de classe dans `Strat1.ai` appelée `actions` et qui n'est rien d'autre qu'une liste contenant toutes les actions efféctuées par les joueurs. Il était inutile de démultiplier cette information et de la placer dans les différentes mains des joueurs, la variable de classe paraissait alors adaptée à la situation et s'apparente à un savoir collectif.

## La fonction c_i
Un des éléments important de la stratégie de recommandation est de déterminer le coefficient ci donné à chanque mains. Nous avons décidé de créer une fonction dédier à ce calcul. Nous l'avons simplement nommé `c_i`.

La fonction c_i permet d'attribuer un chiffre modulo 8 à une main correspondant à la recommandation qui lui est donnée.
Elle prend en argument la main d'un joueur sous forme de liste de card
et renvoie un chiffre entre 0 et 7.

Cette fonction permet au donneur d'indice, en sommant les
c_i de chaque main, de donner un indice à chaque joueur de la table
selon le principe du hat gessing.

Cette fonction permet aussi aux joueurs de décoder l'indice donné en
additionnant les c_i des autres joueurs (sauf celui du donneur d'indice)

## Fonction ou tableau is_indispensable

Pour le calcul de ci il faut être capable de déterminer si une carte est indispensable. Nous avons alors créer une fonction `is_indispensable` qui détermine si une carte est indispensable ou non. 

Plus tard nous nous sommes rendu compte que la fonction que nous avions codé ,qui était extrêmement simple, ne prenait pas en compte toutes les possibilités. En effet, la fonction considérait par exemple que le 5 d'une couleur serait d'office indispensable. Or ce n'est pas le cas puisqu'en effet, si les deux 4 ou les deux 3 de la même couleurs avaient déjà été défaussés, le 5 ne serait alors pas indispensable, il serait même inutile.

Dans un premier temps nous avons donc créé une nouvelle fonction `is_indispensable2` en prenant en compte tous les cas de défausse.

Plus tard, en réfléchiqqant sur l'optimalité de l'algorithme nous nous sommes rendu compte que la carte 5 de l'exemple précédent étant inutile, il faudrait alors la compter comme une *dead_card*. Ce changement a un impact sur le code puisque dans la priorité des indices, défausser une *dead_card* est plus important que de défausser une carte qui est non *is_indispensable*. Nous avons alors mis en évidence deux façons de proceder.

### Utiliser les fonctions déjà écrites 

Nous avons remarqué que la fonction is_indispensable2 nous donnait **False** pour les *dead_card* et les non *is_indispensable* et **True** pour les *is_indispensable* pendant que la fonction is_indispensable nous donnait par définition **False** pour les non *is_indispensable* et **True** pour les *is_indispensable*. Ainsi une *dead_card* sera alors simplement définie par une card telle que ```is_indispensable(self, card) == True and is_indispensable2(self,card) == False```. 

Ainsi, nous avions une définition d'une dead_card assez simple. Mais nous avons remarqué que cette façon de faire n'était pas très explicite ou pratique pour une personne qui reprendrait notre code plus tard. 

### Créer un tableau de dead_card

Une *dead_card* étant définie par:
* Soit cette carte a déjà été jouée sur le plateau auquel cas elle ne servira plus
* Soit cette carte est injouable car un nombre suffisant de cartes de la même couleur et d'un nombre inférieur a été défaussé.

Nous avons alors créé le tableau dans la fonction play
* Lorsqu'une carte est (bien) jouée on l'ajoute dans le tableau 
* Lorsqu'une carte est défaussée on vérifie si elle était indispensable
  * Si elle l'était alors toutes les cartes de nombre supérieur sont ajoutées au tableau
  * Sinon rien ne se passe
  
## La fonction clue()

La fonction renvoie l'indice à donner en regardant les cartes de touts les autres joueurs sous forme d'une chaine de caractère

## La fonction from_clue_to_play()

La fonction est lancée au moment où le joueur donne l'indice. Elle doit mettre à jour hand.recommendation pour tous les autres joueurs
c'est-à-dire traduire l'indice pour chaque joueur.

## La fonction played_since_hint()

La fonction répond à la question : Une carte a-t-elle été joué depuis que l'on m'a donné un indice (current hand.recommendation)

## La fonction play()
La fonction qui "repond" au jeu selon l'algorithme de la classe.
Après avoir joué on met a jour la liste actions et si besoin est on appelle from_clue_to_play

## L'interface graphique

Nous avons décidé d'utiliser TKinter pour réaliser l'interface graphique puisque c'est un module de base de python et qu'il n'y avait rien besoin de telecharger en plus.

Nous avons décidé d'utiliser les classes et d'utiliser une fonction par menu, ainsi chaque commande (chaque clic sur un bouton) lance une fonction qui remet à zero l'affichage de la fenêtre et ajoute ses propres élémennts. Cela permet de passer aisément d'un menu à l'autre et de toujours disposer de tous les boutons que l'on souhaite. En réalité je ne vois pas comment nous aurions pu nous passer des classes. 

Comme c'était la première fois que nous manipulions des interfaces graphiques nous sommes allés au plus simple, ainsi le code est assez long et très redondant. Il serait possible de le factoriser en réduisant toutes les fonctions qui se ressemblent à l'appelle d'une fonction à paramètres : 
```
def play_1(self):
	self.play(1)

def play_2(self):
	self.play(2)
```

Cette partie n'a pas été spécialement compliqué puisque, une fois le module TKinter compris, il suffisait de faire dialoguer l'interface avec le jeu et comme nous avions déjà codé une partie de l'ai à ce stade du projet nous avions bien compris comment le fichier deck.py fonctionnait. 


# Tests unitaires

## Test c_i

On initialise d'abord une simulation de partie:
```
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

game.piles[Green]=2
game.piles[Yellow]=4
game.piles[White] = 1
game.piles[Red]= 4
game.piles[Blue] = 0
```

On construit les cas tests en fonction de la priorité des indices:
* Jouer le 5 jouable de plus bas indice: on propose le cas test:
```
card1 = hanabi.deck.Card(Red, 5)
card2 = hanabi.deck.Card(Yellow, 5)
card3 = hanabi.deck.Card(Red, 2)
card4 = hanabi.deck.Card(Blue, 5)
L = [card1, card2, card3, card4]
```
Ici, les deux premiers 5 sont jouables, on cherche donc à vérifier que l'indice donné sera c_i(L) = 0 c'est à dire *play card 1* 

* Jouer la carte de plus petit nombre jouable. A nombre égale, on prendra le plus petit indice

```
card6 = hanabi.deck.Card(Red, 4)
card7 = hanabi.deck.Card(Yellow, 4)
card8 = hanabi.deck.Card(Green, 3)
card9 = hanabi.deck.Card(Blue, 1)
L2 = [card6, card7, card8, card9]
```
Ici, on s'attend à ce que la fonction c_i retourne 3 c'est à dire *Play card 4*. Nous avons de même essayé avec deux carte 'B1' et en effet, c_i retourne bien l'indice le plus bas. 
Ce cas test nous a permis de déceler deux erreurs que nous n'avions pas encore vu dans le code. 

* Défausser la *dead_card* de plus petit indice

Il suffit pour cela de ne mettre que des cartes injouables (indispensables ou non) et des *dead_card* dans notre liste test. 

**Par exemple:** [B2,Y2,R2,B5]

* Défausser la carte non indispensable de plus haut rang
 Ici, il ne faut mettre que des cartes injouable et non *dead_card* 
 **Par exemple :** [B2,W5,W4,B5]
 Ce test a été fait avant de considérer que comme les deux W2 avaient été défaussées, W4 et W5 sont en fait *dead*
 
 * Défausser c_1
 Il suffit ici de ne mettre que des cartes consiérées comme indispensables.

## Test is_indispensable() et is_indispensable2()

Les deux fonctions n'utilisent que le tableau de défausse. On considère alors la même liste de défausse que précédemment dans le cas test des c_i. Et on test ici trois cas:

* **Cas indispensable** : la carte est la seule qui existe dans le deck et les cartes défaussées ne la rendent pas inutile. **Par exemple :** on a défaussé deux fois la carte 1 Rouge rendant la carte **1 Rouge indispensable**. On remarque que le cas test ne peut pas interférer avec l'assertion *dead_card* car si elle a été défaussée deux fois et jouée une fois elle ne peut plus être dans la main d'un joueur.
```
t1=hanabi.deck.Card(Red,1)
if ai.is_indispensable2(t1) : print("test 1 OK")
else: print("test 1 not OK ")
```
* **Cas non indispensable** : La carte a au moins un doublons dans le deck, elle peut donc être défaussée sans crainte. (Possibilité d'erreur dans le programme: Si deux personnes ont la même carte et que l'indice qui leur est donné est de défausser pour les deux, que l'un défausse cette carte, cette carte dans la main du deuxième joueur devient indispensable. Il ne peut donc pas défausser cette carte. La probabilité étant assez faible on ne comptera pas ce cas dans notre programme) **Par exemple:** Ici le 3 Jaune n'a jamais été défaussé au regard de la pile de défausse on peut donc affirmer qu'il est non indispensable. 

* **Cas mort** : Le cas tel que les cartes défaussées rendent la carte inutile. Nous testons alors l'efficacité de notre fonction is_indispensable2 par rapport à la fonction is_indispensable. **Par exemple :** C'est ici le cas de la carte 5 Blanche. Le cas test est alors très simple:
```
t3=hanabi.deck.Card(White,5)
if not(ai.is_indispensable2(t3)) and ai.is_indispensable(t3) : print("test 3 OK")
else: print("test 6 not OK ")
```

## L'interface graphique

Nous n'avons pas réalisé de test unitaires pour cette partie, nous nous sommes contenté de jouer avec l'interface et de verifier que celle-ci fonctionnait correctement. 
Et comme une image vaut mieux que mille mots...
![bienvenue](bienvenue.png)
![](play_advanced.png)
![](clue.png)
![](piles.png)
![](discard.png)
![](play.png)



Pour tester la fin de la partie et le menu de fin, nous avons créé un bouton supléméntaire "pop" qui permettait de vider le deck manuellement et ainsi arriver à la fin de partie très rapidement.




# Statistiques

Le fichier `get_data.py` permet de tester sur un grand nombre de parties l'éfficaciter de l'ai que nous avons codé. Il lance 1000 parties calcul la moyenne et résume les résultats dans un histograme. 

Le score moyen après 1000 parties est 22.24 et la répartition des scores est la suivante :

![resultats](result.png)


# Conclusion et perspectives

Finalement notre score est équivalent à celui de l'article, les quelques détails que nous pourrions changer ne devraient pas tellement influencer l'allure globale de notre courbe. En revanche ils pourraient peut-être améliorer l'efficacité et la lisibilité du code.
Nous n'avons pas eu le temps de finir la liste de dead_card pour rendre le code plus clair et utilisable par des personnes extérieures. De plus nous pourrions changer la fonciton is_indispensable pour en faire une liste rendant encore une fois les choses plus claires et utilisables. Nous pourrions aussi traiter le cas où deux personnes sur la table reçoivent le même conseil de défausser une même carte qui devient alors indispensable. 

Il serait aussi extrêmement intéressant d'essayer de coder les règles implicites du véritable jeu. 
