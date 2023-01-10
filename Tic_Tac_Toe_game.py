
from ast import Global
from gettext import find
from multiprocessing import Value
from operator import truediv
from optparse import Values
from pickle import GLOBAL, TRUE
import pprint
from tkinter import ALL, Grid
from turtle import goto, update
from typing import Any, Dict, Tuple
import random



teamSelect="a"
botTeam="b"
ActiveGame=True

#select team 
    # takes input from user 
    # selects team based on user input
         #use if statement to check if is one team 
         
#generate grid 
#take player input 
#programAi 


def GameMananger():
    
    ActiveGame=True
    if ActiveGame== True:
        TeamSelectfunc()
        print(f"You have selected: {teamSelect}")
        CoordinatesGeneration()


   
   
    
def GenerateBoard(GridValue):
    #creates the game board 
    
    #if ActiveGame==True:

    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(GridValue[0,0],GridValue[0,1],GridValue[0,2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(GridValue[1,0],GridValue[1,1],GridValue[1,2]))
    print('\t_____|_____|_____')
 
    print("\t     |     |")
 
    print("\t  {}  |  {}  |  {}".format(GridValue[2,0],GridValue[2,1],GridValue[2,2]))
    print("\t     |     |")
    print("\n")
    ActiveGame=winconditions(GridValue)
    if ActiveGame==False:
       
            print("Bye Bye!")
            quit()

    CoordatesEntering(GridValue)

def TeamSelectfunc():
    #has the player select if theyre x or o
    global teamSelect
    global botTeam
    print("Welcome please select team:")
    teamSelect = input("x or o")
    teamSelect=teamSelect.lower()
    if teamSelect=="x":
        botTeam="o"
        print(botTeam)
    if teamSelect=="o":
        botTeam="x"
        print(botTeam)
    while teamSelect not in ['x','o']:
    
        teamSelect = input("Invalid input. Please try again. ")
        teamSelect = teamSelect.lower() 
       
    
def winconditions(GridValue):

    x=0


    while x<3:
        if GridValue[x,0] =='x' and GridValue[x,1] =='x' and GridValue[x,2] =='x' or GridValue[x,0] =='o' and GridValue[x,1] =='o' and GridValue[x,2] =='o':
        
            print("Game Over!")
            return ActiveGame==False
        if GridValue[0,x] =='x' and GridValue[1,x] =='x' and GridValue[2,x] =='x' or GridValue[0,x] =='o' and GridValue[1,x] =='o' and GridValue[2,x] =='o':
        
            print("Game Over!")
            return ActiveGame==False
        if GridValue[0,0] =='x' and GridValue[1,1] =='x' and GridValue[2,2] =='x' or GridValue[0,0] =='o' and GridValue[1,1] =='o' and GridValue[2,2] =='o':
        
            print("Game Over!")
            return ActiveGame==False
        if GridValue[0,2] =='x' and GridValue[1,1] =='x' and GridValue[2,2] =='x' or GridValue[0,2] =='o' and GridValue[1,1] =='o' and GridValue[2,0] =='o':
        
            print("Game Over!")
            return ActiveGame==False
        x=x+1
        
  
    else:
       return ActiveGame==True

    
        


#def updateBoard(GridValue):
    
    #GridValue.update({(0,0):teamSelect})
    #GridValue.update({(0,1):botTeam})
    #for item in GridValue:
     #   print("Key : {} , Value : {}".format(item,GridValue[item])) - Used to check that the dict is updating only 
  
 #  GenerateBoard(GridValue)
    

 #created a dictionary - list to say xy = ' ' or x o 
def CoordinatesGeneration():
    #generates the coordinates in x,y
    coordinates = []
    for x in range(3):
      for y in range(3):
        coordinates.append((x, y))
    #says put a value of nothing in for each coordinate
    coordinates= tuple(coordinates)
    #has to be a tuple as its umutable 
    

    ClearGridValue = dict(((x,y), ' ') for (x,y) in coordinates ) #fpr each item in the tuple with the key asign it the value of ' ' as a dict
    GridValue=dict()
    GridValue=ClearGridValue
    #print(GridValue) #REMOVE ONCE DONE 
    
    #for item in GridValue: #This is just to check on run rather than breakpoint the values of the dict 
     #   print("Key : {} , Value : {}".format(item,GridValue[item]))
    #print(GridValue)  #REMOVE ONCE DONE 
    
    GenerateBoard(GridValue)
    #updateBoard(GridValue)

    #def updateBoard(GridValue):
    
     #   GridValue.update({(0,0):teamSelect})
      #  GridValue.update({(0,1):botTeam})
       # for item in GridValue:
        #    print("Key : {} , Value : {}".format(item,GridValue[item]))
  
        #GenerateBoard(GridValue)
        


def CoordatesEntering(GridValue):
    
    EnteredCoordX=int(input("Enter Coordinates X for your turn:"))
    EnteredCoordy=int(input("Enter Coordinates Y for your turn:"))
    #EnteredCoordTest= tuple(int,int)
     
    EnteredCoord=(int(EnteredCoordX),int(EnteredCoordy))
    print (f"Your coordinates = {EnteredCoord}")
       
    #checks if the coordinate is in the generated ones and then updates the player value
   
    if EnteredCoord not in GridValue:
        print("This is not a valid move, please try values 0,0 through 2,2 again")
        CoordatesEntering(GridValue)
    if EnteredCoord in GridValue and GridValue[EnteredCoord] !=' ':
        print("This is an occupied tile, please try again")
        CoordatesEntering(GridValue)
    if EnteredCoord in GridValue                                  and GridValue[EnteredCoord] ==' ':
        GridValue.update({EnteredCoord:teamSelect})
        
        #goes gens a random number for the thing which is valid and update the bot 
        EnteredCoordAI=GenerateAIPos(GridValue)
        GridValue.update({EnteredCoordAI:botTeam})
        
        GenerateBoard(GridValue)    
        
def GenerateAIPos(GridValue):
    
    EnteredCoordx=random.randint(0,2)
    EnteredCoordy=random.randint(0,2)
    EnteredCoordAI=EnteredCoordx,EnteredCoordy
    if GridValue[EnteredCoordAI] !=' ':
        
        print(f"AI BAD NUMBER{EnteredCoordAI}")
        GenerateAIPos(GridValue)
    if GridValue[EnteredCoordAI]==' ':
        print(f"AI: {EnteredCoordAI}")

        return EnteredCoordAI

            
        
GameMananger()