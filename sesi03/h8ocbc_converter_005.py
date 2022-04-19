def fromCelcius(toUnit, number):  #converter untuk celcius
    if (toUnit == 'k' or toUnit == 'K'):  #ke kelvin
        return (number + 273.15)
    elif (toUnit == 'f' or toUnit == 'F'):  #ke fahrenheit
        return (number * (9 / 5) + 32)
    else:
        return "Nothing to convert."


def fromKelvin(toUnit, number):  #converter untuk kelvin
    if (toUnit == 'c' or toUnit == 'C'):  #ke celcius
        return (number - 273.15)
    elif (toUnit == 'f' or toUnit == 'F'):  #ke fahrenheit
        return ((number - 273.15) * (9 / 5) + 32)
    else:
        return "Nothing to convert."


def fromFahrenheit(toUnit, number):  #converter untuk fahrenheit
    if (toUnit == 'c' or toUnit == 'C'):  #ke celcius
        return ((number - 32) * (5 / 9))
    elif (toUnit == 'k' or toUnit == 'K'):  #ke kelvin
        return ((number - 32) * (5 / 9) + 273.15)
    else:
        return "Nothing to convert."


def convertTempUnit(input, output, number):  #converter utama
    if (input == 'c' or input
            == 'C'):  #kondisi temperatur unit yang mau di ubah apabila celcius
        return print(
            fromCelcius(output, number),
            output.capitalize())  #print hasil dari function converter celcius
    elif (input == 'k' or input
          == 'K'):  #kondisi temperatur unit yang mau di ubah apabila kelvin
        return print(
            fromKelvin(output, number),
            output.capitalize())  #print hasil dari function converter kelvin
    elif (input == 'f' or input == 'F'
          ):  #kondisi temperatur unit yang mau di ubah apabila fahrenheit
        return print(fromFahrenheit(output, number), output.capitalize()
                     )  #print hasil dari function converter fahrenheit
    else:
        return print("Wrong Parameters.")  #apabila inputan parameter salah


temperature = 'C'
number = 27

convertTempUnit(temperature, 'k', number)
convertTempUnit('k', 'C', 270.372)
convertTempUnit('c', 'f', 32)
convertTempUnit('f', 'c', 76)