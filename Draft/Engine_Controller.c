// Online C compiler to run C program online
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Macros
#define WITH_ENGINE_TEMP_CONTROLLER 1
#define vehicle_ON 1
#define vehicle_Off 2
#define Quit 3
#define AC_ON 1
#define AC_OFF 0

// Function prototype
void Menue_1(void);
void Mode_Switch(int mode);
void Sensors_set_menu(void);
void Syetem_status(void);

// Global variable 
int mode ;
int Sensor_Menue  ;

struct Engine
{
   int traffic_light;
   int vehicle_speed;
   int Room_temperature;
   int Engine_temperature;
   int AC_status;
   int Eng_Temp_Controller_Status;
}Parameters;



//========================
int main() {
    while(1)
    {
    Menue_1();
    Mode_Switch(mode);
    Syetem_status();
    }
    printf("End of main\n");
    return 0;
}

void Menue_1(void)
{
    printf("1. Turn on the vehicle engine\n");
    printf("2. Turn off the vehicle engine\n");
    printf("3. Quit the system\n");
    printf("Select Mode: ");
    scanf("%d", &mode);  
    system("clear");
}

void Mode_Switch(int mode)
{
    switch(mode)
    {
    case vehicle_ON:
    printf("System Status :vehicle_ON \n");
    Sensors_set_menu();
    break;
    
    case vehicle_Off:
    mode = 2 ;
    printf("System Status :vehicle_Off \n");
    Menue_1();
    break;
    
    case Quit:
    printf("System Status : Quit the system \n");
       // End program 
       exit(0);
     break;
     
     default:
      printf("Not valid option\n");
      Mode_Switch(mode);
    }
}

void Sensors_set_menu(void)
{
    printf("1. Turn off the engine \n");
    printf("2. Set the traffic light color. \n");
    printf("3. Set the room temperature (Temperature Sensor) \n");
    #ifdef WITH_ENGINE_TEMP_CONTROLLER
    printf("4. Set the engine temperature (Engine Temperature Sensor) \n");
    #endif
    printf("5. Done of setting all parameters \n");
    printf("Select Sensor_Menue: ");
    scanf("%d", &Sensor_Menue); 
    switch(Sensor_Menue)
    {
    case 1:
    system("clear");
    printf("System Status :vehicle_Off \n");
    Menue_1();
    break;
    
    case 2: // Trafic Light Setting 
    system("clear");
    printf("2. Set the traffic light color. \n");
    printf("Set Trafic Light \n 1.G \n 2.O \n 3.R  \n");
    scanf("%d", &(Parameters.traffic_light));
    if (Parameters.traffic_light == 1)
    {
        Parameters.vehicle_speed = 100;
    }
    else if (Parameters.traffic_light == 2)
    {
      Parameters.vehicle_speed = 30 ;
    }
    else if (Parameters.traffic_light == 3)
    {
      Parameters.vehicle_speed = 0  ;
    }
    Sensors_set_menu();
    break;
    
    case 3: // Room Temprature 
    system("clear");
    printf("3. Set the room temperature (Temperature Sensor)\n");
    system("clear");
    printf("Set the room temperature:\n");
    scanf("%d", &(Parameters.Room_temperature));
    if (Parameters.Room_temperature < 10)
    {
        Parameters.AC_status = AC_ON ;
        Parameters.Room_temperature = 20;
    }
     else if (Parameters.Room_temperature > 30)
     {
         Parameters.AC_status = AC_ON ;
         Parameters.Room_temperature = 20;
     }
     else
     {
         Parameters.AC_status = AC_OFF ;
         
     }
    Sensors_set_menu();
     break;
     #ifdef WITH_ENGINE_TEMP_CONTROLLER
    case 4:// Engine Temp
    system("clear");
    printf("4. Set the engine temperature (Engine Temperature Sensor) \n");
    scanf("%d", &(Parameters.Engine_temperature));
    if (Parameters.Engine_temperature < 100)
    {
        Parameters.Eng_Temp_Controller_Status = AC_ON ;
        Parameters.Room_temperature = 125;
    }
     else if (Parameters.Engine_temperature > 150)
     {
         Parameters.Eng_Temp_Controller_Status = AC_ON ;
         Parameters.Engine_temperature = 125;
     }
     else
     {
         Parameters.Eng_Temp_Controller_Status = AC_OFF ;
         
     }
    Sensors_set_menu();
     break;
     #endif
     case 5:
      break;
     default:
      printf("Not valid option\n");
      Sensors_set_menu();
    }
    
    // check vehicle speed 
    if (Parameters.vehicle_speed == 30)
    {
        #ifdef WITH_ENGINE_TEMP_CONTROLLER
        Parameters.Eng_Temp_Controller_Status = AC_ON ;
        Parameters.Engine_temperature = Parameters.Engine_temperature*(5/4) + 1;
        #endif
    Parameters.AC_status = AC_ON ;
    Parameters.Room_temperature = Parameters.Room_temperature*(5/4) + 1;
        
    }
    
}

void Syetem_status(void)
{
     printf("System Status : \n");
     printf("\ni. Engine state: ON/OFF:");
     if (mode == 1)
     {
         printf("ON\n");
     }
     else if(mode == 2)
     {
         printf("OFF\n");
     }
     printf("\nii. AC status:");
     if (Parameters.AC_status == 1)
     {
         printf("ON\n");
     }
     else if(Parameters.AC_status == 0)
     {
         printf("OFF\n");
     }
     printf("\niii. Vehicle Speed:%d \n",Parameters.vehicle_speed);
     
     printf("\niv. Room Temperature :%d \n",Parameters.Room_temperature);
     
     #ifdef WITH_ENGINE_TEMP_CONTROLLER
     printf("\nv. Engine Temperature Controller State:");
     if (Parameters.Eng_Temp_Controller_Status == 1)
     {
         printf("ON\n");
     }
     else if(Parameters.Eng_Temp_Controller_Status == 0)
     {
          printf("OFF\n");
     }
     printf("\nvi. Engine Temperature:%d \n",Parameters.Engine_temperature);
     #endif

}