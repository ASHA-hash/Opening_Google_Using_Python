import os
import signal
import subprocess
import time

# Path to the Google Chrome executable
chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

# URL you want to open
url = "https://www.google.com"

# Command to open Google Chrome with the specified URL
# process = subprocess.Popen([chrome_path, url])
#
# # Wait for 3 minutes (180 seconds)
# time.sleep(10)

# Command to open Google Chrome with the specified URL
process = subprocess.Popen([chrome_path, url])

# Wait for a few minutes (e.g., 2 minutes)
time.sleep(10)  # 120 seconds

# Close the Google Chrome window
# os.kill(process.pid, signal.SIGTERM)  # Send the termination signal to the process
# Close the Google Chrome window
# subprocess.Popen(['taskkill', '/F', '/T', '/PID', str(process.pid)])
# Close all instances of Google Chrome
subprocess.Popen(['taskkill', '/F', '/IM', 'chrome.exe'])