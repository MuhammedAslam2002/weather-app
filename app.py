from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Get the API key from environment variables
API_KEY = os.getenv("OPENWEATHER_API_KEY")

@app.route('/')
def home():
    return "Welcome to the Weather Info App! Use /weather?city=<city_name> to get weather details."

@app.route('/weather', methods=['GET'])
def weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "City name is required!"}), 400

    # Fetch weather data
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return jsonify({
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "weather": data["weather"][0]["description"]
        })
    else:
        return jsonify({"error": "Could not fetch weather data"}), response.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
