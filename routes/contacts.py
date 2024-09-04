from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.contact import Contact
from utils.db import db

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts = contacts)

@contacts.route('/add', methods=['POST'])
def add_Contact():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    
    new_contact = Contact(name, email, phone)
    
    db.session.add(new_contact)  # Guardar en la base de datos
    db.session.commit() # Terminar Conxion
    
    flash("Contact added successfully!")
    
    return redirect(url_for('contacts.index'))

@contacts.route('/update/<id>', methods = ['POST', 'GET'])
def update_Contact(id):
    
    contact = Contact.query.get(id)
    
    if request.method == 'POST':

        contact.name = request.form['name']           
        contact.email = request.form['email']
        contact.phone = request.form['phone']
        
        db.session.commit()
        
        flash("Contact updated successfully!")
        
        return redirect(url_for('contacts.index'))
    
    else:
        return render_template('edit.html', contact = contact)
    



@contacts.route('/delete/<id>')
def delete_Contact(id):
    contact = Contact.query.get(id)
    db.session.delete(contact)
    db.session.commit()
    flash("Contact deleted successfully!")
    return redirect(url_for('contacts.index'))

@contacts.route('/about')
def about():
    return render_template('about.html')