import os

# pre game
os.system('cls')

# welcome phrase 1
welcome = "◘ Welcomed To TicTacToe (X/O) ◘ ".center(120)
print(welcome)
print()
print()
print()

# asking for the name
name1 = ''
while(name1 == ""):
    name1 = input(" « PLAYER 1, enter your name please » ")
    print()

print()
print()
name2 = ''
while(name2 == ""):
    name2 = input(" « PLAYER 2, enter your name please » ")
    print()

print()
print()


name1 = name1.upper()
name2 = name2.upper()
welcome1 = " Hello "+"'"+name1+"'"+' and '+"'"+name2+"'"
welcome1 = welcome1.center(120)
print(welcome1)
print()

print()


def clrscr():
    response = input(" press 'ENTER' to Continue ")
    if response == '':
        os.system('cls')


clrscr()


field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


sbl1 = ''
while(sbl1.upper() not in ('X', 'O')):
    sbl1 = input(" « PLAYER 1, Pick a symbol ('X' or 'O') » ")
    print()
sbl1 = sbl1.upper()


if sbl1 == 'X':
    sbl2 = 'O'
else:
    sbl2 = 'X'


def aff(list):
    print('--------- ')
    print(list[0]+' | '+list[1]+' | '+list[2]+'')
    print('--------- ')
    print(list[3]+' | '+list[4]+' | '+list[5]+'')
    print('--------- ')
    print(list[6]+' | '+list[7]+' | '+list[8]+'')
    print('--------- ')
    print()


aff(field)

# returns true when all the field is filled with 'X's and 'O's which results in the game over


def check(list):
    v = True
    for i in list:
        if (i <= '9' and i >= '1'):
            v = False
            break
    return v

# returns true if one of the players has won


def winner(t, sbl):
    if t[2] == t[4] == t[6] == sbl:
        return True
    elif t[0] == t[3] == t[6] == sbl:
        return True
    elif t[2] == t[5] == t[8] == sbl:
        return True
    elif t[1] == t[4] == t[7] == sbl:
        return True
    elif t[0] == t[4] == t[8] == sbl:
        return True
    elif t[0] == t[1] == t[2] == sbl:
        return True
    elif t[3] == t[4] == t[5] == sbl:
        return True
    elif t[6] == t[7] == t[8] == sbl:
        return True
    else:
        return False


def congratsp1():
    print("""
        CCCCCCCCCCCCC                                                                                             tttt                               PPPPPPPPPPPPPPPPP    1111111   
     CCC::::::::::::C                                                                                          ttt:::t                               P::::::::::::::::P  1::::::1   
   CC:::::::::::::::C                                                                                          t:::::t                               P::::::PPPPPP:::::P1:::::::1   
  C:::::CCCCCCCC::::C                                                                                          t:::::t                               PP:::::P     P:::::111:::::1   
 C:::::C       CCCCCC  ooooooooooo  nnnn  nnnnnnnn      ggggggggg   ggggrrrrr   rrrrrrrrr  aaaaaaaaaaaaa ttttttt:::::ttttttt       ssssssssss          P::::P     P:::::P  1::::1   
C:::::C              oo:::::::::::oon:::nn::::::::nn   g:::::::::ggg::::r::::rrr:::::::::r a::::::::::::at:::::::::::::::::t     ss::::::::::s         P::::P     P:::::P  1::::1   
C:::::C             o:::::::::::::::n::::::::::::::nn g:::::::::::::::::r:::::::::::::::::raaaaaaaaa:::::t:::::::::::::::::t   ss:::::::::::::s        P::::PPPPPP:::::P   1::::1   
C:::::C             o:::::ooooo:::::nn:::::::::::::::g::::::ggggg::::::grr::::::rrrrr::::::r        a::::tttttt:::::::tttttt   s::::::ssss:::::s       P:::::::::::::PP    1::::l   
C:::::C             o::::o     o::::o n:::::nnnn:::::g:::::g     g:::::g r:::::r     r:::::r aaaaaaa:::::a     t:::::t          s:::::s  ssssss        P::::PPPPPPPPP      1::::l   
C:::::C             o::::o     o::::o n::::n    n::::g:::::g     g:::::g r:::::r     rrrrrraa::::::::::::a     t:::::t            s::::::s             P::::P              1::::l   
C:::::C             o::::o     o::::o n::::n    n::::g:::::g     g:::::g r:::::r          a::::aaaa::::::a     t:::::t               s::::::s          P::::P              1::::l   
 C:::::C       CCCCCo::::o     o::::o n::::n    n::::g::::::g    g:::::g r:::::r         a::::a    a:::::a     t:::::t    tttttssssss   s:::::s        P::::P              1::::l   
  C:::::CCCCCCCC::::o:::::ooooo:::::o n::::n    n::::g:::::::ggggg:::::g r:::::r         a::::a    a:::::a     t::::::tttt:::::s:::::ssss::::::s     PP::::::PP         111::::::111
   CC:::::::::::::::o:::::::::::::::o n::::n    n::::ng::::::::::::::::g r:::::r         a:::::aaaa::::::a     tt::::::::::::::s::::::::::::::s      P::::::::P         1::::::::::1
     CCC::::::::::::Coo:::::::::::oo  n::::n    n::::n gg::::::::::::::g r:::::r          a::::::::::aa:::a      tt:::::::::::tts:::::::::::ss       P::::::::P         1::::::::::1
        CCCCCCCCCCCCC  ooooooooooo    nnnnnn    nnnnnn   gggggggg::::::g rrrrrrr           aaaaaaaaaa  aaaa        ttttttttttt   sssssssssss         PPPPPPPPPP         111111111111
                                                                 g:::::g                                                                                                            
                                                     gggggg      g:::::g                                                                                                            
                                                     g:::::gg   gg:::::g                                                                                                            
                                                      g::::::ggg:::::::g                                                                                                            
                                                       gg:::::::::::::g                                                                                                             
                                                         ggg::::::ggg                                                               

    """)


def congratsp2():
    print("""
        CCCCCCCCCCCCC                                                                                             tttt                               PPPPPPPPPPPPPPPPP   222222222222222    
     CCC::::::::::::C                                                                                          ttt:::t                               P::::::::::::::::P 2:::::::::::::::22  
   CC:::::::::::::::C                                                                                          t:::::t                               P::::::PPPPPP:::::P2::::::222222:::::2 
  C:::::CCCCCCCC::::C                                                                                          t:::::t                               PP:::::P     P:::::2222222     2:::::2 
 C:::::C       CCCCCC  ooooooooooo  nnnn  nnnnnnnn      ggggggggg   ggggrrrrr   rrrrrrrrr  aaaaaaaaaaaaa ttttttt:::::ttttttt       ssssssssss          P::::P     P:::::P           2:::::2 
C:::::C              oo:::::::::::oon:::nn::::::::nn   g:::::::::ggg::::r::::rrr:::::::::r a::::::::::::at:::::::::::::::::t     ss::::::::::s         P::::P     P:::::P           2:::::2 
C:::::C             o:::::::::::::::n::::::::::::::nn g:::::::::::::::::r:::::::::::::::::raaaaaaaaa:::::t:::::::::::::::::t   ss:::::::::::::s        P::::PPPPPP:::::P         2222::::2  
C:::::C             o:::::ooooo:::::nn:::::::::::::::g::::::ggggg::::::grr::::::rrrrr::::::r        a::::tttttt:::::::tttttt   s::::::ssss:::::s       P:::::::::::::PP     22222::::::22   
C:::::C             o::::o     o::::o n:::::nnnn:::::g:::::g     g:::::g r:::::r     r:::::r aaaaaaa:::::a     t:::::t          s:::::s  ssssss        P::::PPPPPPPPP     22::::::::222     
C:::::C             o::::o     o::::o n::::n    n::::g:::::g     g:::::g r:::::r     rrrrrraa::::::::::::a     t:::::t            s::::::s             P::::P            2:::::22222        
C:::::C             o::::o     o::::o n::::n    n::::g:::::g     g:::::g r:::::r          a::::aaaa::::::a     t:::::t               s::::::s          P::::P           2:::::2             
 C:::::C       CCCCCo::::o     o::::o n::::n    n::::g::::::g    g:::::g r:::::r         a::::a    a:::::a     t:::::t    tttttssssss   s:::::s        P::::P           2:::::2             
  C:::::CCCCCCCC::::o:::::ooooo:::::o n::::n    n::::g:::::::ggggg:::::g r:::::r         a::::a    a:::::a     t::::::tttt:::::s:::::ssss::::::s     PP::::::PP         2:::::2       222222
   CC:::::::::::::::o:::::::::::::::o n::::n    n::::ng::::::::::::::::g r:::::r         a:::::aaaa::::::a     tt::::::::::::::s::::::::::::::s      P::::::::P         2::::::2222222:::::2
     CCC::::::::::::Coo:::::::::::oo  n::::n    n::::n gg::::::::::::::g r:::::r          a::::::::::aa:::a      tt:::::::::::tts:::::::::::ss       P::::::::P         2::::::::::::::::::2
        CCCCCCCCCCCCC  ooooooooooo    nnnnnn    nnnnnn   gggggggg::::::g rrrrrrr           aaaaaaaaaa  aaaa        ttttttttttt   sssssssssss         PPPPPPPPPP         22222222222222222222
                                                                 g:::::g                                                                                                                    
                                                     gggggg      g:::::g                                                                                                                    
                                                     g:::::gg   gg:::::g                                                                                                                    
                                                      g::::::ggg:::::::g                                                                                                                    
                                                       gg:::::::::::::g                                                                                                                     
                                                         ggg::::::ggg                                                                                                                       
                                                            gggggg                                           
    """)


def draw():
    print("""

                                                                                                       
                                                                                                       
DDDDDDDDDDDDD      RRRRRRRRRRRRRRRRR                  AAA   WWWWWWWW                           WWWWWWWW
D::::::::::::DDD   R::::::::::::::::R                A:::A  W::::::W                           W::::::W
D:::::::::::::::DD R::::::RRRRRR:::::R              A:::::A W::::::W                           W::::::W
DDD:::::DDDDD:::::DRR:::::R     R:::::R            A:::::::AW::::::W                           W::::::W
  D:::::D    D:::::D R::::R     R:::::R           A:::::::::AW:::::W           WWWWW           W:::::W 
  D:::::D     D:::::DR::::R     R:::::R          A:::::A:::::AW:::::W         W:::::W         W:::::W  
  D:::::D     D:::::DR::::RRRRRR:::::R          A:::::A A:::::AW:::::W       W:::::::W       W:::::W   
  D:::::D     D:::::DR:::::::::::::RR          A:::::A   A:::::AW:::::W     W:::::::::W     W:::::W    
  D:::::D     D:::::DR::::RRRRRR:::::R        A:::::A     A:::::AW:::::W   W:::::W:::::W   W:::::W     
  D:::::D     D:::::DR::::R     R:::::R      A:::::AAAAAAAAA:::::AW:::::W W:::::W W:::::W W:::::W      
  D:::::D     D:::::DR::::R     R:::::R     A:::::::::::::::::::::AW:::::W:::::W   W:::::W:::::W       
  D:::::D    D:::::D R::::R     R:::::R    A:::::AAAAAAAAAAAAA:::::AW:::::::::W     W:::::::::W        
DDD:::::DDDDD:::::DRR:::::R     R:::::R   A:::::A             A:::::AW:::::::W       W:::::::W         
D:::::::::::::::DD R::::::R     R:::::R  A:::::A               A:::::AW:::::W         W:::::W          
D::::::::::::DDD   R::::::R     R:::::R A:::::A                 A:::::AW:::W           W:::W           
DDDDDDDDDDDDD      RRRRRRRR     RRRRRRRAAAAAAA                   AAAAAAAWWW             WWW            
                                                                                              

    """)


def testexistance(t, x):
    v = True
    for i in t:
        if i == x:
            v = False
            break
    return v


replay = True
total1 = total2 = 0
while replay:
    field = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    gameover = False
    while gameover == False:

        aff(field)
        # getting the input of the indices
        if gameover == False:
            p1choice = ''
            while(p1choice == '') or (testexistance(field, p1choice)) or (p1choice > '9' and p1choice < '1'):
                p1choice = input(
                    'PLAYER 1, Choose one of the given Numbers inside the table ^^ ')
                print()
            field[int(p1choice)-1] = sbl1

        aff(field)

        if winner(field, sbl1):
            gameover = True
            total1 += 1
            congratsp1()
            print("GGs "+name1+" you've won ")
            print("better Luck next time "+name2)

        if not winner(field, sbl1) and check(field):
            gameover = True
            print('DRAW! seems like you both are good players! ')
            draw()

        if gameover == False:
            p2choice = ''
            while(p2choice == '') or (testexistance(field, p2choice)) or (p2choice > '9' and p2choice < '1'):
                p2choice = input(
                    'PLAYER 2, Choose one of the given Numbers inside the table ^^ ')
                print()
            field[int(p2choice)-1] = sbl2
            aff(field)

        if winner(field, sbl2):
            gameover = True
            total2 += 1
            congratsp2()
            print("GGs "+name2+" you've won ")
            print("better Luck next time "+name1)

    print("The Score now is:      Player1 (" +
          str(total1)+")  -  ("+str(total2)+") Player2  ")

    print('Wanna replay ? ')
    rep = input("Type 'YES' to replay, or 'No' to quit: ")

    rep = rep.upper()

    if rep != 'YES':
        replay = False
    else:
        os.system('cls')
        
  # ╟╟╟   Created by mouhib 17/07/2020 :)   ╟╟╟

