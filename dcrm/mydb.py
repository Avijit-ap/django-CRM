import mysql.connector

dataBase=mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Avi8584",
    )

#prepare cusrsor object using cursor() method

cursorObject=dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE elderco")
print("Database created successfully")
