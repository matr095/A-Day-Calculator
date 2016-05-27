from ftplib import FTP
from datetime import *
from tkinter import *

def interval():
	now = date.today()
	yourDay = int(input("Vous êtes né quel jour ? "))
	yourMonth = int(input("Vous êtes né quel mois ? "))
	yourYear = int(input("Vous êtes né quelle année ? "))
	birthday = date(yourYear, yourMonth, yourDay)

	daysPassed = now - birthday

	import os
	clear = lambda: os.system('clear')
	clear()

	endOfString = str(daysPassed).index(" ")
	print("Tu as " + str(daysPassed)[:endOfString] + " jours !")


def calculate():
	global result
	global response
	try:
		result.destroy()
	except:
		print("no")
	now = date.today()
	yourDay = int(day.get('1.0', END))
	yourMonth = int(month.get('1.0', END))
	yourYear = int(year.get('1.0', END))
	birthday = date(yourYear, yourMonth, yourDay)
	daysPassed = now - birthday
	endOfString = str(daysPassed).index(" ")
	response = str(daysPassed)[:endOfString]
	result = Label(root, text="Félicitations ! Tu as exactement: " + response + " jours !!!")
	result.pack()
	




root = Tk()
root.minsize(width=640, height=480)
root.maxsize(width=640, height=480)
root.wm_title("A Day Calculator")

Label(root, text="A Day Calculator calcule ton nombre de jours passés depuis ta naissance !").pack()

calc = Button(root, text="Calculer", command=calculate)
calc.pack()

Label(root, text="Jour de naissance").pack()
day = Text(root, width="4", height="2", background="gray")
day.pack()

Label(root, text="Mois de naissance").pack()
month = Text(root, width="4", height="2", background="gray")
month.pack()

Label(root, text="Année de naissance").pack()
year = Text(root, width="4", height="2", background="gray")
year.pack()

Label(root, text="-----------------").pack()



root.mainloop()



