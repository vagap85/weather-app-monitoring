from flask import Flask, render_template, jsonify
import os
import time
import random

app = Flask(__name__)
CITY = os.getenv('CITY', 'Moscow')

# Счетчики для метрик
request_count = 0
start_time = time.time()


@app.route('/')
def index():
    global request_count
    request_count += 1

    weather = {
        'city': CITY,
        'temperature': round(random.uniform(10, 25), 1),
        'feels_like': round(random.uniform(8, 23), 1),
        'humidity': random.randint(40, 80),
        'pressure': random.randint(990, 1020),
        'wind_speed': round(random.uniform(1, 10), 1),
        'description': random.choice(['ясно', 'облачно', 'солнечно']),
        'icon': '01d'
    }
    return render_template('index.html', weather=weather)


@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'city': CITY,
        'service': 'weather-app',
        'uptime': time.time() - start_time,
        'requests': request_count
    })


@app.route('/metrics')
def metrics():
    """Простая конечная точка с метриками в формате Prometheus"""
    current_time = time.time()
    metrics_text = f"""# HELP weather_app_uptime_seconds Application uptime in seconds
# TYPE weather_app_uptime_seconds gauge
weather_app_uptime_seconds {current_time - start_time}

# HELP weather_app_requests_total Total number of requests
# TYPE weather_app_requests_total counter
weather_app_requests_total {request_count}

# HELP weather_app_info Application information
# TYPE weather_app_info gauge
weather_app_info{{app="weather", city="{CITY}"}} 1
"""
    return metrics_text, 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    print("=" * 50)
    print("🌤️  Погодное приложение с мониторингом")
    print(f"📍 Город: {CITY}")
    print("🌐 Главная: http://0.0.0.0:5000")
    print("❤️  Health: http://0.0.0.0:5000/health")
    print("📊 Метрики: http://0.0.0.0:5000/metrics")
    print("=" * 50)

    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)