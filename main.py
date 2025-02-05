import requests

class weatherApp:
    def __init__(self):
        self.city = input("Enter the city: ")
        self.apiKey = "59f90efbb6009c6032689d23ad946c3c"
        self.url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.apiKey}&units=metric&lang=eng"

        
    def main(self):
        self.cevap = requests.get(self.url)  
        self.data = self.cevap.json()
        self.temperature = self.data["main"]["temp"]
        self.weather = self.data["weather"][0]["description"]
        
        print(f"Today, {self.city} is {self.weather} , {self.temperature} degree celcius")
        
        
        
if __name__ == "__main__":
    wA = weatherApp()
    wA.main()
        
        
    