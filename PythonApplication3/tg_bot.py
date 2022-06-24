# -*- coding: cp1251 -*-
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token
import PythonApplication3 as pya


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
@dp.message_handler(Text(equals="Назад"))
async def start(message: types.Message):
    start_button = ["Смеси"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.clean()
    keyboard.add(*start_button)
    await message.answer("Приказывайте", reply_markup=keyboard)

@dp.message_handler(Text(equals="Смеси"))
async def get_all(message: types.Message):
    button = ["Детский мир","Лента" ,"Назад"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.clean()
    keyboard.add(*button)
    await message.answer("Категория смеси", reply_markup=keyboard)


@dp.message_handler(Text(equals="Детский мир"))
async def get_smec_DM(message: types.Message):
    await message.answer("Подождите , идет сбор актуальной информации")
    pya.read_data_from_dm()
    with open ("data.csv", "r", encoding="utf-8-sig") as file:
        for line in file:
            rep = ["[","]","'",'<p class=""S_4"">',"</p>",'"']
            for item in rep:
                if item in line:
                    line = line.replace(item,'')
            await message.answer(line)

@dp.message_handler(Text(equals="Лента"))
async def get_smec_DM(message: types.Message):
    await message.answer("Подождите , идет сбор актуальной информации")
    pya.read_data_from_lenta()
    with open ("data_lenta.csv", "r", encoding="utf-8-sig") as file:
        for line in file:
            rep = ['<span class=""price-label__integer"">','"[<div class=""sku-card-small-header__title"">','</div>]',"</p>",'</span>',"[","]","'"]
            for item in rep:
                if item in line:
                    line = line.replace(item,'')
            await message.answer(line)

@dp.message_handler(Text(equals="Назад"))
async def back(message: types.Message):
    await message.answer("Назад")

if __name__ == '__main__':
    executor.start_polling(dp)