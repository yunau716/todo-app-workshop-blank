from Flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

todos = []

@app.route('/')
def index():
    return render_template('-----.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    todo = request.form['todo']
    todos.-----(todo)
    return redirect(url_for('index'))

@app.route('/delete/<int:index>')
def delete(index):
    del todos[-----]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)