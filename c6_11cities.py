
cities = {
                "beijing":{
                "country":"china",
                "population":"30million",
                "fact":"capital of China"
                },
                "shanghai":{
                "country":"china",
                "population":"20million",
                "fact":"finicial center of China"
                },
                "shenzhen":{
                "country":"china",
                "population":"25million",
                "fact":"economical district"
                }
            }
            
for city,info in cities.items():
    print("The information about " + city)
    print(info)
