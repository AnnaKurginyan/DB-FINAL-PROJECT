import requests
import random
from datetime import datetime, timedelta

API_URL = "http://127.0.0.1:8080"

SHIP_TYPES = ["Cargo", "Passenger", "Fishing", "Military", "Container", "Tanker", "Submarine"]
PORT_CATEGORIES = ["International", "Domestic", "Military", "River", ]
VISIT_PURPOSES = ["Tourism", "Cargo Delivery", "Maintenance", "Military Operations"]

def create_ships(count=1000):
    for i in range(count):
        ship_data = {
            "name": f"Ship_{i+1}",
            "ship_type": random.choice(SHIP_TYPES),
            "captain": f"Captain_{i+1}",
            "home_port": random.randint(1, 500),
            "water_displacement": random.randint(1000, 50000)
        }
        response = requests.post(f"{API_URL}/ships/", json=ship_data)
        if response.status_code == 200:
            print(f"Создано: {response.json()}")
        else:
            print(f"Ошибка создания: {response.text}")

def create_ports(count=500):
    for i in range(count):
        port_data = {
            "daily_price": random.randint(100, 5000),
            "category": random.choice(PORT_CATEGORIES),
            "name": f"Port_{i+1}",
            "country": f"Country_{i+1}"
        }
        response = requests.post(f"{API_URL}/ports/", json=port_data)
        if response.status_code == 200:
            print(f"Создано: {response.json()}")
        else:
            print(f"Ошибка создания: {response.text}")

def create_visits(count=3000):
    for i in range(count):
        arrival_date = datetime.now() - timedelta(days=random.randint(1, 365))
        departure_date = arrival_date + timedelta(days=random.randint(1, 30))
        visit_data = {
            "purpose": random.choice(VISIT_PURPOSES),
            "arrival": arrival_date.strftime("%Y-%m-%d"),
            "departure": departure_date.strftime("%Y-%m-%d"),
            "dock": random.randint(1, 50),
            "ship_id": random.randint(1, 1000), 
            "port_id": random.randint(1, 500)  
        }
        response = requests.post(f"{API_URL}/visits/", json=visit_data)
        if response.status_code == 200:
            print(f"Создано: {response.json()}")
        else:
            print(f"Ошибка создания: {response.text}")

def populate_database():
    create_ports()
    create_ships()
    create_visits()

if __name__ == "__main__":
    populate_database()
