# Create a function, halved that takes an list of numbers and returns an new list consisting of those numbers, halved.

def halved(l):
    new_l = []
    for i in l:
        new_l.append(i / 2)
    return new_l

# Create a function, only_positive, that takes an list of numbers and returns a new list consisting only of the positive numbers.

def only_positive(l):
    new_l = []
    for i in l:
        if i > 0:
            new_l.append()
    return new_l

# Write a function, sum, that takes an list of numbers and returns the sum of those numbers.

def sum(l):
    acc = 0
    for i in l:
        acc += i
    return acc

# Create a function called stripped_strings that takes an list of strings and returns a new list of the strings with all non-alphanumeric characters removed.
import re
def stripped_strings(l_str):
    new_l = []
    for i in l_str:
        new_l.append(re.sub(r'\W'), '', i)

# Create function, find_special, that takes an list of words and returns the index of the first occurrence of the word "special". If the word "special" is not present, it should return, -1.

def find_special(l_str):
    return l_str.occurrence('special')

# Create a function called valid_contacts. This function takes an list of contact dictionaries (name and phoneNumber property, remember?). It should return an list of only contact objects that have a phoneNumber that is a 10-digit string.

def valid_contacts(contacts):
    return contacts.filter(check_phones)

def check_phones(contact):
    if len(contact.phoneNumber) == 10:
        return True
    return False


contacts_1 = [
  {'name': 'Reuben', 'phoneNumber': '9196218777'},
  {'name': 'Laisha', 'phoneNumber': '0123334766'},
  {'name': 'Cielo', 'phoneNumber': '764'},
  {'name': 'Maya', 'phoneNumber': '7653324599'}
]


# Create a function, contact_names, that takes an list of contact objects and returns an list of contact names.

def contact_names(contacts):
    new_l = []
    for i in contacts:
        new_l.append(i['name'])
    return new_l

contacts = [{"name": 'Reuben', "phoneNumber": '9196218777'}, {"name": 'Laisha', "phoneNumber": '0123334766'}, {"name": 'Cielo', "phoneNumber": '764'}, {"name": 'Maya', "phoneNumber": '7653324599'}]

print(contact_names(contacts)) # ['Reuben', 'Laisha', 'Cielo', 'Maya'];