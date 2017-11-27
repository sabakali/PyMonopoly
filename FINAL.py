# Shaheer Bakali
# 15-112 Project
# PyMonopoly

import pygame
import random

global proplist
proplist = []

global rallist
raillist = []

global utilist
utilist = []

global money
money = 1500

position = 0

global currentPlayer
currentPlayer = 0



def Property(name,color,whattype,owner,cost,rent,mortgage,housecost,hotelcost,houses,h1,h2,h3,h4,h5):
    
    return [name,cost,whattype,owner,rent]


def Railroad(name,owner,whattype,cost,rent):

    return [name,cost,whattype,owner,rent]

def Utilities(name,owner,whattype,cost,rent):
    
    return [name,cost,whattype,owner,rent]
    

def CommunityChest(name,something=None,andsomething=None,alsosomething=None,stuff=None):
    return [name,something,andsomething,alsosomething,stuff]

def Chance(name,something=None,andsomething=None,alsosomething=None,stuff=None):
    return [name,something,andsomething,alsosomething,stuff]


def Tax(name,whattype,tax):
    return [name,whattype,tax]

def FreeBlock(name,something=None,andsomething=None,alsosomething=None,stuff=None):
    return [name,something,andsomething,alsosomething,stuff]


def CommunityChestCard(description,move,collect,pay,payperhouse,getoutofjailfree,gotojail,collect50):
    return description

def ChanceCard(description,move,collect,pay,payperhouse,getoutofjailfree,gotojail,moveback):
    return description


def Board():
    
    global PropertyList #list containing all properties on the board
    global cclist #list containing all community chest cards
    global chancelist #list containing all chance cards

    PropertyList = [] #first initialize this list 

    fb1 = FreeBlock('GO!')
    PropertyList.append(fb1)
    
    ma = Property('Mediterranean Avenue','brown','Property','bank',60,2,50,50,30,0,10,30,90,160,250)
    PropertyList.append(ma)
    
    cc1 = CommunityChest('Community Chest')
    PropertyList.append(cc1)
    
    ba = Property('Baltic Avenue','brown','Property','bank',60,4,30,50,50,0,20,60,180,320,450)
    PropertyList.append(ba)

    it1 = Tax('Income Tax','Tax',200)
    PropertyList.append(it1)

    rr = Railroad('Reading Railroad','bank','Railroad',200,25)
    PropertyList.append(rr)
    
    oa = Property('Oriental Avenue','light blue','Property','bank',100,6,50,50,50,0,30,90,270,400,550)
    PropertyList.append(oa)

    c1 = Chance('Chance')
    PropertyList.append(c1)

    va = Property('Vermont Avenue','light blue','Property','bank',100,6,50,50,50,0,30,90,270,400,550)
    PropertyList.append(va)

    ca = Property('Connecticut Avenue','Property','light blue','bank',120,8,60,50,50,0,40,100,300,450,600)
    PropertyList.append(ca)

    fb2 = FreeBlock('Just Visiting Jail')
    PropertyList.append(fb2)

    scp = Property('St. Charles Place','pink','Property','bank',140,10,70,100,100,0,50,150,450,625,750)
    PropertyList.append(scp)

    ec = Utilities('Electric Company','bank','Utility',150,0)
    PropertyList.append(ec)

    sa = Property('States Avenue','pink','Property','bank',140,10,70,100,100,0,50,150,450,625,750)
    PropertyList.append(sa)

    va1 = Property('Virginia Avenue','pink','Property','bank',160,12,80,100,100,0,60,180,500,700,900)
    PropertyList.append(va1)

    pr = Railroad('Pennsylvania Railroad','bank','Railroad',200,25)
    PropertyList.append(pr)

    sjp = Property('St. James Place','orange','Property','bank',180,14,90,100,100,0,70,200,550,750,950)
    PropertyList.append(sjp)

    cc2 = CommunityChest('Community Chest')
    PropertyList.append(cc2)

    ta = Property('Tennessee Avenue','orange','Property','bank',180,14,90,100,100,0,70,200,550,750,950)
    PropertyList.append(ta)

    nya = Property('New York Avenue','orange','Property','bank',200,16,100,100,100,0,80,220,600,800,100)
    PropertyList.append(nya)

    fb3 = FreeBlock('Free Parking')
    PropertyList.append(fb3)
    
    ka = Property('Kentucky Avenue','red','Property','bank',220,18,110,150,150,0,90,250,700,875,1050)
    PropertyList.append(ka)

    c2 = Chance('Chance')
    PropertyList.append(c2)

    ia = Property('Indiana Avenue','red','Property','bank',220,18,110,150,150,0,90,250,700,875,1050)
    PropertyList.append(ia)

    ia1 = Property('Illinois Avenue','red','Property','bank',240,20,120,150,150,0,100,300,750,925,1100)
    PropertyList.append(ia1)

    bando = Railroad('B&O Railroad','bank','Railroad',200,25)
    PropertyList.append(bando)

    aa = Property('Atlantic Avenue','yellow','Property','bank',260,22,130,150,150,0,110,330,800,975,1150)
    PropertyList.append(aa)

    va2 = Property('Ventnor Avenue','yellow','Property','bank',260,22,130,150,150,0,110,330,800,975,1150)
    PropertyList.append(va2)

    ww = Utilities('Water Works','bank','Utility',150,0)
    PropertyList.append(ww)

    mg = Property('Marvin Gardens','yellow','Property','bank',280,24,140,150,150,0,120,360,850,1025,1200)
    PropertyList.append(mg)

    fb4 = FreeBlock('Go To Jail')
    PropertyList.append(fb4)

    pa = Property('Pacific Avenue','green','Property','bank',300,26,150,200,200,0,130,390,900,1100,1275)
    PropertyList.append(pa)

    nca = Property('North Carolina Avenue','green','Property','bank',300,26,150,200,200,0,130,390,900,1100,1275)
    PropertyList.append(nca)

    cc3 = CommunityChest('Community Chest')
    PropertyList.append(cc3)

    pa1 = Property('Pennsylvania Avenue','green','Property','bank',320,28,160,200,200,0,150,450,1000,1200,1400)
    PropertyList.append(pa1)
    
    sl = Railroad('Short Line','bank','Railroad',200,25)
    PropertyList.append(sl)

    c3 = Chance('Chance')
    PropertyList.append(c3)

    pp = Property('Park Place','dark blue','Property','bank',350,35,175,200,200,0,175,500,1100,1300,1500)
    PropertyList.append(pp)

    lt = Tax('Luxury Tax','Tax',100)
    PropertyList.append(lt)

    b = Property('Boardwalk','dark blue','Property','bank',400,50,200,200,200,0,200,600,1400,1700,2000)
    PropertyList.append(b)

    cclist = [] #first initialize this list

    ccdesc1 = "GRAND OPERA OPENING. COLLECT $50 FROM EVERY PLAYER"
    cc1 = CommunityChestCard(ccdesc1,0,0,0,0,0,0,50)
    cclist.append(cc1)
    
    ccdesc2 = "RECEIVE FOR SERVICES $25"
    cc2 = CommunityChestCard(ccdesc2,0,10,0,0,0,0,0)
    cclist.append(cc2)
   
    ccdesc3 = "ADVANCE TO GO (COLLECT $200) "
    cc3 = CommunityChestCard(ccdesc3,1,0,0,0,0,0,0)
    cclist.append(cc3)
  
    ccdesc4 = "PAY HOSPITAL $100 "
    cc4 = CommunityChestCard(ccdesc3,0,0,100,0,0,0,0)
    cclist.append(cc4)
    
    ccdesc5 = "DOCTOR'S FEE. PAY $50 "
    cc5 = CommunityChestCard(ccdesc5,0,0,50,0,0,0,0)
    cclist.append(cc5)
  
    ccdesc6 = "GET OUT OF JAIL FREE CARD"
    cc6 = CommunityChestCard(ccdesc6,0,0,0,0,1,0,0)
    cclist.append(cc6)
    
    ccdesc7 = "FROM SALE OF STOCK YOU GET $45"
    cc7 = CommunityChestCard(ccdesc7,0,45,0,0,0,0,0)
    cclist.append(cc7)
 
    ccdesc8 = "YOU INHERIT $100"
    cc8 = CommunityChestCard(ccdesc8,0,100,0,0,0,0,0)
    cclist.append(cc8)
  
    ccdesc9 = "GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT $200"
    cc9 = CommunityChestCard(ccdesc9,0,0,0,0,0,1,0)
    cclist.append(cc9)
    
    ccdesc10 = "LIFE INSURANCE MATURES. COLLECT $100"
    cc10 = CommunityChestCard(ccdesc10,0,100,0,0,0,0,0)
    cclist.append(cc10)
 
    ccdesc11 = "YOU HAVE WON SECOND PRIZE IN A BEAUTY CONTEST. COLLECT $10"
    cc11 = CommunityChestCard(ccdesc11,0,10,0,0,0,0,0)
    cclist.append(cc11)
  
    ccdesc12 = "XMAS FUND MATURES. COLLECT $100"
    cc12 = CommunityChestCard(ccdesc12,0,100,0,0,0,0,0)
    cclist.append(cc12)

    ccdesc13 = "YOU ARE ASSESSED FOR STREET REPAIRS. $40 PER HOUSE."
    cc13 = CommunityChestCard(ccdesc13,0,0,0,40,0,0,0)
    cclist.append(cc13)
    
    ccdesc14 = "BANK ERROR IN YOUR FAVOR. COLLECT $200"
    cc14 = CommunityChestCard(ccdesc14,0,200,0,0,0,0,0)
    cclist.append(cc14)
    
    ccdesc15 = "INCOME TAX REFUND. COLLECT $20"
    cc15 = CommunityChestCard(ccdesc15,0,20,0,0,0,0,0)
    cclist.append(cc15)
    

    chancelist = [] #first initialize this list

    cdesc1 = "ADVANCE TO ILLINOIS AVE. IF YOU PASS GO, COLLECT $200.00"
    c1 = ChanceCard(cdesc1,25,0,0,0,0,0,0)
    chancelist.append(c1)
    
    cdesc2 = "YOU ARE ASSESSED FOR STREET REPAIRS. $40.00 PER HOUSE."
    c2 = ChanceCard(cdesc2,0,0,0,40,0,0,0)
    chancelist.append(c2)
    
    cdesc3 = "GET OUT OF JAIL FREE CARD"
    c3 = ChanceCard(cdesc3,0,0,0,0,1,0,0)
    chancelist.append(c3)
    
    cdesc4 = "ADVANCE TO GO."
    c4 = ChanceCard(cdesc4,1,0,0,0,0,0,0)
    chancelist.append(c4)
    
    cdesc5 = "ADVANCE TO ST.CHARLES PLACE. IF YOU PASS GO, COLLECT $200.00"
    c5 = ChanceCard(cdesc5,12,0,0,0,0,0,0)
    chancelist.append(c5)
    
    cdesc6 = "PARKING FINE $15.00"
    c6 = ChanceCard(cdesc6,0,0,15,0,0,0,0)
    chancelist.append(c6)
    
    cdesc7 = "BANK PAYS YOU DIVIDEND OF $50.00"
    c7 = ChanceCard(cdesc7,0,50,0,0,0,0,0)
    chancelist.append(c7)
    
    cdesc8 = "YOUR XMAS FUND MATURES. COLLECT $100.00"
    c8 = ChanceCard(cdesc8,0,100,0,0,0,0,0)
    chancelist.append(c8)
    
    cdesc9 = "TAKE A WALK ON THE BOARDWALK"
    c9 = ChanceCard(cdesc9,40,0,0,0,0,0,0)
    chancelist.append(c9)
    
    cdesc10 = "PAY POOR TAX OF $12.00"
    c10 = ChanceCard(cdesc10,0,0,12,0,0,0,0)
    chancelist.append(c10)
    
    cdesc11 = "TAKE A RIDE ON THE READING. ADVANCE TOKEN AND IF YOU PASS GO COLLECT $200.00"
    c11 = ChanceCard(cdesc11,6,0,0,0,0,0,0)
    chancelist.append(c11)
    
    cdesc12 = "GO BACK THREE SPACES"
    c12 = ChanceCard(cdesc12,0,0,0,0,0,0,3)
    chancelist.append(c12)
    
    cdesc13 = "YOUR BUILDING AND LOAN MATURES - RECIEVE $150.00"
    c13 = ChanceCard(cdesc13,0,150,0,0,0,0,0)
    chancelist.append(c13)
    
    cdesc14 = "MAKE GENERAL REPAIRS ON ALL OF YOUR HOUSES. FOR EACH HOUSE PAY $25.00"
    c14 = ChanceCard(cdesc14,0,0,0,25,0,0,0)
    chancelist.append(c14)
    
    cdesc15 = "GO TO JAIL. GO DIRECTLY TO JAIL. DO NOT PASS GO. DO NOT COLLECT $200.00"
    c15 = ChanceCard(cdesc15,0,0,0,0,0,1,0)
    chancelist.append(c15)



    return PropertyList
    return cclist
    return chancelist

    
Board()

def Taxblock(tb): #function defined if player lands on a Tax block

    global currentPlayer
    global biglist

    if PropertyList[position][1] == 'Tax': #if player lands on Tax block
        
        if biglist[currentPlayer][0] > 0: #money should be greater than 0
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - PropertyList[position][2] #deduct money and pay tax
            print 'You have to pay Tax of '+str(PropertyList[position][2])
            print 'Player '+str(currentPlayer)+"'s "+'Money : $',biglist[currentPlayer][0]
        else:
            print 'You do not have enough money !'


def addProperty(newProperty): #function defined if player wants to buy a property

    global position
    global currentPlayer
    global biglist

    if PropertyList[position][2] == 'Property': #if player lands on Property
        
        checkifbuy = raw_input('Do you want to buy '+PropertyList[position][0]+' for $'+str(PropertyList[position][1])+' ?') #ask player if they want to buy this property
        if checkifbuy == 'Yes': #if they say yes

            
            if biglist[currentPlayer][0] > 0: #money should be greater than 0
                biglist[currentPlayer][0] = biglist[currentPlayer][0] - PropertyList[position][1] #deduct money and pay to buy this property
                print 'Player '+str(currentPlayer)+"'s "+'Money : $',biglist[currentPlayer][0]
            else:
                print 'You do not have enough money !'

            global proplist
            biglist[currentPlayer][2].append(PropertyList[position][0]) #append this recently bought property to proplist

            print 'Player '+str(currentPlayer)+"'s "+'Property List : ',biglist[currentPlayer][2]
            
        elif checkifbuy == 'No':
            print 'Player '+str(currentPlayer)+"'s "+'Property List : ',biglist[currentPlayer][2]
        

    

def addRailroad(newRailroad): #function defined if player wants to buy a railroad

    global position
    global currentPlayer
    global biglist

    if PropertyList[position][2] == 'Railroad': #if player lands on Railroad
       
        checkifbuy = raw_input('Do you want to buy '+PropertyList[position][0]+' for $'+str(PropertyList[position][1])+' ?') #ask player if they want to buy this railroad
        if checkifbuy == 'Yes': #if they say yes
            
            

            global money
            if biglist[currentPlayer][0] > 0: #money should be greater than 0
                biglist[currentPlayer][0] = biglist[currentPlayer][0] - PropertyList[position][1] #deduct money and pay to buy this railroad
                print 'Player '+str(currentPlayer)+"'s "+'Money : $',biglist[currentPlayer][0]
            else:
                print 'You do not have enough money !'
                
            global raillist
            biglist[currentPlayer][3].append(PropertyList[position][0]) #append this recently bought railroad to raillist

            print 'Player '+str(currentPlayer)+"'s "+'Railroad List : ',biglist[currentPlayer][3]
        elif checkifbuy == 'No':
            print 'Player '+str(currentPlayer)+"'s "+'Railroad List : ',biglist[currentPlayer][3]
        

    

def addUtility(newUtility): #function defined if player wants to buy a utility

    global position
    global currentPlayer
    global biglist

    if PropertyList[position][2] == 'Utility': #if player lands on Utility
        
        checkifbuy = raw_input('Do you want to buy '+PropertyList[position][0]+' for $'+str(PropertyList[position][1])+' ?') #ask player if they want to buy this utility
        if checkifbuy == 'Yes': #if they say yes
        
            

            global money
            if biglist[currentPlayer][0] > 0: #money should be greater than 0
                biglist[currentPlayer][0] = biglist[currentPlayer][0] - PropertyList[position][1] #deduct money and pay to buy this utility
                print 'Player '+str(currentPlayer)+"'s "+'Money : $',biglist[currentPlayer][0]
            else:
                print 'You do not have enough money !'

            global utilist
            biglist[currentPlayer][4].append(PropertyList[position][0])
            #append this recently bought utility to utilist

            print 'Player '+str(currentPlayer)+"'s "+'Utility List : ',biglist[currentPlayer][4]
        if checkifbuy == 'No':
            print 'Player '+str(currentPlayer)+"'s "+'Utility List : ',biglist[currentPlayer][4]

            

def LandingonCC(cc): #function defined if players lands on community chest

    global position
    global money
    global cclist
    global currentPlayer
    global biglist

    if PropertyList[position] == 'Community Chest': #if player lands on community chest
        randomcc = random.choice(cclist) #randomly select a card from community chest cards
        print randomcc #print it on screen

        if cclist.index(randomcc) == 0: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 50
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
            
        elif cclist.index(randomcc) == 1: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 25
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 2: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = 0
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[0]
            
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 200
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 3: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 100
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 4: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 50
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 5: #if the card is at this index, do whatever it says on the card
            jailcard = 1

        elif cclist.index(randomcc) == 6: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 45
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 7: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 100
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 8: #if the card is at this index, do whatever it says on the card
            print 'You are Gone to Jail !'

        elif cclist.index(randomcc) == 9: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 100
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 10: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 10
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 11: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 100
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 12: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 40
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 13: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 200
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif cclist.index(randomcc) == 14: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 20
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
            
            
def LandingonChance(c): #function defined if player lands on chance
    print 'yess'

    global pposition
    global money
    global currentPlayer
    global biglist

    if PropertyList[position] == 'Chance':
        randomcc = random.choice(chancelist) #randomly select a card from chance cards list
        print randomcc #print it on screen

        if chancelist.index(randomcc) == 0: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = 24
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[24]
            
        elif chancelist.index(randomcc) == 1: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 40
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0] 

        elif chancelist.index(randomcc) == 2: #if the card is at this index, do whatever it says on the card
            jailcard = 1

        elif chancelist.index(randomcc) == 3: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = 0
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[0]

        elif chancelist.index(randomcc) == 4: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = 11
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[11]

        elif chancelist.index(randomcc) == 5: #if the card is at this index, do whatever it says on the card 
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 15
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif chancelist.index(randomcc) == 6: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 50
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif chancelist.index(randomcc) == 7: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 100
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif chancelist.index(randomcc) == 8: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = 39
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[39]

        elif chancelist.index(randomcc) == 9: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 12
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif chancelist.index(randomcc) == 10: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = 5
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[5]

        elif chancelist.index(randomcc) == 11: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][1] = biglist[currentPlayer][1] - 3
            print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[position]

        elif chancelist.index(randomcc) == 12: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] + 150
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif chancelist.index(randomcc) == 13: #if the card is at this index, do whatever it says on the card
            
            biglist[currentPlayer][0] = biglist[currentPlayer][0] - 25
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

        elif chancelist.index(randomcc) == 14: #if the card is at this index, do whatever it says on the card
            print 'You are Gone to Jail !'


def updatePlayer():
    global currentPlayer 
##    print 'current player: ',currentPlayer
    print '                                                                              '
    global howmanyPlayers
     
    currentPlayer = (currentPlayer + 1) % int(howmanyPlayers) #update players after each turn
    print 'Player '+str(currentPlayer)+"'s Turn"

##    biglist[currentPlayer]

        
    
    
    
 

biglist =[]
money = 1500
def ActualGame(): #this function is for the actual game to run

    

    global howmanyPlayers
    global position 

    howmanyPlayers = raw_input('How Many Players are Playing?') #ask user how many players are playing
    global biglist
    global money
    biglist =[]
    for i in range(int(howmanyPlayers)):
        biglist.append([money,0,[],[],[]])
##    print 'over here:',biglist


    
    def Player(): #function defined to represent a player

        global biglist
        
        addProperty(PropertyList[position]) #call this function to buy a property on this position on board

        addRailroad(PropertyList[position]) #call this function to buy a railroad on this position on board
    
        addUtility(PropertyList[position]) #call this function to buy utility on this position on board

        LandingonCC(PropertyList[position]) #call this function when player lands on community chest on this position on board

        LandingonChance(PropertyList[position]) #call this function when players lands on chance on this position on board

        Taxblock(PropertyList[position]) #call this function when player lands on tax block on this position on board



##    print 'current player: ',currentPlayer

    
     #this is global because it is being used everywhere
    position = 0 #initialy the position is zero
    print 'Initial Position : ',PropertyList[0][0]

    print 'Player '+str(currentPlayer)+"'s"+' Initial Money : ',1500 #display players intial money1
    print '                             '


    Game = True
    while Game == True: #repeat until game ends
    
        dice1 = random.randint(1,6) #dice 1 being rolled
        print 'Dice1 : ',dice1 #print result on screen
        dice2 = random.randint(1,6) #dice 2 being rolled
        print 'Dice2 : ',dice2 #print result on screen

        total = dice1 + dice2 #add result of both dices 
        print 'Total : ',total #print the total of both dices on screen

        position = position + total #update position

        if position > 39: #if position is bigger than 39, because there are 40 blocks on monopoly
            position = position - 40 #update position
            money = money + 200
            print 'You Passed GO!, collect $200'
            print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',money

        print '                                                                          '    
        print 'Player '+str(currentPlayer)+"'s"+ ' Position : ',PropertyList[position][0] #print players position on board

        Player() #call player function

  
        if biglist[currentPlayer][0] <= 0: #check if money is positive
            print 'You do not have enough money ! You lost the Game!'
            Game = False #end game


        updatePlayer() #call this function to update player after each turn

##ActualGame()









###############################################################################
###############################################################################
###############################################################################

## NOTE : i learned pygame from youtube video series, link : https://www.youtube.com/watch?v=ujOTNg17LjI&t=3s





import pygame
import random


pygame.init() #FIRST THING TO DO ! initiate pygame


display_width = 1000
display_height = 800



bg = (220,235,216)
bg1 = (255, 153, 153)

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
gray = (201,189,189)
yellow = (255,255,0)


bright_yellow = (255,255,179)
block_color = (53,115,255)
bright_red = (255, 51, 51)
bright_green = (0,255,0)
bright_blue = (128, 128, 255)


light_green = (0, 204, 0)
vlight_green = (102, 255, 102)
light_red = (255,77,77)





#set up the window frame
gameDisplay = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)#set size of display

pygame.display.set_caption('PyMonopoly') #sets title of window



clock = pygame.time.Clock() #specific game clock


mrmonopolyImg = pygame.image.load('mrmonopoly.gif').convert()
backgroundImg = pygame.image.load('mbackground.jpg').convert()
welcomeImg = pygame.image.load('mwelcome.jpg')
boardImg = pygame.image.load('actualboardgame.jpg').convert()
diceImg = pygame.image.load('dice.png')
hdiceImg = pygame.image.load('hdice.png')
mrImg = pygame.image.load('mrmonopoly.gif')
backImg = pygame.image.load('back.jpg')







#function to draw stuff
def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])
    

#function to display an image
def displayImg(img,x,y): ## NOTE : i learned pygame from youtube video series, link : https://www.youtube.com/watch?v=ujOTNg17LjI&t=3s
    gameDisplay.blit(img,(x,y)) #draw the image on the surface


#set the coordinates
x = (display_width * 0.45)
y = (display_height * 0.8)



def text_objects(text, font): ## NOTE : i learned pygame from youtube video series, link : https://www.youtube.com/watch?v=ujOTNg17LjI&t=3s
    textSurface = font.render(text, True, black) #render : draw text on surface
    return textSurface, textSurface.get_rect() #get_rect() : get the rectangular area of the surface


def message_display(text): ## NOTE : i learned pygame from youtube video series, link : https://www.youtube.com/watch?v=ujOTNg17LjI&t=3s
    largeText = pygame.font.Font('freesansbold.ttf',115) #choose font and size
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()




def box(x,y,w,h,ic,ac,action=None):

    #get mouse position
    mouse = pygame.mouse.get_pos()
##    print 'mouse pos: ',mouse


    #click definition
    click = pygame.mouse.get_pressed() #event pressed by mouse
##    print click 


    #make button interactive here
    #check if x and width is in between the box button
    #check if y and height is in between the box button
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h),3) #draw rectangle of active color of mouse is over the position


        #buttion functions
        if click[0] == 1 and action != None:
            action()
            
            
##            if action == 'play':
##                Gameloopfortwo()
##            elif action == 'quit':
##                pygame.quit()
##                quit()
            

    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h),3) #draw rectangle of inactive color of mouse is over the position





def button(mssg,x,y,w,h,ic,ac,textSize,action=None):
    
    #get mouse position
    mouse = pygame.mouse.get_pos()
##    print 'mouse pos: ',mouse


    #click definition
    click = pygame.mouse.get_pressed() #event pressed by mouse
##    print click 


    #make button interactive here
    #check if x and width is in between the box button
    #check if y and height is in between the box button
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay,ac,(x,y,w,h)) #draw rectangle of active color of mouse is over the position


        #buttion functions
        if click[0] == 1 and action != None:
            action()
            
            
##            if action == 'play':
##                Gameloopfortwo()
##            elif action == 'quit':
##                pygame.quit()
##                quit()
            

    else:
        pygame.draw.rect(gameDisplay,ic,(x,y,w,h)) #draw rectangle of inactive color of mouse is over the position



    #text on button
    smallText = pygame.font.Font('freesansbold.ttf',textSize)
    textSurf,textRect = text_objects(mssg,smallText)
    #centre the text
    textRect.center = (((x+(w/2)),(y+(h/2))))
    gameDisplay.blit(textSurf,textRect)

    

##global currentPlayer
##currentPlayer = 0













#quit game function
def quitGame():
    pygame.quit()
    quit()




def Gameintro():
    intro = True

    while intro:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
    
        gameDisplay.fill(white)
        displayImg(backgroundImg,0,0)
        largeText = pygame.font.Font('freesansbold.ttf',50)
        TextSurf,TextRect = text_objects('Welcome to PyMonopoly',largeText)
        TextRect.center = ((display_width/3),(display_height/15))
        gameDisplay.blit(TextSurf,TextRect)




        #call button function
        button('Start!',0,100,170,50,bg,bright_green,20,mainmenu)
        button('Quit PyMonopoly',0,200,174,50,bg,red,20,quitGame)


        pygame.display.update()
        clock.tick(6)
        



def mainmenu():    
    main = True

    while main:
        for event in pygame.event.get():
##            print event
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
    
        gameDisplay.fill(white)

        displayImg(backImg,0,152)
        
        displayImg(welcomeImg,300,0)
        
        someText = pygame.font.Font('freesansbold.ttf',50)
        textsurf,textrect = text_objects('Main Menu',someText)
        textrect.center = (500,180)
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',30)
        textsurf,textrect = text_objects('Choose one of the Game Modes :',someText)
        textrect.center = (242,250)
        gameDisplay.blit(textsurf,textrect)





        ########################### LOCAL MULTIPLAYER OPTION ###########################

##        button('Local Multiplayer',0,270,250,50,bright_yellow,yellow,25,Gameloopfortwo)

        someText = pygame.font.Font('freesansbold.ttf',25)
        textsurf,textrect = text_objects('Local Multiplayer',someText)
        textrect.center = (120,300)
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',19)
        textsurf,textrect = text_objects('This is where two or more players will play on the same screen.',someText)
        textrect.center = (340,330)
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',18)
        textsurf,textrect = text_objects('Choose the number of players :',someText)
        textrect.center = (185,350)
        gameDisplay.blit(textsurf,textrect)


        
        ########################### AI OPTION ###########################


        someText = pygame.font.Font('freesansbold.ttf',25)
        textsurf,textrect = text_objects('Player vs Computer',someText)
        textrect.center = (135,520)
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',19)
        textsurf,textrect = text_objects('This is where will play against computer on the same screen.',someText)
        textrect.center = (325,550)
        gameDisplay.blit(textsurf,textrect)

        button('Start!',275,570,85,30,bright_blue,yellow,30,Gameloopfortwo)


        two = button('2',340,342,25,32,bright_blue,yellow,30,Gameloopfortwo)
        
        three = button('3',380,342,25,32,bright_blue,yellow,30,Gameloopforthree)

        four = button('4',420,342,25,32,bright_blue,yellow,30,Gameloopforfour)
        
        five = button('5',460,342,25,32,bright_blue,yellow,30,Gameloopforfive)
        
        

        #call button function
        
        button('Back to Welcome Screen',800,730,200,25,bright_red,red,15,Gameintro)
        button('Quit PyMonopoly',850,775,150,25,bright_red,red,15,quitGame)


        
        pygame.display.update()
        clock.tick(6)






dice1rolls = 0
dice2rolls = 0
totalrolls = 0

def dice():
    global dice1rolls
    global dice2rolls
    global totalrolls
    global currentPlayer
    
    dice1rolls = random.randint(1,6)
    dice2rolls = random.randint(1,6)
    totalrolls = dice1rolls + dice2rolls

    biglist[currentPlayer][1] = int(biglist[currentPlayer][1]) + totalrolls #update position

    if biglist[currentPlayer][1] > 39: #if position is bigger than 39, because there are 40 blocks on monopoly
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You received a salary of $200',someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)

        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 200


        
        biglist[currentPlayer][1] = int(biglist[currentPlayer][1]) - 40 #update position



def addNewProperty(): #function defined if player wants to buy a property

    global PropertyList
    global currentPlayer

    if int(biglist[currentPlayer][0]) > 0: #if player's money is greater than 0
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - int(PropertyList[biglist[currentPlayer][1]][1]) #deduct money and pay to buy this property
        biglist[currentPlayer][2].append(PropertyList[biglist[currentPlayer][1]][0]) #add this property to player's property list
        biglist[currentPlayer][2] = list(set(biglist[currentPlayer][2])) #remove duplicates if any
        PropertyList[biglist[currentPlayer][1]][3] = currentPlayer #set owner of this property to the currrent player
   
    if int(biglist[currentPlayer][0]) <= 0: #if player's money is 0 or less than 0
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You lost the game !',someText)
        textrect.center = ((490),(180))
        gameDisplay.blit(textsurf,textrect)
        button('YOU LOST !',100,100,100,100,red,light_red,25,quitGame)



def addNewRailroad(): #function defined if player wants to buy a railroad

    global PropertyList
    global currentPlayer

    if int(biglist[currentPlayer][0]) > 0: #if player's money is greater than 0
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - int(PropertyList[biglist[currentPlayer][1]][1]) #deduct money and pay to buy this property
        biglist[currentPlayer][3].append(PropertyList[biglist[currentPlayer][1]][0]) #add this property to player's property list
        biglist[currentPlayer][3] = list(set(biglist[currentPlayer][3])) #remove duplicates if any
        PropertyList[biglist[currentPlayer][1]][3] = currentPlayer #set owner of this property to the currrent player
    
    if int(biglist[currentPlayer][0]) <= 0: #if player's money is 0 or less than 0
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You lost the game !',someText)
        textrect.center = ((490),(180))
        gameDisplay.blit(textsurf,textrect)
        button('YOU LOST !',100,100,100,100,red,light_red,25,quitGame)



def addNewUtility(): #function defined if player wants to buy a utility

    global PropertyList
    global currentPlayer

    if int(biglist[currentPlayer][0]) > 0: #if player's money is greater than 0
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - int(PropertyList[biglist[currentPlayer][1]][1]) #deduct money and pay to buy this property
        biglist[currentPlayer][4].append(PropertyList[biglist[currentPlayer][1]][0]) #add this property to player's property list
        biglist[currentPlayer][4] = list(set(biglist[currentPlayer][4])) #remove duplicates if any
        PropertyList[biglist[currentPlayer][1]][4] = currentPlayer #set owner of this property to the currrent player

            
    if int(biglist[currentPlayer][0]) <= 0: #if player's money is 0 or less than 0
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You lost the game !',someText)
        textrect.center = ((490),(180))
        gameDisplay.blit(textsurf,textrect)
        button('YOU LOST !',100,100,100,100,red,light_red,25,quitGame)




def Playerchar(mssg,r,ac):
    global dice1rolls
    global dice2rolls
    global totalrolls
    global pposition
    global currentPlayer
    global biglist
    
    pos = [(746,750),(662,770),(600,770),(530,770),(464,770),(400,770),(335,770),(268,770),(200,770),(135,763),(50,750),(30,663),(30,597),(30,533),(30,465),(30,402),(30,335),(30,269),(30,203),(30,139),(50,54),(138,30),(205,30),(268,30),(337,30),(400,30),(464,30),(532,30),(597,30),(662,30),(751,50),(765,135),(765,203),(765,270),(765,334),(756,400),(756,465),(765,532),(757,597),(765,663)]

    pygame.draw.circle(gameDisplay,ac,(pos[biglist[currentPlayer][1]]),r)
    
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf,textRect = text_objects(mssg,smallText)
    #centre the text
    textRect.center = (pos[biglist[currentPlayer][1]])
    gameDisplay.blit(textSurf,textRect)



def LandingOnChance(): #function defined if player lands on chance
    
    global currentPlayer
    global biglist
    global chancelist

    randomcc = random.choice(chancelist) #randomly select a card from chance cards list
    print randomcc #print it on screen


    if chancelist.index(randomcc) == 0: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[0],someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = 24
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Position Now : '+str(PropertyList[24][0]),someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[24]
         
        
    elif chancelist.index(randomcc) == 1: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[1],someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = biglist[currentPlayer][0] - 40
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money Now : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif chancelist.index(randomcc) == 2: #if the card is at this index, do whatever it says on the card
        jailcard = 1

    elif chancelist.index(randomcc) == 3: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[3],someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = 0
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Position Now : '+str(PropertyList[0]),someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[0]
         

    elif chancelist.index(randomcc) == 4: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[4],someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = 11
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Position Now : '+str(PropertyList[11]),someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[11]
         

    elif chancelist.index(randomcc) == 5: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[5],someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - 15
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money Now : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((800),(185))
        gameDisplay.blit(textsurf,textrect)
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif chancelist.index(randomcc) == 6: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[6],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 50
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         
        

    elif chancelist.index(randomcc) == 7: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[7],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 100
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif chancelist.index(randomcc) == 8: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[8],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = 39
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[39]
        biglist[currentPlayer][1]

    elif chancelist.index(randomcc) == 9: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[9],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - 12
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif chancelist.index(randomcc) == 10: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[10],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = 5
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[5]
         

    elif chancelist.index(randomcc) == 11: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[11],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = int(biglist[currentPlayer][1]) - 3
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[biglist[currentPlayer][1]]
         

    elif chancelist.index(randomcc) == 12: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[12],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 150
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif chancelist.index(randomcc) == 13: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[13],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = biglist[currentPlayer][0] - 25
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif chancelist.index(randomcc) == 14: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(chancelist[14],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        print 'You are Gone to Jail !'


def LandingOnCC(): #function defined if players lands on community chest
    global cclist
    global currentPlayer
    global biglist

    randomcc = random.choice(cclist) #randomly select a card from community chest cards

    if cclist.index(randomcc) == 0: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[0],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 50
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         
        
    elif cclist.index(randomcc) == 1: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[1],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 25
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 2: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[2],someText)
        textrect.center = ((500),(175))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][1] = 0
        print 'Player '+str(currentPlayer)+"'s "+'Position Now : ',PropertyList[0]

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money Now : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 200
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 3: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[3],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - 100
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 4: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[4],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - 50
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 5: #if the card is at this index, do whatever it says on the card
        jailcard = 1

    elif cclist.index(randomcc) == 6: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[6],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 45
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 7: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[7],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 100
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 8: #if the card is at this index, do whatever it says on the card
        print 'You are Gone to Jail !'

    elif cclist.index(randomcc) == 9: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[9],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 100
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 10: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[10],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 10
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]

    elif cclist.index(randomcc) == 11: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[11],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 100
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 12: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[12],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - 40
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 13: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[13],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 200
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         

    elif cclist.index(randomcc) == 14: #if the card is at this index, do whatever it says on the card

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(cclist[14],someText)
        textrect.center = ((500),(185))
        gameDisplay.blit(textsurf,textrect)
        
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) + 20
        print 'Player '+str(currentPlayer)+"'s "+'Money Now : $',biglist[currentPlayer][0]
         





def LandingOnProperty():
    global biglist
    global currentPlayer
    global PropertyList
    
    if PropertyList[biglist[currentPlayer][1]][3] == 'bank': #if the owner of this property is bank
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Do you want to buy '+PropertyList[biglist[currentPlayer][1]][0]+' for $'+str(PropertyList[biglist[currentPlayer][1]][1])+' ?',someText)
        textrect.center = ((490),(120))
        gameDisplay.blit(textsurf,textrect)
        button('Yes',450,140,40,23,light_green,vlight_green,20,addNewProperty) #button to buy this property
        button('No',510,140,40,23,red,light_red,20,Gameloopfortwo) #button to not buy this property
        
    if PropertyList[biglist[currentPlayer][1]][3] != 'bank' and  PropertyList[biglist[currentPlayer][1]][3] != currentPlayer: #if owner of this property is not band and not this current player
        
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+ str(PropertyList[biglist[currentPlayer][1]][3])+' owns this! ',someText)
        textrect.center = ((485),(175))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You have to pay rent of $'+str(PropertyList[biglist[currentPlayer][1]][4]),someText)
        textrect.center = ((485),(189))
        gameDisplay.blit(textsurf,textrect)
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - int(PropertyList[biglist[currentPlayer][1]][4]) #deduct money and pay rent


def LandingOnRailroad():
    global biglist
    global currentPlayer
    global PropertyList

    if PropertyList[biglist[currentPlayer][1]][3] == 'bank': #if the owner of this property is bank
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Do you want to buy '+PropertyList[biglist[currentPlayer][1]][0]+' for $'+str(PropertyList[biglist[currentPlayer][1]][1])+' ?',someText)
        textrect.center = ((490),(120))
        gameDisplay.blit(textsurf,textrect)
        button('Yes',450,140,40,23,light_green,vlight_green,20,addNewProperty) #button to buy this property
        button('No',510,140,40,23,red,light_red,20,Gameloopfortwo) #button to not buy this property
        
    elif PropertyList[biglist[currentPlayer][1]][3] != 'bank' and  PropertyList[biglist[currentPlayer][1]][3] != currentPlayer: #if owner of this property is not band and not this current player
        
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+ str(PropertyList[biglist[currentPlayer][1]][3])+' owns this! ',someText)
        textrect.center = ((485),(175))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You have to pay rent of $'+str(PropertyList[biglist[currentPlayer][1]][4]),someText)
        textrect.center = ((485),(189))
        gameDisplay.blit(textsurf,textrect)
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - int(PropertyList[biglist[currentPlayer][1]][4]) #deduct money and pay rent


def LandingOnUtility():
    global biglist
    global currentPlayer
    global PropertyList

    if PropertyList[biglist[currentPlayer][1]][3] == 'bank': #if the owner of this property is bank
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Do you want to buy '+PropertyList[biglist[currentPlayer][1]][0]+' for $'+str(PropertyList[biglist[currentPlayer][1]][1])+' ?',someText)
        textrect.center = ((490),(120))
        gameDisplay.blit(textsurf,textrect)
        button('Yes',450,140,40,23,light_green,vlight_green,20,addNewProperty) #button to buy this property
        button('No',510,140,40,23,red,light_red,20,Gameloopfortwo) #button to not buy this property
        
    elif PropertyList[biglist[currentPlayer][1]][3] != 'bank' and  PropertyList[biglist[currentPlayer][1]][3] != currentPlayer: #if owner of this property is not band and not this current player
        
        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+ str(PropertyList[biglist[currentPlayer][1]][3])+' owns this! ',someText)
        textrect.center = ((485),(175))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('You have to pay rent of $'+str(PropertyList[biglist[currentPlayer][1]][4]),someText)
        textrect.center = ((485),(189))
        gameDisplay.blit(textsurf,textrect)
        biglist[currentPlayer][0] = int(biglist[currentPlayer][0]) - int(PropertyList[biglist[currentPlayer][1]][4]) #deduct money and pay rent






biglist =[]

for i in range(2):
    biglist.append([1500,0,[],[],[]])

########################### TWO PLAYER OPTION ###########################
def Gameloopfortwo():
    global biglist
    global currentPlayer
    
    currentPlayer = (currentPlayer + 1) % int(2) #update players after each turn

    gameEnded = False
    
    while not gameEnded: #while game has not ended

        #event handling loop:
        for event in pygame.event.get(): #get any event happening on screen
            if event.type == pygame.QUIT: #if X button has been clicked
                gameEnded = True

##            print event #print whatever event is happening on screen

        gameDisplay.fill(white) #background color

        displayImg(boardImg,0,0) #call this function

        

        global dice1rolls
        global dice2rolls
        global totalrolls
        global PropertyList
    
        

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s Turn",someText)
        textrect.center = ((880),(10))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('You have landed on : ',someText)
        textrect.center = ((865),(130))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(str(PropertyList[biglist[currentPlayer][1]][0]),someText)
        textrect.center = ((883),(140))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 1: '+str(dice1rolls),someText)
        textrect.center = ((825),(40))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 2: '+str(dice2rolls),someText)
        textrect.center = ((825),(60))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Total: '+str(totalrolls),someText)
        textrect.center = ((825),(80))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Position: '+str(biglist[currentPlayer][1]),someText)
        textrect.center = ((827),(100))
        gameDisplay.blit(textsurf,textrect)


        box(300,597,100,60,gray,blue,dice)
        displayImg(diceImg,300,600)

        
        if currentPlayer == 0:
            Playerchar('0',15,red)
        else:
            Playerchar('1',15,yellow)
            


        ########################### LANDING ON CHANCE ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Chance':
            LandingOnChance()

        ########################### LANDING ON COMMUNITY CHEST ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Community Chest':
            LandingOnCC()
        
        ########################### LANDING ON PROPERTY ###########################
        if PropertyList[biglist[currentPlayer][1]][2] == 'Property': #if player lands on property
            LandingOnProperty()
            
                
        ########################### LANDING ON Railroad ###########################    
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Railroad':
            LandingOnRailroad()
            

        ########################### LANDING ON UTILITY ###########################
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Utility':
            LandingOnUtility()
            



        ########################### UPDATING LIST ###########################
        someText = pygame.font.Font('freesansbold.ttf',13)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((882),(180))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',12)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Purchases : ',someText)
        textrect.center = ((880),(200))
        gameDisplay.blit(textsurf,textrect)
        
        x = 855
        y = 215
        for i in biglist[currentPlayer][2]: #updating property list
            for j in biglist[currentPlayer][3]: #updating railroad list
                for k in biglist[currentPlayer][4]: #updating utility list
                    
                    someText = pygame.font.Font('freesansbold.ttf',11)
                    textsurf,textrect = text_objects(str(k),someText)
                    textrect.center = ((x),(y))
                    if int(biglist[currentPlayer][0]) > 0:
                        gameDisplay.blit(textsurf,textrect)
                        y = y + 10
                        
                someText = pygame.font.Font('freesansbold.ttf',11)
                textsurf,textrect = text_objects(str(j),someText)
                textrect.center = ((x),(y))
                if int(biglist[currentPlayer][0]) > 0:
                    gameDisplay.blit(textsurf,textrect)
                    y = y + 10
                    
            someText = pygame.font.Font('freesansbold.ttf',11)
            textsurf,textrect = text_objects(str(i),someText)
            textrect.center = ((x),(y))
            if int(biglist[currentPlayer][0]) > 0:
                gameDisplay.blit(textsurf,textrect)
                y = y + 10



        
        button('End Turn',870,650,130,30,red,bright_red,15,Gameloopfortwo)
        button('Quit MainMenu',870,720,130,30,red,bright_red,15,mainmenu)
        button('Quit PyMonopoly',870,770,130,30,red,bright_red,14,quitGame)

        

        pygame.display.update() #update the display 

        clock.tick(10) #frames per second








biglist =[]

for i in range(3):
    biglist.append([1500,0,[],[],[]])

########################### THREE PLAYER OPTION ###########################
def Gameloopforthree():
    global biglist
    global currentPlayer
    
    currentPlayer = (currentPlayer + 1) % int(3) #update players after each turn

    gameEnded = False
    
    while not gameEnded: #while game has not ended

        #event handling loop:
        for event in pygame.event.get(): #get any event happening on screen
            if event.type == pygame.QUIT: #if X button has been clicked
                gameEnded = True

##            print event #print whatever event is happening on screen

        gameDisplay.fill(white) #background color

        displayImg(boardImg,0,0) #call this function

        

        global dice1rolls
        global dice2rolls
        global totalrolls
        global PropertyList
    
        

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s Turn",someText)
        textrect.center = ((880),(10))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('You have landed on : ',someText)
        textrect.center = ((865),(130))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(str(PropertyList[biglist[currentPlayer][1]][0]),someText)
        textrect.center = ((883),(140))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 1: '+str(dice1rolls),someText)
        textrect.center = ((825),(40))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 2: '+str(dice2rolls),someText)
        textrect.center = ((825),(60))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Total: '+str(totalrolls),someText)
        textrect.center = ((825),(80))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Position: '+str(biglist[currentPlayer][1]),someText)
        textrect.center = ((827),(100))
        gameDisplay.blit(textsurf,textrect)


        box(300,597,100,60,gray,blue,dice)
        displayImg(diceImg,300,600)

        
        if currentPlayer == 0:
            Playerchar('0',15,red)
        elif currentPlayer == 1:
            Playerchar('1',15,yellow)
        elif currentPlayer == 2:
            Playerchar('2',15,blue)
            
            


        ########################### LANDING ON CHANCE ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Chance':
            LandingOnChance()

        ########################### LANDING ON COMMUNITY CHEST ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Community Chest':
            LandingOnCC()
        
        ########################### LANDING ON PROPERTY ###########################
        if PropertyList[biglist[currentPlayer][1]][2] == 'Property': #if player lands on property
            LandingOnProperty()
            
                
        ########################### LANDING ON Railroad ###########################    
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Railroad':
            LandingOnRailroad()
            

        ########################### LANDING ON UTILITY ###########################
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Utility':
            LandingOnUtility()
            



        ########################### UPDATING LIST ###########################
        someText = pygame.font.Font('freesansbold.ttf',13)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((882),(180))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',12)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Purchases : ',someText)
        textrect.center = ((880),(200))
        gameDisplay.blit(textsurf,textrect)
        
        x = 855
        y = 215
        for i in biglist[currentPlayer][2]: #updating property list
            for j in biglist[currentPlayer][3]: #updating railroad list
                for k in biglist[currentPlayer][4]: #updating utility list
                    
                    someText = pygame.font.Font('freesansbold.ttf',11)
                    textsurf,textrect = text_objects(str(k),someText)
                    textrect.center = ((x),(y))
                    if int(biglist[currentPlayer][0]) > 0:
                        gameDisplay.blit(textsurf,textrect)
                        y = y + 10
                        
                someText = pygame.font.Font('freesansbold.ttf',11)
                textsurf,textrect = text_objects(str(j),someText)
                textrect.center = ((x),(y))
                if int(biglist[currentPlayer][0]) > 0:
                    gameDisplay.blit(textsurf,textrect)
                    y = y + 10
                    
            someText = pygame.font.Font('freesansbold.ttf',11)
            textsurf,textrect = text_objects(str(i),someText)
            textrect.center = ((x),(y))
            if int(biglist[currentPlayer][0]) > 0:
                gameDisplay.blit(textsurf,textrect)
                y = y + 10



        
        button('End Turn',870,650,130,30,red,bright_red,15,Gameloopforthree)
        button('Quit MainMenu',870,720,130,30,red,bright_red,15,mainmenu)
        button('Quit PyMonopoly',870,770,130,30,red,bright_red,14,quitGame)

        

        pygame.display.update() #update the display 

        clock.tick(10) #frames per second

        


biglist =[]

for i in range(4):
    biglist.append([1500,0,[],[],[]])

########################### FOUR PLAYER OPTION ###########################
def Gameloopforfour():
    global biglist
    global currentPlayer
    
    currentPlayer = (currentPlayer + 1) % int(4) #update players after each turn

    gameEnded = False
    
    while not gameEnded: #while game has not ended

        #event handling loop:
        for event in pygame.event.get(): #get any event happening on screen
            if event.type == pygame.QUIT: #if X button has been clicked
                gameEnded = True

##            print event #print whatever event is happening on screen

        gameDisplay.fill(white) #background color

        displayImg(boardImg,0,0) #call this function

        

        global dice1rolls
        global dice2rolls
        global totalrolls
        global PropertyList
    
        

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s Turn",someText)
        textrect.center = ((880),(10))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('You have landed on : ',someText)
        textrect.center = ((865),(130))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(str(PropertyList[biglist[currentPlayer][1]][0]),someText)
        textrect.center = ((883),(140))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 1: '+str(dice1rolls),someText)
        textrect.center = ((825),(40))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 2: '+str(dice2rolls),someText)
        textrect.center = ((825),(60))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Total: '+str(totalrolls),someText)
        textrect.center = ((825),(80))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Position: '+str(biglist[currentPlayer][1]),someText)
        textrect.center = ((827),(100))
        gameDisplay.blit(textsurf,textrect)


        box(300,597,100,60,gray,blue,dice)
        displayImg(diceImg,300,600)

        
        if currentPlayer == 0:
            Playerchar('0',15,red)
        elif currentPlayer == 1:
            Playerchar('1',15,yellow)
        elif currentPlayer == 2:
            Playerchar('2',15,blue)
        elif currentPlayer == 3:
            Playerchar('3',15,gray)
            
            


        ########################### LANDING ON CHANCE ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Chance':
            LandingOnChance()

        ########################### LANDING ON COMMUNITY CHEST ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Community Chest':
            LandingOnCC()
        
        ########################### LANDING ON PROPERTY ###########################
        if PropertyList[biglist[currentPlayer][1]][2] == 'Property': #if player lands on property
            LandingOnProperty()
            
                
        ########################### LANDING ON Railroad ###########################    
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Railroad':
            LandingOnRailroad()
            

        ########################### LANDING ON UTILITY ###########################
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Utility':
            LandingOnUtility()
            



        ########################### UPDATING LIST ###########################
        someText = pygame.font.Font('freesansbold.ttf',13)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((882),(180))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',12)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Purchases : ',someText)
        textrect.center = ((880),(200))
        gameDisplay.blit(textsurf,textrect)
        
        x = 855
        y = 215
        for i in biglist[currentPlayer][2]: #updating property list
            for j in biglist[currentPlayer][3]: #updating railroad list
                for k in biglist[currentPlayer][4]: #updating utility list
                    
                    someText = pygame.font.Font('freesansbold.ttf',11)
                    textsurf,textrect = text_objects(str(k),someText)
                    textrect.center = ((x),(y))
                    if int(biglist[currentPlayer][0]) > 0:
                        gameDisplay.blit(textsurf,textrect)
                        y = y + 10
                        
                someText = pygame.font.Font('freesansbold.ttf',11)
                textsurf,textrect = text_objects(str(j),someText)
                textrect.center = ((x),(y))
                if int(biglist[currentPlayer][0]) > 0:
                    gameDisplay.blit(textsurf,textrect)
                    y = y + 10
                    
            someText = pygame.font.Font('freesansbold.ttf',11)
            textsurf,textrect = text_objects(str(i),someText)
            textrect.center = ((x),(y))
            if int(biglist[currentPlayer][0]) > 0:
                gameDisplay.blit(textsurf,textrect)
                y = y + 10



        
        button('End Turn',870,650,130,30,red,bright_red,15,Gameloopforfour)
        button('Quit MainMenu',870,720,130,30,red,bright_red,15,mainmenu)
        button('Quit PyMonopoly',870,770,130,30,red,bright_red,14,quitGame)

        

        pygame.display.update() #update the display 

        clock.tick(10) #frames per second




biglist =[]

for i in range(5):
    biglist.append([1500,0,[],[],[]])

########################### FIVE PLAYER OPTION ###########################
def Gameloopforfive():
    global biglist
    global currentPlayer
    
    currentPlayer = (currentPlayer + 1) % int(5) #update players after each turn

    gameEnded = False
    
    while not gameEnded: #while game has not ended

        #event handling loop:
        for event in pygame.event.get(): #get any event happening on screen
            if event.type == pygame.QUIT: #if X button has been clicked
                gameEnded = True

##            print event #print whatever event is happening on screen

        gameDisplay.fill(white) #background color

        displayImg(boardImg,0,0) #call this function

        

        global dice1rolls
        global dice2rolls
        global totalrolls
        global PropertyList
    
        

        someText = pygame.font.Font('freesansbold.ttf',15)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s Turn",someText)
        textrect.center = ((880),(10))
        gameDisplay.blit(textsurf,textrect)

        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects('You have landed on : ',someText)
        textrect.center = ((865),(130))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',10)
        textsurf,textrect = text_objects(str(PropertyList[biglist[currentPlayer][1]][0]),someText)
        textrect.center = ((883),(140))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 1: '+str(dice1rolls),someText)
        textrect.center = ((825),(40))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Dice 2: '+str(dice2rolls),someText)
        textrect.center = ((825),(60))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Total: '+str(totalrolls),someText)
        textrect.center = ((825),(80))
        gameDisplay.blit(textsurf,textrect)
        someText = pygame.font.Font('freesansbold.ttf',8)
        textsurf,textrect = text_objects('Position: '+str(biglist[currentPlayer][1]),someText)
        textrect.center = ((827),(100))
        gameDisplay.blit(textsurf,textrect)


        box(300,597,100,60,gray,blue,dice)
        displayImg(diceImg,300,600)

        
        if currentPlayer == 0:
            Playerchar('0',15,red)
        elif currentPlayer == 1:
            Playerchar('1',15,yellow)
        elif currentPlayer == 2:
            Playerchar('2',15,blue)
        elif currentPlayer == 3:
            Playerchar('3',15,gray)
        elif currentPlayer == 4:
            Playerchar('4',15,green)
            
            


        ########################### LANDING ON CHANCE ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Chance':
            LandingOnChance()

        ########################### LANDING ON COMMUNITY CHEST ###########################
        if PropertyList[biglist[currentPlayer][1]][0] == 'Community Chest':
            LandingOnCC()
        
        ########################### LANDING ON PROPERTY ###########################
        if PropertyList[biglist[currentPlayer][1]][2] == 'Property': #if player lands on property
            LandingOnProperty()
            
                
        ########################### LANDING ON Railroad ###########################    
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Railroad':
            LandingOnRailroad()
            

        ########################### LANDING ON UTILITY ###########################
        elif PropertyList[biglist[currentPlayer][1]][2] == 'Utility':
            LandingOnUtility()
            



        ########################### UPDATING LIST ###########################
        someText = pygame.font.Font('freesansbold.ttf',13)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Money : $'+str(biglist[currentPlayer][0]),someText)
        textrect.center = ((882),(180))
        gameDisplay.blit(textsurf,textrect)
        
        someText = pygame.font.Font('freesansbold.ttf',12)
        textsurf,textrect = text_objects('Player '+str(currentPlayer)+"'s "+'Purchases : ',someText)
        textrect.center = ((880),(200))
        gameDisplay.blit(textsurf,textrect)
        
        x = 855
        y = 215
        for i in biglist[currentPlayer][2]: #updating property list
            for j in biglist[currentPlayer][3]: #updating railroad list
                for k in biglist[currentPlayer][4]: #updating utility list
                    
                    someText = pygame.font.Font('freesansbold.ttf',11)
                    textsurf,textrect = text_objects(str(k),someText)
                    textrect.center = ((x),(y))
                    if int(biglist[currentPlayer][0]) > 0:
                        gameDisplay.blit(textsurf,textrect)
                        y = y + 10
                        
                someText = pygame.font.Font('freesansbold.ttf',11)
                textsurf,textrect = text_objects(str(j),someText)
                textrect.center = ((x),(y))
                if int(biglist[currentPlayer][0]) > 0:
                    gameDisplay.blit(textsurf,textrect)
                    y = y + 10
                    
            someText = pygame.font.Font('freesansbold.ttf',11)
            textsurf,textrect = text_objects(str(i),someText)
            textrect.center = ((x),(y))
            if int(biglist[currentPlayer][0]) > 0:
                gameDisplay.blit(textsurf,textrect)
                y = y + 10



        
        button('End Turn',870,650,130,30,red,bright_red,15,Gameloopforfive)
        button('Quit MainMenu',870,720,130,30,red,bright_red,15,mainmenu)
        button('Quit PyMonopoly',870,770,130,30,red,bright_red,14,quitGame)

        

        pygame.display.update() #update the display 

        clock.tick(10) #frames per second













Gameintro()
mainmenu()
Gameloopfortwo()
Gameloopforthree()
Gameloopfortfour()
Gameloopforfive()

pygame.quit() #stop pygame from running
quit()
