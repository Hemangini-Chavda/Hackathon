import mysql.connector
from flask import current_app
 
def get_db_connection():
    conn = mysql.connector.connect(
        host=current_app.config['DATABASE_CONFIG']['host'],
        user=current_app.config['DATABASE_CONFIG']['user'],
        password=current_app.config['DATABASE_CONFIG']['password'],
        database=current_app.config['DATABASE_CONFIG']['database']
    )
    return conn
 
def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cart (
                    id INT PRIMARY KEY,
                    name VARCHAR(100),
                    price DECIMAL(10, 2),
                    quantity INT)''')
    conn.commit()
    c.close()
    conn.close()
 
def add_to_cart(product):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''INSERT INTO cart (id, name, price, quantity)
                 VALUES (%s, %s, %s, %s)
                 ON DUPLICATE KEY UPDATE quantity = quantity + 1''',
              (product['id'], product['name'], product['price'], 1))
    conn.commit()
    c.close()
    conn.close()
 
def update_quantity(product_id, quantity):
    conn = get_db_connection()
    c = conn.cursor()
    if quantity > 0:
        c.execute("UPDATE cart SET quantity = %s WHERE id = %s", (quantity, product_id))
    else:
        c.execute("DELETE FROM cart WHERE id = %s", (product_id,))
    conn.commit()
    c.close()
    conn.close()
 
def delete_from_cart(product_id):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM cart WHERE id = %s", (product_id,))
    conn.commit()
    c.close()
    conn.close()
 
def get_cart():
    conn = get_db_connection()
    c = conn.cursor(dictionary=True)
    c.execute("SELECT * FROM cart")
    items = c.fetchall()
    conn.close()
    total = sum(item['quantity'] * item['price'] for item in items)
    return {'items': items, 'total': total}