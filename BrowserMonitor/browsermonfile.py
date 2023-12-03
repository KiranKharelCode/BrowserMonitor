import time
import pyautogui
screenWidth, screenHeight = pyautogui.size()
from browser_history.browsers import Brave
import os
import sqlite3
banned_words_list = [""]


Brave_Browser = Brave()

import datetime


file = open(r'C:\Users\{user}\PycharmProjects\BrowserMonitor\task.txt','a')
file.write(f'{datetime.datetime.now()} - script ran main script \n')
print("done")
def delete_his():
    conn = sqlite3.connect("c:/Users/yujgj/AppData/Local/BraveSoftware/Brave-Browser/User Data/Default/History")

    c = conn.cursor()

    # res = c.execute("SELECT title FROM 'urls'") //gets title from database ex: Reddit,Google,Twitter

    res = c.execute("SELECT * FROM 'urls'")
    res = list(res)
    index = []
    if len(res) != 0:
        for items in (res[-10:]):
            for stuff in banned_words_list:
                if stuff.upper() in items[1].upper():
                    index.append(items[0])

        if len(index) != 0:
            for items in index:
                res = c.execute(f"DELETE FROM urls WHERE id='{items}'")
                conn.commit()
    else:
        pass


while True:
    try:
        outputs = Brave_Browser.fetch_history()
        his = outputs.histories
        item = his[-1]

        item = (str(item))

        time.sleep(2)
        for words in banned_words_list:
            if words.upper() in item.upper():
                with pyautogui.hold('ctrl'):  # Press the Shift key down and hold it.
                    pyautogui.press(['shift','W'])
                delete_his()
                print("Done")
                break

        else:
            pass
    except:
        pass