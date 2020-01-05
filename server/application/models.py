'''
Database structure (table schema, relationships, etc.) are defined here.
'''
from application import db, login_manager

# Class to define the table schema for the user information stored in the database
class Users(db.Model, UserMixin):
    # Define columns

    # Defines the format when querying the database in the terminal
    def __repr__(self):
    	return ''.join([
            
	])
