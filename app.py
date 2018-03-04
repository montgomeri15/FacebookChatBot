from flask import Flask, request  # Импортируем библиотеку Flask
from pymessenger import Bot  # Импортируем нужный PyMessenger с ботом (https://github.com/davidchua/pymessenger)
import random

app = Flask(__name__)  # Создаем объект приложения (наследуя Flask)

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
VERIFY_TOKEN = 'YOUR_VERIFY_TOKEN'

bot = Bot(ACCESS_TOKEN)


@app.route('/', methods=['GET', 'POST'])
def receive_message():  # получаем соо от ФБ боту.

    # до того, как позволить людям отправлять что-либо боту, Facebook проверяет маркер,
    # подтверждающий, что все запросы, получаемые ботом, приходят из Facebook:

    if request.method == 'GET':
        token_sent = request.args['hub.verify_token']
        return verify_fb_token(token_sent)

    else:  # если запрос не был GET, это был POST-запрос, и мы обрабатываем запрос пользователя

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
        return 'Сообщение обработано.'


def verify_fb_token(token_sent):  # функция проверки токена/маркера (бот должен его иметь для ФБ)
    if token_sent == VERIFY_TOKEN:  # Сверяет токен ФБ и наш. При совпадении можно делать запрос, иначе - ошибка.
        return request.args.get('hub.challenge')
    return 'Ошибка: неверный токен.'


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)  # отправляет пользователю текст в соответствии с параметром response
    return 'Успешно!'


def get_message():
    sample_responses = ['Потрясающе!', 'Я вами горжусь!', 'Продолжайте в том же духе!',
                        'Лучшее, что я когда-либо видел!']  # отправляет случайные сообщения юзеру
    return random.choice(sample_responses)


if __name__ == "__main__":
    app.run()
