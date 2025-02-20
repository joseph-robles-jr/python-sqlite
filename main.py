from Radio_Contacts import make_contact, menu, setTXCallsign, create_table

def main():
	TXCallsign = setTXCallsign()
	create_table()
	menu(TXCallsign)
	

main()