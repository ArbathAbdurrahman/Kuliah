def ftk(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return print(f"{'='*40}\n{fahrenheit} F = {kelvin} K\n{'='*40}\n")