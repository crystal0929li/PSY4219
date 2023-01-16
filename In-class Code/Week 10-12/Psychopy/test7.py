#
# test7.py
#
# gui
#

from psychopy import gui, core, event

# create gui interface
subgui = gui.Dlg()
subgui.addField('Subject Number:')
subgui.addField('Session Number:')
subgui.addField('Condition:', choices=['Experimental', 'Control'])
subgui.addField('Check Box:', initial=False)

# show the gui until valid subject and session number
while True:
    subgui.show()
    if (subgui.data[0].isdigit() and subgui.data[1].isdigit()):
        subj = int(subgui.data[0])
        sess = int(subgui.data[1])
        cond = subgui.data[2]
        chck = subgui.data[3]
        break

# extract data from gui
print('Subject Number : ', subj)
print('Session Number : ', sess)
print('Condition      : ', cond)
print('Check Box      : ', chck)

core.quit()
