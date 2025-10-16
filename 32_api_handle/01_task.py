import requests
from time import sleep

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
max_retries = 3  # number of retry attempts
retry_delay = 5  # seconds to wait before retry

for attempt in range(1, max_retries + 1):
    try:
        response = requests.get(url, timeout=10)  # timeout to avoid hanging
        response.raise_for_status()  # raise an exception for HTTP errors

        data = response.json()
        print("Bitcoin Price Data:")
        print(data)
        break  # success, exit the loop

    except requests.exceptions.ConnectionError:
        print(f"[Attempt {attempt}] Connection failed. Retrying in {retry_delay}s...")
        sleep(retry_delay)

    except requests.exceptions.Timeout:
        print(f"[Attempt {attempt}] Request timed out. Retrying in {retry_delay}s...")
        sleep(retry_delay)

    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")
        break  # no point in retrying for HTTP errors like 404

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        break
else:
    print("All retries failed. Please check your network or API status.")
