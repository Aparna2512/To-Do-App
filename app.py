from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task = request.form['task']
        tasks.append({'name': task, 'completed': False})
    return render_template('index.html', tasks_with_index=enumerate(tasks))

@app.route('/delete/<int:task_id>', methods=['GET'])
def delete(task_id):
    if task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>', methods=['GET'])
def complete(task_id):
    if task_id < len(tasks):
        tasks[task_id]['completed'] = True
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
