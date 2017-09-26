"""
	helps with stuff
"""
from sys import argv
from os import system
from models import getModels
from peewee import SqliteDatabase

if "--create" in argv:
	print "[+] Creating Tables..."
	db = SqliteDatabase("devClone.db")
	Rant, Action = getModels(db)

	db.create_tables([Rant, Action])

elif "--recreate" in argv:
	print "[+] Recreating..."
	system("rm devClone.db")
	system("python tool.py --create")
