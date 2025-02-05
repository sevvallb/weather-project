import requests

class weatherApp:
    def __init__(self, city):
        self.city = city
        self.apiKey = "59f90efbb6009c6032689d23ad946c3c"
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apiKey}&units=metric&lang=eng"

    def get_weather(self):   
        self.cevap = requests.get(self.url)  
        self.data = self.cevap.json()
        self.temperature = self.data["main"]["temp"]
        self.weather = self.data["weather"][0]["description"]
    
    def display_weather(self):    
        print(f"Today, {self.city} is {self.weather} , {self.temperature} degree celcius")
        
    def clothes_suggest(self):
        if "rain" in self.weather:
            if float(self.temperature) > 20.0 :
                print("You need to take your umbrella and you can wear your t-shirt")
            elif 10 < float(self.temperature) < 20.0:
                print("You need to take your jacket and umbrella")
            elif float(self.temperature) < 10:
                print("You need to take your coat and umbrella")
                
        if "sun" in self.weather:
            if float(self.temperature) > 20.0 :
                print("You can wear your shorts and sun glasses")
            elif 10 < float(self.temperature) < 20.0:
                print("You can wear your denim jacket and sun glasses")
            elif float(self.temperature) < 10:
                print("You can take your trench coat")
                
        if "snow" in self.weather:
            if float(self.temperature) > 20.0 :
                print("You can wear your jacket.")
            elif 10 < float(self.temperature) < 20.0:
                print("You can wear your trench coat")
            elif float(self.temperature) < 10:
                print("You need to take your coat and boots")
        
        if "cloud" in self.weather:
            if float(self.temperature) > 20.0 :
                print("You can wear your shirt")
            elif 10 < float(self.temperature) < 20.0:
                print("You can wear your trench coat")
            elif float(self.temperature) < 10:
                print("You need to take your coat")
         

    def main(self):
        self.get_weather()
        self.display_weather()
        self.clothes_suggest()
        
    
if __name__ == "__main__":
    city = input("Enter the city: ")
    wA = weatherApp(city)
    wA.main()
      
      
  
        
    