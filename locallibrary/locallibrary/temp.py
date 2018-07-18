class Celsius:
    def __init__(self, temperature = 0):
        self._temperature  = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temp(self):
        print("Getting value")
        return self._temperature

    @temp.setter
    def temp(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

c = Celsius()
print(c.temp)
c.temp = 38
