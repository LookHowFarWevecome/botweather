import telebot
import pyowm


owm = pyowm.OWM('53dbc220ffe694fcbd8c90637b946c45', language='ru')
bot = telebot.TeleBot("772719862:AAF3tfTPt0CimGKjyJnRlUgV03j_HJ2qwYc")

@bot.message_handler(commands=['help'])
def help(message):
	answer = "Привет, я бот который показывает статистику погоды в определенной локации или городе. \
	\nДля работы со мной, напише мне название города или скинь свою локацию."
	bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['location'])
def send_weather_location(message):
	obs = owm.weather_at_coords(message.location.latitude, message.location.longitude)
	w = obs.get_weather()
	temp = w.get_temperature('celsius')["temp_min"]
	windspeed = w.get_wind()['speed']
	humidity = w.get_humidity()
	pressure = w.get_pressure()['press']
	answer = "\nТемпература: " + str(temp) +"°C\n" + w.get_detailed_status().title() + \
	"\nСкорость ветра: " + str(windspeed) + " м/с\n" + "Влажность: " + str(humidity) +\
	"%\n" + "Давление: " + str(pressure) + " гПа"

	bot.send_message(message.chat.id, answer)

@bot.message_handler(content_types=['text'])
def send_weather_text(message):
	try:
		obs = owm.weather_at_place(message.text)
		w = obs.get_weather()
		temp = w.get_temperature('celsius')["temp_min"]
		windspeed = w.get_wind()['speed']
		humidity = w.get_humidity()
		pressure = w.get_pressure()['press']
		answer = "\nТемпература: " + str(temp) +"°C\n" + w.get_detailed_status().title() +\
		"\nСкорость ветра: " + str(windspeed) + " м/с\n" + "Влажность: " + str(humidity) +\
		"%\n" + "Давление: " + str(pressure) + " гПа"
	except:
		answer = "Город не найден. Если не знаете как работать с ботом, напишите /help"
	bot.send_message(message.chat.id, answer)
bot.polling(none_stop=True)