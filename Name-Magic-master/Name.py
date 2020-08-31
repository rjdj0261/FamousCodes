def a():
 print(" AAAAAAA\nA       A\nA       A\nAAAAAAAAA\nA       A\nA       A\n")
def b():
 print("BBBBBB\nB      B\nB      B\nBBBBBBB\nB      B\nB      B\nBBBBBB \n")
def c():
 print(" CCCCCCC \nC       C\nC\nC\nC       C\n CCCCCCC \n")
def d():
 print("DDDDDDD\nD       D\nD       D\nD       D\nD       D\nDDDDDDD\n")
def e():
 print("EEEEEEEE\nE\nE\nEEEEEEE\nE\nE\nEEEEEEEE\n")
def f():
 print("FFFFFFFFF\nF\nF\nFFFFFFFF\nF\nF\nF\n")
def g():
 print(" GGGGGGG \nG       G\nG\nG   GGGG \nG       G\n GGGGGGG \n")
def h():
 print("H       H\nH       H\nHHHHHHHHH\nH       H\nH       H\n")
def i():
 print(" IIIIIII\n    I\n    I\n    I\n    I\n IIIIIII\n")
def j():
 print(" JJJJJJJ\n       J\n       J\n       J\n       J\n J     J\n  JJJJJ\n")
def k():
 print("K    K\nK   K\nK  K\nKK\nK  K\nK   K\nK    K\n")
def l():
 print("L\nL\nL\nL\nL\nLLLLLLLL\n")
def m():
 print("M        M\nMM      MM\nM M    M M\nM  M  M  M\nM   MM   M\nM        M\nM        M\n")
def mm():
 print("N       N\nN N     N\nN  N    N\nN    N  N\nN     N N\nN       N\n")
def o():
 print(" OOOOOO\nO      O\nO      O\nO      O\nO      O\n OOOOOO\n")
def p():
 print(" PPPPPP\nP      P\nP      P\nPPPPPPP\nP\nP\n")
def q():
 print(" QQQQQQ\nQ      Q\nQ      Q\nQ      Q\nQ    Q Q\n QQQQQQQ\n        Q\n")
def r():
 print("RRRRRRR\nR      R\nR      R\nRRRRRRR\nR      R\nR      R\nR      R\n")
def s():
 print("SSSSSSSS\nS   \nS   \nSSSSSSSS\n       S\n       S\nSSSSSSSS\n")
def t():
 print("TTTTTTTTTTT\n     T\n     T\n     T\n     T\n     T\n     T\n     T\n")
def u():
 print("U       U\nU       U\nU       U\nU       U\nU       U\n UUUUUUU\n")
def v():
 print("V       V\n V     V \n  V   V\n   V V\n    V \n")
def w():
 print("W        W\nW        W\nW   WW   W\nW  W  W  W\nWW      WW\nW        W\n")
def x():
 print("X      X\n X    X\n  X  X  \n   XX\n  X  X \n X    X\nX      X\n")
def y():
 print("Y       Y\n Y     Y \n  Y   Y  \n   Y Y   \n    Y\n    Y\n    Y\n    Y\n")
def z():
 print("ZZZZZZZZ\n      Z\n     Z\n    Z\n   Z\n  Z\n Z\nZZZZZZZZ\n")
def dot():
 print(" ...\n.....\n.....\n.....\n ...\n")
def b11():
 print("  (\n (\n( \n(\n(\n (\n  (\n")
def b12():
 print(")\n )\n  )\n  )\n  )\n )\n)")


#variable for the loop count

n=0


#switch for showing invalid letter massage.

swt="off"
swt1="off"
swt2="off"


#int numbers to ignire

intgn=[(99999999999999999999999999999999999)]


#ignoreable signs

ignr=[";","&","$","#","@","%","=","π","}","{","√","°","_","✓","©","®","™","•","¥","?",":","×","*","÷","/","+","!"]


#thanking user and instracting him

print("Thanks "+str(name)+" for enter your name\n        Just ook at the magic\n\n")


#loop for checking every letter if they are in any word.Without loop I had to write this following code for 26×25 time.

while n<len(name):
 if name[n]=="a" or name[n]=="A":
  a()
 elif name[n]=="b" or name[n]=="B":
  b()
 elif name[n]=="c" or name[n]=="C":
  c()
 elif name[n]=="d" or name[n]=="D":
  d()
 elif name[n]=="e"or name[n]=="E":
  e()
 elif name[n]=="f"or name[n]=="F":
  f()
 elif name[n]=="g"or name[n]=="G":
  g()
 elif name[n]=="h"or name[n]=="H":
  h()
 elif name[n]=="i"or name[n]=="I":
  i()
 elif name[n]=="j"or name[n]=="J":
  j()
 elif name[n]=="k"or name[n]=="K":
  k()
 elif name[n]=="l"or name[n]=="L":
  l()
 elif name[n]=="m"or name[n]=="M":
  m()
 elif name[n]=="n"or name[n]=="N":
  mm()
 elif name[n]=="o"or name[n]=="O":
  o()
 elif name[n]=="p"or name[n]=="P":
  p()
 elif name[n]=="q"or name[n]=="Q":
  q()
 elif name[n]=="r"or name[n]=="R":
  r()
 elif name[n]=="s"or name[n]=="S":
  s()
 elif name[n]=="t"or name[n]=="T":
  t()
 elif name[n]=="u"or name[n]=="U":
  u()
 elif name[n]=="v"or name[n]=="V":
  v()
 elif name[n]=="w"or name[n]=="W":
  w()
 elif name[n]=="x"or name[n]=="X":
  x()
 elif name[n]=="y"or name[n]=="Y":
  y()
 elif name[n]=="z"or name[n]=="Z":
  z()
 elif name[n]==".":
  dot()
 elif name[n]=="(":
  b11()
 elif name[n]==")":
  b12()
 elif name[n]==ignr:
  continue
  swt1="on"
 elif name[n]==intgn:
  continue
  swt2="on"
 elif name[n]==" ":
  print("\n\n")
 else:
  print("\n")
  swt="on"
 n+=1


#if warning eneble then warning massages are activated.
if swt2=="on":
 print("Sorry "+str(name)+",I had to skip number/s.")

if swt1=="on":
 print("Sorry "+str(name)+",I had to skip spacial charecter/s.")

if swt=="on":
 print("Sorry "+str(name)+",you used unknown letter/s so I skipped it.")
