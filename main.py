from flask import Flask, render_template, jsonify
import urllib.request
import json

app = Flask(__name__)

ETS2_API_URL = "http://localhost:25555/api/ets2"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def get_data():
    try:
        req = urllib.request.Request(ETS2_API_URL, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=0.5) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            truck = data.get('truck', {})
            controls = data.get('controls', {})
            
            speed_kmh = max(0, int(truck.get('speed', 0.0)))
            rpm = int(truck.get('engineRpm', 0))
            fuel = truck.get('fuel', 0)
            temp = truck.get('engineTemperature', 0)
            
            raw_gear = truck.get('displayedGear', 0)
            if raw_gear == 0:
                gear_str = 'N'
            elif raw_gear < 0:
                gear_str = f'R{abs(raw_gear)}'
            else:
                gear_str = str(raw_gear)

            cc_on = truck.get('cruiseControlOn', False)
            cc_speed = int(truck.get('cruiseControlSpeed', 0) * 3.6) if cc_on else 0
            
            blinker_left = controls.get('blinkerLeftActive', False)
            blinker_right = controls.get('blinkerRightActive', False)

            return jsonify({
                'connected': True,
                'speed': speed_kmh,
                'rpm': rpm,
                'fuel': fuel,
                'temp': temp,
                'gear': gear_str,
                'cruise_speed': cc_speed,
                'cruise_on': cc_on,
                'blinker_left': blinker_left,
                'blinker_right': blinker_right
            })
    except Exception as e:
        return jsonify({
            'connected': False,
            'speed': 0,
            'rpm': 0,
            'fuel': 0,
            'temp': 0,
            'gear': '---',
            'cruise_speed': 0,
            'cruise_on': False,
            'blinker_left': False,
            'blinker_right': False
        })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)