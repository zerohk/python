def city_country(city,country):
    return '"' + city + "," + country + '"'
    
first = city_country("Beijing","China")
second = city_country("Tokyo","Japan")
third = city_country("Moscow","Russia")

print(first)
print(second)
print(third)
