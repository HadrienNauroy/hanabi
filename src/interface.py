"""file that open a graphic interface to play hanabi with some ia"""



from tkinter import *
import hanabi



class application : 

	def __init__(self): 

		"fenetre principale"
		self.master = Tk()
		self.master.title("Hanabi")
		self.master.geometry("500x200")

		"menu du jeu"
		self.champ_label = Label(self.master, text="Bienvenue sur Hanabi",font=("Helvetica", 16))
		self.champ_label.pack()

		self.single=Button(self.master,text='Single Player',command=self.singlep)
		self.single.pack()

		self.multi=Button(self.master,text='Two players',command=self.multip)
		self.multi.pack()

		"tous les boutons qui seront utiles par la suite"

		self.play=Button(self.master,text='Play',command=self.to_play)  #l'erreur est ici il faut mettre self.to_play et non self.to_play()
		self.discard=Button(self.master,text='Discard',command=self.to_discard)
		self.examine=Button(self.master, text = 'examine Piles ', command = self.to_examine)
		self.clue=Button(self.master, text='Give a Clue', command=self.to_clue)

		self.P1=Button(self.master,text='Card 1',command=self.p(1))
		self.P2=Button(self.master,text='Card 2',command=self.p(2))
		self.P3=Button(self.master,text='Card 3',command=self.p(3))
		self.P4=Button(self.master,text='Card 4',command=self.p(4))

		self.D1=Button(self.master,text='Card 1',command=self.d(1))
		self.D2=Button(self.master,text='Card 2',command=self.d(2))
		self.D3=Button(self.master,text='Card 3',command=self.d(3))
		self.D4=Button(self.master,text='Card 4',command=self.d(4))

		self.C1=Button(self.master,text='Clue 1',command=self.c('1'))
		self.C2=Button(self.master,text='Clue 2',command=self.c('2'))
		self.C3=Button(self.master,text='Clue 3',command=self.c('3'))
		self.C4=Button(self.master,text='Clue 4',command=self.c('4'))
		self.C5=Button(self.master,text='Clue Red',command=self.c('R'))
		self.C6=Button(self.master,text='Clue White',command=self.c('W'))
		self.C7=Button(self.master,text='Clue Green',command=self.c('G'))
		self.C8=Button(self.master,text='Clue Yellow',command=self.c('Y'))
		self.C9=Button(self.master,text='Clue Blue',command=self.c('B'))


		

		"tous les labels qui seront utiles par la suite"

		

		self.master.mainloop()



	def singlep(self):

		'''mode 1humain et une ia'''
		
		self.single.pack_forget()
		self.multi.pack_forget()
		self.champ_label.pack_forget()
		self.game=hanabi.Game()
		self.player = 0


	def multip(self):

		'''two humans players'''

		"RAZ affichage"
		self.single.pack_forget()
		self.multi.pack_forget()
		self.champ_label.pack_forget()

		"initialisation jeu"
		self.game=hanabi.Game()
		self.player=0

		"lancement du tour"
		self.multi_turn()


	def multi_turn(self):

		"affichage texte"
		remember=self.game.current_hand.str_clue()
		other_hand=self.game.hands[1]
		see=other_hand.__str__()
		self.champ_label1 = Label(self.master, text=" Player %d this is what you see : %s \n This is what you remember : %s" %(self.player + 1, see ,remember ),font=("Helvetica", 16))
		self.champ_label1.pack()

		"boutons"
		
		self.play.pack()
		self.clue.pack()
		self.examine.pack()
		self.discard.pack()
		self.play.pack_forget()  #FIXME : pas d'erreur 

	def to_play(self):
		
		"MAJ affichage"
		self.play.pack_forget() #FIXME : une erreur (application' object has no attribute 'Play')
		self.discard.pack_forget()
		self.champ_label1.pack_forget()
		self.clue.pack_forget()
		self.examine.pack_forget()
		self.champ_label2 = Label(self.master, text="Wich card do you want to play ? ",font=("Helvetica", 16))
		self.champ_label2.pack()

		"Nouveaux boutons"
		self.P1.pack()
		self.P2.pack()
		self.P3.pack()
		self.P4.pack()


	def to_discard(self):

		"MAJ affichage"
		self.play.pack_forget()
		self.discard.pack_forget()
		self.champ_label1.pack_forget()
		self.clue.pack_forget()
		self.examine.pack_forget()
		self.champ_label2 = Label(self.master, text="Wich card do you want to discard ? ",font=("Helvetica", 16))

		"Nouveaux boutons"
		
		self.D1.pack()
		self.D2.pack()
		self.D3.pack()
		self.D4.pack()

	def to_clue(self) : 

		"MAJ affichage"
		self.play.pack_forget()
		self.discard.pack_forget()
		self.champ_label1.pack_forget()
		self.clue.pack_forget()
		self.self.examine.pack_forget()
		self.champ_label2 = Label(self.master, text="What clue do you want to give ? ",font=("Helvetica", 16))

		"Nouveaux boutons"
		
		self.C1.pack()
		self.C2.pack()
		self.C3.pack()
		self.C4.pack()
		self.C5.pack()
		self.C6.pack()
		self.C7.pack()
		self.C8.pack()
		self.C9.pack()


	def to_examine(self):
		a=2

	def p(self,string):
		a=string

	def c(self,string):
		a=string

	def d(self,string):
		a=string




	

application()