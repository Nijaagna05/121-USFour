from flask import Flask, request, render_template, redirect, url_for
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['inventory']
items_collection = db['items']

# Landing Page
@app.route('/')
def index():
    return redirect(url_for('login'))

# User Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Check login credentials (dummy implementation)
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            return redirect(url_for('dashboard'))
    return render_template('login.html')

# Dashboard - Display all items sorted by nearest warranty due date
@app.route('/dashboard')
def dashboard():
    items = list(items_collection.find().sort('warranty_due_date', 1))
    return render_template('dashboard.html', items=items)

# Add New Item
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        item_data = {
            'name': request.form['name'],
            'company': request.form['company'],
            'serial_number': request.form['serial_number'],
            'model_number': request.form['model_number'],
            'warranty_number': request.form['warranty_number'],
            'warranty_due_date': datetime.strptime(request.form['warranty_due_date'], '%Y-%m-%d'),
            'servicing_date': datetime.strptime(request.form['servicing_date'], '%Y-%m-%d'),
            'bill_image': request.form['bill_image'],
            'customer_care_number': request.form['customer_care_number']
        }
        items_collection.insert_one(item_data)
        return redirect(url_for('dashboard'))
    return render_template('add_item.html')

if __name__ == '__main__':
    app.run(debug=True)