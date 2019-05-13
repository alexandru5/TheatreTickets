import requests, json
import sys, os

server = 'http://172.16.1.3:8080/show/'
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
	print('Choose one of the following action:')
	print('1. Add show')
	print('2. Cancel show')
	print('3. EXIT')

	choice = input(' >> ')
	exec_action(choice)
	return

def cancel():
	print('Please enter the show ID: (If you want cancel type back)')

	id = input(' >> ')

	if id == 'back':
		exec_action('0')

	method = 'deleteByID/' + id

	response = requests.delete(server + method, headers = headers)

	if response.status_code == 200:
		print('----> show successfully deleted')
		exec_action('0')
	else:
		print('!!!!!! Something went wrong. Please try again')
		exec_action('2')
	return

def add():
	print('Write next information separated by comma and then press ENTER:\n'
		  '(If you want cancel type back)\n'
		  'showID, Source, Destination, Departure_hour, Departure_day, '
		  'Duration, Number_of_seats\n')

	method = 'addshow/'

	show = input(' >> ')

	if show == 'back':
		exec_action('0')

	result = [x.strip() for x in show.split(',')]

	if len(result) < 7:
		print('!!!!!!! Too few arguments')
		exec_action('1')


	show_json = json.dumps({
		"showID": result[0],
		"source": result[1],
		"destination": result[2],
		"hour": int(result[3]),
		"day": int(result[4]),
		"duration": int(result[5]),
		"seats": int(result[6])
	})

	response = requests.put(server + method, data = show_json, headers = headers)

	if response.status_code == 200:
		print('-----> show successfully added')
		exec_action('0')
	else:
		print('!!!!!! Something went wrong. Please try again')
		exec_action('1')
	return

def exit():
	sys.exit()

menu_actions = {
'0': main_menu,
'2': cancel,
'1': add,
'3': exit
}
if __name__ == '__main__':
	
	main_menu()

# 71FTR, BUC, AMT, 9, 21, 3, 100
# 32CD, BUC, LON, 3, 23, 4, 123
