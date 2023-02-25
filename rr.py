import threading
import requests

def check_host_status(host, results):
    url = f"http://{host}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"{url}: 200 OK")
            results[host] = True
        elif response.status_code == 403:
            print(f"{url}: 403 Forbidden")
            results[host] = False
        elif response.status_code == 404:
            print(f"{url}: 404 Not Found")
            results[host] = False
    except requests.ConnectionError:
        print(f"{url}: Connection Error")
        results[host] = False

# Prompt the user for the file name
file_name = input("Enter the file name containing the hostnames: ")

# Read hostnames from file
with open(file_name, "r") as f:
    hostnames = f.read().splitlines()

# Add "www." to the beginning of each hostname
hostnames = [f"www.{hostname.strip()}" for hostname in hostnames]

# Check the status of each hostname in a separate thread
threads = []
results = {}
for hostname in hostnames:
    thread = threading.Thread(target=check_host_status, args=(hostname, results))
    thread.start()
    threads.append(thread)

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Prompt the user for the file name to save the results to
results_file = input("Enter the file name to save the results to: ")

# Write the results to a file
with open(results_file, "w") as f:
    for hostname, status in results.items():
        if status:
            f.write(hostname + "\n")

# Save the results to a file in case the script is stopped abruptly
try:
    with open("results_backup.txt", "w") as f:
        for hostname, status in results.items():
            if status:
                f.write(hostname + "\n")
except Exception as e:
    print(f"Error saving results to backup file: {e}")
