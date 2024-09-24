import os
import subprocess
import sys

# Step 1: Install Required Libraries
def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Try importing pandas and requests, install if missing
try:
    import pandas as pd
except ImportError:
    print("Pandas not found. Installing...")
    install("pandas")

try:
    import requests
except ImportError:
    print("Requests not found. Installing...")
    install("requests")

import pandas as pd
import requests

# Step 2: Read URLs from CSV File and Check Status Codes
def check_url_status(csv_file):
    try:
        # Load the CSV file (assuming the CSV has a column 'url' with the URLs)
        urls_df = pd.read_csv(csv_file)

        # Create an empty list to store results
        results = []

        # Loop through each URL in the CSV
        for url in urls_df['url']:
            try:
                response = requests.get(url)
                # Append the URL and status code to the results
                results.append({'url': url, 'status_code': response.status_code})
            except requests.exceptions.RequestException as e:
                # Append the URL and an error message if the request fails
                results.append({'url': url, 'status_code': f"Error: {e}"})

        # Convert the results into a DataFrame
        results_df = pd.DataFrame(results)

        # Save the results to a new CSV
        output_file = 'url_status_results.csv'
        results_df.to_csv(output_file, index=False)
        print(f"URL status codes have been saved to '{output_file}'")
    except FileNotFoundError:
        print(f"File '{csv_file}' not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Step 3: Main Execution
if __name__ == "__main__":
    # Check if the user has provided a CSV file as an argument
    if len(sys.argv) != 2:
        print("Usage: python3 check_url_status.py <path_to_csv>")
    else:
        csv_file_path = sys.argv[1]
        check_url_status(csv_file_path)
