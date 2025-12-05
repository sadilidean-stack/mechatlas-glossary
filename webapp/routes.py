from flask import Blueprint, render_template, redirect, url_for, request

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return redirect(url_for('views.glossary_home'))

@views.route('/glossary')
def glossary_home():
    return render_template('glossary/index.html')

@views.route('/search')
def search():
    query = request.args.get('query')
    return f"You searched for: {query}"





