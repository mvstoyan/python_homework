import sqlite3

with sqlite3.connect("../db/lesson.db") as conn:
    print("Database connected successfully.")
    
    conn.execute("PRAGMA foreign_keys = 1")

    cursor = conn.cursor()
    query = """SELECT orders.order_id, SUM(products.price * line_items.quantity) 
    AS total_order_value 
    FROM orders 
    JOIN line_items ON orders.order_id = line_items.order_id 
    JOIN products ON products.product_id = line_items.product_id 
    GROUP BY orders.order_id 
    ORDER BY orders.order_id 
    LIMIT 5;"""

#Task2
    subquery = """SELECT 
    customers.customer_name, 
    AVG(order_totals.total_price) AS average_total_price
    FROM customers
    LEFT JOIN (
    SELECT orders.customer_id AS customer_id_b, 
    SUM(products.price * line_items.quantity) AS total_price
    FROM orders
    JOIN line_items ON orders.order_id = line_items.order_id
    JOIN products ON products.product_id = line_items.product_id
    GROUP BY orders.order_id
    ) AS order_totals
    ON customers.customer_id = order_totals.customer_id_b
    GROUP BY customers.customer_id;"""

    #cursor.execute(subquery)
    #results = cursor.fetchall()
    #print(results)
    #Task3
    cursor.execute("""
        SELECT customer_id FROM customers 
        WHERE customer_name = 'Perez and Sons';
    """)
    customer_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT employee_id FROM employees 
        WHERE first_name = 'Miranda' AND last_name = 'Harris';
    """)
    employee_id = cursor.fetchone()[0]

    cursor.execute("""
        SELECT product_id FROM products 
        ORDER BY price ASC 
        LIMIT 5;
    """)
    product_ids = [row[0] for row in cursor.fetchall()]

    cursor.execute("""
        INSERT INTO orders (customer_id, employee_id)
        VALUES (?, ?)
        RETURNING order_id;
    """, (customer_id, employee_id))
    
    order_id = cursor.fetchone()[0]

    for product_id in product_ids:
        cursor.execute("""
            INSERT INTO line_items (order_id, product_id, quantity)
            VALUES (?, ?, 10);
        """, (order_id, product_id))

    cursor.execute("""
        SELECT 
            line_items.line_item_id, 
            line_items.quantity, 
            products.product_name
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        WHERE line_items.order_id = ?;
    """, (order_id,))
    
    #print("\nOrder Summary:")
    #for row in cursor.fetchall():
    #    print(row)

    #Task4
cursor.execute("""
    SELECT 
        employees.employee_id, 
        employees.first_name, 
        employees.last_name,
        COUNT(orders.order_id) AS order_count
    FROM employees
    JOIN orders ON orders.employee_id = employees.employee_id
    GROUP BY employees.employee_id
    HAVING COUNT(orders.order_id) > 5;
""")

print("\nEmployees with more than 5 orders:")
for row in cursor.fetchall():
    print(row)