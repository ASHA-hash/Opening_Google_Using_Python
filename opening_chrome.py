import os
import signal
import subprocess
import time

# Path to the Google Chrome executable
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# URL you want to open
url = "https://www.google.com"



# Command to open Google Chrome with the specified URL
process = subprocess.Popen([chrome_path, url])

# Wait for a few minutes (e.g., 2 minutes)
time.sleep(10)  # 120 seconds

# Close all instances of Google Chrome
subprocess.Popen(['taskkill', '/F', '/IM', 'chrome.exe'])
