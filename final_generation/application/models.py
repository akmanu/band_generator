'''
Database structure (table schema, relationships, etc.) are defined here.
'''
from application import db

# Class to define the table schema for the user information stored in the database
class names(db.Model):
    # Define columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(50), nullable = False)
    name_type = db.Column(db.String(10)), nullable = False) # Defines whether the name is a male, female or sur- name

    # Defines the format when querying the database in the terminal
    def __repr__(self):
    	return ''.join([
            "Word ID: ", self.id, '\r\n'
            "Word: ", self.word, '\r\n' 
            "Word Type: ", self.word_type, '\r\n'
	])