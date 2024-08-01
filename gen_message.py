from gigachat import GigaChat
import asyncio

# Открываем файл в режиме чтения
with open('senior/api_gigachat.txt', 'r') as file:
    # Читаем содержимое файла
    content = file.read()

# Извлекаем значение credentials из содержимого файла
credentials = content

# Выводим значение переменной credentials для проверки
# print(credentials)
# def generate_messange(prompt, api=credentials) -> str:
#     # Используйте токен, полученный в личном кабинете из поля Авторизационные данные
#     with GigaChat(credentials=api, verify_ssl_certs=False) as giga:
#         response = giga.chat(prompt, model="GigaChat-Pro")
#     return response.choices[0].message.content

async def generate_messange(prompt, api=credentials) -> str:
    giga = GigaChat(credentials=api, 
                    # model="GigaChat-Pro", 
                    verify_ssl_certs=False)
    response = giga.chat(prompt)
    return response.choices[0].message.content
# print(asyncio.run(generate_messange(prompt='напиши алгоритм сортировки пузырьком на python')))