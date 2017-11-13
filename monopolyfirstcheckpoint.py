


# Shaheer Bakali
# 15-112 Project
# PyMonopoly


import random

global proplist
proplist = []

global rallist
raillist = []

global utilist
utilist = []

global money
money = int(1500)

global whichPlayer
whichPlayer = 0

def Property(name,color,whattype,owner,cost,rent,mortgage,housecost,hotelcost,houses,h1,h2,h3,h4,h5):
    return name,cost,whattype


def Railroad(name,owner,whattype,cost,rent):

    return name,cost,whattype

def Utilities(name,owner,whattype,cost,rent):
    return name,cost,whattype
    

def CommunityChest(name):
    return name

def Chance(name):
    return name


def Tax(name,whattype,tax):
    return name,whattype,tax

def FreeBlock(name):
    return name


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

    if PropertyList[position][1] == 'Tax': #if player lands on Tax block
        
        global money
        if money > 0: #money should be greater than 0
            money = money - PropertyList[position][2] #deduct money and pay tax
            print 'You have to pay Tax of '+str(PropertyList[position][2])
            print 'Player '+str(whichPlayer)+"'s "+'Money : ',money
        else:
            print 'You do not have enough money !'


def addProperty(newProperty): #function defined if player wants to buy a property

    if PropertyList[position][2] == 'Property': #if player lands on Property
        
        checkifbuy = raw_input('Do you want to buy '+PropertyList[position][0]+' for $'+str(PropertyList[position][1])+' ?') #ask player if they want to buy this property
        if checkifbuy == 'Yes': #if they say yes

            global position
            
            global money
            if money > 0: #money should be greater than 0
                money = money - PropertyList[position][1] #deduct money and pay to buy this property
                print 'Player '+str(whichPlayer)+"'s "+'Money : ',money
            else:
                print 'You do not have enough money !'

            global proplist
            proplist.append(PropertyList[position][0]) #append this recently bought property to proplist

            print 'Player '+str(whichPlayer)+"'s "+'Property List : ',proplist
            
        elif checkifbuy == 'No':
            print 'Player '+str(whichPlayer)+"'s "+'Property List : ',proplist
        

    

def addRailroad(newRailroad): #function defined if player wants to buy a railroad

    if PropertyList[position][2] == 'Railroad': #if player lands on Railroad
       
        checkifbuy = raw_input('Do you want to buy '+PropertyList[position][0]+' for $'+str(PropertyList[position][1])+' ?') #ask player if they want to buy this railroad
        if checkifbuy == 'Yes': #if they say yes
            
            global position

            global money
            if money > 0: #money should be greater than 0
                money = money - PropertyList[position][1] #deduct money and pay to buy this railroad
                print 'Player '+str(whichPlayer)+"'s "+'Money : ',money
            else:
                print 'You do not have enough money !'
                
            global raillist
            raillist.append(PropertyList[position][0]) #append this recently bought railroad to raillist

            print 'Player '+str(whichPlayer)+"'s "+'Railroad List : ',raillist
        elif checkifbuy == 'No':
            print 'Player '+str(whichPlayer)+"'s "+'Railroad List : ',raillist
        

    

def addUtility(newUtility): #function defined if player wants to buy a utility

    if PropertyList[position][2] == 'Utility': #if player lands on Utility
        
        checkifbuy = raw_input('Do you want to buy '+PropertyList[position][0]+' for $'+str(PropertyList[position][1])+' ?') #ask player if they want to buy this utility
        if checkifbuy == 'Yes': #if they say yes
        
            global position

            global money
            if money > 0: #money should be greater than 0
                money = money - PropertyList[position][1] #deduct money and pay to buy this utility
                print 'Player '+str(whichPlayer)+"'s "+'Money : ',money
            else:
                print 'You do not have enough money !'

            global utilist
            utilist.append(PropertyList[position][0]) #append this recently bought utility to utilist

            print 'Player '+str(whichPlayer)+"'s "+'Utility List : ',utilist
        if checkifbuy == 'No':
            print 'Player '+str(whichPlayer)+"'s "+'Utility List : ',utilist

            

def LandingonCC(cc): #function defined if players lands on community chest

    if PropertyList[position] == 'Community Chest': #if player lands on community chest
        randomcc = random.choice(cclist) #randomly select a card from community chest cards
        print randomcc #print it on screen

        if cclist.index(randomcc) == 0: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 50
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money
            
        elif cclist.index(randomcc) == 1: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 25
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 2: #if the card is at this index, do whatever it says on the card
            global position
            position = 0
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[0]
            
            global money
            money = money + 200
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 3: #if the card is at this index, do whatever it says on the card
            global money
            money = money - 100
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 4: #if the card is at this index, do whatever it says on the card
            global money
            money = money - 50
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 5: #if the card is at this index, do whatever it says on the card
            jailcard = 1

        elif cclist.index(randomcc) == 6: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 45
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 7: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 100
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 8: #if the card is at this index, do whatever it says on the card
            print 'You are Gone to Jail !'

        elif cclist.index(randomcc) == 9: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 100
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 10: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 10
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 11: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 100
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 12: #if the card is at this index, do whatever it says on the card
            global money
            money = money - 40
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 13: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 200
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif cclist.index(randomcc) == 14: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 20
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money
            
            
def LandingonChance(c): #function defined if player lands on chance

    if PropertyList[position] == 'Chance':
        randomcc = random.choice(chancelist) #randomly select a card from chance cards list
        print randomcc #print it on screen

        if chancelist.index(randomcc) == 0: #if the card is at this index, do whatever it says on the card
            global position
            position = 24
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[24]
            
        elif chancelist.index(randomcc) == 1: #if the card is at this index, do whatever it says on the card
            global money
            money = money - 40
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money 

        elif chancelist.index(randomcc) == 2: #if the card is at this index, do whatever it says on the card
            jailcard = 1

        elif chancelist.index(randomcc) == 3: #if the card is at this index, do whatever it says on the card
            global position
            position = 0
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[0]

        elif chancelist.index(randomcc) == 4: #if the card is at this index, do whatever it says on the card
            global position
            position = 11
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[11]

        elif chancelist.index(randomcc) == 5: #if the card is at this index, do whatever it says on the card 
            global money
            money = money - 15
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif chancelist.index(randomcc) == 6: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 50
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif chancelist.index(randomcc) == 7: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 100
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif chancelist.index(randomcc) == 8: #if the card is at this index, do whatever it says on the card
            global position
            position = 39
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[39]

        elif chancelist.index(randomcc) == 9: #if the card is at this index, do whatever it says on the card
            global money
            money = money - 12
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif chancelist.index(randomcc) == 10: #if the card is at this index, do whatever it says on the card
            global position
            position = 5
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[5]

        elif chancelist.index(randomcc) == 11: #if the card is at this index, do whatever it says on the card
            global position
            position = position - 3
            print 'Player '+str(whichPlayer)+"'s "+'Position Now : ',PropertyList[position]

        elif chancelist.index(randomcc) == 12: #if the card is at this index, do whatever it says on the card
            global money
            money = money + 150
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif chancelist.index(randomcc) == 13: #if the card is at this index, do whatever it says on the card
            global money
            money = money - 25
            print 'Player '+str(whichPlayer)+"'s "+'Money Now : ',money

        elif chancelist.index(randomcc) == 14: #if the card is at this index, do whatever it says on the card
            print 'You are Gone to Jail !'


def updatePlayer():
    print '                                   '
    global howmanyPlayers
    global whichPlayer  
    whichPlayer = (whichPlayer + 1) % int(howmanyPlayers) #update players after each turn
    print 'Player '+str(whichPlayer)+"'s Turn"
    
 


def ActualGame(): #this function is for the actual game to run

    global howmanyPlayers

    howmanyPlayers = raw_input('How Many Players are Playing?') #ask user how many players are playing

    
    def Player(): #function defined to represent a player

        global money #this is global because it is being used everywhere

        global proplist #this is global property list that player buys because it is being used everywhere
       
        global railist #this is global railroad list that player buys because it is being used everywhere

        global utilist #this is global utilist list that player buys because it is being used everywhere

        addProperty(PropertyList[position]) #call this function to buy a property on this position on board

        addRailroad(PropertyList[position]) #call this function to buy a railroad on this position on board
    
        addUtility(PropertyList[position]) #call this function to buy utility on this position on board

        LandingonCC(PropertyList[position]) #call this function when player lands on community chest on this position on board

        LandingonChance(PropertyList[position]) #call this function when players lands on chance on this position on board

        Taxblock(PropertyList[position]) #call this function when player lands on tax block on this position on board

        
    global position #this is global because it is being used everywhere
    position = 0 #initialy the position is zero
    print 'Initial Position : ',PropertyList[0]
    
    print 'Player '+str(whichPlayer)+"'s"+' Initial Money : ',1500 #display players intial money


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
            

        print 'Player '+str(whichPlayer)+"'s"+ ' Position : ',PropertyList[position] #print players position on board

        Player() #call player function

        if money <= 0: #check if money is positive
            print 'You do not have enough money ! You lost the Game!'
            Game = False #end game


        updatePlayer() #call this function to update player after each turn

ActualGame()

   


    
    

