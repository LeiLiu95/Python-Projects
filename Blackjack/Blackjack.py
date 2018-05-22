#  File: Blackjack.py
#  Description: plays a single game of blackjack
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 2/13/17
#  Date Last Modified: 2/24/17
import random

#create list for suits and numbers
suits=["C", "D", "H", "S"]
ranks=["2","3","4","5","6","7","8","9","10","J","Q","K","A"]    

class Card():   #class card 
    def __init__(self, Suit, Rank): #on initialization, the card will get a suit, rank, and a value that is used for calculating the total of a card
        self.Suit=Suit
        self.Rank=Rank
        if(Rank=="J" or Rank=="Q" or Rank=="K"):    #if the card is a face card, the value will be 10
            self.Value=10
        elif(Rank=="A"):        #if card is ace start off value with 11
            self.Value=11
        else:                   #else just store the value of the card number
            self.Value=int(Rank)

    def __str__(self):  #string function that returns the rank and suit of the card
        return str(self.Rank)+str(self.Suit)
    
    def __len__(self):  #len length returns the length of rank and suit of card
        return len(self.Suit) + len(self.Rank)
    
class Deck():   #class deck
    cardList=[] #deck has a list to contain all of the cards
    def __init__(self):     #initialization, iterates through all 4 suits and 13 ranks to generate a deck
        for i in suits:
            for j in ranks:
                self.cardList.append(Card(i,j)) #adds the card to the list
                
    def shuffle(self):  #shuffle function
        random.shuffle(self.cardList)   #shuffles the list of cards
        
    def dealOne(self, other):   #deal one removes the first card of the list and deals it to the player or dealer
        card=self.cardList.pop(0)
        other.hand.append(card)
        return
    
    def __str__(self):  #if the deck is called to be printed on a screen then all of the cards in the deck will be printed
        for i in range(0,4):
            for j in range(0,13):
                if(i*13+j<len(self.cardList)):
                    if(len(self.cardList[i*13+j])<3):
                        print("  " + str(self.cardList[i*13+j]), end="")
                    else:
                        print(" " + str(self.cardList[i*13+j]), end="")
            print()
        return ""

class Player(): #player class
    def __init__(self): #initializes the player with a list for their hand and total of their hand
        self.hand=[]
        self.handTotal=0
    def __str__(self):  #str function that returns the players hand
        for i in range (0,len(self.hand)):
            print(self.hand[i],end = "  ")
        return ""
    
def showHands(opponent, dealer):    #function that shows the dealt card of the opponent and dealer
    print()
    print("Dealer shows " + str(dealer.hand[1])+ " faceup")
    print("You show " + str(opponent.hand[1])+ " faceup")
    print()

def print_Hand(self):   #print hand iterates through to print out the players hand
    for i in range (0,len(self.hand)):
        print(self.hand[i],end=" ")
    return

def print_Hand2(self):  #prints hand except with a differrent format
    for i in range (0,len(self.hand)):
        print(self.hand[i],end="  ")
    return
        
def contain11(self):    #a function that checks if the player has an ace with the value 11 still used
    for i in range(0,len(self.hand)):
        if(self.hand[i].Value==11):
            return True
    return False

def containAce(self):   #function used to change the value of an ace from 11 to 1
    for i in range(0,len(self.hand)):
        if(self.hand[i].Value==11):
            self.hand[i].Value=1
            return
    return

def calc_Total(self):   #calculates the total of the user's hand
    total=0
    for i in range (0, len(self.hand)):
        total+=self.hand[i].Value
    return total

def opponentTurn(cardDeck, dealer, opponent): #function that iterates through players turn
    print("You go first.")  #initialization for player turn
    print()
    playing=True
    while(playing==True):   #keeps looping until player hits 21, busts, or stays
        if(contain11(opponent)):    #checks if player has an ace at value 11
            if(calc_Total(opponent)>21):  #if player is over 21 then check if he has 2 aces
                if(contain11(opponent)):
                    containAce(opponent)
                    print("Over 21. switching an ace from 11 points to 1.")
                    total=calc_Total(dealer)
                    print("New total: " + str(total))
                    print()
            print("Assuming " + str(opponent.hand[1].Value) + " points for an ace you were dealt for now.")
        total=calc_Total(opponent)  #check player total
            
        print("You hold ",end="")   #check total of player's hand
        print_Hand(opponent)
        print(" for a total of " + str(total))
        if(calc_Total(opponent)==21):
            print("21! My turn. . .")
            print()
            return
        next=int(input("1 (hit) or 2 (stay)? "))    #check if the user wants to hit or stay
        
        if(next==1):    #if he hits then deal player a card
            print()     
            cardDeck.dealOne(opponent)  #deal a card to player
            print("Card dealt: " + str(opponent.hand[len(opponent.hand)-1]))    #print the dealt card
            total+=opponent.hand[len(opponent.hand)-1].Value    #check total and see if player busts
            if(total>21):
                if(contain11(opponent)):    #if player busts with an ace then check to reduce ace value
                    containAce(opponent)
                    print("Over 21. switching an ace from 11 points to 1.")
                    total=calc_Total(opponent)  #check total again and show to player
                    print("New total: " + str(total))
                print()
            if(calc_Total(opponent)>21):    #if player is over 21 then player busts
                print("Opponent has " + str(calc_Total(opponent)) + ".  Opponent busts!  Dealer win.")
                playing=False
            if(calc_Total(opponent)==21):   #if player hit 21 then go to dealers turn
                print("21!  My turn. . .")
                playing=False
        if(next==2):    #if player stays then go to dealers turn
            print("Staying with " + str(calc_Total(opponent)))
            print()
            playing=False

def dealerTurn(cardDeck,dealer,opponent):
    print("Dealer's turn")  #initialization for dealers turn

    print("Your hand:  ", end="")
    print_Hand2(opponent)
    print("  for a total of " + str(calc_Total(opponent)))
    print("Dealer's hand:  ", end="")
    print_Hand2(dealer)
    print("  for a total of " + str(calc_Total(dealer)))
    print()

    if(calc_Total(opponent)>21):    #if player busts then dealer wins automatically
        print("Dealer has " + str(calc_Total(dealer)) + ". Dealer's hand did not bust, Dealer wins!")
        print()
        return
    if(calc_Total(dealer)>21):  #if dealer is over 21 then check if he has 2 aces
        if(contain11(dealer)):  #switches the other ace value to a 1
                containAce(dealer)
                print("Over 21. switching an ace from 11 points to 1.")
                total=calc_Total(dealer)
                print("New total: " + str(total))
                print()
    index=2
    if(calc_Total(dealer)<calc_Total(opponent)):
        while(calc_Total(dealer)<calc_Total(opponent)): #dealer must play until bust or beats opponent
            if(contain11(dealer)):  #formating
                print("Assuming 11 points for an ace I was dealt for now.")
            cardDeck.dealOne(dealer)    #deal a card to dealer
            print("Dealer hits:  " + str(dealer.hand[index]))
            print("New total: " + str(calc_Total(dealer)))
            print()
            index+=1
            if(calc_Total(dealer)>21):  #check if dealer busts
                if(contain11(dealer)):  #check if dealer has an ace then reduce ace value
                    containAce(dealer)
                    print("Over 21. switching an ace from 11 points to 1.")
                    total=calc_Total(dealer)
                    print("New total: " + str(total))
                    print()
                else:   #if no ace then dealer loses
                    print("Dealer has " + str(calc_Total(dealer)) + ". Dealer busts!  You win.")
                    print()
                    return
            if(calc_Total(dealer)>calc_Total(opponent)):    #if dealer does not bust and beats opponent then dealer wins
                print("Dealer has " + str(calc_Total(dealer)) + ".  Dealer's hand is greater than your hand " + str(calc_Total(opponent)) + "!  You lose.")
                print()
                return
            if(calc_Total(dealer)==calc_Total(opponent)):   #if dealer is equal to opponent and does not bust then dealer wins
                print("Dealer has " + str(calc_Total(dealer)) + ".  Dealer's hand is equal your hand " + str(calc_Total(opponent)) + "!  You lose.")
                print()
                return
    else:
        if(calc_Total(dealer)>calc_Total(opponent)):    #if dealer does not bust and beats opponent then dealer wins
            print("Dealer has " + str(calc_Total(dealer)) + ".  Dealer's hand is greater than your hand " + str(calc_Total(opponent)) + "!  You lose.")
            print()
            return
        if(calc_Total(dealer)==calc_Total(opponent)):   #if dealer is equal to opponent and does not bust then dealer wins
            print("Dealer has " + str(calc_Total(dealer)) + ".  Dealer's hand is equal your hand " + str(calc_Total(opponent)) + "!  You lose.")
            print()
            return
        
def main():
    cardDeck = Deck()               # create a deck of 52 cards called "cardDeck"
    print("Initial deck:")
    print(cardDeck)                 # print the deck so we can see that you built it correctly
    
    random.seed(50)                 # leave this in for grading purposes
    cardDeck.shuffle()              # shuffle the deck
    print("Shuffled deck:")
    print(cardDeck)                 # print the deck so we can see that your shuffle worked
    
    dealer = Player()               # create the player:  you play for this Player
    opponent = Player()             # create the dealer:  the computer plays for this Player
    
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face down (the "hole" card)
    cardDeck.dealOne(opponent)      # face up
    cardDeck.dealOne(dealer)        # face up

    print("Deck after dealing two cards each:")
    print(cardDeck)
    
    showHands(opponent,dealer)      # remember not to show face down cards
    
    opponentTurn(cardDeck,dealer,opponent)     # this is where half of the hard stuff is done
    dealerTurn(cardDeck,dealer,opponent)       # this is where the other half of the hard stuff is done
    
    print ("Game over.")
    print ("Final hands:")
    print ("   Dealer:   ", dealer)
    print ("   Opponent: ", opponent)
    
main()
