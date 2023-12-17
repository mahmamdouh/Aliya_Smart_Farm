/*       
       UART communication
       send/receive byte array (64 bytes)
       
       Arduino Due slave
       ver uartmux0001
       
 */

 
// (C) Helmut Wunder (HaWe) 2015
// freie Verwendung für private Zwecke
// für kommerzielle Zwecke nur nach Genehmigung durch den Autor.
// Programming language: Arduino Sketch C/C++ (IDE 1.6.1 - 1.6.5)
// protected under the friendly Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License
// http://creativecommons.org/licenses/by-nc-sa/3.0/




#define SYNCSLOT      0  // start sync signal of this Msg: bsync  (e.g. 0xff/255)
#define CKSSLOT       1  // chksum this Msg
#define BYTE0         2  // byte 0      // byte: 8-bit => 8 digital bits 0-7
#define BYTE1         3  // byte 1      // byte: 8-bit => 8 digital bits 8-15
#define INT0          4  // int0        // 3x long: 32-bit/4byte
#define INT1          8  // int1
#define INT2         12  // int2
#define DOUBL0       16  // double0     // 2x double 64bit/8byte
#define DOUBL1       24  // double1
#define FLOAT0       32  // float0      // 3x float 32bit/4byte
#define FLOAT1       36  // float1
#define FLOAT2       40  // float2
#define ANA0         44  // analog 0    // 9x ananog (ADC) 16-bit/2byte
#define ANA1         46  // analog 1    
#define ANA2         48  // analog 2
#define ANA3         50  // analog 3
#define ANA4         52  // analog 4
#define ANA5         54  // analog 5
#define ANA6         56  // analog 6
#define ANA7         58  // analog 7
#define ANA8         60  // analog 8
#define BYTE2        62  // byte 2      //  1 byte custom
#define TERM         63  // terminating //  1 byte custom 

//=====================================================================================

const    uint8_t  MSGSIZE=64;
uint8_t  bsync=255;
uint8_t  bterm=254;
uint8_t  sendbuf[MSGSIZE];
uint8_t  recvbuf[MSGSIZE];


//=====================================================================================

const uint32_t UARTclock = 115200;

//=====================================================================================

void displayvalues(char * caption, uint8_t array[]) {
  int cnt;
  char sbuf[128];
 
  sprintf(sbuf, "%s ", caption);  
  Serial.println(sbuf);
  for(cnt=0; cnt<8; ++cnt) {
    if(cnt%8==0) Serial.println();
    sprintf(sbuf, "%3d ", array[cnt]);      // print on TFT
    Serial.print(sbuf);                      // Print sendbufue to the Serial Monitor
  }   
  Serial.println(); 
 
} 


//=====================================================================================
// serial transmission

uint8_t calcchecksum(uint8_t array[]) {
  int32_t  sum=0;
  for(int i=2; i<MSGSIZE; ++i) sum+=(array[i]);
  return (sum & 0x00ff);
}

#define  checksumOK(array)  (calcchecksum(array)==array[1]) 


// ================================================================
// addToBuffer and receive function courtesy of chucktodd

bool addToBuffer( uint8_t buf[], uint8_t *cnt, uint16_t timeout){
bool inSync = *cnt>0;
unsigned long start=millis();
while((*cnt<MSGSIZE)&&(millis()-start<timeout)){
  if(Serial1.available()){ // grab new char, test for sync char, if so start adding to buffer
    buf[*cnt] = (uint8_t)Serial1.read();
    if(inSync) *cnt += 1;   
    else{
     if(buf[*cnt]==bsync){
       inSync = true;
       *cnt +=1;
       }
     }
    }
  }
return (*cnt==MSGSIZE);
}


//=====================================================================================

bool receive(uint8_t * buf, uint16_t timeout, uint8_t *cnt){ // by passing cnt in and out,
// i can timeout and still save a partial buffer, so a resync costs less (less data lost)

bool inSync=false;
unsigned long start=millis();
uint8_t * p;  // pointer into buf for reSync operation
bool done=false;

do{
  done = addToBuffer(buf,cnt,timeout); // if this return false, a timeout has occured, and the while will exit.
  if(done){ // do checksumOK test of buffer;
    done=checksumOK(buf);
    if(!done){// checksumOK failed, scan buffer for next sync char
       p = (uint8_t*)memchr((buf+1),bsync,(MSGSIZE-1));         
       
       if(p){ // found next sync char, shift buffer content, refill buffer
         *cnt = MSGSIZE -(p-buf); // count of characters to salvage from this failure
         memcpy(buf,p,*cnt); //cnt is now where the next character from Serial is stored!
         }
       else *cnt=0; // whole buffer is garbage
       }
    }
   
  }while(!done&&(millis()-start<timeout));

return done; // if done then buf[] contains a sendbufid buffer, else a timeout occurred
}

//=====================================================================================
//=====================================================================================

void loop()
{ 
  char     sbuf[128],  resOK;   
  static   uint8_t cnt=0; 
  uint8_t  cbuf[MSGSIZE], chk;
 

  //     Receive from master 

  memset(cbuf, 0, sizeof(cbuf)); 
   
  resOK = receive ( cbuf, 10000,&cnt);
 
  if( resOK ) {                                      // byte 0 == syncbyte ?
    cnt=0;

    //displayvalues(60, "Received...:", cbuf);
     chk=(byte)calcchecksum(cbuf);     
     memcpy(recvbuf, cbuf, sizeof(cbuf));
 
        // change values to send back!
        memcpy(sendbuf, recvbuf, sizeof(sendbuf));   // copy inbuf to outbuf
        sendbuf[4]+=1;                               // change [6] to send back 
        sendbuf[6]+=1;                               // change [6] to send back    
  }


 
  //   send to master 
 
  //Serial.println(); 
  sendbuf[0]=bsync;
  sendbuf[1]=calcchecksum(sendbuf);
  for(uint8_t i=0; i<MSGSIZE; i++) {       
     Serial1.write(sendbuf[i]);                      // Send value to the Rx Arduino       
  }       
  //Serial1.flush();                                 // clear output buffer
  //displayvalues(20, "Transmitted...: ", sendbuf);
  sprintf(sbuf, "recieve: %4d %4d     send: %4d %4d", recvbuf[4], recvbuf[6], sendbuf[4], sendbuf[6]);
  Serial.println(sbuf); 
 
}


//=====================================================================================



void setup() {
   char sbuf[128];   
   int32_t  i=0;

               
   // Serial
   Serial.begin(115200);   // USB terminal
 
   Serial1.begin(UARTclock);                    // RX-TX UART
   while(Serial1.available())  Serial1.read();  // clear output buffer
    
   sprintf(sbuf, "setup(): done.");
   Serial.println(); Serial.println(sbuf);   
 
   sprintf(sbuf, "Rx slave, BAUD= %ld", UARTclock );;

}

//=====================================================================================
