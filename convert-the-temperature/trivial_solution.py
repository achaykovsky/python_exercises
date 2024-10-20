from typing import List


def convertTemperature(celsius: float) -> List[float]:
    kelvin = celsius + 273.15
    fahrenheit = celsius * 1.80 + 32.00
    return [round(kelvin, 5), round(fahrenheit, 5)]


if __name__ == '__main__':
    celsius = 36.50
    result = convertTemperature(celsius)
    print(result)
