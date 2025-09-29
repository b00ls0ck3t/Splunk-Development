#!/usr/bin/env python3
import time
import random
import json
import os
from datetime import datetime

# Simple faker replacement to avoid dependencies
def fake_uuid():
    return f"{random.randint(10000000, 99999999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(100000000000, 999999999999)}"

def fake_ipv4():
    return f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 255)}"

def generate_web_log():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
    level = random.choice(['INFO', 'WARN', 'ERROR', 'DEBUG'])
    user_id = fake_uuid()
    ip = fake_ipv4()
    
    messages = [
        f"User login successful user_id={user_id} ip={ip}",
        f"API request processed endpoint=/api/users response_time={random.randint(50, 500)}ms",
        f"Database query executed table=users duration={random.randint(10, 200)}ms",
        f"Payment processed amount=${random.uniform(10, 1000):.2f} status=success"
    ]
    
    message = random.choice(messages)
    return f"{timestamp} [{level}] [WebApp] - {message}"

def main():
    log_dir = '/var/log/applications'
    os.makedirs(log_dir, exist_ok=True)
    
    print("Starting log generator...")
    
    while True:
        try:
            apps = ['web-api', 'payment-service', 'user-service']
            
            for app in apps:
                log_file = f"{log_dir}/{app}.log"
                
                with open(log_file, 'a') as f:
                    for _ in range(random.randint(1, 3)):
                        log_entry = generate_web_log()
                        f.write(log_entry + '\n')
                        f.flush()
            
            print(f"Generated logs at {datetime.now()}")
            time.sleep(5)
            
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    main()