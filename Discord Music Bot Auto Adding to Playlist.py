import random
from contextlib import suppress
from time import sleep

import pyautogui as pag
import numpy as np
import pyperclip
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

banlist = ['Dritter Teil - Kommunionsgesange', "Lakmé, ACT 1: Dôme épais le jasmin à la rose s'assemble (Lakmé/Mallika)", "Prokofiev: Romeo and Juliet, Op. 64 / Act 1 - Dance Of The Knights",
           'Мания', 'Lions In Cages', 'Мотыльки']

driver = webdriver.Firefox()
driver.get("https://music.yandex.kz/home")

for _ in range(10):
    with suppress(Exception):
        driver.find_element(By.XPATH, '/html/body/div[1]/div[20]/div/span').click()
        break

print('Zooming')

for _ in range(10):
    pag.hotkey('ctrl', '-')
    sleep(.01)

print('Continuing')

for _ in range(10):
    with suppress(Exception):
        driver.find_element(By.XPATH, '/html/body/div[1]/div[20]/div/span').click()
        break

for _ in range(10):
    with suppress(Exception):
        driver.find_element(By.XPATH, '/html/body/div[5]/button').click()
        break

driver.get('https://music.yandex.kz/users/yamusic-daily/playlists/108494846')

sleep(1)

titles = driver.find_elements(By.XPATH, "//div[@class='d-track__overflowable-column']//a[contains(@class, 'd-track__title')]")
artists = driver.find_elements(By.XPATH,"//div[@class='d-track__overflowable-column']//span[@class='d-track__artists']//a[contains(@class, 'deco-link')][1]")

print('Found all songs')

songs = dict()

for i in range(len(titles)):
    
    songs.update({titles[i].text: artists[i].text})
    print(i, titles[i].text, end=' - ')

    print(artists[i].text)

print(songs)

print('Started pushing songs in discord bot\'s queue')

driver.close()
driver.quit()

sleep(1)

shuffled_songs = list(songs.items())
random.shuffle(shuffled_songs)

sleep(1)
# shuffled_songs = [('Феноменально', 'Ty Gjj & Yami'), ('Рассвет-закат', 'Хас'), ('Позови меня с собой', 'TSOY'), ('Все пройдет', 'HOLLYFLAME'), ('Не забывай', 'Джоззи'), ('Money', 'V $ X V PRiNCE'), ('Terrorist', 'Givemerap.'), ('В хлам', 'Deesmi'), ('Сумбур', 'Ty Gjj & Yami'), ('Дайсё', 'Aodzu'), ('Шёлковая простынь', 'O.G EzzY'), ('Pesetas', 'Rilès'), ('Мумия', 'Limee'), ('Go Down Deh', 'Spice'), ('Шаг в темноту', 'Рок-Опера Орфей'), ('Тлеет', 'Deydara'), ('Прочная вера', 'Пабло'), ('Самурай', 'Miyagi'), ('Моя хулиганка', 'XOLIDAYBOY'), ('Основа основ', 'Mealon'), ('Холст', 'Шалих'), ('Go Girl', 'Pitbull'), ('Статус души', 'Bakr'), ('Далеко', 'ДжиАш'), ('Нет назад пути', 'A.Ja'), ('За рулём', 'Zorkii'), ('За закатами', 'Сарги'), ('Белой птицей', 'Истов'), ('Я хочу любить', 'Амура'), ('аппарат президента 2', 'масло черного тмина'), ('OneLove', 'Miyagi & Эндшпиль'), ('La Misère', '$krrt Cobain'), ('Оставь бокал', 'XOLIDAYBOY'), ('Девочка рай', 'DronGo'), ('Endorphin', 'Andy Panda'), ('Ты и Я', 'Xcho'), ('Во мгле', 'Сарги'), ('Скорпион', 'Monday'), ('Джанго', 'Эндшпиль'), ('Фантом', 'BODIEV'), ('Ни кола, ни двора', 'Lustova'), ('Gaichite', 'Misha Xramovi'), ('Очи', 'Bakr'), ('Игра', 'Александр Эгромжан'), ('Чудеса', 'BODIEV'), ('Гангстер', 'Xcho'), ('Peeping in My window (JuanMendezFreestyle)', 'Juan Mendez'), ('АЗИАТСКАЯ ЭСТЕТИКА', 'Ulukmanapo'), ('Снизу вверх', 'Честер Небро'), ('Заплаканный Лондон', 'NEEL'), ('Зёрна (Electro)', 'Odnono'), ('Два мустанга', 'Шалих'), ('Дикари', 'Xassa'), ('Лонг айленд', 'Золотое Перо'), ('10 стилей (Prod. by GROM MUSIC)', 'KSON'), ('Воином', 'Намо Миниган'), ('Душа моей души', 'ADAM'), ('Тропа', 'Пабло'), ('Enjoy You Life', 'LIOVA'), ('Далада', 'V $ X V PRiNCE')]

for song, artist in shuffled_songs:
    print(f'{song} - {artist}')
    pag.typewrite('/play ', interval=0.01)
    pyperclip.copy(f'{song} - {artist}')
    pag.hotkey("ctrl", "v")
    sleep(1.5)
    pag.press('enter')
    sleep(.05)
    pag.press('enter')
    sleep(.1)

