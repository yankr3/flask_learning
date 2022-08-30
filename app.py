from flask import Flask, render_template
from game_of_life import GameOfLife

app = Flask(__name__)


@app.route('/')
def index():
    GameOfLife(25, 25)
    return render_template('index.html')


@app.route('/live')
def live():
    my_life = GameOfLife()
    if my_life.counter > 0:
        my_life.form_new_generation()
    my_life.counter = my_life.counter + 1
    return render_template('live.html',
                           life=my_life,
                           counter=my_life.counter)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
