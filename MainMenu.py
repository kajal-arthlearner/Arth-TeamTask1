from os import system

while True:
	while True:
		system("clear")
		print("\n\t"+48*"-")
		print("\t\tAutomation Menu" by Arth Team-3.12)
		print("\t"+48*"-")
		print("\n\tNote: For the best experience, please ensure that yum is configured properly")
		print("\n\tPlease select an option: \n")
		system("tput setaf 14")
		print("\t\t1 : AWS & Hadoop configuration")
		print("\t\t2 : LVM configuration")
		print("\t\t3 : Docker configuration")
		print("\t\t0 : Exit")
		
		
		if opt == '1':
			os.system('python3 AWS & Hadoop configuration.py')
			
		elif opt == '2':
    	                os.system('python3 lvm.py')
			
			
		elif opt == '3':
			os.system('python3 docker.py')	
				
		elif opt == '0':
			exit()