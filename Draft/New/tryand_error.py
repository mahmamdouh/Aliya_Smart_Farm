from Correct_Filter import Correct_factor_runable

Factor_value = 2
# initializing dictionary
test_dict = {
"Sensor 1" :40.5,
"Sensor 2" :210.1,
"Sensor 3" :19,
"Sensor 4" :20.5,
"Sensor 5" :21,
"Sensor 6" :32.9,
}
  

new_Dictionary = Correct_factor_runable(test_dict, Factor_value)
print("filter ",new_Dictionary)
'''
new_Dictionary2 = Correct_factor_runable(new_Dictionary, Factor_value)
print("filter 2",new_Dictionary2)
new_Dictionary3 = Correct_factor_runable(new_Dictionary2, Factor_value)
print("filter 3",new_Dictionary3)
new_Dictionary4 = Correct_factor_runable(new_Dictionary3, Factor_value)
print("filter 4",new_Dictionary4)
'''