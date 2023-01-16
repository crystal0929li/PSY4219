#
# test2.py
#
# example PsychoPy program
#

from psychopy import visual, core, event

# test PsychoPy

# make a window
mywin = visual.Window(size=[800,600], screen=0, fullscr=False, allowGUI=True, monitor="testMonitor",
                      units='deg', color='gray')

# create some stimuli
grating = visual.GratingStim(win=mywin, mask='circle', size=3, pos=[-4,0], sf=3)
fixation = visual.GratingStim(win=mywin, size=0.5, pos=[0,0], sf=0, rgb=-1)

# draw the stimuli and update the window
while True:
    grating.setPhase(0.05, '+')
    grating.draw()
    fixation.draw()
    mywin.flip()

    if len(event.getKeys()) > 0:
        break
    event.clearEvents()

# cleanup
mywin.close()
core.quit()

#%%

