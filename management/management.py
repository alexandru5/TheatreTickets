import requests, json
import sys, os

server = 'http://server:8080/show/'
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
	print('Please enter the name of the show you would like to delete:\n' +
		 'If you want cancel type back)')

	id = input(' >> ')

	if id == 'back':
		exec_action('0')

	method = 'delete/' + id

	response = requests.delete(server + method, headers = headers)

	if response.status_code == 200:
		print('----> Show successfully deleted')
		exec_action('0')
	else:
		print('!!!!!! Something went wrong. Please try again')
		exec_action('2')
	return

def add():
	print('Write next information separated by comma and then press ENTER:\n'
		  '(If you want cancel type back)\n'
		  'Name, No_of_tickets, Price_per_ticket, Date, Hour\n')

	method = 'add/'

	show = input(' >> ')

	if show == 'back':
		exec_action('0')

	result = [x.strip() for x in show.split(',')]

	if len(result) < 5:
		print('!!!!!!! Too few arguments')
		exec_action('1')


	show_json = json.dumps({
		"name": result[0],
		"no_of_tickets": int(result[1]),
		"price_per_ticket": int(result[2]),
		"date": result[3],
		"hour": result[4]
	})

	print(show_json)
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

# Altenosfera, 9, 21, 16/3/2021, 22
# Untold, 3, 23, 12/2/2020, 20
