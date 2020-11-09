from os import system


while True:
        while True:
                system("clear")
                print("\n\t"+48*"-")
                print("\t\tAutomation Menu by Arth Team-3.12")
                print("\t"+48*"-")
                print("\n\tNote: For the best experience, please ensure that yum is configured properly")
                print("\n\tPick one: \n")
                system("tput setaf 14")
                print("\t\t1 : AWS & Hadoop configuration")
                print("\t\t2 : LVM configuration")
                print("\t\t3 : Docker configuration")
                print("\t\t0 : Exit")
                opt=input()

                if opt == '1':
                        system('python3 'AWS & Hadoop configurations.py'')

                elif opt == '2':
                        system('python3 lvm.py')


                elif opt == '3':
                        system('python3 docker.py')

                elif opt == '0':
                        exit()
~
