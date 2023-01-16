#
# test5.py
#
# drawing example
#

from psychopy import visual, core, event
import numpy as np


def main(mywin):

    # https://www.psychopy.org/api/visual/line.html#psychopy.visual.Line
    el1 = visual.Line(win=mywin, start=[+.3,-.2], end=[-.4,-.3], lineWidth=20, lineColor='blue')
    el1.autoDraw = True
    print('el1 : ', dir(el1))
    #el1.draw()
    mywin.flip(); core.wait(0.5)

    # https://www.psychopy.org/api/visual/circle.html#psychopy.visual.Circle
    el2 = visual.Circle(win=mywin, radius=.1, pos=[-.2,+.1], edges=128, fillColor='green')
    el2.autoDraw = True
    print('el2 : ', dir(el2))
    #el2.draw()
    mywin.flip(); core.wait(0.5)

    # https://www.psychopy.org/api/visual/rect.html#psychopy.visual.Rect
    el3 = visual.Rect(win=mywin, size=[.2,.1], pos=[+.3,+.2], lineWidth=10, lineColor='#F016A3')
    print('el3 : ', dir(el3))
    el3.autoDraw = True
    #el3.draw()
    mywin.flip(); core.wait(0.5)

    # https://www.psychopy.org/api/visual/shapestim.html#psychopy.visual.ShapeStim
    vert = np.array([[-.1,+.2], [+.1,+.1], [+.2,-.1], [-.1,-.3], [-.1,+.2]])
    el4 = visual.ShapeStim(win=mywin, vertices=vert, fillColor=[+.3,-.7,+.8], lineWidth=20, lineColor=[-.6,+.4,+.6])
    print('el4 : ', dir(el4))
    el4.autoDraw = True
    #el4.draw()
    mywin.flip(); core.wait(0.5)

    event.waitKeys()

    mywin.flip(); core.wait(0.5)


if __name__ == '__main__':
    try:
        event.globalKeys.add(key='q', func=core.quit)

        mywin = visual.Window(size=[800, 800], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                              units='height', color='white')

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
