# ETS2 Pro Tablet Dashboard 🚚💨

A high-fidelity, professional digital dashboard for **Euro Truck Simulator 2 (ETS2)**, designed specifically for tablet usage via **Spacedesk**. Built with a Flask backend and a clean, realistic TFT-style frontend.

![Dashboard Preview](https://img.shields.io/badge/ETS2-Telemetry-blue) ![Flask](https://img.shields.io/badge/Flask-Python-green) ![Status](https://badge.fury.io/gh/username%2Fets2-dashboard.svg)

---

## ✨ Features

- **Realistic Gauge Graphics**: High-resolution generated gauge faces featuring accurate scales (Speedometer up to 140 km/h, Tachometer up to 30 x1000 RPM with a realistic redline, Fuel, and Engine Temperature).
- **TFT Onboard Computer**: A clean, modern central digital display showing the active gear (`N`, `R`, numbers) and Cruise Control status.
- **Live Telemetry Sync**: Real-time polling via Funbit's ETS2 Telemetry Web Server with smooth needle animations.
- **Blinker Indicators**: Synchronized left and right turn signal indicators.
- **Tablet Optimized**: Designed to run seamlessly as a secondary screen using Spacedesk.

---

## 🛠️ Prerequisites

1. **Euro Truck Simulator 2** installed on your PC.
2. **Funbit ETS2 Telemetry Web Server** running locally (default port: `25555`).
3. **Python 3.x** installed on your system.
4. **Spacedesk** (or any web-based second screen tool) to display the dashboard on your tablet.

---

## 📦 Project Structure

```text
ets2-dashboard/
│
├── main.py                 # Flask backend server (polls ETS2 telemetry)
├── generate_images.py      # Automated script to generate high-res gauge assets
├── static/
│   └── img/                # Generated gauge PNG graphics (speed, rpm, fuel, temp)
└── templates/
    └── index.html          # Frontend dashboard UI & polling logic
