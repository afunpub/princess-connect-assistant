#! python3
"""princess connect assistant
afunpub@gmail.com
I learn to develop the princess connect assistant with python language.It's unfinished
"""
import keyboard, pyautogui, time, logging, os

width, height = pyautogui.size()


class Get():
    wait = False

    def doThis(self, e):
        self.wait = not self.wait


def imPath(filename):
    """A shortcut for joining the 'images/'' file path, since it is used so often. Returns the filename with 'images/' prepended."""
    return os.path.join('images', filename)


def getGameRegion():
    """Obtains the region that the Sushi Go Round game is on the screen and assigns it to GAME_REGION. The game must be at the start screen (where the PLAY button is visible)."""
    global GAME_REGION

    # identify the top-left corner
    logging.info('Finding game region...')
    region = pyautogui.locateOnScreen(imPath('top_right_corner.png'))
    if region is None:
        raise Exception('Could not find game on screen. Is the game visible?')

    # calculate the region of the entire game
    topRightX = region[0] + region[2]  # left + width
    topRightY = region[1]  # top
    GAME_REGION = (topRightX - 1280, topRightY, 1280, 720)  # the game screen is always 1280 x 720
    logging.info('Game region found: %s' % (GAME_REGION,))


def challenge():
    global battleStep
    pos = pyautogui.locateCenterOnScreen(imPath('challenge.png'), region=GAME_REGION)
    if pos:
        pyautogui.click(pos)
        battleStep = 2
        print('battleStep :' + str(battleStep))
    else:
        pos = pyautogui.locateCenterOnScreen(imPath('challenge02.png'), region=GAME_REGION)
    if pos:
        pyautogui.click(pos)
        battleStep = 2
        print('battleStep :' + str(battleStep))


def start():
    global battleStep
    pos = pyautogui.locateCenterOnScreen(imPath('start.png'), region=GAME_REGION)
    if pos:
        pyautogui.click(pos)
        battleStep = 3
        print('battleStep :' + str(battleStep))


def nextStep():
    global battleStep
    pos = pyautogui.locateCenterOnScreen(imPath('nextStep.png'), region=GAME_REGION)
    if pos and battleStep == 3:
        pyautogui.click(pos)
        battleStep = 4
        pos = False
        print('battleStep :' + str(battleStep))
    elif pos and battleStep == 4:
        pyautogui.click(pos)
        battleStep = 1
        print('battleStep :' + str(battleStep))


def ok():
    while True:
        pos = pyautogui.locateCenterOnScreen('ok.png')
        if pos:
            pyautogui.click(pos)
            break


def main():
    if __name__ == '__main__':
        if battleStep == 1:
            challenge()
        elif battleStep == 2:
            start()
        elif battleStep == 3:
            nextStep()
        elif battleStep == 4:
            nextStep()

    # talkNextStep()


a = Get()
keyboard.on_press_key("f12", a.doThis)
##keyboard.add_hotkey('f3',a.doThis)
# keyboard.add_hotkey('f11',buff)
# keyboard.add_hotkey('5',skill3)
last_time = time.time()
GAME_REGION = ()
getGameRegion()
battleStep = 1

while True:
    if a.wait:
        print('Loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        main()
