# importing sys
import sys
# adding Folder_2 to the system path
sys.path.insert(0, '/components/IO driver')
from IO driver import Heater_1_ON,Heater_2_ON,Collar_1_OFF,Collar_2_OFF,Heater_1_OFF,Heater_2_OFF,Collar_1_ON,Collar_2_ON

# Temp limits
Temp_Lw_limit = 25
Temp_Up_limit = 30

# Hmid limits
Humid_Lw_limit = 10
Humid_Up_limit = 40

# temp now

def Hvac_control(Temp , Humid):
    # check temp exceed upper limit
    if(Temp > Temp_Up_limit ):
        Heater_1_ON()
        Heater_2_ON()
        Collar_1_OFF()
        Collar_2_OFF()

    if (Temp < Temp_Lw_limit):
        Heater_1_OFF()
        Heater_2_OFF()
        Collar_1_ON()
        Collar_2_ON()

    if(Humid > Humid_Up_limit ):
        # allarm of Humid
        print ("humis excced upper limit ")


    if (Humid < Humid_Lw_limit):
        # allarm of Humid
        print("humis decced lowwer limit ")






# update limits of temp
def Hvac_Set_Limits(TL,TU,HL,HU):
    # Temp limits
    Temp_Lw_limit = TL
    Temp_Up_limit = TU

    # Hmid limits
    Humid_Lw_limit = HL
    Humid_Up_limit = HU

#Get temp limits
def Hvac_Get_Limits():
    return Temp_Lw_limit , Temp_Up_limit , Humid_Lw_limit , Humid_Up_limit




