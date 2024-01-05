import requests
import sys

login_url = "https://webkiosk.thapar.edu/CommonFiles/UserAction.jsp"
success_url = "https://webkiosk.thapar.edu/StudentFiles/StudentPage.jsp"
failure_url = "https://webkiosk.thapar.edu/index.jsp"

# Replace these with your actual username and password
username = "102396005"
password = "12345"

payload = {
    "UserType": "S",
    "MemberCode": username,
    "Password": password,
    "BTNSubmit": "Submit",  # Name of the submit button
    "BTNReset": "Reset"  # Name of the reset button
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

with requests.Session() as session:
    try:
        response = session.post(login_url, data=payload, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error during request: {e}")
        sys.exit(1)

    if response.url == success_url:
        print("Login SUCCESS")
        # You can now continue making requests within the session
        # For example, you can fetch data from the successful login page.
    elif response.url == failure_url:
        print("Login FAILED")
    else:
        print("Unexpected response page:", response.url)
