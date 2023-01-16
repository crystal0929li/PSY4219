#
# test6.py
#
# controlling mouse
#

from psychopy import visual, core, event
import numpy as np


def main(mywin):

    mouse = event.Mouse(win=mywin, visible=True)

    mouse.setPos([0,0])
    mouse.clickReset(buttons=(0, 1, 2))

    cpos = [0, 0]
    center = visual.Circle(win=mywin, radius=.025, pos=cpos, edges=128, fillColor='green')
    center.draw()
    mywin.flip()

    prevpos = mouse.getPos()
    mouse.setVisible(True)

    while not event.getKeys():
        currpos = mouse.getPos()

        if not(np.array_equal(currpos, prevpos)):
            print(currpos)
            prevpos = currpos

        but = mouse.getPressed()
        if but[0]:
            print('mouse clicked')
            mouse.setVisible(False)
        else:
            mouse.setVisible(True)

        if mouse.isPressedIn(shape=center):
            print('mouse clicked in center')


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[400, 400], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='height', color='white')

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
