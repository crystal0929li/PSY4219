#
# test9.py
#
# ABSOLUTE clock timing
#

from psychopy import visual, core, event, logging
import numpy as np


def main(mywin):
    # reading in images
    r = 600; c = 800; ar = r/c
    fnames = ['images/IMG_3221.jpg', 'images/IMG_3258.jpg', 'images/IMG_3374.jpg']
    mypic = [[]]*len(fnames)
    mypic[0] = visual.ImageStim(win=mywin, image=fnames[0], size=[.5, .5*ar], contrast=1.0, ori=0)
    mypic[1] = visual.ImageStim(win=mywin, image=fnames[1], size=[.5, .5*ar], contrast=1.0, ori=0)
    mypic[2] = visual.ImageStim(win=mywin, image=fnames[2], size=[.5, .5*ar], contrast=1.0, ori=0)

    # create fixation point at center of screen
    fixation = visual.TextStim(win=mywin, text='+', height=.05, color='black')

    # duration parameters
    fixDur   = .5
    stimDur  = .5
    blankDur = 1.0
    trialDur = fixDur+stimDur+blankDur

    Nrep = 1

    # initial delay to start (blank screen)
    expDelay = 0.5

    # create clocks
    expClock   = core.Clock()   # full experiment clock

    logging.console.setLevel(logging.WARNING)
    logging.setDefaultClock(expClock)
    lastLog = logging.LogFile('test9.log', level=logging.INFO, filemode='w')

    # initial (blank) flip to sync up timing better
    mywin.flip()
    expClock.reset()

    for i in range(len(fnames)*Nrep):
        # draw fixation
        fixation.draw()

        # wait until start of trial
        while expClock.getTime() < expDelay + i*trialDur:
            core.wait(.0001)

        mywin.logOnFlip(level=logging.EXP, msg=f'fix on {i}')
        mywin.flip()

        # get read to draw image to screen after fixation
        mypic[i % len(fnames)].draw()

        # wait for fixation duration
        while expClock.getTime() < expDelay + i*trialDur + fixDur:
            core.wait(.0001)

        # display image
        mywin.logOnFlip(level=logging.EXP, msg=f'fix off / stimulus on {i}')
        mywin.flip()

        while expClock.getTime() < expDelay + i*trialDur + fixDur + stimDur:
            # later we will add looking for responses
            core.wait(.0001)

        # image off
        mywin.logOnFlip(level=logging.EXP, msg=f'stimulus off {i}')
        mywin.flip()


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
