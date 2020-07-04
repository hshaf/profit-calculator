import requests, sqlite3, time

conn = sqlite3.connect('players.db')
c = conn.cursor()

def getPages():

	for x in range(3,72):
		payload = {"type": "mlb_card", "page": x}
		r = requests.get("https://theshownation.com/mlb20/apis/listings.json", params = payload)

	r_dict = r.json()
	listings = r_dict['listings']

	for listing in listings:
		c.execute("INSERT INTO mlb_card VALUES (?, ?, ?)", (listing['name'], listing['best_sell_price'], listing['best_buy_price']))

	time.sleep(10)

# c.execute("SELECT * FROM mlb_card WHERE name='Manny Machado'")
# print(c.fetchall())

conn.commit()
conn.close()