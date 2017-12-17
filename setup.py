'''
	Copyright (c) 2017 Naveen Venkat
	nav.naveenvenkat@gmail.com
	https://github.com/nmakes/simple-db
'''

from os import system

def menu():

	print "SimpleDB v0.1"
	print "-------------"
	print "1. Update"
	print "2. Copyright Information"
	print "3. Exit"
	print

if __name__=='__main__':

	inp = None

	while(inp!=3):

		menu()
		inp = raw_input(": ")

		if inp.strip()=='1':

			print "Running git pull ..."
			system('git pull https://github.com/nmakes/simple-db master')

		elif inp.strip()=='2':
			
			print "Copyright (c) 2017 Naveen Venkat\nnav.naveenvenkat@gmail.com\nhttps://github.com/nmakes/simple-db"
			s  = raw_input("\n\nPress enter to continue .. ")

		elif inp.strip() == '3':

			exit()