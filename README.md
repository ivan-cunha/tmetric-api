# Time Tracking Analysis
This script allows you to retrieve and analyze time entries from the TMetric API. It retrieves time entries for a specified user and calculates the total duration worked, balance, and daily durations.

## Prerequisites
Before running the script, please ensure you have the following:

* Python installed on your machine.
* The `requests` library installed. You can install it using pip install requests.

## Getting Started

1. Open the script in a text editor or an integrated development environment (IDE) of your choice.
2. Replace the value of the API_KEY variable with your TMetric API key. You can obtain an API key from the TMetric application.
3. Set the ACCOUNT_ID and USER_ID variables to your TMetric account and user IDs respectively.
4. Adjust the values of work_h (work hours per day) and work_m (work minutes per day) according to your work schedule.
5. Set the init_h (initial balance hours) and init_m (initial balance minutes) variables to reflect any existing balance you may have.
6. Modify the start_day variable to specify the start date from which you want to retrieve time entries. Time entries from this date until yesterday will be fetched.
7. Save the script.

## Running the Script

To run the script, follow these steps:

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is saved.
3. Run the following command: python script_name.py (replace script_name.py with the actual name of the script file).
4. The script will retrieve time entries from the TMetric API and perform calculations.
5. The total duration worked and the balance will be displayed as an output.
6. If desired, uncomment the last line to print the daily durations.
Note: Make sure you have an active internet connection for the script to communicate with the TMetric API.

## Output
The script will display the following information:

* Total duration worked: This shows the total duration worked, including the balance and deducting weekends.
* Balance: This indicates the balance of hours and minutes you have.
* Daily durations: If uncommented, the script will display the durations worked each day.
* 
## Customization

Feel free to modify the script according to your specific requirements. You can adjust variables such as work hours, balance, and the date range for time entry retrieval to suit your needs.

Remember to save the modified script before running it.

## Troubleshooting
If you encounter any issues while running the script, consider the following:

Double-check that you have entered the correct API key, account ID, and user ID.
Ensure you have a stable internet connection.
Verify that you have installed the requests library correctly.
If the problem persists, refer to the TMetric API documentation or seek further assistance from the TMetric support team.

Disclaimer
This script is provided as-is and without warranty. Use it at your own risk. The author is not responsible for any consequences arising from the use of this script.

If you have any questions or need further assistance, please don't hesitate to contact me.