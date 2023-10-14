import telebot,random,os
from dotenv import load_dotenv
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
# тестовое изменениеееее
def create_enemy():
    list = ['walkers','people']
    name = random.choice(list)
    hp = random.randint(1,20)
    damage = random.randint(10,30)
    return [name, hp, damage]


load_dotenv()
Token = os.getenv('tg_token')
bot = telebot.TeleBot(Token)

damage = 20
hp = 50
enemy = 0
@bot.message_handler(commands=['start'])
def starting(message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton('Начать игру')
    btn2 = KeyboardButton('об игре')
    keyboard.add(btn1,btn2)
    text = '''Вы очнулись в больнице после ранения пулей.
     Вы не нашли ни единой души кроме мертвых и не совсем мертвых людей...
    Ваша цель выжить и найти свою семью...'''
    img = open('start.jpg','rb')
    bot.send_photo(message.chat.id, img, caption = text, reply_markup = keyboard)
@bot.message_handler(content_types=['text'])
def answer(message):
    global damage, hp,enemy
    def choice():
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('Сражаться')
        btn2 = KeyboardButton('Скрыться')
        btn3 = KeyboardButton('Меню')
        keyboard.add(btn1, btn2,btn3)
        bot.send_message(message.chat.id, 'Что вы выбираете?', reply_markup=keyboard)

    if message.text == 'Начать игру':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('Меню')
        btn2 = KeyboardButton('Продолжить историю')
        keyboard.add(btn1, btn2)
#        bot.send_message(message.chat.id, '''Вы проснулись в роли Рика Граймса шерифа штата.
# После долгой комы у вас осталось 50 здоровья и 20 урона.''', reply_markup = keyboard)
        text = '''Вы проснулись в роли Рика Граймса шерифа штата.
После долгой комы у вас осталось 50 здоровья и 20 урона.'''
        img = open('start2.jpg', 'rb')
        bot.send_photo(message.chat.id, img, caption= text, reply_markup = keyboard)
    if message.text == 'Продолжить историю':
        event = random.randint(1,3)
        if event == 1:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = KeyboardButton('Меню')
            btn2 = KeyboardButton('Продолжить историю')
            keyboard.add(btn1, btn2)
            bot.send_message(message.chat.id, text='''Вы никого не встретили и пошли дальше.''', reply_markup=keyboard)
        if event == 2:
            enemy = create_enemy()
            bot.send_message(message.chat.id, text=f'Вы встретили {enemy[0]}, у него {enemy[1]} здоровья и {enemy[2]} урона.')
            choice()
        if event == 3:
            even2 = random.randint(1,10)
            if even2 == 1:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = KeyboardButton('Меню')
                btn2 = KeyboardButton('Продолжить историю')
                keyboard.add(btn1, btn2)
                hp += 10
                bot.send_message(message.chat.id, text = f'Ты нашел аптечку. теперь твое здоровье увеличилось на 10. у вас {hp} здоровья.', reply_markup=keyboard)
            else:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = KeyboardButton('Меню')
                btn2 = KeyboardButton('Продолжить историю')
                keyboard.add(btn1, btn2)
                bot.send_message(message.chat.id,text=f'Ты отправился на вылазку за припасами,но ничего не нашел.',reply_markup=keyboard)
    if message.text == 'Скрыться':
        keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = KeyboardButton('Меню')
        btn2 = KeyboardButton('Продолжить историю')
        keyboard.add(btn1, btn2)
        bot.send_message(message.chat.id, text='Ты успешно скрылся от врага.', reply_markup=keyboard)
    if message.text == 'Сражаться':
        enemy[1] -= damage
        if enemy[1] <= 0:
            keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = KeyboardButton('Меню')
            btn2 = KeyboardButton('Продолжить историю')
            keyboard.add(btn1, btn2)
            bot.send_message(message.chat.id, text=f'Ты убил {enemy[0]}.', reply_markup=keyboard)
        else:
            hp -= enemy[2]
            if hp <= 0:
                keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = KeyboardButton('Меню')
                keyboard.add(btn1)
                bot.send_message(message.chat.id, text=f'ты не смог справиться с ходячим...', reply_markup=keyboard)
            else:
                bot.send_message(message.chat.id, text=f'Вы нанесли урон {enemy[0]}, теперь у него {enemy[1]} здоровья,но он тоже нанёс тебе урон и теперь у тебя {hp} здоровья .')
                choice()














bot.polling(none_stop=True)
