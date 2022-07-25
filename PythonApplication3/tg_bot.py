# -*- coding: cp1251 -*-
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from config import token
import PythonApplication3 as pya


bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands="start")
@dp.message_handler(Text(equals="�����"))
async def start(message: types.Message):
    start_button = ["�����"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.clean()
    keyboard.add(*start_button)
    await message.answer("������������", reply_markup=keyboard)

@dp.message_handler(Text(equals="�����"))
async def get_all(message: types.Message):
    button = ["������� ���","�����" ,"�����"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.clean()
    keyboard.add(*button)
    await message.answer("��������� �����", reply_markup=keyboard)


@dp.message_handler(Text(equals="������� ���"))
async def get_smec_DM(message: types.Message):
    await message.answer("��������� , ���� ���� ���������� ����������")
    pya.read_data_from_dm()
    with open ("data_dm.txt", "r", encoding="utf-8-sig") as file:
        for line in file:
            await message.answer(line)

@dp.message_handler(Text(equals="�����"))
async def get_smec_DM(message: types.Message):
    await message.answer("��������� , ���� ���� ���������� ����������")
    pya.read_data_from_lenta()
    with open ("data_lenta.txt", "r", encoding="utf-8-sig") as file:
        for line in file:
            await message.answer(line)

@dp.message_handler(Text(equals="�����"))
async def back(message: types.Message):
    await message.answer("�����")

if __name__ == '__main__':
    executor.start_polling(dp)