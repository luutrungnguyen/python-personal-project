from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import sys
import asyncio
from datetime import datetime as dt
import telegram
from telegram import Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Update

# Credentials
f = open('./credential.txt', "r")
lines = f.readlines()
f.close()
MSNV=lines[0].replace('\r','')
print(MSNV)
UserName=lines[1].replace('\r','')
print(UserName)
Password=lines[2].replace('\r','')
print(Password)
bot_token = "6587123968:AAGY6Ra1oMGLyLIwhhs8YMD43V7OmFN56UU"  # Replace with your bot token
bot_chatID_Trungnl = "-4040013930"  # Replace with your chat ID
img_path_in = "C:\\CNext-Trungnl\\cnext_in.png"
img_path_out = "C:\\CNext-Trungnl\\cnext_out.png"
currentDT = dt.now()
photo_caption_in = f"Clock in Successful ✅✅✅\nUser: {UserName}\nDate: {currentDT.day}-{currentDT.month}-{currentDT.year}\nTime: {currentDT.hour}:{currentDT.minute}:{currentDT.second}"
photo_caption_out = f"Clock out Successful ✅✅✅\nUser: {UserName}\nDate: {currentDT.day}-{currentDT.month}-{currentDT.year}\nTime: {currentDT.hour}:{currentDT.minute}:{currentDT.second}"

# Define the send_photo_async function outside of clock_in
async def send_photo_async(bot, chat_id, img_path, photo_caption):
    bot.send_photo(chat_id=chat_id, photo=open(img_path, 'rb'), caption=photo_caption)
bot = None
def clock_in(update: telegram.Update, context: CallbackContext) -> None:
    try:
        # URLs
        update.message.reply_text("Clock In Process is running, please wait a minute! 😂")
        url_login = "https://cnext.centralgroup.com/"
        url_wta = "https://central.wta-eu3.wfs.cloud/workforce/Mobile.do;jsessionid=B8E3FB820182F8EE96C0D5647BB606B23109D3BE-n1#app"

        # Configure Chrome options for headless mode and enable location access
        chrome_options = Options()
        chrome_options.add_argument("--allow-file-access-from-files")
        chrome_options.add_argument("--enable-precise-geolocation")
        chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Enable location access without prompts
        chrome_options.add_argument("--window-size=1920x979")

        chromedriver_path = "C:\\chromedriver\\chromedriver.exe"  # Update with your path

        # Create a Chrome WebDriver instance with a specified executable path
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Login to cnext
        driver.get(url_login)

        wait = WebDriverWait(driver, 10)

        # Wait for the login page elements to be ready
        user_input = wait.until(EC.presence_of_element_located((By.NAME, "UserName")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "Password")))

        user_input.send_keys(UserName)
        password_input.send_keys(Password)
        password_input.submit()
        time.sleep(5)
        # Load the target page
        driver.get(url_wta)

        # Simulate pressing the "Tab" key twice
        driver.switch_to.active_element.send_keys(Keys.TAB)
        driver.switch_to.active_element.send_keys(Keys.TAB)

        # Simulate pressing the "Enter" key once
        driver.switch_to.active_element.send_keys(Keys.ENTER)

        # Wait for the element with the XPath //*[@id="ext-button-2"] to become clickable
        element_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-button-2"]')))

        # Click on the element
        element_to_click.click()

        # Take a screenshot and save it
        current_time = dt.now()  # Use dt instead of datetime
        nowtime = current_time.strftime("%Y-%m-%d_%H%M%S")
        clockintime = nowtime
        name_img_in = f'C:\\CNext-Trungnl\\cnext_in_{clockintime}.png'
        time.sleep(5)
        driver.save_screenshot(name_img_in)

        # Print the screenshot URL and save it to a file
        img_url_in = f'file://{name_img_in}'
        print(img_url_in)

        # Close the driver
        driver.quit()
        
#        context.bot.send_message(chat_id=update.message.chat_id, text="Clock in successful! ✅")
        
        # Call the send_photo_async function to send the photo
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_photo_async(bot, bot_chatID_Trungnl, name_img_in, photo_caption_in))

    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"An error occurred: {str(e)}")

def clock_out(update: telegram.Update, context: CallbackContext) -> None:
    try:
        # URLs
        update.message.reply_text("Clock Out Process is running, please wait a minute! 😂")
        url_login = "https://cnext.centralgroup.com/"
        url_wta = "https://central.wta-eu3.wfs.cloud/workforce/Mobile.do;jsessionid=B8E3FB820182F8EE96C0D5647BB606B23109D3BE-n1#app"

        # Configure Chrome options for headless mode and enable location access
        chrome_options = Options()
        chrome_options.add_argument("--allow-file-access-from-files")
        chrome_options.add_argument("--enable-precise-geolocation")
        chrome_options.add_argument("--use-fake-ui-for-media-stream")  # Enable location access without prompts
        chrome_options.add_argument("--window-size=1920x979")

        chromedriver_path = "C:\\chromedriver\\chromedriver.exe"  # Update with your path

        # Create a Chrome WebDriver instance with a specified executable path
        service = Service(chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)

        # Login to cnext
        driver.get(url_login)

        wait = WebDriverWait(driver, 10)

        # Wait for the login page elements to be ready
        user_input = wait.until(EC.presence_of_element_located((By.NAME, "UserName")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "Password")))

        user_input.send_keys(UserName)
        password_input.send_keys(Password)
        password_input.submit()
        time.sleep(4)
        # Load the target page
        driver.get(url_wta)

        # Simulate pressing the "Tab" key twice
        driver.switch_to.active_element.send_keys(Keys.TAB)
        driver.switch_to.active_element.send_keys(Keys.TAB)

        # Simulate pressing the "Enter" key once
        driver.switch_to.active_element.send_keys(Keys.ENTER)

        # Wait for the element with the XPath //*[@id="ext-button-2"] to become clickable
        element_to_click = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-button-5"]')))

        # Click on the element
        element_to_click.click()

        # Take a screenshot and save it
        current_time = dt.now()  # Use dt instead of datetime
        nowtime = current_time.strftime("%Y-%m-%d_%H%M%S")
        clockouttime = nowtime
        name_img_out = f'C:\\CNext-Trungnl\\cnext_out_{clockouttime}.png'
        time.sleep(5)
        driver.save_screenshot(name_img_out)

        # Print the screenshot URL and save it to a file
        img_url_out = f'file://{name_img_out}'
        print(img_url_out)

        # Close the driver
        driver.quit()
        
#        context.bot.send_message(chat_id=update.message.chat_id, text="Clock in successful! ✅")
        
        # Call the send_photo_async function to send the photo
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_photo_async(bot, bot_chatID_Trungnl, name_img_out, photo_caption_out))
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"An error occurred: {str(e)}")
def start(update: telegram.Update, context: CallbackContext) -> None:
    try:
        # URLs
        update.message.reply_text("Use /clockin for Clock In Process and /clockout for Clock Out Process 👌")
    except Exception as e:
        context.bot.send_message(chat_id=update.message.chat_id, text=f"An error occurred: {str(e)}")

def main() -> None:
    global bot
    # Initialize your bot and other variables
    bot_token = "6587123968:AAGY6Ra1oMGLyLIwhhs8YMD43V7OmFN56UU"  # Replace with your bot token
    bot_chatID_Trungnl = "-4040013930"  # Replace with your chat ID
    img_path = "C:\\CNext-Trungnl\\cnext.png"
    currentDT = dt.now()
    photo_caption = f"User: {UserName}\nDate: {currentDT.day}-{currentDT.month}-{currentDT.year}\nTime: {currentDT.hour}:{currentDT.minute}:{currentDT.second}"

    # Set up the Telegram Bot
    bot = Bot(token=bot_token)

    # Set up the Telegram Updater
    updater = Updater(bot=bot)

    dispatcher = updater.dispatcher

    # Register a command handler for /clockin
    dispatcher.add_handler(CommandHandler("clockin", clock_in))
    dispatcher.add_handler(CommandHandler("clockout", clock_out))
    dispatcher.add_handler(CommandHandler("start", start))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()