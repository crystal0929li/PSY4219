#
# test4.py
#
# image display example
#

from psychopy import visual, core, event
from PIL import Image
import os
import re


def main(mywin):
    dr = './images'
    pattern = r'.*.((jpg)|(JPG))'

    r = 600; c = 800; ar = r / c
    with os.scandir(dr) as entries:
        for entry in entries:
            if re.search(pattern, dr + '/' + entry.name):
                fullpath = dr + '/' + entry.name
                mypic = visual.ImageStim(win=mywin, image=fullpath, size=[.6, .6*ar], contrast=.50, ori=180)
                # https://www.psychopy.org/api/visual/imagestim.html

                mypic.draw()

                mywin.flip()

                core.wait(0.5)


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[500, 500], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='height', color='gray')

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
