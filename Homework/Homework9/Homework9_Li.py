from psychopy import visual, core, event


def main(mywin):
    # Print a text message
    msg = visual.TextStim(win=mywin, text='A Sunny Moment', color='orange',
                          font='times', height=.1, pos=[0.0,+.2])
    msg.autoDraw = False
    msg.draw()
    mywin.flip(); core.wait(1.0)

    # draw the ground
    ground = visual.Rect(win=mywin, size=[1.5,.4], pos=[0.0, -0.5],
                         lineWidth=10, fillColor='green')
    ground.autoDraw = True
    mywin.flip(); core.wait(0.5)

    # draw a cloud
    cloud1 = visual.Rect(win=mywin, size=[.15, .1], pos=[0.3, 0.35],
                         lineWidth=10, fillColor='white')
    cloud1.autoDraw = True
    cloud2 = visual.Circle(win=mywin, radius=.05, pos=[0.225, 0.35],
                           lineWidth=10, fillColor='white')
    cloud2.autoDraw = True
    cloud3 = visual.Circle(win=mywin, radius=.05, pos=[0.375, 0.35],
                           lineWidth=10, fillColor='white')
    cloud3.autoDraw = True
    cloud4 = visual.Circle(win=mywin, radius=.05, pos=[0.29, 0.4],
                           lineWidth=10, fillColor='white')
    cloud4.autoDraw = True
    mywin.flip(); core.wait(0.5)

    # draw a sun
    sun = visual.Circle(win=mywin, radius=.1, pos=[-.35, +.35], edges=128,
                        lineColor='black', fillColor='orange')
    sun.autoDraw = True
    mywin.flip(); core.wait(0.5)

    # draw a rainbow
    rb_red = visual.Pie(win=mywin, radius=.5, start=-90, end=90, fillColor='red', pos=[.0, -.3])
    rb_red.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_or = visual.Pie(win=mywin, radius=.45, start=-90, end=90, fillColor='orange', pos=[.0, -.3])
    rb_or.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_ye = visual.Pie(win=mywin, radius=.4, start=-90, end=90, fillColor='yellow', pos=[.0, -.3])
    rb_ye.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_gr = visual.Pie(win=mywin, radius=.35, start=-90, end=90, fillColor='green', pos=[.0, -.3])
    rb_gr.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_bl = visual.Pie(win=mywin, radius=.3, start=-90, end=90, fillColor='blue', pos=[.0, -.3])
    rb_bl.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_in = visual.Pie(win=mywin, radius=.25, start=-90, end=90, fillColor='indigo', pos=[.0, -.3])
    rb_in.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_vio = visual.Pie(win=mywin, radius=.2, start=-90, end=90, fillColor='violet', pos=[.0, -.3])
    rb_vio.autoDraw = True
    mywin.flip(); core.wait(0.5)

    rb_vio = visual.Pie(win=mywin, radius=.15, start=-90, end=90, fillColor='cyan', pos=[.0, -.3])
    rb_vio.autoDraw = True
    mywin.flip(); core.wait(0.5)

    # erase and clean
    mywin.flip(); core.wait(3.0)


if __name__ == '__main__':
    try:
        mywin = visual.Window(size=[800, 600], screen=0, fullscr=False, allowGUI=True, monitor='testMonitor',
                              units='height', color='cyan')

        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
