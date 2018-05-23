#  File: RPG.py
#  Description: RPG Game
#  Student's Name: Lei Liu
#  Student's UT EID: LL28379
#  Course Name: CS 313E 
#  Unique Number: 51915
#
#  Date Created: 2/5/17
#  Date Last Modified: 2/10/17
class Weapon:                   #Weapon class that includes the name and damage of the weapon
    weapon="none"
    damage=1
    def __init__(self,weapon):  #checks to see what weapon is being created
        self.weapon=weapon
        if (weapon=="dagger"):
            self.damage=4
        elif (weapon=="axe" or weapon=="staff"):
            self.damage=6
        elif(weapon=="sword"):
            self.damage=10
        else:
            self.weapon="none"
            self.damage=1
        
class Armor:                    #Armor class that includes the name and armor points of the armor
    armor="none"
    armor_Class=10
    def __init__(self,armor):   #checks to see what armor is being created
        if(armor=="leather"):
            self.armor=armor
            self.armor_Class=8
        elif(armor=="chain"):
            self.armor=armor
            self.armor_Class=5
        elif(armor=="plate"):
            self.armor=armor
            self.armor_Class=2
        else:
            self.armor="none"
            self.armor_Class=10
        return
    
def checkForDefeat(self):   #function that checks if the character is defeated or not
    if(self.health<=0):
        self.defeated=True
    return

class RPGCharacter:         #class of the character that has all the main functions
    def __init__(self,name):
        self.name=name
        
    def wield(self, weapon):    #function that equips a weapon to a character
        if(self.equip==False):  #wizards can only equip daggers and staffs
            if(weapon=="sword" or weapon=="axe"):
                print("Weapon not allowed for this character class")
                return
            else:
                self.weapon=weapon
                print(self.name + " is now wielding a(n) " + self.weapon.weapon)
        else:                   #else equip the weapon to character
            self.weapon=weapon
            print(self.name + " is now wielding a(n) " + self.weapon.weapon)
        return
    
    def unwield(self):          #removes the weapon of the character
        self.weapon=Weapon("none")
        print(self.name + " is no longer wielding anything")

    def putOnArmor(self,armor): #function that equips a armor
        if(self.equip==False):  #wizards cannot equip armor while warriors can
            print("Armor not allowed for this character class")
        else:
            self.armor=armor
            print(self.name + " is now wearing " + self.armor.armor)
            
    def takeOffArmor(self): #removes armor from character
        self.armor=Armor("none")
        print(self.name + " is no longer wearing anything")

    def fight(self, other): #fight fuction
        print(self.name + " attacks " + other.name + " with a(n) " + self.weapon.weapon)        #prints what happens and then calculates damage and health
        other.health-=self.weapon.damage
        print(self.name + " does " + str(self.weapon.damage) + " damage to " + other.name)
        print(other.name + " is now down to " + str(other.health) + " health")
        checkForDefeat(other)       #checks to see if the character is defeated or not
        if(other.defeated==True):
            print(other.name + " has been defeated!")
        return
    
    def show(self): #function that shows the current status of the character
        print()
        print(" " + self.name)
        print("   Current Health: " + str(self.health))
        print("   Current Spell Points: " + str(self.spell_P))
        print("   Wielding: " + self.weapon.weapon)
        print("   Wearing: " + self.armor.armor)
        print("   Armor class: " + str(self.armor.armor_Class))
        print()

class Fighter(RPGCharacter):    #subclass of character and is a fighter
    def __init__(self,name):    #constructor for fighter class
        self.name=name
        self.health=40
        self.spell_P=0
        self.weapon=Weapon("none")
        self.armor=Armor("none")
        self.equip=True
        self.defeated=False
        
class Wizard(RPGCharacter):     #subclass of character and is a wizard
    def __init__(self,name):    #constructor class of wizard
        self.name=name
        self.health=16
        self.spell_P=20
        self.weapon=Weapon("none")
        self.armor=Armor("none")
        self.equip=False
        self.defeated=False

    def castSpell(self, spell, other):      #wizard gets to cast spells while a fighter can not
        if(spell=="Fireball" or spell=="Lightning Bolt" or spell=="Heal"):
            if(spell=="Fireball"):      #checks what spell the character has casted
                if(self.spell_P<3):     #if they have enough spell points then process the spell
                    print("Insufficient spell points")
                    return
                else:
                    self.spell_P-=3
                    other.health-=5
                    print(self.name + " casts " + spell + " at " + other.name)
                    print(self.name + " does 5 damage to " + other.name)
                    print(other.name + " is now down to " + str(other.health) + " health")
                    checkForDefeat(other)
                    if(other.defeated==True):
                            print(other.name + " has been defeated!")
                    return
            elif(spell=="Lightning Bolt"):
                if(self.spell_P<10):
                    print("Insufficient spell points")
                    return
                else:
                    self.spell_P-=10
                    other.health-=10
                    print(self.name + " casts " + spell + " at " + other.name)
                    print(self.name + " does 10 damage to " + other.name)
                    print(other.name + " is now down to " + str(other.health) + " health")
                    checkForDefeat(other)
                    if(other.defeated==True):
                            print(other.name + " has been defeated!")
                    return
            else:       #heal spell that heals the targeted character
                if(self.spell_P<6):
                    print("Insufficient spell points")
                    return
                else:
                    self.spell_P-=6
                    other.health+=6
                    print(self.name + " casts " + spell + " at " + other.name)
                    print(self.name + " heals " + other.name + " for 6 health points.")
                    print(self.name + " is now at " + str(other.health) + " health")
                    return
        else:
            print("Unknown spell name. Spell failed.")
            return
        
def main():
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)
    
    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)
    
    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Fireball",aragorn)
    aragorn.fight(gandalf)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Lightning Bolt",aragorn)
    aragorn.wield(sword)

    gandalf.show()
    aragorn.show()

    gandalf.castSpell("Heal",gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)

    gandalf.show()
    aragorn.show()
main()
