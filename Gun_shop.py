print('''
 *******************************************                                      
|_t+.__________________......_  /;_      
;________________/     :    \ t""o.\__   
:---|------------------t-----^-`--'  /   
 \__L___________________\____________\   
              ""-. o .--. \--'/  l  .-t+.
                  \ (   l) ;""   : /     
     _  _  _       l `--" o;      Y      
 |_||_ |_|| \       """""";:  .-. :\     
 | |:_ | |:_/             ::  '-'  ;\    
  _  _    _  _  _  _       ;;      : ;   
 | ||_l  | \|_ |_|| \      :: bug   ;|   
 :_l|`,  :_/:_ | |:_/      ;'-------';   
                           '"------""   
*********************************************                           
                           
''')
print("Welcome to the Gary's pistol shop.")
print("Your mission is to find the shot gun.") 

start = input("Press S to start the game. >> ").lower()
if(start == 's'):
  print("You are inside the pistol shop.")
  item = input("Shopkeeper: What do you want buddy? Gun or Bomb >> ").lower()
  if(item == 'gun' or item == 'bomb'):
    gang_name = input("Shopkeeper: What's your gang name? CatRat or WolfGang >> ").lower()
    if gang_name == 'catrat':
      code = input("Shopkeeper: Tell me your code >> ").lower()
      if code == 'sudo':
        print("Here is your shot gun, Mission Passed.")
      else:
        print("Incorrect code, Get out of the shop.")
    else:
      print("Game Over.")
else:
  print("You pressed the wrong button. you are wasted")    
