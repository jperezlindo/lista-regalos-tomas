from flask import Flask, render_template, redirect, url_for, request
from gift_dao import GiftDAO
from gift import Gift

app = Flask(__name__)

@app.route('/') #url http://localhost:500/
@app.route('/index.html')
def index():
    gifts = GiftDAO.get_gifts()
    return render_template('index.html', gifts=gifts)

@app.route('/give-away', methods=['POST'])
def set_presents():
    if request.method == 'POST':
        gifts, gift = Gift.delete_gift(request.form['id'])
        GiftDAO.store_gifts(gifts)
        gift['who'] = [request.form['person']]
        gifted = Gift.set_to_gifted(gift)
        GiftDAO.store_gifted(gifted)
    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thanks.html')


if __name__ == '__main__':
    print('Holas')
    app.run(debug=True)