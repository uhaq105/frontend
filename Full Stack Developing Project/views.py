from flask import render_template, redirect,  url_for, Blueprint, request

my_view = Blueprint('my_view', __name__)

@my_view.route('/', methods=['POST', 'GET' ])
def home():
    return render_template('index.html')

@my_view.route('/home')
@my_view.route('/js')
@my_view.route('/javascript')
def home_redirect():
    return redirect(url_for('my_view.home'))

@my_view.route('/contact')
def contact():
    return render_template('contact.html')

@my_view.route('/Contact')
def contact_redirect():
    return redirect(url_for('my_view.contact'))


@my_view.route('/pricing')
def pricing():
    return render_template('pricing.html')

@my_view.route('/Pricing')
def pricing_redirect():
    return redirect(url_for('my_view.pricing'))

@my_view.route('/testimonials')
def testimonials():
    return render_template('testimonials.html')

@my_view.route('/Testimonials')
def testimonials_redirect():
    return redirect(url_for('my_view.testimonials'))

@my_view.route('/free')
def freeTrial():
    return render_template('freeTrial.html')

@my_view.route('/free-trial')
def free_redirect():
    return redirect(url_for('my_view.freeTrial'))