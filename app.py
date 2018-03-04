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
        return verify_fb_token(token_sent)

    # если запрос не был GET, это был POST-запрос, и мы обрабатываем запрос пользователя
    else:
        # получаем сообщение, отправленное пользователем боту
        output = request.get_json()
        for event in output['entry']:
            messaging = event['messaging']
            for message in messaging:
                if message.get('message'):
                    recipient_id = message['sender']['id']  # определяем ID, чтобы знать, куда отправлять ответ
                    if message['message'].get('text'):  # если текстовое сообщение, то:
                        response_sent_text = get_message()
                        send_message(recipient_id, response_sent_text)
                    if message['message'].get('attachments'):  # если это вложение (не текст), то:
                        response_sent_nontext = get_message()
                        send_message(recipient_id, response_sent_nontext)
        return 'Message Processed'

def verify_fb_token(token_sent):  # функция проверки токена/маркера (бот должен его иметь для ФБ)
    '''Сверяет токен, отправленный фейсбуком, с имеющимся у вас.
        При соответствии позволяет осуществить запрос, в обратном случае выдает ошибку.'''
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def send_message(recipient_id, response):
    '''Отправляет пользователю текстовое сообщение в соответствии с параметром response.'''
    bot.send_text_message(recipient_id, response)
    return "success"


