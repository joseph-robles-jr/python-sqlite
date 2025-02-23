import sqlite3


def create_table():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS contacts (
        TXCallsign TEXT NOT NULL,
        TXrst INTEGER CHECK(TXrst BETWEEN 0 AND 599),
        RXCallsign TEXT NOT NULL,
        RXrst INTEGER CHECK(RXrst BETWEEN 0 AND 599),
        mode TEXT CHECK(LENGTH(mode) = 3),
        power INTEGER CHECK(power BETWEEN 0 AND 1500),
        frequency INTEGER CHECK(frequency BETWEEN 0 AND 9999999999)
    )
    ''')
    conn.commit()
    conn.close()

def setTXCallsign():
	TXCallsign = ''
	while len(TXCallsign) == 0: 
			inputTXCallsign = input('Enter Your Callsign: ')
			if inputTXCallsign.isalnum() > 0:
				TXCallsign = str.capitalize(inputTXCallsign)
			else:
				print('TX Callsign must be alphanumeric. Try Again.')

	return TXCallsign

def update_contact(TXCallsign, TXrst, RXCallsign, RXrst, mode, power, frequency):
	conn = sqlite3.connect('contacts.db')
	cursor = conn.cursor()
	cursor.execute('''UPDATE contacts SET TXrst = ?, RXCallsign = ?, RXrst = ?, mode = ?, power = ?, frequency = ? WHERE TXCallsign = ?''', (TXCallsign, TXrst, RXCallsign, RXrst, mode, power, frequency))
	conn.commit()
	conn.close()

def insert_contact( TXCallsign, TXrst, RXCallsign, RXrst, mode, power, frequency):
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO contacts (TXcallsign, TXrst, RXCallsign, RXrst, mode, power, frequency) VALUES (?, ?, ?, ?, ?, ?, ?)''', (TXCallsign, TXrst, RXCallsign, RXrst, mode, power, frequency))
    conn.commit()
    conn.close()

def get_contacts():
    conn = sqlite3.connect('contacts.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contacts')
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_contact():
	RXCallsign = str.capitalize(input('Enter RX Callsign: '))

	conn = sqlite3.connect('contacts.db')
	cursor = conn.cursor()
	cursor.execute('''
	DELETE FROM contacts WHERE RXCallsign = ?''', (RXCallsign,))
	conn.commit()
	conn.close()

def make_contact(TXCallsign, update	= False):
	contact_complete = False

	while contact_complete == False:
		
		TXrst = 0
		RXCallsign = ''
		RXrst = 0
		mode = 'a'
		power = 0
		frequency = 0

		if update == True:
			while len(RXCallsign) == 0:
				callsign_to_update = str.capitalize(input('Enter RX Callsign Of The Contact That You Wish To Update: '))	
				if callsign_to_update.isalnum() > 0:
					conn = sqlite3.connect('contacts.db')
					cursor = conn.cursor()
					cursor.execute('SELECT * FROM contacts WHERE RXCallsign = ?', (callsign_to_update,))
					rows = cursor.fetchall()
					conn.close()
					if len(rows) == 0:
						print('Callsign not found. Try Again.')
					else:
						RXCallsign = callsign_to_update

		

		while TXrst.bit_length() == 0: #TX RST section
			inputTXrst = int(input('Enter TX RST: '))
			if inputTXrst >= 0 and inputTXrst <= 59:
				TXrst = inputTXrst
			else:
				print('TX RST must be between 0 and 59. Try Again.')
	
		if update == False:
			while len(RXCallsign) == 0: #RX Callsign section
				inputRXCallsign = input('Enter RX Callsign: ')
				if inputRXCallsign.isalnum() > 0:
					RXCallsign = str.capitalize(inputRXCallsign)
				else:
					print('RX Callsign must be alphanumeric. Try Again.')

		while RXrst.bit_length() == 0: #RX RST section
			inputRXrst = int(input('Enter RX RST: '))
			if inputRXrst >= 0 and inputRXrst <= 59:
				RXrst = inputRXrst
			else:
				print('RX RST must be between 0 and 59. Try Again.')

		while len(mode) != 3: #Mode section
			inputMode = input('Enter Mode: ')
			if len(inputMode) <= 3 and len(inputMode) > 0:
				if inputMode == 'fm' or inputMode == 'FM':
					mode = 'FM '
				elif inputMode == 'ssb' or inputMode == 'SSB':
					mode = 'SSB'
				elif inputMode == 'usb' or inputMode == 'USB':
					mode = 'USB'
				elif inputMode == 'lsb' or inputMode == 'LSB':
					mode = 'USB'
				elif inputMode == 'cw' or inputMode == 'CW':
					mode = 'CW '
				elif inputMode == 'am' or inputMode == 'AM':
					mode = 'AM '
				else: print('Mode must be FM, SSB, USB, LSB, CW, or AM. Try Again.')

		while power.bit_length() == 0: #Power section
			inputPower = int(input('Enter Power: '))
			if inputPower >= 0 and inputPower <= 1500:
				power = inputPower
			else:
				print('Power must be between 0 and 1500. Try Again.')

		while frequency.bit_length() == 0: #Frequency section
			inputFrequency = int(input('Enter Frequency: '))
			if inputFrequency >= 0 and inputFrequency <= 9999999999:
				frequency = inputFrequency
			else:
				print('Frequency must be between 0 and 9999999999. Try Again.')		

		contact_complete = True 
	if update == False:	
		insert_contact(TXCallsign, TXrst, RXCallsign, RXrst, mode, power, frequency) 
	elif update == True:
		update_contact(TXCallsign, TXrst, RXCallsign, RXrst, mode, power, frequency)

def menu(TXCallsign):
	choice = -1
	while choice != 5:
		print('1. Add Contact')
		print('2. Update Contact')
		print('3. Delete Contact')
		print('4. View Contacts')
		print('5. Exit')
		choice = int(input('Enter Choice: '))

		if choice == 1:
			make_contact(TXCallsign)
		elif choice == 2:
			make_contact(TXCallsign, update=True)
		elif choice == 3:
			delete_contact()
		elif choice == 4:
			print(get_contacts())

