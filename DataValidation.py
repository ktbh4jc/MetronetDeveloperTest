import re
import json
import sys

# To run: $ python3 DataValidation.py Web\ Developer\ Test

class Contact:
  email_regex = '^[^@]+@[^@]+'
  phone_number_regex = '^[0-9 -]+'

  def __init__(self, name, city, phone_number, email_address):
    self.name = name
    self.city = city
    self.phone_number = phone_number
    self.email_address = email_address
  
  def __str__(self):
    return f'Name: {self.name}\tCity: {self.city}\tPhone Number: {self.phone_number}\tEmail Address: {self.email_address}'
  
  def validate_validity(self):
    email_match = re.search(self.email_regex, self.email_address)
    phone_match = re.search(self.phone_number_regex, self.phone_number)
    if email_match and phone_match:
      return("Valid")
    if not email_match and not phone_match:
      return("Email and Phone are invalid.")
    if email_match:
      return("Phone is invalid")
    return("Email is invalid")

def main():
  contacts = []
  cities = {}
  with open(sys.argv[1], 'r') as contact_file:
    data = json.load(contact_file)
    for contact in data:
      contacts.append(Contact(contact['fullName'], contact['cityName'], contact['phoneNumber'], contact['emailAddress']))
      cities[contact['cityName']] = 0
  contact_file.close()
  
  contacts.sort(key=lambda contact: contact.name)
  for contact in contacts:
    validity = contact.validate_validity()
    print(f'{contact.name} {validity}')
    if validity != "Valid":
      cities[contact.city] += 1
  for city in sorted(cities, key=lambda c: cities[c], reverse=True):
    print(f'{city} {cities[city]}')

if __name__ == "__main__":
  main()
