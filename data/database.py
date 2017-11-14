import sqlite3

class Database:
	def __init__(self, database_name):
		self.db = sqlite3.connect(database_name)
		self.cursor = self.db.cursor()

	def insert(self, flat, table_name):
		try:
			self.cursor.execute('''INSERT INTO ''' + table_name + ''' VALUES(?,?,?,?,?,?,?,?)''', (flat["id"], flat["title"], flat["description"], flat["latitude"],
				flat["longitude"], flat["price"], flat["url"], True))
			self.db.commit()
		except Exception as e:
			pass

	def select_news(self, table_name):
		try:		
			self.cursor.execute('''SELECT id, title, description, latitude, longitude, price, url FROM ''' + table_name + ''' WHERE new = 1''')
			rooms = []
			rows = self.cursor.fetchall()
			for row in rows:
				id, title, description, latitude, longitude, price, url = row
				room = {'id': id, 'title': title, 'description': description, 'latitude': latitude, 'longitude': longitude, 'price': price, 'url': url}
				rooms.append(room)
			return rooms
		except Exception as e:
			pass

	def update_readed(self, room_id, table_name):
		try:
			self.cursor.execute('''UPDATE ''' + table_name + ''' SET new = 0 WHERE id = ?''', (room_id,))
			self.db.commit()
		except Exception as e:
			pass

	def close(self):
		try:
			self.db.close()
		except Exception as e:
			pass
