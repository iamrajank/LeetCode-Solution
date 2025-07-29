class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        temp = []
        celsius_to_fahrenheit = (celsius * 9 / 5) + 32
        celsius_to_kelvin = celsius + 273.15

      
        temp.append(celsius_to_kelvin)
        temp.append(celsius_to_fahrenheit)
        return temp
        