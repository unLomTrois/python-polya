# -*- coding: cp1251 -*-

import logelement

elNot = logelement.TNot() 
elAnd = logelement.TAnd() 
elAnd.link(elNot, 1) 

print ( " A | B | not(A&B) " ); 
print ( "-------------------" ); 

for A in range(2): 
    elAnd.In1 = bool(A) 
    for B in range(2): 
        elAnd.In2 = bool(B) 
        print ( " ", A, "|", B, "|", int(elNot.Res) )

        