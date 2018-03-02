from flask import Flask
app = Flask(__name__)  # name - аргумент для определения пути к корневому каталогу


@app.route('/user/<name>')
def index(name):  # функция представления
    return '<h1>Hello, %s!</h1>' % name


if __name__ == '__main__':  # сервер запускается только при выполнении сценария
    app.run(debug=True)  # запуск с отладчиком и перезагрузчиком

