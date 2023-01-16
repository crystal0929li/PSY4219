#
# test3.py
#
# text message example
#

from psychopy import visual, core, event


def main(mywin):
    msg = visual.TextStim(win=mywin, text='hello', color='red', font='times', height=.1, pos=[-.2,+.2])
    msg.autoDraw = False
    msg.draw()
    mywin.flip()

    core.wait(1.0)

    mywin.flip()

    core.wait(1.0)

    msg.text = 'world'
    msg.color = 'black'
    msg.height = .2
    msg.pos = [+.2,-.3]
    msg.draw()
    mywin.flip()

    core.wait(1.0)


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[800, 400], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='height', color='gray')
        #
        # units = 'height' normalized window units where y ranges from -.5 to .5 and x range is determined
        #                  by aspect ratio (e.g. -.5 to .5 for a square screen).
        # units = 'norm'   fully normalized window units where both x and y values range from -1 to 1.
        #                  does not maintain aspect ratio
        # units = 'cm'     defines all positions and sizes in real world cm
        # units = 'deg'    defines all positions and sizes in real world degrees of visual angle
        #
        # cm & deg require monitor information (pixels, screen size, and viewing distance), which
        # can be set up in the monitor center
        #

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
