
output: ASF.o Diag_H.o HVAC.o Sensor_H.o
	g++ ASF.o Diag_H.o HVAC.o Sensor_H.o -o output

ASF.o: ASF.cpp
	g++ -c ASF.cpp
	
Diag_H.o: Diag_H.cpp Diag_H.h
	g++ -c Diag_H.cpp Diag_H.h
	
HVAC.o: HVAC.cpp HVAC.h
	g++ -c HVAC.cpp HVAC.h
	
Sensor_H.o: Sensor_H.cpp Sensor_H.h
	g++ -c Sensor_H.cpp Sensor_H.h

clean:
	rm *.o output
	
target: deoendencies
	actions
	