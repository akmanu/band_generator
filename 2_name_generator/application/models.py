'''
Database structure (table schema, relationships, etc.) are defined here.
'''
from application import db

# Class to define the table schema for the user information stored in the database
class Words(db.Model):
    # Define columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    word = db.Column(db.String(50), nullable = False)
    word_type = db.Column(db.String(10), nullable = False) # Defines whether the word is a noun, adjective, etc.
    band_or_genre = db.Column(db.String(10), nullable = False)

    # Defines the format when querying the database in the terminal
    def __repr__(self):
    	return ''.join([
            "Word ID: ", str(self.id), '\r\n'
            "Word: ", str(self.word), '\r\n' 
            "Word Type: ", str(self.word_type), '\r\n'
	])
    