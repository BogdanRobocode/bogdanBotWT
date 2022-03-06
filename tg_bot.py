# '5127358340:AAHwM9i66ndLhEqLJP39zxVrtGgX3EYYRWI', use_context=True)
API_KEY = '5127358340:AAHwM9i66ndLhEqLJP39zxVrtGgX3EYYRWI'
from email import message
from pickletools import markobject
import telebot
import random
import requests



bot = telebot.TeleBot(API_KEY)

# url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=9c6412d22ee09805ef56e37a3a4cac9c"



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Запуск работы")

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Запуск помощника")

@bot.message_handler(commands=['random'])
def randomnum(message):
    num = random.randint(0,100)
    bot.send_message(message.chat.id, str(num))

@bot.message_handler(commands=['weather'])
def get_weather(message):
    bot.send_message(message.chat.id, "Введите название города")
   
    @bot.message_handler(content_types=['text'])
    
    def test(message):
        global city
        city = message.text
        bot.send_message(message.chat.id, str(city))
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid=9c6412d22ee09805ef56e37a3a4cac9c"

        response = requests.get(url)
        weather_list = response.json()
        weather = weather_list["weather"][0]["description"] 
        celc = weather_list["main"]["temp"] 
        bot.send_message(message.chat.id, weather )
        bot.send_message(message.chat.id, str(celc) + " ℃")

    bot.register_next_step_handler(message, test)



@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, Богдан')
    if message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока, Богдан')
    if message.text.lower() == 'Погода':
        bot.send_message(message.chat.id, 'Введи название города ')
    





bot.polling()
