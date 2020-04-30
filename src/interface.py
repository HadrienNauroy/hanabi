"""file that open a graphic interface to play hanabi with some ia"""


import time
from tkinter import *
import hanabi


	
class Application : 

	def __init__(self): 

		"fenetre principale"
		self.master = Tk()
		self.master.title("Hanabi")
		self.master.geometry("800x500")

		

		"tous les boutons qui seront utiles par la suite"

		self.single=Button(self.master,text='Single Player',command=self.singlep)
		self.multi=Button(self.master,text='Two players',command=self.multi_turn)

		self.play=Button(self.master,text='Play',command=self.to_play)  #l'erreur est ici il faut mettre self.to_play et non self.to_play()
		self.discard=Button(self.master,text='Discard',command=self.to_discard)
		self.examine=Button(self.master, text = 'examine Piles ', command = self.to_examine)
		self.clue=Button(self.master, text='Give a Clue', command=self.to_clue)

		self.P1=Button(self.master,text='Card 1',command=self.p_1)
		self.P2=Button(self.master,text='Card 2',command=self.p_2)
		self.P3=Button(self.master,text='Card 3',command=self.p_3)
		self.P4=Button(self.master,text='Card 4',command=self.p_4)
		self.P5=Button(self.master,text='Card 5',command=self.p_5)

		self.D1=Button(self.master,text='Card 1',command=self.d_1)
		self.D2=Button(self.master,text='Card 2',command=self.d_2)
		self.D3=Button(self.master,text='Card 3',command=self.d_3)
		self.D4=Button(self.master,text='Card 4',command=self.d_4)
		self.D5=Button(self.master,text='Card 4',command=self.d_5)

		self.C1=Button(self.master,text='Clue 1',command=self.c_1)
		self.C2=Button(self.master,text='Clue 2',command=self.c_2)
		self.C3=Button(self.master,text='Clue 3',command=self.c_3)
		self.C4=Button(self.master,text='Clue 4',command=self.c_4)
		self.C5=Button(self.master,text='Clue Red',command=self.c_R)
		self.C6=Button(self.master,text='Clue White',command=self.c_W)
		self.C7=Button(self.master,text='Clue Green',command=self.c_G)
		self.C8=Button(self.master,text='Clue Yellow',command=self.c_Y)
		self.C9=Button(self.master,text='Clue Blue',command=self.c_B)

		self.OK=Button(self.master,text='Okay',command=self.multi_turn)
		self.back=Button(self.master,text='Back',command=self.multi_turn)
		
		self.quit=Button(self.master,text='Quit',command=self.master.destroy)
		self.back_menu=Button(self.master,text='Back to menu',command=self.menu)


		"tous les labels qui seront utiles par la suite"

		self.champ_label = Label(self.master, text="Bienvenue sur Hanabi",font=("Helvetica", 16))

		self.champ_label2 = Label(self.master, text="These are piles :  " ,font=("Helvetica", 16))
		self.champ_label3 = Label(self.master, text="Can't clue this ! " ,font=("Helvetica", 16))
		self.champ_label4 = Label(self.master, text="Can't clue anymore ! " ,font=("Helvetica", 16))
		

		self.photo = PhotoImage(file = "fireworks.gif",format="gif -index 2")
		self.image = Label(self.master, image = self.photo)
		self.bravo= Label(self.master, text='Well done !', font=("Helvetica",16))
		self.sad= Label(self.master, text='Maybe next time !', font=("Helvetica",16))
		self.loss= Label(self.master, text='You loose : 3 red coins !', font=("Helvetica",16))


		self.menu()
		self.master.mainloop()
		

	def menu(self):
		"set up du jeu"
		self.game=hanabi.Game()
		self.player=0
		#self.red_coins=0  

		"Maj affichage"

		self.loss.pack_forget()
		self.back_menu.pack_forget()
		self.quit.pack_forget()
		self.sad.pack_forget()


		"menu du jeu"
		self.champ_label.pack()
		self.single.pack()
		self.multi.pack()


	def verrif_color(self,color):
		for k in range(4):
			if str(self.game.hands[1].cards[k].color) == color:
				return True
		return False

	def verrif_number(self,nb):
		for k in range(4):
			if self.game.hands[1].cards[k].number == nb :
				return True
		return False



	def singlep(self):

		'''mode 1humain et une ia'''
		
		self.single.pack_forget()
		self.multi.pack_forget()
		self.champ_label.pack_forget()
		self.game=hanabi.Game()
		self.player = 0


	

	def multi_turn(self):
		
		"affichage texte"
		remember=self.game.current_hand.str_clue()
		other_hand=self.game.hands[1]
		see=other_hand.__str__()
		self.champ_label1 = Label(self.master, text=" Player %d this is what you see : %s \n This is what you remember : %s" %(self.player + 1, see ,remember ),font=("Helvetica", 16))
		self.champ_label1.pack()
		self.OK.pack_forget()
		self.champ_label2.pack_forget()
		self.single.pack_forget()
		self.multi.pack_forget()
		self.champ_label.pack_forget()
		self.champ_label3.pack_forget()
		self.champ_label4.pack_forget()
		self.back.pack_forget()
		self.D1.pack()
		self.D1.pack_forget()
		self.D2.pack_forget()
		self.D3.pack_forget()
		self.D4.pack_forget()
		self.D5.pack_forget()
		self.P1.pack_forget()
		self.P2.pack_forget()
		self.P3.pack_forget()
		self.P4.pack_forget()
		self.P5.pack_forget()
		self.C1.pack_forget()
		self.C2.pack_forget()
		self.C3.pack_forget()
		self.C4.pack_forget()
		self.C5.pack_forget()
		self.C6.pack_forget()
		self.C7.pack_forget()
		self.C8.pack_forget()
		self.C9.pack_forget()


		"boutons"
		
		self.play.pack()
		self.clue.pack()
		self.examine.pack()
		self.discard.pack()
		

	def to_play(self):
		
		"MAJ affichage"
		self.bravo.pack_forget()
		self.sad.pack_forget()
		self.play.pack_forget() 
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
		self.P5.pack()
		self.back.pack()



	def to_discard(self):

		"MAJ affichage"
		self.bravo.pack_forget()
		self.sad.pack_forget()
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
		self.D5.pack()
		self.back.pack()


	def to_clue(self) : 

		if  not (self.game.blue_coins > 0 ) :
			self.champ_label4.pack()
		else :

			"MAJ affichage"
			self.bravo.pack_forget()
			self.sad.pack_forget()
			self.play.pack_forget()
			self.discard.pack_forget()
			self.champ_label1.pack_forget()
			self.clue.pack_forget()
			self.examine.pack_forget()
			self.champ_label2 = Label(self.master, text="What clue do you want to give ? ",font=("Helvetica", 16))
			self.champ_label2.pack()

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
			self.back.pack()


	def to_examine(self):

		"MAJ affichage"
		self.bravo.pack_forget()
		self.sad.pack_forget()
		self.play.pack_forget()
		self.discard.pack_forget()
		self.champ_label1.pack_forget()
		self.clue.pack_forget()
		self.examine.pack_forget()
		piles=self.game.piles
		self.champ_label2 = Label(self.master, text="These are piles : \n %s " %piles,font=("Helvetica", 16))
		self.champ_label2.pack()

		"Nouveaux boutons"
		self.OK.pack()

	def p_1(self):
		card=self.game.current_hand.cards[0]
		pile=self.game.piles[card.color]
		if card.number == pile+1 : 
			self.bravo.pack()
			self.game.turn("p1")
			self.player=(self.player+1)%2
			self.multi_turn()

		else : 
			self.sad.pack()
			#self.red_coins+=1
			if self.game.red_coins==2 :
				print("OK")
				"MAJ affichage"
				self.OK.pack_forget()
				self.champ_label2.pack_forget()
				self.single.pack_forget()
				self.multi.pack_forget()
				self.champ_label.pack_forget()
				self.champ_label3.pack_forget()
				self.champ_label4.pack_forget()
				self.back.pack_forget()
				self.loss.pack()
				self.P1.pack_forget()
				self.P2.pack_forget()
				self.P3.pack_forget()
				self.P4.pack_forget()
				self.P5.pack_forget()

				"boutons"
				self.quit.pack()
				self.back_menu.pack()
			else :
				self.game.turn("p1")
				self.player=(self.player+1)%2
				self.multi_turn()

		
			
		

	def p_2(self):
		card=self.game.current_hand.cards[1]
		pile=self.game.piles[card.color]
		if card.number == pile+1 : 
			self.bravo.pack()
			self.game.turn("p2")
			self.player=(self.player+1)%2
			self.multi_turn()

		else : 
			self.sad.pack()
			#self.red_coins+=1
			if self.game.red_coins==2 :
				print("OK")
				"MAJ affichage"
				self.OK.pack_forget()
				self.champ_label2.pack_forget()
				self.single.pack_forget()
				self.multi.pack_forget()
				self.champ_label.pack_forget()
				self.champ_label3.pack_forget()
				self.champ_label4.pack_forget()
				self.back.pack_forget()
				self.loss.pack()
				self.P1.pack_forget()
				self.P2.pack_forget()
				self.P3.pack_forget()
				self.P4.pack_forget()
				self.P5.pack_forget()

				"boutons"
				self.quit.pack()
				self.back_menu.pack()
			else :
				self.game.turn("p2")
				self.player=(self.player+1)%2
				self.multi_turn()

		

	def p_3(self):
		card=self.game.current_hand.cards[2]
		pile=self.game.piles[card.color]
		if card.number == pile+1 : 
			self.bravo.pack()
			self.game.turn("p3")
			self.player=(self.player+1)%2
			self.multi_turn()

		else : 
			self.sad.pack()
			#self.red_coins+=1
			if self.game.red_coins==2 :
				print("OK")
				"MAJ affichage"
				self.OK.pack_forget()
				self.champ_label2.pack_forget()
				self.single.pack_forget()
				self.multi.pack_forget()
				self.champ_label.pack_forget()
				self.champ_label3.pack_forget()
				self.champ_label4.pack_forget()
				self.back.pack_forget()
				self.loss.pack()
				self.P1.pack_forget()
				self.P2.pack_forget()
				self.P3.pack_forget()
				self.P4.pack_forget()
				self.P5.pack_forget()

				"boutons"
				self.quit.pack()
				self.back_menu.pack()
			else :
				self.game.turn("p3")
				self.player=(self.player+1)%2
				self.multi_turn()

		

	def p_4(self):
		card=self.game.current_hand.cards[3]
		pile=self.game.piles[card.color]
		if card.number == pile+1 : 
			self.bravo.pack()
			self.game.turn("p4")
			self.player=(self.player+1)%2
			self.multi_turn()

		else : 
			self.sad.pack()
			#self.red_coins+=1
			if self.game.red_coins==2 :
				print("OK")
				"MAJ affichage"
				self.OK.pack_forget()
				self.champ_label2.pack_forget()
				self.single.pack_forget()
				self.multi.pack_forget()
				self.champ_label.pack_forget()
				self.champ_label3.pack_forget()
				self.champ_label4.pack_forget()
				self.back.pack_forget()
				self.loss.pack()
				self.P1.pack_forget()
				self.P2.pack_forget()
				self.P3.pack_forget()
				self.P4.pack_forget()
				self.P5.pack_forget()

				"boutons"
				self.quit.pack()
				self.back_menu.pack()
			else :
				self.game.turn("p4")
				self.player=(self.player+1)%2
				self.multi_turn()

		

	def p_5(self):
		card=self.game.current_hand.cards[4]
		pile=self.game.piles[card.color]
		if card.number == pile+1 : 
			self.bravo.pack()
			self.game.turn("p5")
			self.player=(self.player+1)%2
			self.multi_turn()

		else : 
			self.sad.pack()
			#self.red_coins+=1
			if self.game.red_coins==2 :
				print("OK")
				"MAJ affichage"
				self.OK.pack_forget()
				self.champ_label2.pack_forget()
				self.single.pack_forget()
				self.multi.pack_forget()
				self.champ_label.pack_forget()
				self.champ_label3.pack_forget()
				self.champ_label4.pack_forget()
				self.back.pack_forget()
				self.loss.pack()
				self.P1.pack_forget()
				self.P2.pack_forget()
				self.P3.pack_forget()
				self.P4.pack_forget()
				self.P5.pack_forget()

				"boutons"
				self.quit.pack()
				self.back_menu.pack()
			else :
				self.game.turn("p5")
				self.player=(self.player+1)%2
				self.multi_turn()

		
	
	def d_1(self):
		card=self.game.current_hand.cards[0]
		pile=self.game.piles[card.color]
		self.game.turn("d1")
		self.player=(self.player+1)%2
		self.multi_turn()

	def d_2(self):
		card=self.game.current_hand.cards[1]
		pile=self.game.piles[card.color]
		self.game.turn("d2")
		self.player=(self.player+1)%2
		self.multi_turn()

	def d_3(self):
		card=self.game.current_hand.cards[2]
		pile=self.game.piles[card.color]
		self.game.turn("d3")
		self.player=(self.player+1)%2
		self.multi_turn()

	def d_4(self):
		card=self.game.current_hand.cards[3]
		pile=self.game.piles[card.color]
		self.game.turn("d4")
		self.player=(self.player+1)%2
		self.multi_turn()

	def d_5(self):
		card=self.game.current_hand.cards[4]
		pile=self.game.piles[card.color]
		self.game.turn("d5")
		self.player=(self.player+1)%2
		self.multi_turn()


	def c_1(self):
		if ( self.verrif_number(1)):
			self.game.turn("c1")
			self.player=(self.player+1)%2
			self.multi_turn()
		else : 
			self.champ_label3.pack()



	def c_2(self):
		if ( self.verrif_number(2)):
			self.game.turn("c2")
			self.player=(self.player+1)%2
			self.multi_turn()
		else : 
			self.champ_label3.pack()
			
	def c_3(self):
		if ( self.verrif_number(3)):
			self.game.turn("c3")
			self.player=(self.player+1)%2
			self.multi_turn()
		else : 
			self.champ_label3.pack()
			

	def c_4(self):
		if ( self.verrif_number(4)):
			self.game.turn("c4")
			self.player=(self.player+1)%2
			self.multi_turn()
		else : 
			self.champ_label3.pack()
			

	def c_R(self):
		color="Red"
		if self.verrif_color(color):
			self.game.turn("cR")
			self.player=(self.player+1)%2
			self.multi_turn()
		else :
			self.champ_label3.pack()

	def c_W(self):
		color="Red"
		if self.verrif_color(color):
			self.game.turn("cR")
			self.player=(self.player+1)%2
			self.multi_turn()
		else :
			self.champ_label3.pack()

	def c_Y(self):
		color="Yellow"
		if self.verrif_color(color):
			self.game.turn("cY")
			self.player=(self.player+1)%2
			self.multi_turn()
		else :
			self.champ_label3.pack()

	def c_B(self):
		color="Blue"
		if self.verrif_color(color):
			self.game.turn("cB")
			self.player=(self.player+1)%2
			self.multi_turn()
		else :
			self.champ_label3.pack()

	def c_G(self):
		color="Green"
		if self.verrif_color(color):
			self.game.turn("cG")
			self.player=(self.player+1)%2
			self.multi_turn()
		else :
			self.champ_label3.pack()



Application()
