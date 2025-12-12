import datetime
from datetime import datetime as dt
from collections import defaultdict

# Extended ride dataset
rides = [
    {"id": 1, "distance_km": 2.5, "duration_min": 12, "start": "2024-12-01 10:00"},
    {"id": 2, "distance_km": 7.2, "duration_min": 25, "start": "2024-12-01 16:30"},
    {"id": 3, "distance_km": 4.8, "duration_min": 18, "start": "2024-12-02 09:15"},
    {"id": 4, "distance_km": 10.5, "duration_min": 40, "start": "2024-12-03 07:50"},
    {"id": 5, "distance_km": 1.9, "duration_min": 9, "start": "2024-12-03 19:20"},
    {"id": 6, "distance_km": 6.7, "duration_min": 22, "start": "2024-12-03 21:10"},
    {"id": 7, "distance_km": 8.1, "duration_min": 29, "start": "2024-12-04 06:45"},
]

# Convert timestamps to datetime objects
for r in rides:
    r["start_dt"] = dt.strptime(r["start"], "%Y-%m-%d %H:%M")

# Basic statistics
total_rides = len(rides)
total_distance = sum(r["distance_km"] for r in rides)
total_duration = sum(r["duration_min"] for r in rides)
avg_distance = total_distance / total_rides
avg_duration = total_duration / total_rides

# Average speed (km/h)
avg_speed = (total_distance / (total_duration / 60))

# Find longest ride
longest_ride = max(rides, key=lambda r: r["duration_min"])

# Group by date
rides_by_day = defaultdict(list)
for r in rides:
    date_key = r["start_dt"].strftime("%Y-%m-%d")
    rides_by_day[date_key].append(r)

# Build detailed report
report_lines = []
report_lines.append("======================================")
report_lines.append("         EXTENDED RIDE REPORT          ")
report_lines.append("======================================")
report_lines.append(f"Total rides: {total_rides}")
report_lines.append(f"Total distance: {total_distance:.2f} km")
report_lines.append(f"Total duration: {total_duration} minutes")
report_lines.append(f"Average distance per ride: {avg_distance:.2f} km")
report_lines.append(f"Average duration per ride: {avg_duration:.2f} min")
report_lines.append(f"Average speed: {avg_speed:.2f} km/h")
report_lines.append("--------------------------------------")
report_lines.append("Longest Ride:")
report_lines.append(f"  ID: {longest_ride['id']}")
report_lines.append(f"  Distance: {longest_ride['distance_km']} km")
report_lines.append(f"  Duration: {longest_ride['duration_min']} min")
report_lines.append(f"  Started at: {longest_ride['start']}")
report_lines.append("--------------------------------------")
report_lines.append("Rides Per Day:")

for day, rides_list in rides_by_day.items():
    report_lines.append(f"  {day}: {len(rides_list)} rides")

report_lines.append("======================================")

# Join report
final_report = "\n".join(report_lines)

# Print to console
print(final_report)

# Save to file (for Jenkins artifact)
with open("ride_report_v2.txt", "w") as f:
    f.write(final_report)
