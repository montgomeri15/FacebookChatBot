from flask import Flask, request  # Импортируем библиотеку Flask
app = Flask(__name__)  # Создаем объект приложения (наследуя Flask)


@app.route('/', methods=['GET', 'POST'])  # Выведет в http://localhost:5000/
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    app.run()

    # до того как позволить людям отправлять что-либо боту, Facebook проверяет маркер,
    # подтверждающий, что все запросы, получаемые ботом, приходят из Facebook:

    if request.method == 'GET':
        token_sent = request.args["hub.verify_token"]
        # return verify_fb_token(token_sent)

    # если запрос не был GET, это был POST-запрос, и мы обрабатываем запрос пользователя
    else:
        # получаем сообщение, отправленное пользователем боту
        output = request.get_json()


