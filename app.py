from flask import Flask  # Импортируем библиотеку Flask
app = Flask(__name__)  # Создаем объект приложения (наследуя Flask)


@app.route('/', methods=['GET', 'POST'])
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()
