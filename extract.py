import wikipedia, time, pyautogui
infoTopic = input("Enter your topic(please be specific):")

print (wikipedia.summary(infoTopic))

tryit = input("Do you want to perform a manual search? (y/n)")
a = 'y'
b = 'n'
if tryit == a:
    print("Program Initiated")
    time.sleep(2)
    pyautogui.click(1149, 1051)
    time.sleep(2)
    pyautogui.hotkey('ctrl', 't')
    time.sleep(3)
    pyautogui.write(infoTopic)
    pyautogui.keyDown("enter")
else:
    print("Thanks for your query!!")