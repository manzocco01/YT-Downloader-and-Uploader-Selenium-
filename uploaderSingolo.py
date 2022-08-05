from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
import os, glob
import pyautogui

opt = webdriver.ChromeOptions()
opt.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
chromedriver_exe_location = os.path.join(os.getcwd(), 'F:\Lavoro\Python\seleniumDriver\chromedriver.exe')
profile_path = r'C:\Users\liamm\AppData\Local\Google\Chrome\User Data'  # path minus last folder
opt.add_argument('--user-data-dir={}'.format(profile_path))
opt.add_argument('--profile-directory={}'.format('Profile 3'))  # last folder name
driver = webdriver.Chrome(chromedriver_exe_location, options=opt, service_args='')

driver.get('https://studio.youtube.com/channel/UC2XrPuH8Iv-NDNlMkrTQlhg/videos/upload?d=ud&filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D')

time.sleep(3)

os.chdir(r"F:\\Lavoro\\Python\\MemeYT\\")
for file in glob.glob("*.mp4"):
     nome = file

driver.find_element(By.NAME,'Filedata').send_keys(r"F:\\Lavoro\\Python\\MemeYT\\" + str(nome))

time.sleep(3)

descrizione = driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-social-suggestions-textbox/ytcp-form-input-container/div[1]/div[2]/div/ytcp-social-suggestion-input/div")
descrizione.send_keys("#meme #funny #goofy #ahh #goofy #laugh #funnymeme #short #shorts")

driver.find_element(By.NAME, "VIDEO_MADE_FOR_KIDS_NOT_MFK").click()

time.sleep(3)

driver.find_element(By.ID, "toggle-button").click()

time.sleep(3)

driver.find_element(By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[4]/ytcp-form-input-container/div[1]/div/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input").send_keys("meme, funny, goofy, ahh, goofy, laugh, funnymeme, short, shorts")

time.sleep(3)

#driver.find_element(By.XPATH,"/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-ve/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[7]/div[3]/ytcp-form-select/ytcp-select/ytcp-text-dropdown-trigger/ytcp-dropdown-trigger").click()

#time.sleep(3)

#driver.find_element(By.XPATH, "/html/body/ytcp-text-menu/tp-yt-paper-dialog/tp-yt-paper-listbox/tp-yt-paper-item[14]").click()downloaderIG.p

#time.sleep(3)

driver.find_element(By.ID, "allow-all-radio-button").click()

time.sleep(3)

driver.find_element(By.ID, "next-button").click()

time.sleep(3)

driver.find_element(By.ID, "next-button").click()

time.sleep(3)

driver.find_element(By.ID, "next-button").click()

time.sleep(3)

driver.find_element(By.NAME, "PUBLIC").click()

time.sleep(3)

driver.find_element(By.ID, "done-button").click()

time.sleep(3)

driver.get("https://www.tiktok.com/upload?lang=it-IT")  #cambiare

time.sleep(3)

time.sleep(3)

pyautogui.click(598, 541)
time.sleep(1)
pyautogui.click(216, 475)
time.sleep(1)
pyautogui.write(r'F:\Lavoro\Python\MemeYT')
pyautogui.press('enter')
time.sleep(1)
pyautogui.click(332, 165)
time.sleep(1)
pyautogui.click(790, 505)
time.sleep(3)
pyautogui.click(1425, 355)
time.sleep(1)
pyautogui.write('goofy')
time.sleep(1)
pyautogui.press('enter')
pyautogui.click(1425, 355)
time.sleep(1)
pyautogui.write('funny')

time.sleep(1)
pyautogui.press('enter')
pyautogui.click(1425, 355)
time.sleep(1)
pyautogui.write('meme')

time.sleep(1)
pyautogui.press('enter')
pyautogui.click(1425, 355)
time.sleep(1)
pyautogui.write('ahh')

time.sleep(1)
pyautogui.press('laugh')
pyautogui.click(1425, 355)
time.sleep(1)
pyautogui.write('funnymeme')

time.sleep(1)
pyautogui.press('shorts')
time.sleep(20)
pyautogui.click(1022, 903)

time.sleep(10)

driver.close()

os.remove(r"F:\\Lavoro\\Python\\MemeYT\\" + str(nome))
