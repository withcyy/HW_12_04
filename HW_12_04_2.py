class TemperatureSensor:
    def __init__(self, min_temp, max_temp):
        self._temperature = None
        self.min_temp = min_temp
        self.max_temp = max_temp

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        if self.min_temp <= value <= self.max_temp:
            self._temperature = value
        else:
            print(f"Error: Temperature value {value} is out of range [{self.min_temp}, {self.max_temp}].")

sensor = TemperatureSensor(min_temp=-20, max_temp=40)

sensor.temperature = 25
print("Current temperature:", sensor.temperature)

