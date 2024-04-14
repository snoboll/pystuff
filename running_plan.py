from icalendar import Calendar, Event
from datetime import datetime, timedelta, date
import pytz

# Create a new calendar
cal = Calendar()
cal.add('prodid', '-//Half Marathon Training Calendar//mxm.dk//')
cal.add('version', '2.0')

# Function to add an event to the calendar
def add_event(summary, description, start_date):
    event = Event()
    event.add('summary', summary)
    event.add('description', description)
    event.add('dtstart', start_date)
    event.add('dtend', start_date + timedelta(days=1))  # Marked as a full day event
    event.add('dtstamp', datetime.now())
    cal.add_component(event)

# Start date should be a Sunday for the long run alignment
# Adjust the start date if necessary to ensure it's a Sunday.
start_date = datetime(2024, 4, 7, 6, 0, 0, tzinfo=pytz.UTC).date() # Adjusted to a Sunday

# Define the training for 16 weeks
easy_run_distance = 5 # Starting distance for easy runs
for week in range(4):
    # Easy Run on Tuesday
    add_event(f"Easy Run - {round(easy_run_distance, 1)} km", "Build endurance with a comfortable pace.", start_date + timedelta(days=2 + week*7))
    easy_run_distance += 0.5 # Gradually increase the distance
    
    # Easy Run on Thursday
    add_event(f"Easy Run - {round(easy_run_distance, 1)} km", "Continue building endurance.", start_date + timedelta(days=4 + week*7))
    
    # Long Run on Sunday, gradually increasing distance
    long_run_distance = round(8 + week * 0.5, 1)  # Starting at 8 km, increasing by 0.5 km each week
    add_event(f"Long Run - {long_run_distance} km", "The cornerstone of half marathon training.", start_date + timedelta(week*7))

# Save the calendar to an ics file
filename = 'half_marathon_training.ics'
with open(filename, 'wb') as f:
    f.write(cal.to_ical())

print(f"iCalendar file created: {filename}")
