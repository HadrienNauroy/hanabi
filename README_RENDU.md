# Stratégie retenue

Nous avons fais le choix de nous intéresser au document sur le  [hat guessing](https://d0474d97-a-62cb3a1a-s-sites.googlegroups.com/site/rmgpgrwc/research-papers/Hanabi_final.pdf?attachauth=ANoY7coMzpFRtLM4k0xQFM5uHV6_UW4qjYf5C8FRXvHy0NDu8d82FC8cK7Up3O2EhV64LSXjWuFUPUBg5NqQdXyli6nmdMelkYIhgqJlN1v8Gt94H9BJjQmYpiJSPaVfueaxEeqdr70QNzejFypRwhcEw3EGT2FcH0E4WnmQ-LL49xHzV-DIL_O1kCZ12Dq2KIrjElFK-RgkRR1qoM20dsjxFYIweSsDmIlBAMvAX2kAntIKHMHfddk%3D&attredirects=0). Le document étant extrêmement bien fait nous décidons de coder pas à pas la stratégie de recommendation. 


# Points techniques

## La fonction c_i
Dans ce document, nous trouvons que pour optimiser le code il vaudrait mieux créer une fonction que nous nommons c_i.

La fonction c_i permet d'attribuer un chiffre modulo 8 à une main correspondant à la recommendation qui lui est donnée.
Elle prend en argument la main d'un joueur sous forme de liste de card
et renvoie un chiffre entre 0 et 7.

Cette fonction permet au donneur d'indice, en sommant les
c_i de chaque main, de donner un indice à chaque joueur de la table
selon le principe du hat gessing.

Cette fonction permet aussi aux joueurs de décoder l'indice donné en
additionnant les c_i des autres joueurs (sauf celui du donneur d'indice)

## Fonction ou tableau is_indispensable

Cette fonction suit les règles du hat guessing décrites dans le document mais nous demande de créer un élément nous disant si une carte étudiée est indispensable ou non. Il faut alors que nous décidions la forme de cet élément. Soit un tableau qui serait au fur et à mesure du jeu réactualisé, soit une fonction qui prendrait en argument la carte et le statut du jeu et renverrait un booléen. On a alors choisi la fonction car elle nous semblait alors plus facile à coder et à utiliser. 

Plus tard nous nous rendons compte que la fonction que nous avons codé ,qui était extrêmement simple, ne prenait pas en compte toutes les possibilités. En effet, la fonction considérait par exemple que le 5 d'une couleur serait d'office indispensable. Or ce n'est pas le cas puisqu'en effet, si les deux 4 ou les deux 3 de la même couleurs avaient déjà été défaussés, le 5 ne serait alors pas indispensable, il serait même inutile.

Dans un premier temps nous avons donc crée une nouvelle fonction is_indispensable2 en prenant en compte tous les cas de défausse.

Plus tard, nous réfléchissons sur l'optimalité de l'algorithme. On se rend compte que la carte 5 de l'exemple précédent étant inutile, il faudrait la compter comme une *dead_card*. Ce changement a un impact sur le code puisque dans la priorité des indices, défausser une *dead_card* est plus important que de défausser une carte qui est non *is_indispensable*. Nous vient alors à l'esprit deux façons de faire
### Utiliser les fonctions déjà écrites 

Nous remarquons que la fonction is_indispensable2 nous donnera **False** pour les *dead_card* et les non *is_indispensable* et **True** pour les *is_indispensable* pendant que la fonction is_indispensable nous donnera par définition **False** pour les non *is_indispensable* et **True** pour les *is_indispensable*. Ainsi une *dead_card* sera alors simplement définie par une card telle que ```is_indispensable(self, card) == True and is_indispensable2(self,card) == False```. 

Ainsi, nous aurions une définition d'une dead_card assez simple. Mais nous remarquons que cette façon de faire n'est pas très explicite ou pratique pour une personne qui reprendrait notre code plus tard. 

### Créer un tableau de dead_card

Une *dead_card* étant définie par:
* Soit cette carte a déjà été jouée sur le plateau auquel cas elle ne servira plus
* Soit cette carte est injouable car un nombre suffisant de cartes de la même couleur et d'un nombre inférieur a été défaussé.

Nous créons alors le tableau dans la fonction play
* Lorsqu'une carte est (bien) jouée on l'ajoute dans le tableau 
* Lorsqu'une carte est défaussée on vérifie si elle était indispensable
  * Si elle l'était alors toutes les cartes de nombre supérieur sont ajoutées au tableau
  * Sinon rien ne se passe
