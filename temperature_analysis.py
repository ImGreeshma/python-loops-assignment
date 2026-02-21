# Name: GREESHMA B
# Roll Number: IITP_AIMLTN_2602170
# Assignment: Python Loops & Automation - Subjective Question

print("===== Task 1: Find Maximum and Minimum =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
max_temp = min_temp = temperatures[0]
for i in range(1,len(temperatures)):
    if (temperatures[i] > max_temp):
        max_temp = temperatures [i]
    if (temperatures[i] < min_temp):
        min_temp = temperatures [i]
print(f"Highest Temperature: {max_temp}°C")
print(f"Lowest Temperature: {min_temp}°C")

print("\n===== Task 2: Count Hot Days =====")
temperatures = [28, 32, 35, 29, 31, 27, 30]
hot_days = 0
for temp in temperatures:
    if temp <= 30:
        continue
    else:
        hot_days += 1
print(f"Hot Days (>30)°C): {hot_days}")
    

print("\n===== Task 3: Alert System =====")
temperature = [28, 32, 35, 40, 31, 33, 30]
hot_days_before_alert = 0
day = 0
for i in range(0,len(temperature)):
    if temperature[i] >= 40:
        day = i + 1
        break
    if temperature[i] > 30:
        hot_days_before_alert += 1
    
print(f"Hot Days before alert: {hot_days_before_alert}")
print(f"Alert! Extreme temperature 40°C detected on Day {day}")
