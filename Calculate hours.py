#!/usr/bin/env python3

# Example list of times
time_pairs = [
	["9:15", "17:45"],
	["8:15", "16:00"],
	["9:30", "17:45"],
	["8:30", "16:00"],
	["9:15", "17:45"]
]







from datetime import datetime, timedelta

def calculate_hours(times):
	total_hours = 0
    
	for start_time, end_time in times:
		fmt = '%H:%M'
		start = datetime.strptime(start_time, fmt)
		end = datetime.strptime(end_time, fmt)
        
		# Calculate difference in hours and minutes
		diff = end - start
        
		if (diff.total_seconds() > 5 * 3600):
			# Subtract lunch break of 30 minutes
			lunch_break = timedelta(minutes=30)
			diff -= lunch_break
        
		# Convert difference to total hours
		hours = diff.total_seconds() / 3600
        
		# Add to weekly total
		total_hours += hours
    
	return total_hours

# Calculate weekly hours
weekly_hours = calculate_hours(time_pairs)

print(f"Total weekly hours: {weekly_hours:.2f}")
input()
input()