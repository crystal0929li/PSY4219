#
# test5.py#
#
# drawing example
#

from psychopy import visual, core, misc, event
import numpy as np


def main(mywin):
    circle = visual.Circle(
        win=mywin,
        units='pix',
        fillColor=[-1]*3,
        lineColor=[-1]*3,
        edges=128
    )

    # 'test' circles
    circle.radius = 12

    test_offset = 100

    for offset in [-1, +1]:
        circle.pos = [test_offset * offset, 0]
        circle.draw()

    # 'surround' circles
    surr_thetas = [0, 72, 144, 216, 288]
    surr_r = 50

    for i_surr in range(len(surr_thetas)):
        [surr_pos_x, surr_pos_y] = misc.pol2cart(
            surr_thetas[i_surr],
            surr_r
        )
        surr_pos_x = surr_pos_x + test_offset

        circle.pos = [surr_pos_x, surr_pos_y]
        circle.radius = 25
        circle.draw()

    mywin.flip()

    mywin.getMovieFrame()
    event.waitKeys()


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[500, 500], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='pix', color='white')

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()