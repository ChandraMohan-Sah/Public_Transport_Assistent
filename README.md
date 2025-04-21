# 🚌 Public Transport Assistant

A GPS-based smart public transport tracking system that enables real-time location updates, estimated time of arrival prediction, and route/fare visualization through a dynamic web interface.

---

## 🚀 Features

- 📡 Real-Time Bus Tracking — Uses GPS and GSM modules to transmit live location via ThingSpeak Server.  
- 🧭 ETA Prediction — Integrated Deep Neural Network model for predicting Estimated Time of Arrival using historical GPS data.  
- 🌐 Interactive Web Interface — Displays live location, route map, fare price, and bus status using Django + WebSocket.  
- 🛠️ Arduino-Powered Hardware — Built using Arduino Mega, GPS module, and SIM800L GSM for seamless communication.  
- 🧾 Route & Fare Info — Easily visualizes stop points and fare details for users.

---

## ⚙️ Installation & Setup

Follow the steps to run the web interface locally:

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/public-transport-assistant.git
cd public-transport-assistant

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# 3. Install required packages
pip install -r requirements.txt

# 4. Run the server
python manage.py runserver
