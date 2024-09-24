# URL-Status-Checker
This script reads URLs from a CSV file and checks their HTTP status codes. It outputs the results to a new CSV file.

**Features:**
Automatically installs missing dependencies (pandas, requests).
Takes a CSV file with URLs and checks their HTTP status codes.
Saves the status codes to a new CSV file (url_status_results.csv).
Prerequisites
Python 3.x
pip (Python package manager)

**Steps:**
Install dependencies if they aren't installed.
Read a CSV file containing URLs.
Hit each URL and check the status code.
Output the results to a new CSV file.

**Usage**
Clone the Repository:

git clone https://github.com/yourusername/URL-Status-Checker.git
cd URL-Status-Checker

**Run the Script:**
python3 check_url_status.py <path_to_csv>
Replace <path_to_csv> with the path to your CSV file containing URLs.

**Example CSV (urls.csv):**
url
https://example.com
https://another-example.com

**Result:**
A new CSV file url_status_results.csv will be generated containing the URLs and their HTTP status codes.
