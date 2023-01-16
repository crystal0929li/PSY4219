#
# test12.py
#
# keyboard examples
#

from psychopy import visual, core, event, logging, info


def main(mywin):

    event.clearEvents()

    keyspressed = []

    while True:
        #keys = event.waitKeys()
        keys = event.getKeys()

        if len(keys):
            print(keys)

            keyspressed.append(keys)

            if keys[0] == 'q':
                break
        else:
            print('NO KEY')

        core.wait(.01)

    print(keyspressed)


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