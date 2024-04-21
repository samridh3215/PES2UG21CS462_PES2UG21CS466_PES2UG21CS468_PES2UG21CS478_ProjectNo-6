import requests




def handleAuth(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            return response.content  # or response.json() for JSON data
        else:
            print(f"Failed to make request. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None


url =''
data = handleAuth(url)
if data:
    print("Request successful!")
    print(data)
else:
    print("Request failed.")


