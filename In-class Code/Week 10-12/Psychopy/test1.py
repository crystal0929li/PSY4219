#
# test1.py
#
# open a window
#

from psychopy import visual, core, event

mywin = visual.Window(size=[800,600], screen=0, fullscr=False, allowGUI=True, monitor='testMonitor', color='gray')
core.wait(1.0)

mywin.close()
core.quit()
