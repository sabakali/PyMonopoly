


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
    name = name
    color = color
    owner = owner
    cost = int(cost)
    rent = int(rent)
    mortgage = int(mortgage)
    housecost = int(housecost)
    hotelcost = int(hotelcost)
    houses = int(houses)
    h1 = int(h1) #house 1
    h2 = int(h2) #house 2
    h3 = int(h3) #house 3
    h4 = int(h4) #house 4
    h5 = int(h5) #hotel
    return name,cost,whattype


def Railroad(name,owner,whattype,cost,rent):
    name = name
    owner = owner
    cost = int(cost)
    rent = int(rent)

    return name,cost,whattype

def Utilities(name,owner,whattype,cost,rent):
    name = name
    owner = owner
    cost = int(cost)
    rent = int(rent)
    
    return name,cost,whattype
    

def CommunityChest(name):
    name = name

    return name

def Chance(name):
    name = name
    
    return name


def Tax(name,whattype,tax):
    name = name
    tax = int(tax)

    return name,whattype,tax

def FreeBlock(name):
    name = name

    return name


def CommunityChestCard(description,move,collect,pay,payperhouse,getoutofjailfree,gotojail,collect50):
    description = description
    move = int(move)
    collect = int(collect)
    pay = int(pay)
    payperhouse = int(payperhouse)
    getoutofjailfree = getoutofjailfree
    gotojail = gotojail
    collect50 = collect50

    return description

def ChanceCard(description,move,collect,pay,payperhouse,getoutofjailfree,gotojail,moveback):
    description = description
    move = int(move)
    collect = int(collect)
    pay = int(pay)
    payperhouse = int(payperhouse)
    getoutofjailfree = getoutofjailfree
    gotojail = gotojail
    moveback = moveback

    return description


def Board():
    
    global BoardList
    global cclist
    global chancelist

    BoardList = []

    fb1 = FreeBlock('GO!')
    BoardList.append(fb1)
    
    ma = Property('Mediterranean Avenue','brown','Property','bank',60,2,50,50,30,0,10,30,90,160,250)
    BoardList.append(ma)
    
    cc1 = CommunityChest('Community Chest')
    BoardList.append(cc1)
    
    ba = Property('Baltic Avenue','brown','Property','bank',60,4,30,50,50,0,20,60,180,320,450)
    BoardList.append(ba)

    it1 = Tax('Income Tax','Tax',200)
    BoardList.append(it1)

    rr = Railroad('Reading Railroad','bank','Railroad',200,25)
    BoardList.append(rr)
    
    oa = Property('Oriental Avenue','light blue','Property','bank',100,6,50,50,50,0,30,90,270,400,550)
    BoardList.append(oa)

    c1 = Chance('Chance')
    BoardList.append(c1)

    va = Property('Vermont Avenue','light blue','Property','bank',100,6,50,50,50,0,30,90,270,400,550)
    BoardList.append(va)

    ca = Property('Connecticut Avenue','Property','light blue','bank',120,8,60,50,50,0,40,100,300,450,600)
    BoardList.append(ca)

    fb2 = FreeBlock('Just Visiting Jail')
    BoardList.append(fb2)

    scp = Property('St. Charles Place','pink','Property','bank',140,10,70,100,100,0,50,150,450,625,750)
    BoardList.append(scp)

    ec = Utilities('Electric Company','bank','Utility',150,0)
    BoardList.append(ec)

    sa = Property('States Avenue','pink','Property','bank',140,10,70,100,100,0,50,150,450,625,750)
    BoardList.append(sa)

    va1 = Property('Virginia Avenue','pink','Property','bank',160,12,80,100,100,0,60,180,500,700,900)
    BoardList.append(va1)

    pr = Railroad('Pennsylvania Railroad','bank','Railroad',200,25)
    BoardList.append(pr)

    sjp = Property('St. James Place','orange','Property','bank',180,14,90,100,100,0,70,200,550,750,950)
    BoardList.append(sjp)

    cc2 = CommunityChest('Community Chest')
    BoardList.append(cc2)

    ta = Property('Tennessee Avenue','orange','Property','bank',180,14,90,100,100,0,70,200,550,750,950)
    BoardList.append(ta)

    nya = Property('New York Avenue','orange','Property','bank',200,16,100,100,100,0,80,220,600,800,100)
    BoardList.append(nya)

    fb3 = FreeBlock('Free Parking')
    BoardList.append(fb3)
    
    ka = Property('Kentucky Avenue','red','Property','bank',220,18,110,150,150,0,90,250,700,875,1050)
    BoardList.append(ka)

    c2 = Chance('Chance')
    BoardList.append(c2)

    ia = Property('Indiana Avenue','red','Property','bank',220,18,110,150,150,0,90,250,700,875,1050)
    BoardList.append(ia)

    ia1 = Property('Illinois Avenue','red','Property','bank',240,20,120,150,150,0,100,300,750,925,1100)
    BoardList.append(ia1)

    bando = Railroad('B&O Railroad','bank','Railroad',200,25)
    BoardList.append(bando)

    aa = Property('Atlantic Avenue','yellow','Property','bank',260,22,130,150,150,0,110,330,800,975,1150)
    BoardList.append(aa)

    va2 = Property('Ventnor Avenue','yellow','Property','bank',260,22,130,150,150,0,110,330,800,975,1150)
    BoardList.append(va2)

    ww = Utilities('Water Works','bank','Utility',150,0)
    BoardList.append(ww)

    mg = Property('Marvin Gardens','yellow','Property','bank',280,24,140,150,150,0,120,360,850,1025,1200)
    BoardList.append(mg)

    fb4 = FreeBlock('Go To Jail')
    BoardList.append(fb4)

    pa = Property('Pacific Avenue','green','Property','bank',300,26,150,200,200,0,130,390,900,1100,1275)
    BoardList.append(pa)

    nca = Property('North Carolina Avenue','green','Property','bank',300,26,150,200,200,0,130,390,900,1100,1275)
    BoardList.append(nca)

    cc3 = CommunityChest('Community Chest')
    BoardList.append(cc3)

    pa1 = Property('Pennsylvania Avenue','green','Property','bank',320,28,160,200,200,0,150,450,1000,1200,1400)
    BoardList.append(pa1)
    
    sl = Railroad('Short Line','bank','Railroad',200,25)
    BoardList.append(sl)

    c3 = Chance('Chance')
    BoardList.append(c3)

    pp = Property('Park Place','dark blue','Property','bank',350,35,175,200,200,0,175,500,1100,1300,1500)
    BoardList.append(pp)

    lt = Tax('Luxury Tax','Tax',100)
    BoardList.append(lt)

    b = Property('Boardwalk','dark blue','Property','bank',400,50,200,200,200,0,200,600,1400,1700,2000)
    BoardList.append(b)

    cclist = []

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
    

    chancelist = []

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



    return BoardList
    return cclist
    return chancelist

    
Board()

def Taxblock(t):

    if BoardList[position][1] == 'Tax':
        
        global money
        if money > 0:
            money = money - BoardList[position][2]
            print 'You have to pay Tax of '+str(BoardList[position][2])
            print 'Player'+"'"+'s '+'Money : ',money
        else:
            print 'You do not have enough money !'

def addProperty(newProperty):

    if BoardList[position][2] == 'Property':
        otherPlayers()
        checkifbuy = raw_input('Do you want to buy '+BoardList[position][0]+' for $'+str(BoardList[position][1])+' ?')
        if checkifbuy == 'Yes':

            global position

            
            global money
            if money > 0:
                money = money - BoardList[position][1]
                print 'Player'+"'"+'s '+'Money : ',money
            else:
                print 'You do not have enough money !'

            global proplist
            proplist.append(BoardList[position][0])

            print 'Property List : ',proplist
            
        elif checkifbuy == 'No':
            print 'Property List : ',proplist
        

    

def addRailroad(newRailroad):

    if BoardList[position][2] == 'Railroad':
        otherPlayers()
        checkifbuy = raw_input('Do you want to buy '+BoardList[position][0]+' for $'+str(BoardList[position][1])+' ?')
        if checkifbuy == 'Yes':
            
            global position

            global money
            if money > 0:
                money = money - BoardList[position][1]
                print 'Player'+"'"+'s '+'Money : ',money
            else:
                print 'You do not have enough money !'
                
            global raillist
            raillist.append(BoardList[position][0])

            print 'Railroad List : ',raillist
        elif checkifbuy == 'No':
            print 'Railroad List : ',raillist
        

    

def addUtility(newUtility):

    if BoardList[position][2] == 'Utility':
        otherPlayers()
        checkifbuy = raw_input('Do you want to buy '+BoardList[position][0]+' for $'+str(BoardList[position][1])+' ?')
        if checkifbuy == 'Yes':
        
            global position

            global money
            if money > 0:
                money = money - BoardList[position][1]
                print 'Player'+"'"+'s ' 'Money : ',money
            else:
                print 'You do not have enough money !'

            global utilist
            utilist.append(BoardList[position][0])

            print 'Utility List : ',utilist
        if checkifbuy == 'No':
            print 'Utility List : ',utilist

            

def LandingonCC(cc):

    if BoardList[position] == 'Community Chest':
        randomcc = random.choice(cclist)
        print randomcc

        if cclist.index(randomcc) == 0:
            global money
            money = money + 50
            print 'Player'+"'"+'s ' 'Money Now : ',money
            
        elif cclist.index(randomcc) == 1:
            global money
            money = money + 25
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 2:
            global position
            position = 0
            print 'Position Now : ',BoardList[0]
            
            global money
            money = money + 200
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 3:
            global money
            money = money - 100
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 4:
            global money
            money = money - 50
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 5:
            jailcard = 1

        elif cclist.index(randomcc) == 6:
            global money
            money = money + 45
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 7:
            global money
            money = money + 100
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 8:
            print 'You are Gone to Jail !'

        elif cclist.index(randomcc) == 9:
            global money
            money = money + 100
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 10:
            global money
            money = money + 10
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 11:
            global money
            money = money + 100
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 12:
            global money
            money = money - 40
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 13:
            global money
            money = money + 200
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif cclist.index(randomcc) == 14:
            global money
            money = money + 20
            print 'Player'+"'"+'s ' 'Money Now : ',money
            
            
def LandingonChance(c):

    if BoardList[position] == 'Chance':
        randomcc = random.choice(chancelist)
        print randomcc

        if chancelist.index(randomcc) == 0:
            global position
            position = 24
            print 'Position Now : ',BoardList[24]
            
        elif chancelist.index(randomcc) == 1:
            global money
            money = money - 40
            print 'Player'+"'"+'s ' 'Money Now : ',money 

        elif chancelist.index(randomcc) == 2:
            jailcard = 1

        elif chancelist.index(randomcc) == 3:
            global position
            position = 0
            print 'Position Now : ',BoardList[0]

        elif chancelist.index(randomcc) == 4:
            global position
            position = 11
            print 'Position Now : ',BoardList[11]

        elif chancelist.index(randomcc) == 5:
            global money
            money = money - 15
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif chancelist.index(randomcc) == 6:
            global money
            money = money + 50
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif chancelist.index(randomcc) == 7:
            global money
            money = money + 100
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif chancelist.index(randomcc) == 8:
            global position
            position = 39
            print 'Position Now : ',BoardList[39]

        elif chancelist.index(randomcc) == 9:
            global money
            money = money - 12
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif chancelist.index(randomcc) == 10:
            global position
            position = 5
            print 'Position Now : ',BoardList[5]

        elif chancelist.index(randomcc) == 11:
            global position
            position = position - 3
            print 'Position Now : ',BoardList[position]

        elif chancelist.index(randomcc) == 12:
            global money
            money = money + 150
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif chancelist.index(randomcc) == 13:
            global money
            money = money - 25
            print 'Player'+"'"+'s ' 'Money Now : ',money

        elif chancelist.index(randomcc) == 14:
            print 'You are Gone to Jail !'
            

def otherPlayers():

    #howmanyPlayers = raw_input('How Many Players are Playing?')
##    global howmanyPlayers
##
##    global whichPlayer
##    
##    #print whichPlayer, "wp before"
##
##    whichPlayer = (whichPlayer + 1) % int(howmanyPlayers)
##
##    #print whichPlayer, "wp after"

    
    print 'Player '+str(whichPlayer)+"'s Turn"

def updatePlayer():
    global howmanyPlayers
    global whichPlayer  
    whichPlayer = (whichPlayer + 1) % int(howmanyPlayers)
 


def ActualGame():

    global howmanyPlayers

    howmanyPlayers = raw_input('How Many Players are Playing?')

    
    def Player():

        global money
        

        global proplist
       
        global railist

        global utilist

        addProperty(BoardList[position])

        addRailroad(BoardList[position])
    
        addUtility(BoardList[position])

        LandingonCC(BoardList[position])

        LandingonChance(BoardList[position])

        Taxblock(BoardList[position])
        

    #initialize variables
    otherPlayers()

        
    global position
    position = 0
    print 'Initial Position : ',BoardList[0]
    print 'Player'+"'"+'s '+'Initial Money : ',1500

    Game = True
    #repeat until game ends
    while Game == True:
    
        dice1 = random.randint(1,6)
        print 'Dice1 : ',dice1
        dice2 = random.randint(1,6)
        print 'Dice2 : ',dice2

        total = dice1 + dice2
        print 'Total : ',total

        position = position + total

        if position > 39:
            position = position - 40
            

        print 'Player'+"'"+'s ' 'Position : ',BoardList[position]

        Player()

        if money <= 0:
            print 'You do not have enough money ! You lost the Game!'
            Game = False
        #print 'here',otherPlayers()
        otherPlayers()
        #print 'end',otherPlayers()
        updatePlayer()

ActualGame()

   


    
    

