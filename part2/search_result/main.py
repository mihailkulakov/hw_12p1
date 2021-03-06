# У вас есть список с названиями блюд, 
# пользователь выполняет поиск (поисковая строка передается квери-параметром 'meal'), 
# выведите количество, а также элементы списка, которые содержат искомую строку
# в соответствии с шаблоном.
# Также дополните сам шаблон.
# Если блюд не найдено - возвращайте простую строку "Блюд не найдено"
# Если параметр meal передан - возвращайте простую строку "Введите параметр meal"

from flask import Flask
app = Flask(__name__)


meals = [
    "Пицца с ананасами",
    "Пицца с сыром",
    "Суп с грибами",
    "Суп со шпинатом",
    "Кальцоне",
    "Креветта",
    "Вишневый пирог",
    "Лимонный пирог"
]


@app.route('/search/')
def search():
    # TODO напишите view-функцию здесь
    pass

if __name__=="__main__":
    app.run()