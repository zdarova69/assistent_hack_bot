from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
import asyncio

# Открываем файл в режиме чтения
with open('api_gigachat.txt', 'r') as file:
    # Читаем содержимое файла
    content = file.read()

# Извлекаем значение credentials из содержимого файла
credentials = content


payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="Ты бот для помощи команде в хакатоне."
        )
    ],
    temperature=0.7,
    max_tokens=100,
)

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
    payload.messages.append(Messages(role=MessagesRole.USER, content=prompt))
    response = giga.chat(payload)
    return response.choices[0].message.content
# print(asyncio.run(generate_messange(prompt='напиши алгоритм сортировки пузырьком на python')))