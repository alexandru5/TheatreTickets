import requests, json
import sys, os

username = ''
userid = 0
server = 'http://172.16.1.3:8080/'
user = 'user/'
show = 'show/'
ticket = 'ticket/'
reservation = 'reservation/'
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
	print('1. Get shows available')
	print('2. Book ticket')
	print('3. Buy ticket')
	print('4. EXIT')

	choice = input(' >> ')
	exec_action(choice)
	return

def get():
	print('\nWrite next information separated by comma and then press ENTER:\n'
		  '(If you want cancel type back)\n'
		  'Source, Destination, Max_shows, Departure_day')

	method = 'findBySourceAndDestinationAndDay/'

	inn = input(' >> ')

	if inn == 'back':
		exec_action('0')

	result = [x.strip() for x in inn.split(',')]

	if len(result) < 4:
		print('!!!!!!! Too few arguments')
		exec_action('1')

	source = result[0]
	destination = result[1]
	maxshows = int(result[2])
	day = result[3]

	response = requests.get(server + show + method + source + '/' + destination + '/' + day)
	if response.status_code == 200:
		if response.text != '[]':
			print('-----> show successfuly found: ')
			out = [x.strip() for x in response.text.split(',')]

			for i in range(0, 7):
				print(out[i])
		else:
			print("We could not have found any route for you. We're sowy :( ")

		exec_action('0')
	else:
		print('!!!!!! Something went wrong. Please try again')
		exec_action('1')
	return

def book():
	print('\nPlease enter the shows ID separated by comma: (If you want cancel type back)')

	stream = input(' >> ')

	if stream == 'back' or stream == '':
		exec_action('0')

	shows = [x.strip() for x in stream.split(',')]

	method = 'add/'
	for show in shows:
		link = server + reservation + method + username + '/' + show;
		response = requests.put(link, headers = headers)
		if response.status_code == 200:
			print('----> show successfully booked')
			print('Please use this ticket id to buy your ticket: ' +  response.text)
			exec_action('0')
		else:
			print('!!!!!! Something went wrong. Please try again')
			exec_action('2')

	return

def buy():
	print('\nPlease enter the ticket ID you would like to buy and your credit card info separated by comma: (If you want cancel type back)')

	stream = input(' >> ')

	if stream == 'back':
		exec_action('0')


	args = [x.strip() for x in stream.split(',')]

	if len(args) < 2:
		print("\nYou need to provide us with your ticket ID and your credit card info separated by comma. \nPlease try again")
		exec_action('3')

	method = 'payTicket/' + args[0]

	response = requests.delete(server + ticket + method, headers = headers)

	if response.status_code == 200:
		print('----> Ticket successfully paid with next credit card: ' + args[1])
		print(' --------------------------------------------------------------- \n'
			  'Your ticket information is: \nticketID: ' + args[0] + '\nName: ' + username
			  + '\nshows: ' + response.text + '\n-------------------------------------------------------------- \n')
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
'2': book,
'3': buy,
'4': exit
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

# 71FTR, BUC, AMT, 9, 21, 3, 100
# 32CD, BUC, LON, 3, 23, 4, 123
