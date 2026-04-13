import asyncio
import time
import discord
from discord.ext import commands
from discord import AllowedMentions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Configuración de Discord bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Configuración de Selenium
chrome_options = Options()
options = webdriver.ChromeOptions()




# Función para hacer scraping con Selenium
def check_price():
    driver = None  # Inicializa el driver como None
    try:

        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.cardmarket.com/en/Vanguard/Users/Onlycards/Offers/Singles?idExpansion=6221&sortBy=price_asc")

        # Espera explícita hasta que el elemento esté presente (máximo 10 segundos)
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '/html/body/main/section/div[4]/div[2]/div[1]/div[4]/div/div[2]/div/div[2]/div[2]/div/span'))
        ).text
        price_value = element.replace('€', '').split(',')[0].strip()

        print(price_value)
        # Verifica si el valor es distinto de 999
        Dprice = 999.99
        if price_value != 999:
            return True, price_value
        else:
            return False, price_value
    except Exception as e:
        print(f"Error durante el scraping: {e}")
        return False, None
    finally:
        if driver:
            driver.quit()


# Función asincrónica para chequear el valor periódicamente
async def periodic_check(*users):
    while True:
        found, price_value = check_price()
        if found:
            for user in users:
                await user.send(f"¡El valor ha cambiado! El nuevo valor es: {price_value}")
            break
        else:
            print(f"No se encontró el valor deseado, esperando 1 minuto... (Valor actual: {price_value})")
            await asyncio.sleep(60)


# Evento al iniciar el bot
@client.event
async def on_ready():
    print(f'{client.user} ha iniciado sesión')

    # Busca al usuario por su ID
    user = await client.fetch_user(360826355669270528)
    user2 = await client.fetch_user(400025171970490369)

    # Ejecutar ambos chequeos en paralelo
    await asyncio.gather(
        await periodic_check(user, user2)

    )


# Ejecuta el bot (reemplaza 'YOUR_DISCORD_BOT_TOKEN' por el token de tu bot)
client.run('token')