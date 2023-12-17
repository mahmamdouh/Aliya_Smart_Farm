from Correct_Filter import Correct_factor_runable

Factor_value = 2
# initializing dictionary
test_dict = {"Sensor1" : 30,
             "Sensor2" : 33,
             "Sensor3" : 32,
             "Sensor4" : 29,
             "Sensor5" : 25,	 
             "Sensor6" : 20,	 
			 }
  

new_Dictionary = Correct_factor_runable(test_dict, Factor_value)
print(new_Dictionary)


