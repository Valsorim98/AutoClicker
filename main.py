import pyautogui
import time

def clicker():

    # TOP LEVEL-----------------------------------

    # for i in range(500):

    #     # top level click
    #     pyautogui.click(900, 270)
    #     time.sleep(0.005)
    #     i += 1

    #     if i == 500:
    #         #top level upgrade
    #         pyautogui.click(930, 390)
    #         time.sleep(0.1)


    # MIDDLE LEVEL-----------------------------------

    for i in range(500):

        # middle level click
        pyautogui.click(620, 535)
        time.sleep(0.005)
        i += 1

        if i == 1:
            #middle level upgrade
            pyautogui.click(930, 600)
            time.sleep(0.1)


    # BOTTOM-RIGHT LEVEL-----------------------------------

    # for i in range(300):

    #     # bottom-right level click
    #     pyautogui.click(1175, 730)
    #     time.sleep(0.005)
    #     i += 1

        # if i == 300:
        #     # bottom-right level upgrade
        #     pyautogui.click(1260, 805)
        #     time.sleep(0.1)

def main():

    flag = True
    while flag != False:
        clicker()

main()
