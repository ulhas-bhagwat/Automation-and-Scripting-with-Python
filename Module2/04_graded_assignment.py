# Step 3.1: Fetch HTML Content
# Please be careful to follow instructions on how to run the program; 
# the Run menu or right-click > Run options do not work in the simulated environment. 
# Ensure you have run the terminal command to install the correct libraries using pip.
# You must use the terminal window as directed in Step 3.
import requests
from bs4 import BeautifulSoup

# Fetch the webpage content
url = "http://127.0.0.1:5500/baseball_stats.html"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Print the HTML content to inspect
print(soup.prettify())

# Step 3.2: Extract the Required Data
### YOUR CODE HERE ###

# Step 4.1: Convert to a DataFrame
# Import pandas
### YOUR CODE HERE ###

# Convert the game data into a pandas DataFrame
### YOUR CODE HERE ###

# Inspect the DataFrame
### YOUR CODE HERE ###

# Save and print the shaped data
### YOUR CODE HERE ###

# Step 5.1: Save to a CSV File
# Save the DataFrame to a CSV file named sports_statistics.csv
### YOUR CODE HERE ###