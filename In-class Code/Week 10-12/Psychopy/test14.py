#
# test14.py
#
# keyboard timing and control
#

from psychopy import visual, core, event, logging, info
import numpy.random as R


def main(mywin):

    myClock = core.Clock()
    maxwait = 1
    maxstim = .1

    fixation = visual.TextStim(win=mywin, text='+', height=.05, color='black')
    circle   = visual.Circle(win=mywin, radius=.2, pos=[0,0], edges=128, fillColor='red')

    while True:
        mywin.flip()

        event.clearEvents()               # clear event buffer at trial start

        fixation.draw()
        core.wait(0.5)                   # coarse timing here

        mywin.flip()                      # show fixation

        circle.draw()
        core.wait(R.uniform(.05, 2.0))    # coarse random timing here

        mywin.flip()                      # show circle
        myClock.reset()                   # start timer

        loop = True
        while loop:
            if myClock.getTime() > maxstim:
                mywin.flip()

            keys = event.getKeys(keyList=['space', 'q'], timeStamped=myClock)

            if len(keys):
                loop = False

            core.wait(0.0001)

        mywin.flip()

        print(keys)

        if keys[0][0] == 'q':
            break


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[600, 600], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='height', color='white')

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()