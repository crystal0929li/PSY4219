#
# test5.py#
#
# drawing example
#

from psychopy import visual, core, event
import numpy as np
import random as R


def main(mywin):

    rect = visual.Rect(win=mywin)

    n_rect = 500

    for _ in range(n_rect):
        # calling methods rather than setting attributes
        rect.setWidth(R.uniform(.05, .25))
        rect.setHeight(R.uniform(.05, .25))

        rect_color = [R.uniform(-1, 1)]*3
        rect.setFillColor(rect_color, 'rgb')
        rect.setLineColor(rect_color, 'rgb')

        rect.setPos([R.uniform(-.5, +.5), R.uniform(-.5, +.5)])

        rect.draw()

    mywin.flip()

    event.waitKeys()


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[400, 400], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='height', color=[1, 1, 1])

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
