from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token='6285295766:AAFyHSpyhw-PwKDa7jig8lwNQ58utfohejE')
dp = Dispatcher(bot)

'#Main Menu'
button1 = KeyboardButton('各科学习群')
button2 = KeyboardButton('必考科')
button3 = KeyboardButton('商科')
button4 = KeyboardButton('理科')

'#必考科 Menu'
button5 = KeyboardButton('Notes / Nota ✍🏻')
button6 = KeyboardButton('Modul / Exercises ✍🏻')
button7 = KeyboardButton('Video ✍🏻')

'#商科 Menu'
button8 = KeyboardButton('Notes / Nota 💴')
button9 = KeyboardButton('Modul / Exercises 💴')
button10 = KeyboardButton('Video 💴')

'#理科 Menu'
button11 = KeyboardButton('Notes / Nota 🧬')
button12 = KeyboardButton('Modul / Exercises 🧬')
button13 = KeyboardButton('Video 🧬')

'#必考科 Notes/Nota'
button14 = KeyboardButton('BM')
button15 = KeyboardButton('BI')
button16 = KeyboardButton('BC')
button17 = KeyboardButton('SEJ')
button18 = KeyboardButton('PM')
button19 = KeyboardButton('MATHS')

'#商科 Notes/Nota'
button20 = KeyboardButton('SC')
button21 = KeyboardButton('ACC')
button22 = KeyboardButton('EKO')
button23 = KeyboardButton('Perniagaan')

'#理科 Notes/Nota'
button24 = KeyboardButton('BIO')
button25 = KeyboardButton('CHE')
button26 = KeyboardButton('PHY')
button27 = KeyboardButton('ADDMATHS')

'#必考科 Modul / Exercises'
button28 = KeyboardButton('BM')
button29 = KeyboardButton('BI')
button30 = KeyboardButton('BC')
button31 = KeyboardButton('SEJ')
button32 = KeyboardButton('PM')
button33 = KeyboardButton('MATHS')

'#商科 Modul / Exercises'
button34 = KeyboardButton('SC')
button35 = KeyboardButton('ACC')
button36 = KeyboardButton('EKO')
button37 = KeyboardButton('Perniagaan')

'#理科 Modul / Exercises'
button38 = KeyboardButton('BIO')
button39 = KeyboardButton('CHE')
button40 = KeyboardButton('PHY')
button41 = KeyboardButton('ADDMATHS')

'#必考科 Video'
button42 = KeyboardButton('BM')
button43 = KeyboardButton('BI')
button44 = KeyboardButton('BC')
button45 = KeyboardButton('SEJ')
button46 = KeyboardButton('PM')
button47 = KeyboardButton('MATHS')

'#商科 Video'
button48 = KeyboardButton('SC')
button49 = KeyboardButton('ACC')
button50 = KeyboardButton('EKO')
button51 = KeyboardButton('Perniagaan')

'#理科 Video'
button52 = KeyboardButton('BIO')
button53 = KeyboardButton('CHE')
button54 = KeyboardButton('PHY')
button55 = KeyboardButton('ADDMATHS')

'#Main Menu 学习群'
keyboard1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button1).add(button2).add(button3).add(button4)

'#Main Menu 科系'
keyboard2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button5).add(button6).add(button7)
keyboard3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button8).add(button9).add(button10)
keyboard4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button11).add(button12).add(button13)

'#Notes/Nota 科目'
keyboard5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button14).add(button15).add(button16).add(button17).add(button18).add(button19)
keyboard6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button20).add(button21).add(button22).add(button23)
keyboard7 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button24).add(button25).add(button26).add(button27)

'#Modul/Exercises 科目'
keyboard8 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button28).add(button29).add(button30).add(button31).add(button32).add(button33)
keyboard9 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button34).add(button35).add(button36).add(button37)
keyboard10 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button38).add(button39).add(button40).add(button41)

'#Video 科目'
keyboard11 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button42).add(button43).add(button44).add(button45).add(button46).add(button47)
keyboard12 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button48).add(button49).add(button50).add(button51)
keyboard13 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(button52).add(button53).add(button54).add(button55)
@dp.message_handler(commands=['start'])
async def welcome(message: types.Message):
    await message.reply('请点击以下菜单选择, \n同时欢迎大家加入各科学习群。 \n若有什么疑问，可点击左下角的 /help 查询。', reply_markup=keyboard1)
@dp.message_handler()
async def kb_answer(message: types.Message):
    if message.text == '各科学习群':
        await message.answer("以下是全科科目学习群链接：\n 必考科: \n BM: \n https://t.me/+j6UlLBhcPLE3NmM9 \n BI: \n https://t.me/+pzpLKCbxUJZmZTY1 \n BC: \n https://t.me/+UF1YdarLaz9iMmFl \n MM: \n https://t.me/+jeT-Xpc3Kl8yMmM1 \n PM: \n https://t.me/+ywepqgUB8tJlMzk1 \n SEJ: \n https://t.me/+lt-prgM48qk2MGM1 \n \n 商科: \n Acc : \n https://t.me/+B-HQPeHq5ik1NDk1 \n Eko : \n https://t.me/+m5hRLLiGSOdiMWNl \n Perniagaan : \n https://t.me/+X65z5D6iIeU4Yzdl \n Sc: \n https://t.me/+2vPbBO4EZNE0Y2E1 \n \n 理科： \n Fizik: \n https://t.me/+b50p16YkHTY4ZGY9 \n Kimia: \n https://t.me/+Cxq6au4BKDw0MGE1 \n Bio : \n https://t.me/+8BH-WBYeRf0yODc1 \n Add math: \n https://t.me/+NU843K2bc2I3MDhl")
    elif message.text == '必考科':
        await message.answer('请选择：', reply_markup=keyboard2)
    elif message.text == 'Notes / Nota ✍🏻':
        await message.answer('请选择：', reply_markup=keyboard5)
    elif message.text == 'Modul / Exercises ✍🏻':
        await message.answer('请选择：', reply_markup=keyboard8)
    elif message.text == 'Video ✍🏻':
        await message.answer('请选择：', reply_markup=keyboard11)
    elif message.text == '商科':
        await message.answer('请选择：', reply_markup=keyboard3)
    elif message.text == 'Notes / Nota 💴':
        await message.answer('请选择：', reply_markup=keyboard6)
    elif message.text == 'Modul / Exercises 💴':
        await message.answer('请选择：', reply_markup=keyboard9)
    elif message.text == 'Video 💴':
        await message.answer('请选择：', reply_markup=keyboard12)
    elif message.text == '理科':
        await message.answer('请选择：', reply_markup=keyboard4)
    elif message.text == 'Notes / Nota 🧬':
        await message.answer('请选择：', reply_markup=keyboard7)
    elif message.text == 'Modul / Exercises 🧬':
        await message.answer('请选择：', reply_markup=keyboard10)
    elif message.text == 'Video 🧬':
        await message.answer('请选择：', reply_markup=keyboard13)
    else:
        await message.answer('还未更新，请尽请期待')

executor.start_polling(dp, skip_updates=True, on_startup=True, on_shutdown=True)
