import requests
from pprint import pprint
from collections import defaultdict
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

# Get yesterday's date
yesterday = (current_date - timedelta(days=1)).strftime("%Y-%m-%d")

# Replace with your TMetric API key
API_KEY = ""

# Set your TMetric account, user, and other details
ACCOUNT_ID = 0
USER_ID = 0

# Work hours and minutes per day
work_h = 8
work_m = 48

# Initial balance hours and minutes
init_h = 0
init_m = 0

# Start day for time entry retrieval
start_day = "2023-02-09"

# Set the base URL for TMetric API
BASE_URL = "https://app.tmetric.com/api/v3"


# Function to transform a timedelta into a formatted string
def transform_td(td):
    hours = abs(int(td.total_seconds() / 3600))
    minutes = (abs(td.total_seconds()) % 3600) // 60
    signal = "-" if td < timedelta() else "+"
    return f"{signal}{int(hours)}h{int(minutes)}min"


# Helper function to send a GET request to TMetric API
def get_time_entries(start_date, end_date=yesterday):
    headers = {"Authorization": "Bearer " + API_KEY}
    response = requests.get(
        f"{BASE_URL}/accounts/{ACCOUNT_ID}/timeentries?/userId={USER_ID}&startDate={start_date}&endDate={end_date}",
        headers=headers,
    )
    response.raise_for_status()
    return response.json()


# Create a defaultdict to store the durations for each day
d = defaultdict(timedelta)

# Retrieve time entries from TMetric API
resp = get_time_entries(start_day)

# Initialize variables
total_duration = timedelta()
weekdays = set()

# Iterate through the retrieved time entries
for item in resp:
    start_time = datetime.fromisoformat(item["startTime"])
    end_time = datetime.fromisoformat(item["endTime"])
    duration = end_time - start_time
    total_duration += duration

    # Check if the start date is a weekday (0-4: Monday to Friday)
    if start_time.weekday() < 5:
        weekdays.add(start_time.date())  # Collect unique weekdays encountered
    d[start_time.date().strftime("%Y-%m-%d")] += duration

# Calculate the total working duration and balance
time_work = timedelta(hours=work_h, minutes=work_m)
balance = timedelta(hours=init_h, minutes=init_m)
total_duration = total_duration + balance - time_work * len(weekdays)

# Format the total duration as a string
hours = total_duration.total_seconds() // 3600
minutes = (total_duration.total_seconds() % 3600) // 60
formatted_duration = f"Balanço: {int(hours):+}h{int(minutes)}min"

# Transform durations in the defaultdict into formatted strings
d = {key: transform_td(value) for key, value in d.items()}

# Print the formatted duration
print(formatted_duration)

# Uncomment the following line to pprint the durations per day
# pprint(d)
