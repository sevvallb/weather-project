# Weather and Daily Outfit Recommendation Bot

This project is a simple Python application that retrieves real-time weather data for a specified city and provides clothing recommendations based on temperature and weather conditions using the OpenWeather API.

## 🚀 Features
•⁠  ⁠Fetches real-time weather data from the OpenWeather API.
•⁠  ⁠Provides clothing recommendations based on temperature and weather conditions.
•⁠  ⁠Handles errors such as invalid city names.
•⁠  ⁠(Optional) Can be integrated as a Telegram/Discord bot.

## 🛠️ Requirements

Before running the project, make sure you have the following dependencies installed:

•⁠  ⁠Python 3.x
•⁠  ⁠⁠ requests ⁠ module (for HTTP requests)

To install the required packages:
⁠ sh
pip install requests
 ⁠

## 🔧 Installation & Usage

1.⁠ ⁠*Get an OpenWeather API Key*
   - Visit [OpenWeather](https://openweathermap.org/api) and obtain a free API key.
   
2.⁠ ⁠*Clone the Repository*
⁠ sh
git clone https://github.com/sevvallb/weather-project.git
cd weather-project
 ⁠

3.⁠ ⁠*Add Your API Key*
   - Create a ⁠ config.py ⁠ file and add the following line:
⁠ python
API_KEY = "your_api_key"
 ⁠

4.⁠ ⁠*Run the Script*
⁠ sh
python main.py
 ⁠

5.⁠ ⁠*Enter a City Name and Get Recommendations*
   - Enter the city name in the terminal and receive weather-based recommendations:

Enter city name: Istanbul
Weather: Sunny, 25°C
Recommendation: Wear light clothes and don't forget your sunglasses!


## 📌 Future Improvements
•⁠  ⁠Integration with Telegram and Discord bots.
•⁠  ⁠More detailed weather analysis.
•⁠  ⁠Saving and viewing past weather data.

## 👨‍💻 Contributing
Feel free to submit a Pull Request (PR) for any improvements. For any issues, open an Issue!

---

📩 *Contact:*
sevvalbolukbass@gmail.com
