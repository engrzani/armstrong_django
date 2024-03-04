from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3 as sql

app = Flask(__name__)
def create_table():
    con = sql.connect('web_db.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS "users" (
    "cid" INTEGER PRIMARY KEY AUTOINCREMENT,
    "NAME" TEXT,
    "EMAIL" EMAIL,
    "CONTACT" TEXT ,
    "USERNAME" TEXT,
    "PASSWORD" TEXT
)''')
    cur.execute( '''CREATE TABLE IF NOT EXISTS "contact" (
    "cid" INTEGER PRIMARY KEY AUTOINCREMENT,
    "name" TEXT,
    "email" TEXT,
    "sub" TEXT,
    "msg" TEXT
)''')
    con.commit()
    con.close()

@app.route("/booking", methods=['POST','GET'])
def booking():
    con = sql.connect("web_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users")
    data = cur.fetchall()
    return render_template("booking.html", datas=data)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")
@app.route("/index")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/services")
def services():
    return render_template("add_user.html")

@app.route("/car")
def car():
    return render_template("car.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Query the database to check if the username exists
        con = sql.connect("web_db.db")
        con.row_factory = sql.Row
        cur = con.cursor()
        cur.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cur.fetchone()  # Fetch a single row

        con.close()

        if user and user['password'] == password:  # Assuming 'password' is the column name
            # Successful login
            # Redirect to a new page or perform any other desired action
            return render_template('index.html', username=username, login_successful=True)

        # Failed login
        # You might want to redirect to the login page with an error message
        return render_template('login.html', error_message='Invalid credentials')

    # If the request method is GET, simply render the login page
    return render_template('login.html')

@app.route("/rentacar")
def Rent():
    return render_template("rentacar.html")


@app.route("/result")
def result():
    feedback_message = request.args.get('feedback', '')
    return render_template("result.html", feedback_message=feedback_message)
@app.route("/contact", methods=['POST', 'GET'])
def contact():
    if request.method == 'POST':
        nm = request.form.get('name')
        em = request.form.get('em')
        sub = request.form.get('sub')
        msg = request.form.get('msg')

        con = sql.connect("web_db.db")
        cur = con.cursor()

        cur.execute("INSERT INTO contact (name, email, sub, msg) VALUES (?, ?, ?, ?)",
                    (nm, em, sub, msg))

        con.commit()
        con.close()  # Close the database connection

        flash('Feedback submitted successfully!', 'success')

    return render_template("contact.html")
# @app.route("/contact", methods=['POST', 'GET'])
# def contact():
#     if request.method == 'POST':
#         nm = request.form.get('name', False)
#         em = request.form.get('em', False)
#         sub = request.form.get('sub', False)
#         msg = request.form.get('msg', False)


#         con = sql.connect("web_db.db")
#         cur = con.cursor()

#         cur.execute("INSERT INTO contact (name, email, sub, msg) VALUES (?, ?, ?, ?)",
#                     (nm, em, sub, msg))

#         con.commit()
#         flash('Feedback submitted successfully!', 'success')
#         return redirect(url_for("result"))

#     return render_template("contact.html")

@app.route("/feedback")
def feedback():
    con = sql.connect("web_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from contact")
    data = cur.fetchall()
    return render_template("show_Feedback.html")


@app.route("/add_user", methods=['POST','GET'])
def add_user():
    if request.method == 'POST':
        #request.form.get("something", False)
        name = request.form.get('name', False)
        email = request.form.get('email', False)
        contact= request.form.get('contact', False)
        username = request.form.get('username', False)
        password = request.form.get('password', False)
        con = sql.connect("web_db.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users (NAME, EMAIL, CONTACT, USERNAME, PASSWORD) VALUES (?, ?, ?, ?, ?)", (name,email, contact, username,password))
        con.commit()
        flash('User Added', 'success')
        return redirect(url_for("booking"))
    return render_template("add_user.html")


@app.route("/edit_user/<string:cid>", methods=['POST', 'GET'])
def edit_user(cid):
    if request.method == 'POST':
        name = request.form.get('name', False)
        email = request.form.get('email', False)
        contact = request.form.get('contact', False)
        username = request.form.get('username', False)
        password = request.form.get('password', False)
        con = sql.connect("web_db.db")
        cur = con.cursor()
        cur.execute("update users set NAME=?,EMAIL=?,CONTACT=?,USERNAME=?,PASSWORD=? where CID=?", (name, email, contact, username, password, cid))
        con.commit()
        flash('User Updated', 'success')
        return redirect(url_for("booking"))
    con = sql.connect("web_db.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from users where CID=?", (cid,))
    data = cur.fetchone()
    return render_template("edit_user.html", datas=data)

@app.route("/delete_user/<string:cid>", methods=['GET'])
def delete_user(cid):
    con = sql.connect("web_db.db")
    cur = con.cursor()
    cur.execute("delete from users where CID=?", (cid,))
    con.commit()
    flash('User Deleted', 'warning')
    return redirect(url_for("booking"))

# Function to check if a number is an Armstrong number
def is_armstrong(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
    return armstrong_sum == num

@app.route('/find_armstrong', methods=['POST'])
def find_armstrong():
    min_number = int(request.form['min_number'])
    max_number = int(request.form['max_number'])
    armstrong_numbers = [num for num in range(min_number, max_number + 1) if is_armstrong(num)]
    return render_template('result.html', result=armstrong_numbers)

# Route to check if a number is an Armstrong number
@app.route('/check_armstrong', methods=['POST'])
def check_armstrong():
    check_number = int(request.form['check_number'])
    is_armstrong_number = is_armstrong(check_number)
    return render_template('result.html', result=is_armstrong_number)

if __name__ == '__main__':
    app.secret_key = 'admin123'
    app.run(debug=True)
