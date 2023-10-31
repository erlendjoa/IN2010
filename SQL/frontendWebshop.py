import psycopg2

dbname = ""
username = ""
password = ""

connection = \
    "host='dbpg-ifi-kurs01.uio.no' " + \
    "dbname='" + dbname + "' " +\
    "user'" + username + "' " +\
    "password'" + password + "' " +\
    "post='5432'"

def frontend():
    conn = psycopg2.connect(connection)
    ch = 0
    while username == "":
        print("Please choose an option:\n 1. Register\n 2. Login\n 3. Exit")
        ch = int(input("Option: "))
        if ch == 1:
            register(conn)
        elif ch == 2:
            print("")
        elif ch == 3:
            return


def register(conn):
    print(" -- REGISTER USER -- ")

    # GET VARIABLES
    username = input("Username: ")
    password = input("Password: ")
    name = input("Name: ")
    address = input("Address: ")

    #INSERT INTO DB
    cur = conn.cursor()
    cur.execute("INSERT INTO ws.users(name, username, password, address) VALUES (%s, %s, %s, %s);",
                (name, username, password, address))
    
    conn.commit()
    return


def login(conn):
    print(" -- LOGIN USER -- ")
    username = input("USERNAME: ")
    password = input("PASSWORD: ")
    
    cur = conn.cursor()
    cur.execute("SELECT username, name from ws.users WHERE username LIKE %s AND passord LIKE %s;",
                (username, password))
    
    # FETCH TABLE FROM PK = USERNAME, PASSWORD
    rows = cur.fetchall()
    if len(rows) > 0:
        row = rows[0]
        print(f"Welcome, {row[1]}")
        return row[1]
    else:
        print("Incorrect username or password")
        return ""
    

def search(conn, username):
    print(" -- SEARCH -- ")
    name = input("Search: ")
    category = input("Category: ")

    q = "SELECT p.pid, p.name, p.price, c.name AS category, p.description " + \
    "FROM ws.products AS p INNER JOIN ws.categories AS c USING (cid) " + \
    "WHERE p.name LIKE %(name)s"

    if category != "":
        q += " AND c.name LIKE %(category)s"
    q += ";"

    cur = conn.cursor()
    cur.execute(q, {'name' : "%"+ name +"%", 'category' : category})
    
    rows = cur.fetchall()
    if len(rows) == 0:
        print("No results found.")
        return
    print (" -- RESULTS --")
    for row in rows:
        print("=== " + row[1] +  " ===\n" + \
        "Product ID: " + str(row[0]) + "\n" + \
        "Price: " + str(row[2]) + "\n" + \
        "Category: " + row[3])
        if row[4] != "NULL":
            print("Description: " + row[4])
        print("\n")
    
    orderProducts(conn, username)

def orderProducts(conn, username):
    print("")


frontend()