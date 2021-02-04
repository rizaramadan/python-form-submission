from flask import Flask, render_template, request
app = Flask(__name__)


# Fungsi yang menampilkan form
@app.route('/')
def form():
    return render_template('form.html')


# Fungsi yang menangkap form submit
# karena action di form kita tulis '/submit', disini kita tulis juga '/submit'
# supaya nerima data yang dikirim dari form disini
@app.route('/submit', methods=['POST'])
def form_submit():
    username = request.form['username']
    return render_template('submit.html', username=username)


if __name__ == '__main__':
    app.run()
