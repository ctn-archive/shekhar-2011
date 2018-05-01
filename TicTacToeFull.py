import sys
sys.path.append('D:/Telluride2011/Docs/Nengo/nengo-1294/python')

from spa import *
import nef

dimensions=24

import Source
class Rules:
    
    def ruleYM(vision_turn = 'MYMOVE',mode='-DO_ANY'): # Check for your move
        set(attention = 'E', memory = 'BLANK', move = 'DOANY', mode = 'DO_ANY')
    #For Win
    #Row checking
    #First Row
    #Rules for checking first location.
    def ruleWR111(mode='LOOK_ROW',attention='A',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='B')
    def ruleWR112(mode='LOOK_ROW',attention='A',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='D')
    def ruleWR113(mode='LOOK_ROW',attention='A',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='A',attention='B')
        
    #Rules for checking second location.    
    def ruleWR121(mode='LOOK_ROW',attention='B',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C')
    def ruleWR122(mode='LOOK_ROW',attention='B',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='D')
    def ruleWR123(mode='LOOK_ROW',attention='B',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='D')
    def ruleWR124(mode='LOOK_ROW',attention='B',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='B',attention='C')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_ROW',attention='C',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWR131(mode='LOOK_ROW',attention='C',memory='A',vision='O',scale=1.0/4):
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be A and the win function here.
    def ruleWR132(mode='LOOK_ROW',attention='C',memory='B',vision='O',scale=1.0/4):
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be B and the win function here.
    def ruleWR133(mode='LOOK_ROW',attention='C',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be C and the win function here.
    def ruleWR134(mode='LOOK_ROW',attention='C',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='D', memory = 'BLANK')
    def ruleWR135(mode='LOOK_ROW',attention='C',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='D', memory = 'BLANK')
    def ruleWR136(mode='LOOK_ROW',attention='C',memory='B',vision='BLANK',scale=1.0/4):
        set(attention='D', memory = 'BLANK')
        
    #Second Row
    #Rules for checking first location.
    def ruleWR211(mode='LOOK_ROW',attention='D',memory='BLANK',vision='O',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='E')
    def ruleWR212(mode='LOOK_ROW',attention='D',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='G')
    def ruleWR213(mode='LOOK_ROW',attention='D',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='D',attention='E')
        
    #Rules for checking second location.
    def ruleWR221(mode='LOOK_ROW',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='F')
    def ruleWR222(mode='LOOK_ROW',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='G')
    def ruleWR223(mode='LOOK_ROW',attention='E',memory='D',vision='BLANK',scale=1.0/4):
        set(attention='G')
    def ruleWR224(mode='LOOK_ROW',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='F')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_ROW',attention='F',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWR231(mode='LOOK_ROW',attention='F',memory='D',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be D and the win function here.
    def ruleWR232(mode='LOOK_ROW',attention='F',memory='E',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the win function here.
    def ruleWR233(mode='LOOK_ROW',attention='F',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be F and the win function here.
    def ruleWR234(mode='LOOK_ROW',attention='F',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='G', memory = 'BLANK')
    def ruleWR235(mode='LOOK_ROW',attention='F',memory='D',vision='BLANK',scale=1.0/4):
        set(attention='G', memory = 'BLANK')
    def ruleWR236(mode='LOOK_ROW',attention='F',memory='E',vision='BLANK',scale=1.0/4):
        set(attention='G', memory='BLANK')
    
    #Third Row
    #Rules for checking first location.
    def ruleWR311(mode='LOOK_ROW',attention='G',memory='BLANK',vision='O',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='H')
    def ruleWR312(mode='LOOK_ROW',attention='G',memory='BLANK',vision='X',scale=1.0/4):
        set(mode='LOOK_COLUMN',memory='BLANK',attention='A')
    def ruleWR313(mode='LOOK_ROW',attention='G',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='G',attention='H')
        
    #Rules for checking second location.
    def ruleWR321(mode='LOOK_ROW',attention='H',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='I')
    def ruleWR322(mode='LOOK_ROW',attention='H',memory='BLANK',vision='X',scale=1.0/4):
        #Row checking Complete ??
    def ruleWR323(mode='LOOK_ROW',attention='H',memory='G',vision='BLANK',scale=1.0/4):
        #Row checking Complete ?? 
    def ruleWR324(mode='LOOK_ROW',attention='H',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='H',attention='I')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_ROW',attention='I',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWR331(mode='LOOK_ROW',attention='I',memory='G',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be G and the win function here.
    def ruleWR332(mode='LOOK_ROW',attention='I',memory='H',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be H and the win function here.
    def ruleWR333(mode='LOOK_ROW',attention='I',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be I and the win function here.
    def ruleWR334(mode='LOOK_ROW',attention='I',memory='BLANK',vision='X',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleWR335(mode='LOOK_ROW',attention='I',memory='G',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleWR336(mode='LOOK_ROW',attention='I',memory='H',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')

    #Column Checking
    #First Column
    #Rules for checking first location.
    def ruleWC111(mode='LOOK_COL',attention='A',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='D')
    def ruleWC112(mode='LOOK_COL',attention='A',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='B')
    def ruleWC113(mode='LOOK_COL',attention='A',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='A',attention='D')
        
    #Rules for checking second location.    
    def ruleWC121(mode='LOOK_COL',attention='D',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='G')
    def ruleWC122(mode='LOOK_COL',attention='D',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='B')
    def ruleWC123(mode='LOOK_COL',attention='D',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='B')
    def ruleWC124(mode='LOOK_COL',attention='D',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='D',attention='G')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_COL',attention='G',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWC131(mode='LOOK_COL',attention='G',memory='A',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be A and the win function here.
    def ruleWC132(mode='LOOK_COL',attention='G',memory='D',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be D and the win function here.
    def ruleWC133(mode='LOOK_COL',attention='G',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be G and the win function here.
    def ruleWC134(mode='LOOK_COL',attention='G',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='B', memory = 'BLANK')
    def ruleWC135(mode='LOOK_COL',attention='G',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='B', memory = 'BLANK')
    def ruleWC136(mode='LOOK_COL',attention='G',memory='D',vision='BLANK',scale=1.0/4):
        set(attention='B', memory = 'BLANK')
        
    #Second Column
    #Rules for checking first location.
    def ruleWC211(mode='LOOK_COL',attention='B',memory='BLANK',vision='O',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='E')
    def ruleWC212(mode='LOOK_COL',attention='B',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C')
    def ruleWC213(mode='LOOK_COL',attention='B',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='B',attention='E')
        
    #Rules for checking second location.
    def ruleWC221(mode='LOOK_COL',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='H')
    def ruleWC222(mode='LOOK_COL',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C')
    def ruleWC223(mode='LOOK_COL',attention='E',memory='B',vision='BLANK',scale=1.0/4):
        set(attention='C')
    def ruleWC224(mode='LOOK_COL',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='H')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_COL',attention='H',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWC231(mode='LOOK_COL',attention='H',memory='B',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be B and the win function here.
    def ruleWC232(mode='LOOK_COL',attention='H',memory='E',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the win function here.
    def ruleWC233(mode='LOOK_COL',attention='H',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be H and the win function here.
    def ruleWC234(mode='LOOK_COL',attention='H',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleWC235(mode='LOOK_COL',attention='H',memory='B',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleWC236(mode='LOOK_COL',attention='H',memory='E',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    
    #Third Column
    #Rules for checking first location.
    def ruleWC311(mode='LOOK_COL',attention='C',memory='BLANK',vision='O',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='F')
    def ruleWC312(mode='LOOK_COL',attention='C',memory='BLANK',vision='X',scale=1.0/4):
        #Column checking Complete ??
    def ruleWC313(mode='LOOK_COL',attention='C',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='C',attention='F')
        
    #Rules for checking second location.
    def ruleWC321(mode='LOOK_COL',attention='F',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='I')
    def ruleWC322(mode='LOOK_COL',attention='F',memory='BLANK',vision='X',scale=1.0/4):
        #Column checking Complete ??
    def ruleWC323(mode='LOOK_COL',attention='F',memory='C',vision='BLANK',scale=1.0/4):
        #Column checking Complete ?? 
    def ruleWC324(mode='LOOK_COL',attention='F',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='F',attention='I')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_COL',attention='I',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWC331(mode='LOOK_COL',attention='I',memory='C',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be C and the win function here.
    def ruleWC332(mode='LOOK_COL',attention='I',memory='F',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be F and the win function here.
    def ruleWC333(mode='LOOK_COL',attention='I',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be I and the win function here.
    def ruleWC334(mode='LOOK_COL',attention='I',memory='BLANK',vision='X',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleWC335(mode='LOOK_COL',attention='I',memory='C',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleWC336(mode='LOOK_COL',attention='I',memory='F',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')

    #Diagonal Checking
    #First Diagonal
    #Rules for checking first location.
    def ruleWD111(mode='LOOK_DIA',attention='A',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='E')
    def ruleWD112(mode='LOOK_DIA',attention='A',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C')
    def ruleWD113(mode='LOOK_DIA',attention='A',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='A',attention='E')
        
    #Rules for checking second location.    
    def ruleWD121(mode='LOOK_DIA',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='I')
    def ruleWD122(mode='LOOK_DIA',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C')
    def ruleWD123(mode='LOOK_DIA',attention='E',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='C')
    def ruleWD124(mode='LOOK_DIA',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='I')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_DIA',attention='I',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWD131(mode='LOOK_DIA',attention='I',memory='A',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be A and the win function here.
    def ruleWD132(mode='LOOK_DIA',attention='I',memory='E',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the win function here.
    def ruleWD133(mode='LOOK_DIA',attention='I',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be I and the win function here.
    def ruleWD134(mode='LOOK_DIA',attention='I',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleWD135(mode='LOOK_DIA',attention='I',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleWD136(mode='LOOK_DIA',attention='I',memory='E',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
        
    #Second Diagonal
    #Rules for checking first location.
    def ruleWD211(mode='LOOK_DIA',attention='C',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='E')
    def ruleWD212(mode='LOOK_DIA',attention='C',memory='BLANK',vision='X',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') # checking for win done
    def ruleWD213(mode='LOOK_DIA',attention='C',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='C',attention='E')
        
    #Rules for checking second location.    
    def ruleWD221(mode='LOOK_DIA',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='G')
    def ruleWD222(mode='LOOK_DIA',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Diagonal Checking Done
    def ruleWD223(mode='LOOK_DIA',attention='E',memory='C',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Diagonal Checking done
    def ruleWD224(mode='LOOK_DIA',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='G')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_DIA',attention='G',memory='BLANK',vision='O',scale=1.0/4): Already Won   
    def ruleWD231(mode='LOOK_DIA',attention='G',memory='C',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be C and the win function here.
    def ruleWD232(mode='LOOK_DIA',attention='G',memory='E',vision='O',scale=1.0/4)
        set(motor=memory, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the win function here.
    def ruleWD233(mode='LOOK_DIA',attention='G',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='WIN',memory = 'BLANK')
        #put the code to call the 'que' location to be G and the win function here.
    def ruleWD234(mode='LOOK_DIA',attention='G',memory='BLANK',vision='X',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleWD235(mode='LOOK_DIA',attention='G',memory='A',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleWD236(mode='LOOK_DIA',attention='G',memory='E',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    
    #For Block
    #Row checking
    #First Row
    #Rules for checking first location.
    def ruleBR111(mode='LOOK_ROW',attention='A',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='B')
    def ruleBR112(mode='LOOK_ROW',attention='A',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='D')
    def ruleBR113(mode='LOOK_ROW',attention='A',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='A',attention='B')
        
    #Rules for checking second location.    
    def ruleBR121(mode='LOOK_ROW',attention='B',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='C')
    def ruleBR122(mode='LOOK_ROW',attention='B',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='D')
    def ruleBR123(mode='LOOK_ROW',attention='B',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='D')
    def ruleBR124(mode='LOOK_ROW',attention='B',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='B',attention='C')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_ROW',attention='C',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBR131(mode='LOOK_ROW',attention='C',memory='A',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be A and the block function here.
    def ruleBR132(mode='LOOK_ROW',attention='C',memory='B',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be B and the block function here.
    def ruleBR133(mode='LOOK_ROW',attention='C',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be C and the block function here.
    def ruleBR134(mode='LOOK_ROW',attention='C',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='D', memory = 'BLANK')
    def ruleBR135(mode='LOOK_ROW',attention='C',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='D', memory = 'BLANK')
    def ruleBR136(mode='LOOK_ROW',attention='C',memory='B',vision='BLANK',scale=1.0/4):
        set(attention='D', memory = 'BLANK')
        
    #Second Row
    #Rules for checking first location.
    def ruleBR211(mode='LOOK_ROW',attention='D',memory='BLANK',vision='X',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='E')
    def ruleBR212(mode='LOOK_ROW',attention='D',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='G')
    def ruleBR213(mode='LOOK_ROW',attention='D',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='D',attention='E')
        
    #Rules for checking second location.
    def ruleBR221(mode='LOOK_ROW',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='F')
    def ruleBR222(mode='LOOK_ROW',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='G')
    def ruleBR223(mode='LOOK_ROW',attention='E',memory='D',vision='BLANK',scale=1.0/4):
        set(attention='G')
    def ruleBR224(mode='LOOK_ROW',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='F')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_ROW',attention='F',memory='BLANK',vision='X',scale=1.0/4): Already Lost  
    def ruleBR231(mode='LOOK_ROW',attention='F',memory='D',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be D and the block function here.
    def ruleBR232(mode='LOOK_ROW',attention='F',memory='E',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the block function here.
    def ruleBR233(mode='LOOK_ROW',attention='F',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be F and the block function here.
    def ruleBR234(mode='LOOK_ROW',attention='F',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='G', memory = 'BLANK')
    def ruleBR235(mode='LOOK_ROW',attention='F',memory='D',vision='BLANK',scale=1.0/4):
        set(attention='G', memory = 'BLANK')
    def ruleBR236(mode='LOOK_ROW',attention='F',memory='E',vision='BLANK',scale=1.0/4):
        set(attention='G', memory = 'BLANK')
    
    #Third Row
    #Rules for checking first location.
    def ruleBR311(mode='LOOK_ROW',attention='G',memory='BLANK',vision='X',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='H')
    def rulebR312(mode='LOOK_ROW',attention='G',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')
    def ruleBR313(mode='LOOK_ROW',attention='G',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='G',attention='H')
        
    #Rules for checking second location.
    def ruleBR321(mode='LOOK_ROW',attention='H',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='I')
    def ruleBR322(mode='LOOK_ROW',attention='H',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Row Checking Complete
    def ruleBR323(mode='LOOK_ROW',attention='H',memory='G',vision='BLANK',scale=1.0/4):
        set(Attention = 'A', memory = 'BLANK') #Row Checking Complete 
    def ruleBR324(mode='LOOK_ROW',attention='H',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='H',attention='I')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_ROW',attention='I',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBR331(mode='LOOK_ROW',attention='I',memory='G',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be G and the block function here.
    def ruleBR332(mode='LOOK_ROW',attention='I',memory='H',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be H and the block function here.
    def ruleBR333(mode='LOOK_ROW',attention='I',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be I and the block function here.
    def ruleBR334(mode='LOOK_ROW',attention='I',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Row Checking Complete ??
    def ruleBR335(mode='LOOK_ROW',attention='I',memory='G',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Row Checking Complete ??
    def ruleBR336(mode='LOOK_ROW',attention='I',memory='H',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Row checking Complete ??

    #Column Checking
    #First Column
    #Rules for checking first location.
    def ruleBC111(mode='LOOK_COL',attention='A',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='D')
    def ruleBC112(mode='LOOK_COL',attention='A',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='B')
    def ruleBC113(mode='LOOK_COL',attention='A',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='A',attention='D')
        
    #Rules for checking second location.    
    def ruleBC121(mode='LOOK_COL',attention='D',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='G')
    def ruleBC122(mode='LOOK_COL',attention='D',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='B')
    def ruleBC123(mode='LOOK_COL',attention='D',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='B')
    def ruleBC124(mode='LOOK_COL',attention='D',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='D',attention='G')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_COL',attention='G',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBC131(mode='LOOK_COL',attention='G',memory='A',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be A and the block function here.
    def ruleBC132(mode='LOOK_COL',attention='G',memory='D',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be D and the block function here.
    def ruleBC133(mode='LOOK_COL',attention='G',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be G and the block function here.
    def ruleBC134(mode='LOOK_COL',attention='G',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='B', memory = 'BLANK')
    def ruleBC135(mode='LOOK_COL',attention='G',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='B', memory = 'BLANK')
    def ruleBC136(mode='LOOK_COL',attention='G',memory='D',vision='BLANK',scale=1.0/4):
        set(attention='B', memory = 'BLANK')
        
    #Second Column
    #Rules for checking first location.
    def ruleBC211(mode='LOOK_COL',attention='B',memory='BLANK',vision='X',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='E')
    def ruleBC212(mode='LOOK_COL',attention='B',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C')
    def ruleBC213(mode='LOOK_COL',attention='B',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='B',attention='E')
        
    #Rules for checking second location.
    def ruleBC221(mode='LOOK_COL',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='H')
    def ruleBC222(mode='LOOK_COL',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C')
    def ruleBC223(mode='LOOK_COL',attention='E',memory='B',vision='BLANK',scale=1.0/4):
        set(attention='C')
    def ruleBC224(mode='LOOK_COL',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='H')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_COL',attention='H',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBC231(mode='LOOK_COL',attention='H',memory='B',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be B and the block function here.
    def ruleBC232(mode='LOOK_COL',attention='H',memory='E',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the g'que' location to be E and the block function here.
    def ruleBC233(mode='LOOK_COL',attention='H',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be H and the block function here.
    def ruleBC234(mode='LOOK_COL',attention='H',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleBC235(mode='LOOK_COL',attention='H',memory='B',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleBC236(mode='LOOK_COL',attention='H',memory='E',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    
    #Third Row
    #Rules for checking first location.
    def ruleBC311(mode='LOOK_COL',attention='C',memory='BLANK',vision='X',scale=1.0/4): #memory option is useless here in first location checks.
        set(attention='F')
    def ruleBC312(mode='LOOK_COL',attention='C',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Column checking Complete ??
    def ruleBC313(mode='LOOK_COL',attention='C',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='C',attention='F')
        
    #Rules for checking second location.
    def ruleBC321(mode='LOOK_COL',attention='F',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='I')
    def ruleBC322(mode='LOOK_COL',attention='F',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Column checking Complete ??
    def ruleBC323(mode='LOOK_COL',attention='F',memory='C',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Column checking Complete ?? 
    def ruleBC324(mode='LOOK_COL',attention='F',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='F',attention='I')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_COL',attention='I',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBC331(mode='LOOK_COL',attention='I',memory='C',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be C and the block function here.
    def ruleBC332(mode='LOOK_COL',attention='I',memory='F',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be F and the block function here.
    def ruleBC333(mode='LOOK_COL',attention='I',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be I and the block function here.
    def ruleBC334(mode='LOOK_COL',attention='I',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Column Checking Complete ??
    def ruleBC335(mode='LOOK_COL',attention='I',memory='C',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Column Checking Complete ??
    def ruleBC336(mode='LOOK_COL',attention='I',memory='F',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Column checking Complete ??
        
    #Diagonal Checking
    #First Diagonal
    #Rules for checking first location.
    def ruleBD111(mode='LOOK_DIA',attention='A',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='E')
    def ruleBD112(mode='LOOK_DIA',attention='A',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C')
    def ruleBD113(mode='LOOK_DIA',attention='A',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='A',attention='E')
        
    #Rules for checking second location.    
    def ruleBD121(mode='LOOK_DIA',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='I')
    def ruleBD122(mode='LOOK_DIA',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C')
    def ruleBD123(mode='LOOK_DIA',attention='E',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='C')
    def ruleBD124(mode='LOOK_DIA',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='I')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_DIA',attention='I',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBD131(mode='LOOK_DIA',attention='I',memory='A',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be A and the block function here.
    def ruleBD132(mode='LOOK_DIA',attention='I',memory='E',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the block function here.
    def ruleBD133(mode='LOOK_DIA',attention='I',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be I and the block function here.
    def ruleBD134(mode='LOOK_DIA',attention='I',memory='BLANK',vision='O',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleBD135(mode='LOOK_DIA',attention='I',memory='A',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
    def ruleBD136(mode='LOOK_DIA',attention='I',memory='E',vision='BLANK',scale=1.0/4):
        set(attention='C', memory = 'BLANK')
        
    #Second Diagonal
    #Rules for checking first location.
    def ruleBD211(mode='LOOK_DIA',attention='C',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='E')
    def ruleBD212(mode='LOOK_DIA',attention='C',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK') #Diagonal Checking done ??
    def ruleBD213(mode='LOOK_DIA',attention='C',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='C',attention='E')
        
    #Rules for checking second location.    
    def ruleBD221(mode='LOOK_DIA',attention='E',memory='BLANK',vision='X',scale=1.0/4):
        set(attention='G')
    def ruleBD222(mode='LOOK_DIA',attention='E',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')#Diagonal Checking Done
    def ruleBD223(mode='LOOK_DIA',attention='E',memory='C',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')#Diagonal Checking done
    def ruleBD224(mode='LOOK_DIA',attention='E',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(memory='E',attention='G')
    
    #Rules for checking third location.
    # def rule(mode='LOOK_DIA',attention='G',memory='BLANK',vision='X',scale=1.0/4): Already Lost   
    def ruleBD231(mode='LOOK_DIA',attention='G',memory='C',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be C and the block function here.
    def ruleBD232(mode='LOOK_DIA',attention='G',memory='E',vision='X',scale=1.0/4)
        set(motor=memory, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be E and the block function here.
    def ruleBD233(mode='LOOK_DIA',attention='G',memory='BLANK',vision='BLANK',scale=1.0/4):
        set(motor=attention, move='BLOCK',memory = 'BLANK')
        #put the code to call the 'que' location to be G and the block function here.
    def ruleBD234(mode='LOOK_DIA',attention='G',memory='BLANK',vision='O',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')#Diagonal Checking done
    def ruleBD235(mode='LOOK_DIA',attention='G',memory='A',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')#Diagonal Checking done
    def ruleBD236(mode='LOOK_DIA',attention='G',memory='E',vision='BLANK',scale=1.0/4):
        set(attention = 'A', memory = 'BLANK')#Diagonal Checking done
    
    #Do Any Move
    def ruleDA51(mode='DO_ANY',attention='E*2',vision='BLANK*2',scale=1.0/3):
        set(motor='E',move='DOANY',attention='E')
    def ruleDA52(mode='DO_ANY',attention='E*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='A')
    def ruleDA11(mode='DO_ANY',attention='A*2',vision='BLANK*2',scale=1.0/3):
        set(motor='A',move='DOANY',attention='A')
    def ruleDA12(mode='DO_ANY',attention='A*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='C')
    def ruleDA31(mode='DO_ANY',attention='C*2',vision='BLANK*2',scale=1.0/3):
        set(motor='C',move='DOANY',attention = 'C')
    def ruleDA32(mode='DO_ANY',attention='C*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='G')
    def ruleDA71(mode='DO_ANY',attention='G*2',vision='BLANK*2',scale=1.0/3):
        set(motor='G', move='DOANY', attention = 'G')
    def ruleDA72(mode='DO_ANY',attention='G*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='J')    
    def ruleDA91(mode='DO_ANY',attention='J*2',vision='BLANK',scale=1.0/3):
        set(motor='J', move='DOANY',attention='J')
    def ruleDA92(mode='DO_ANY',attention='J*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention = 'B')
    def ruleDA21(mode='DO_ANY',attention='B*2',vision='BLANK',scale=1.0/3):
        set(motor='B',move='DOANY',attention='B')
    def ruleDA22(mode='DO_ANY',attention='B*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='D')
    def ruleDA41(mode='DO_ANY',attention='D*2',vision='BLANK',scale=1.0/3):
        set(motor='D',move='DOANY', attention='D')
    def ruleDA42(mode='DO_ANY',attention='D*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='F')
    def ruleDA61(mode='DO_ANY',attention='F*2',vision='BLANK',scale=1.0/3):
        set(motor='F', move='DOANY',attention='F')
    def ruleDA62(mode='DO_ANY',attention='F*2',vision='X+O-BLANK',scale=1.0/3):
        set(attention='H')
    def ruleDA81(mode='DO_ANY',attention='H*2',vision='BLANK',scale=1.0/3):
        set(motor='H', move='DOANY',attention='H')
    def ruleDA82(mode='DO_ANY',attention='H*2',vision='X+O-BLANK',scale=1.0/3):
        set(move = 'NOMOVE')
    

class SimpleModule(module.Module):
    def __init__(self,klass,*args,**params):
        self.klass=klass
        module.Module.__init__(self,**params)
        self.args=args
        self.params=params
    def create(self):
        self.node=self.klass(*self.args,**self.params)
        self.net.add(self.node)
        self.node.module=self
        self.node.spa=self.spa
        if hasattr(self.node,'create'):
            self.node.create()
    def connect(self):
        if hasattr(self.node,'connect'):
            self.node.connect()
            
game=Source.TicTacToe()            
           
class Vision(nef.SimpleNode):
    def origin_item(self):
        if self.t_start<=0: return [0]*dimensions
        
        location=model.attention.net.network.getNode('buffer').getOrigin('X').getValues().getValues()
        
        vocab=model.vocab('vision')
        similarity=list(vocab.dot(location))
        index=similarity.index(max(similarity))
        symbol=vocab.keys[index]
        
        if symbol in 'ABCDEFGHJ':
            # figure out item at location
            item=game.getSymbolAt('ABCDEFGHJ'.index(symbol))
            #System.out.println("In Python "+item)
            if item=='X': return vocab.parse('X').v
            elif item=='O': return vocab.parse('O').v
            else : return vocab.parse('BLANK').v
        else:
            return [0]*dimensions
            
    def origin_current_turn(self):
        if self.t_start<=0: return [0]*dimensions
        vocab=model.vocab('vision')
        if game.getCompMove()==1:
            return vocab.parse('MYMOVE').v
        else:    
            return vocab.parse('-MYMOVE*10').v
        
        
    def create(self):        
        self.module.add_source(self.getOrigin('item'))        
        self.module.add_source(self.getOrigin('current_turn'),'turn')        
     
class Motor(nef.SimpleNode):
    pstc=0.05
    def termination_move(self,x,dimensions=dimensions):
        location=model.attention.net.network.getNode('buffer').getOrigin('X').getValues().getValues()
        vocab=model.vocab('motor')
        similarity=list(vocab.dot(location))
        #print similarity
        if max(similarity)<0.3: return
        index=similarity.index(max(similarity))
        symbol=vocab.keys[index]        
        #print symbol
        if symbol in 'ABCDEFGHJ':
            index='ABCDEFGHJ'.index(symbol)
            if symbol=='A': game.setIndex(index)
            if symbol=='B': game.setIndex(index)
            if symbol=='C': game.setIndex(index)
            if symbol=='D': game.setIndex(index)
            if symbol=='E': game.setIndex(index)
            if symbol=='F': game.setIndex(index)
            if symbol=='G': game.setIndex(index)
            if symbol=='H': game.setIndex(index)
            if symbol=='J': game.setIndex(index)
        else:
            game.setIndex(-1)        
        

class MyModel(SPA):
    dimensions=dimensions
    align_hrrs=True
    
    attention=Buffer()
    mode=Buffer()
    memory=Buffer()
    move=Buffer()
    vision=SimpleModule(Vision,'vision')        
    #motor=SimpleModule(Motor,'motor')
    #vision=Buffer(feedback=0)
    motor=Buffer(feedback=0)   
    BG=BasalGanglia(Rules())
    thal=Thalamus(BG)
    #input=Input(1,attention='A',mode='DO_ANY*2')

model=MyModel('TicTacToe')

motor2=model.net.add(Motor('motor2'))
model.net.connect(model.net.network.getNode('motor').getOrigin('motor'),motor2.getTermination('move'))
model.net.view()

Source.Main().play(game)