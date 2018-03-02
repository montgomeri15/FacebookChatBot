from flask import Flask
app = Flask(__name__)  # name - аргумент для определения пути к корневому каталогу


@app.route('/user')
def index():  # функция представления
    return '<h1>Hello World!</h1>'


if __name__ == '__main__':  # сервер запускается только при выполнении сценария
    app.run(debug=True)  # запуск с отладчиком и перезагрузчиком

