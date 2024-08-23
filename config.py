import mysql.connector
from dotenv import load_dotenv
import os   

DATABASE = 'cart.db'
 
DEBUG = True

load_dotenv()

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_BUCKET_NAME = os.getenv('AWS_BUCKET_NAME')
AWS_REGION = os.getenv('AWS_REGION')
 
PRODUCT_PRICES = {
    'apple': 20,
    'orange': 80,
    'broccoli': 40,
    'carrot': 90,
    'hot dog': 60,
    'pizza': 50,
    'donut': 90,
    'cake': 40,
    'book': 20,
    'cup': 50,
    'scissors' : 20
}
 
DATABASE_CONFIG = {
    # 'host': 'localhost',  
    # 'user': 'root',
    # 'password': "",
    # 'database': 'cart_db'
    'host': os.getenv("HOST"),  
    'user': os.getenv("USER"),
    'password': os.getenv("PASSWORD"),
    'database': os.getenv("DATABASE"),
    'port':os.getenv("PORT")
}

try:
    conn = mysql.connector.connect(**DATABASE_CONFIG)
    if conn.is_connected():
        print("Connected successfully!")
    conn.close()
except mysql.connector.Error as err:
    print(f"Error: {err}")
 