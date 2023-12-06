print("***************WELCOME TO NYSD GAME***************")

step1 = str(input("where do you want to go 'left' or 'right':  ")).lower()

if step1 == 'right':
    step2 = str(input("you are at the river bank right now. Are you 'waiting' for the boat or going to 'swim':  ")).lower()
    
    if step2 == 'waiting':
        step3 = str(input("there is three door infront of you which door color will you enter'yellow red blue': ")).lower()
        
        if step3 == 'blue':
            print('''********************NYSD Company offer you this gift********************
           __     _______ ____   ___  _   _ ___ ___  _   _ _____  
\ \   / / ____|  _ \ / _ \| \ | |_ _/ _ \| | | | ____| 
 \ \ / /|  _| | |_) | | | |  \| || | | | | | | |  _|   
  \ V / | |___|  _ <| |_| | |\  || | |_| | |_| | |___  
   \_/__|_____|_|_\_\\___/|_| \_|___\__\_\\___/|_____| 
    | ___|___ \ / _ \/ |___ // | || |                  
    |___ \ __) | | | | | |_ \| | || |_                 
     ___) / __/| |_| | |___) | |__   _|                
    |____/_____|\___/|_|____/|_|  |_|  ''')
        else:
            print("////GAME OVER////")    
    else:
        print("////GAME OVER////")
else:
    print("////GAME OVER////")
