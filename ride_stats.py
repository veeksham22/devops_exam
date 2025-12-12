# simple example: prints basic ride stats and saves output to a file
rides = [
    {"id":1, "distance_km":2.5, "duration_min":10},
    {"id":2, "distance_km":5.0, "duration_min":20},
    {"id":3, "distance_km":1.2, "duration_min":5},
]

total_rides = len(rides)
total_distance = sum(r["distance_km"] for r in rides)
avg_distance = total_distance / total_rides
avg_duration = sum(r["duration_min"] for r in rides) / total_rides

report = f"""
Ride statistics
---------------
Total rides: {total_rides}
Total distance (km): {total_distance:.2f}
Average distance (km): {avg_distance:.2f}
Average duration (min): {avg_duration:.2f}
"""

print(report)

# write output to file for Jenkins to archive
with open("ride_report.txt", "w") as f:
    f.write(report)
