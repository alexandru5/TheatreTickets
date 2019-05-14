import requests, json
import sys, os

username = ''
userid = 0
server = 'http://server:8080/'
user = 'user/'
show = 'show/'
ticket = 'ticket/'
headers = {'Content-type': 'application/json'}
menu_actions = {}

def exec_action(ch):
	choice = ch.lower()
	if ch == '':
		menu_actions['0']()
	else:
		try:
			menu_actions[choice]()
		except KeyError:
			print('Invalid selection, please try again.')
			menu_actions['0']()
	return

def main_menu():
	print('\nChoose one of the following action:')
	print('1. Check if the show is in the database')
	print('2. Buy ticket for show')
	print('3. EXIT')

	choice = input(' >> ')
	exec_action(choice)
	return

def get():
	print('\nWrite the name of your show and then press ENTER:\n'
		  '(If you want cancel type: back)\n')

	method = 'getByName/'

	inn = input(' >> ')

	if inn == 'back':
		exec_action('0')

	response = requests.get(server + show + method + inn)
	if response.status_code == 200:
		if response.text != '[]':
			print('-----> show successfuly found: ')
			out = [x.strip() for x in response.text.split(',')]

			for i in range(0, 5):
				print(out[i])
		else:
			print("We could not have found any show with that name for you. We're sowy :( ")

		exec_action('0')
	else:
		print('!!!!!! Something went wrong. Please try again')
		exec_action('1')
	return

def buy():
	print('\nPlease enter the name of the show to buy the ticket: (If you want cancel type back)')

	stream = input(' >> ')

	if stream == 'back':
		exec_action('0')

	method = 'getByName/' + stream

	response = requests.get(server + show + method)

	if response.status_code == 200:
		print('----> Ticket successfully bought\n')
		print(' --------------------------------------------------------------- \n'
			  'Your ticket: \n Name: ' + username + '\nShow: ' + stream +'\n')
		exec_action('0')
	else:
		print('!!!!!! Something went wrong while paying your ticket')
		exec_action('3')
	return

def exit():
	sys.exit()

menu_actions = {
'0': main_menu,
'1': get,
'2': buy,
'3': exit
}
if __name__ == '__main__':

	while username == '':
		print('Please let us know your name: ')
		username = input(' >> ')

	response = requests.get(server + user + 'getByName/' + username)
	if response.status_code == 200:
		print(response.text)
		if response.text == '':
			data = json.dumps({'name' : username})
			response = requests.put(server + user + 'add', data = data, headers = headers)

			if response.status_code == 200:
				main_menu()
		main_menu()
	else:
		print('Something went wrong. Please reboot app')

