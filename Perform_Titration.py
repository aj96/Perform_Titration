import sys
import math

def MainMenu():
    
    print(' ')
    print("Main Menu")
    print("1 Solve for pH when titrating a base with an acid")
    print("2 Solve for pH when titrating an acid with a base")
    print("Q To Quit")
    print(' ')
    
    user_input= input("Enter a choice> ")
    while user_input not in ['1','2','Q','q']:
        user_input= input("Enter a choice> ")
    if user_input == '1':
        return TitrateBaseWithAcid()
    elif user_input == '2':
        return TitrateAcidWithBase()
    elif user_input in ['Q','q']:
        sys.exit(0)


            

def TitrateBaseWithAcid():

    print(' ')
    print("Menu: Titrate Base With Acid")
    
    print(' ')
    print("T Calculate number of liters of titrant needed for equivalence point")
    print("1 Solve for pH before equivalence point")
    print("E Solve for pH at equivalence point")
    print("2 Solve for pH after equivalence point")
    print("D Done")
    print(' ')
    
    user_input = input("Enter a choice> ")
    while user_input not in ['1','2','E','e','D','d','T','t']:
        user_input = input("Enter a choice> ")
    if user_input in ['T','t']:
        #Ct = OnlyAcceptsFloating(Ct,"Enter molarity of titrant> ")
        #Ct = float(Ct)
        Ct = float(input("Enter molarity of titrant> "))
        Co = float(input("Enter molarity of intial solution> "))
        Vo = float(input("Enter volume (liters) of intial solution> "))
        Vt = (Co*Vo)/Ct
        print("Equivalence point occurs when %f liters of titrant are added." % (Vt))
        return TitrateBaseWithAcid()
    elif user_input in ['D','d']:
        return MainMenu()
    elif user_input == '1':
        K = float(input("Enter Kb constant> "))
        Ct = float(input("Enter molarity of titrant> "))
        Co = float(input("Enter molarity of intial solution> "))
        Vo = float(input("Enter volume of intial solution before addition of titrant (liters)> "))
        Vt = 0.1
        while Vt != 0:
            Vt = float(input("Enter volume of titrant added (liters). Enter 0 to stop> "))
            while Vt >= (Co*Vo)/Ct:
                print("Volume of titrant is too large. You have gone past the equivalence point.")
                Vt = float(input("Enter volume of titrant added (liters). Enter 0 to stop> "))
                
            
            if Vt != 0:
                pH_one = 14 + math.log10(((-K*Vo-K*Vt-Ct*Vt)+ (((K*Vo+K*Vt+Ct*Vt)**2)-(4*(Vt+Vo)*(K*Ct*Vt-K*Co*Vo)))**0.5)/(2*(Vt+Vo)))
                print("pH: %f" % pH_one)
        return TitrateBaseWithAcid()
    elif user_input in ['E','e']:
        print("Is this reaction between a strong acid and strong base? Y/N")
        user_input = input("Enter Y or N ")
        while user_input not in ['y','Y','n','N']:
            user_input = input("Enter Y or N ")
        if user_input in ['Y','y']:
            print("The pH at the equivalence point is 7.")
            return TitrateBaseWithAcid()
        else:
        
            K = float(input("Enter Kb constant> "))
            K = (1*(10**-14))/K
            Ct = float(input("Enter molarity of titrant> "))
            Co = float(input("Enter molarity of initial solution> "))
            Vo = float(input("Enter volume (liters) of intial solution> "))
            Vt = (Co*Vo)/Ct
            Co = ((Co*Vo)/(Vt+Vo))
            #pH_one = -math.log10((K + ((K**2 + 4*(K*Co)))**0.5)/-2)
            pH = -math.log10((K - ((K**2 + 4*(K*Co)))**0.5)/-2)
            print("The pH at the equivalence point is %f" % (pH))
            return TitrateBaseWithAcid()
    elif user_input == '2':
        K = float(input("Enter Kb constant> "))
        K = (1*(10**-14))/K
        Ct = float(input("Enter molarity of titrant> "))
        Co = float(input("Enter molarity of initial solution> "))
        Vo = float(input("Enter volume (liters) of intial solution> "))
        Vte = (Co*Vo)/Ct
        Cotwo = ((Co*Vo)/(Vte+Vo))
        Vt = 0.1
        while Vt != 0:        
            Vt = float(input("Enter volume (liters) of titrant added. Enter 0 to stop> "))
            if Vt!= 0:
                CoTwo = (K - ((K**2 + 4*(K*Cotwo)))**0.5)/-2
                pH = -math.log10(((Ct*Vt-Co*Vo)/(Vt+Vo)) + CoTwo)            
                print("pH: %f" % pH)
        return TitrateBaseWithAcid()

def TitrateAcidWithBase():
    print(' ')
    print("Menu: Titrate Acid With Base")
    print(' ')
    print("T Calculate number of liters of titrant needed for equivalence point")
    print("1 Solve for pH before equivalence point")
    print("E Solve for pH at equivalence point")
    print("2 Solve for pH after equivalence point")
    print("D Done")
    print(' ')

    user_input = input("Enter a choice> ")
    while user_input not in ['1','2','E','e','D','d','t','T']:
        user_input = input("Enter a choice> ")
    if user_input in ['T','t']:
        Ct = float(input("Enter molarity of titrant> "))
        Co = float(input("Enter molarity of intial solution> "))
        Vo = float(input("Enter volume (liters) of intial solution> "))
        Vt = (Co*Vo)/Ct
        print("Equivalence point occurs when %f liters of titrant are added." % (Vt))
        return TitrateAcidWithBase()
    elif user_input in ['D','d']:
        return MainMenu()
    
    elif user_input == '1':
        K = float(input("Enter Ka constant> "))
        Ct = float(input("Enter molarity of titrant> "))
        Co = float(input("Enter molarity of intial solution> "))
        Vo = float(input("Enter volume of intial solution before addition of titrant (liters)> "))
        Vt = 0.1
        while Vt != 0:
            Vt = float(input("Enter volume of titrant added (liters). Enter 0 to stop> "))
            if Vt != 0:
                pH_one = -math.log10(((-K*Vo-K*Vt-Ct*Vt)+ (((K*Vo+K*Vt+Ct*Vt)**2)-(4*(Vt+Vo)*(K*Ct*Vt-K*Co*Vo)))**0.5)/(2*(Vt+Vo)))
                
                print("pH: %f" % pH_one)
            
            else:
                return TitrateAcidWithBase()

    elif user_input in ['E','e']:
        print("Is this reaction between a strong acid and strong base? Y/N")
        user_input = input("Enter Y or N ")
        while user_input not in ['y','Y','n','N']:
            user_input = input("Enter Y or N ")
        if user_input in ['Y','y']:
            print("The pH at the equivalence point is 7.")
            return TitrateAcidWithBase()
        else:
        
            K = float(input("Enter Ka constant> "))
            K = (1*(10**-14))/K
            Ct = float(input("Enter molarity of titrant> "))
            Co = float(input("Enter molarity of initial solution> "))
            Vo = float(input("Enter volume (liters) of intial solution> "))
            Vt = (Co*Vo)/Ct
            Co = ((Co*Vo)/(Vt+Vo))
            #pH_one = -math.log10((K + ((K**2 + 4*(K*Co)))**0.5)/-2)
            pH = 14 + math.log10((K - ((K**2 + 4*(K*Co)))**0.5)/-2)
            print("The pH at the equivalence point is %f" % (pH))
            return TitrateAcidWithBase()

    
    elif user_input == '2':
        K = float(input("Enter Ka constant> "))
        K = (1*(10**-14))/K
        Ct = float(input("Enter molarity of titrant> "))
        Co = float(input("Enter molarity of initial solution> "))
        Vo = float(input("Enter volume (liters) of intial solution> "))
        Vte = (Co*Vo)/Ct
        Cotwo = ((Co*Vo)/(Vte+Vo))
        Vt = 0.1
        while Vt != 0:        
            Vt = float(input("Enter volume (liters) of titrant added. Enter 0 to stop> "))
            if Vt != 0:
                CTwo = (K - ((K**2 + 4*(K*Cotwo)))**0.5)/-2
                pH = 14+ math.log10(((Ct*Vt-Co*Vo)/(Vt+Vo)) + CTwo)            
                print("pH: %f" % pH)
        return TitrateAcidWithBase()
    
                      
        
    
if __name__ == "__main__":       
   
    MainMenu()
    
