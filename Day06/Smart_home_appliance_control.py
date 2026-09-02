class SmartThermostat:

    MIN_TEMP = 10.0
    MAX_TEMP = 35.0
   
    def __init__(self,appliance_name , initial_temp=22.0 ):
        self.__appliance_name = appliance_name

        if self.MIN_TEMP <= initial_temp <= self.MAX_TEMP:
            self.__target_temp = initial_temp

        else:
            self.__target_temp = 22.0

    @property
    def target_temp(self):
        return self.__target_temp

    @target_temp.setter
    def target_temp(self , new_temp):

        if self.MIN_TEMP <= new_temp <= self.MAX_TEMP:
            self.__target_temp = new_temp
        
        else:
            raise ValueError("Error")



    @property
    def appliance_name(self):
        return self.__appliance_name

thermostat = SmartThermostat("Living Room AC", 24.0)
print(thermostat.appliance_name)  # Output: Living Room AC
print(thermostat.target_temp)     # Output: 24.0

thermostat.target_temp = 28.0     # Updates successfully
print(thermostat.target_temp)     # Output: 28.0

try:
    thermostat.target_temp = 5.0  # Out of range!
except ValueError as e:
    print(e)  # Output: Temperature must be between 10.0 and 35.0 degrees.