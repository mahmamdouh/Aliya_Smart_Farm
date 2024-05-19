MAKE_DIR = $(PWD)
current_dir = $(shell pwd)
OK = $(COLOR_ON)"Build successfuly!"

#----------------------------------------------------------------#
#Targets Directories 
#----------------------------------------------------------------#
#main targets
MAIN_DIR           := $(current_dir)/Main
MAIN_TARGET        := $(current_dir)/Main/ASF.o
#****************************************************************#
#App targets
HVAC_DIR           := $(current_dir)/App/HVAC
HVAC_TARGET        := $(current_dir)/App/HVAC/HVAC.o

#****************************************************************#
#BSW targets
SENSOR_H_DIR       := $(current_dir)/BSW/Sensor_Stack
SENSOR_H_TARGET    := $(current_dir)/BSW/Sensor_Stack/Sensor_H.o
DIAG_DIR           := $(current_dir)/BSW/DIAG_Stack
DIAG_TARGET        := $(current_dir)/BSW/DIAG_Stack/Diag.o

#****************************************************************#
#MCAL targets

#****************************************************************#
#LIB targets



#----------------------------------------------------------------#
#INFO 
#----------------------------------------------------------------#
$(info ---------------- Aliya Smart farm project ------------------)

$(info current DIR $(MAIN_DIR))

#----------------------------------------------------------------#
#Build targets 
#----------------------------------------------------------------#
ALL:
	$(info ---------------- Build all Targets ------------------)
	@$(MAKE) -C $(MAIN_DIR) -f ASF_makefile
	$(info ---------------- Main ===== $(OK))
	@$(MAKE) -C $(SENSOR_H_DIR) -f Sensor_H_makefile
	$(info ---------------- SENSOR_H ===== $(OK))
	@$(MAKE) -C $(DIAG_DIR) -f Diag_makefile
	$(info ---------------- DIAG_H ===== $(OK))
	@$(MAKE) -C $(HVAC_DIR) -f HVAC_makefile
	$(info ---------------- HVAC ===== $(OK))

#----------------------------------------------------------------#
#Build Layers 
#----------------------------------------------------------------#
MAIN:
	$(info ---------------- Build MAIN ------------------)
	@$(MAKE) -C $(MAIN_DIR) -f ASF_makefile
APP:
	$(info ---------------- Build application ------------------)
	@$(MAKE) -C $(HVAC_DIR) -f HVAC_makefile
BSW:
	$(info ---------------- Build BSW ------------------)
	@$(MAKE) -C $(SENSOR_H_DIR) -f Sensor_H_makefile
	@$(MAKE) -C $(DIAG_DIR) -f Diag_makefile
#MCAL:
#LIB:

#----------------------------------------------------------------#
#Build ASF 
#----------------------------------------------------------------#
ASF: $(MAIN_TARGET) $(DIAG_TARGET) $(HVAC_TARGET) $(SENSOR_H_TARGET)
	g++ $(MAIN_TARGET) $(DIAG_TARGET) $(HVAC_TARGET) $(SENSOR_H_TARGET) -o ASF_App
	
clean:
	@$(MAKE) -C $(MAIN_DIR) -f ASF_makefile clean
	@$(MAKE) -C $(SENSOR_H_DIR) -f Sensor_H_makefile clean
	@$(MAKE) -C $(HVAC_DIR) -f HVAC_makefile clean
	@$(MAKE) -C $(DIAG_DIR) -f Diag_makefile clean
	rm ASF_App
	
target: deoendencies
	actions
	