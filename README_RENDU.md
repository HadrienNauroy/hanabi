# Stratégie retenue

Nous avons fais le choix de nous intéresser au document sur le  [hat guessing](https://d0474d97-a-62cb3a1a-s-sites.googlegroups.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attachauth=ANoY7coMzpFRtLM4k0xQFM5uHV6_UW4qjYf5C8FRXvHy0NDu8d82FC8cK7Up3O2EhV64LSXjWuFUPUBg5NqQdXyli6nmdMelkYIhgqJlN1v8Gt94H9BJjQmYpiJSPaVfueaxEeqdr70QNzejFypRwhcEw3EGT2FcH0E4WnmQ-LL49xHzV-DIL_O1kCZ12Dq2KIrjElFK-RgkRR1qoM20dsjxFYIweSsDmIlBAMvAX2kAntIKHMHfddk%3D&attredirects=0). Le document étant extrêmement bien fait nous décidons de coder pas à pas la stratégie de recommendation. 

# Points techniques

Pour simplifier la lecture du code et pour se repartir aisément le travail nous avons decider de fragmenter le plus possible le code en sous fonctions. La fonction `play`se réduit alors à quelques lignes qui appelent les autres fonctions.

## Hand.recommentation

La stratégie de hat guessing que l'on a retenu necessite que chaque joueur retienne la derrnière recommendation qui lui a été donné plus que l'indice puisque ce dernier ne correspond à rien. Nous avons donc ajouté un élément à la classe `Hand` : l'argument `hand.recomendation` qui contient la dernière recommendation. 

## Actions

La strategie que nous avons retenu necessite aussi que les joueurs se souviennent des actions précédentes pour modeliser ce souvenir nous avons créer une variable de classe dans `Strat1.ai` appelée `actions` et qui n'est rien d'autre qu'une liste contenant toutes les actions efféctuées par les joueurs. Il était inutile de démultiplier cette information et de la placer dans les différentes mains des joueurs, la variable de classe paraissait alors adaptée à la situation et s'apparente à un savoir collectif.

## La fonction c_i
Un des éléments important de la stratégie de recommendation est de déterminer le coefficient ci donné à chanque mains. Nous avons décidé de créer une fonction dédier à ce calcul. Nous l'avons simplement nommé `c_i`.

La fonction c_i permet d'attribuer un chiffre modulo 8 à une main correspondant à la recommendation qui lui est donnée.
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

## L'interface graphique

Nous avons décidé d'utiliser TKinter pour réaliser l'interface graphique puisque c'est un module de base de python et qu'il n'y avait rien besoin de telecharger en plus.

Nous avons décider d'utiliser les classes pour et d'utiliser une fonction par menu, ainsi chaque commande (chaque clic sur un bouton) lance une fonction qui remet à zero l'affichage de la fenêtre et ajoute ses propres élémennts. Cela permet de passer aisément d'un menu à l'autre et de toujours disposer de tous les boutons que l'on souhaite. En réalité je ne vois pas comment nous aurions pu nous passer des classes. 

Comme c'était la première fois que nous manipulions des interface graphique nous sommes allé au plus simple, ainsi le code est assez long et très redondant. Il serait possible de le factoriser en réduisant toutes les fonctions qui se ressemblent à l'appelle d'une fonction à paramètres : 
```
def play_1(self):
	self.play(1)

def play_2(self):
	self.play(2)
```

Cette partie n'a pas été spécialement compliqué puisque, une fois le module TKinter compris, il suffisait de faire dialoguer l'interface avec le jeu et comme nous avions déjà codé une partie de l'ai à ce stade du projet nous avions bien compris comment le fichier deck.py fonctionnait. 

# Tests unitaires

## L'interface graphique

Nous n'avons pas réaliser de test unitaires pour cette partie, nous nous sommes contenter de jouer avec l'interface et de verifier que celle-ci fonctionnait correctement. 

Pour tester la fin de la partie et le menu de fin, nous avons créé un bouton supléméntaire "pop" qui perméttait de vider le deck manuellement et ainsi d'arriver à la fin de partie très rapidement.

# Statistiques

Le fichier `get_data.py` permet de tester sur un grand nombre de parties l'éfficaciter de l'ai que nous avons codé. Il lance 1000 parties calcul la moyenne et résume les résultats dans un histograme. 

Le score moyen après 1000 parties est 24.8 et la répartition des scores est la suivante :

![resultats](/src/results.png)
