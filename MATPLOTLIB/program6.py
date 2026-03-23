import matplotlib.pyplot as plt
import csv

dates = []
highs = []
lows = []

with open("forecast.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        dates.append(row["date"])
        highs.append(float(row["high"]))
        lows.append(float(row["low"]))

plt.plot(dates, highs, label="High Temperature")
plt.plot(dates, lows, label="Low Temperature")

plt.fill_between(dates, highs, lows, alpha=0.3)

plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Daily Temperature Trends")

plt.xticks(rotation=45)

plt.legend()
plt.grid()

plt.tight_layout()
plt.show()