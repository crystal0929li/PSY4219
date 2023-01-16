from psychopy import visual, gui, core, event, logging
import os
import re
import random
import pandas as pd


# check floating numbers
def is_float(n):
    """This function checks if an entered string is a floating number"""
    try:
        float(n)
        return True
    except ValueError:
        return False


def param():
    """This function returns the gui parameters set by the experimenter"""
    # create gui interface
    subgui = gui.Dlg()
    subgui.addField('Subject Number:')
    subgui.addField('Length of the Study List:')
    subgui.addField('Image Presentation Time (s):')

    # show the gui until valid subject and session number
    while True:
        subgui.show()
        if (subgui.data[0].isdigit() and subgui.data[1].isdigit()
                and is_float(subgui.data[2]) and 5 <= int(subgui.data[1]) <= 50):
            subj = int(subgui.data[0])
            lens = int(subgui.data[1])
            stim = float(subgui.data[2])
            break
    return subj, lens, stim


def load_image(dr, subj, lens):
    """This function loads in image paths from the given directory and returns a randomly chosen list that
       will be used in the test phase."""
    pattern = r'.*.((jpg)|(JPG))'
    fnames = []
    with os.scandir(dr) as entries:
        for entry in entries:
            if re.search(pattern, dr + '/' + entry.name):
                fullpath = dr + '/' + entry.name
                fnames.append(fullpath)
    random.seed(subj)
    test_list = random.sample(fnames, lens * 2)
    study_list = random.sample(test_list, lens)
    return study_list, test_list


def study_phase(study_list, subj, stim, bint, rf, block, mywin):
    """This function performs the study phase of the experiment and returns lists of relevant data."""

    r = 600; c = 800; ar = r / c
    slack = rf / 2  # slack time
    trial = 0
    # create a blank dataframe
    dataVars = ['subj', 'block', 'trial', 'image', 'ptime']
    datadf = pd.DataFrame(columns=dataVars)

    # reading in image
    study_img = [[]] * len(study_list)
    for i in range(len(study_list)):
        study_img[i] = visual.ImageStim(win=mywin, image=study_list[i], size=[.5, .5 * ar], contrast=1.0, ori=0)

    # duration parameters
    stimDur = stim
    blankDur = bint
    trialDur = stimDur + blankDur

    # printing a message to participants
    msg = visual.TextStim(win=mywin,
                          text='You will be presented with images, please try to remember them as many as you can',
                          color='black', font='times', height=.1, pos=[0.0, 0.0])
    msg.autoDraw = False
    msg.draw()
    mywin.flip(); core.wait(3.0)

    # create clocks
    expClock = core.Clock()  # full experiment clock

    # set logger
    logging.console.setLevel(logging.WARNING)
    logging.setDefaultClock(expClock)
    lastLog = logging.LogFile('Homework10_Li.log', level=logging.INFO, filemode='w')

    # initial delay to start (blank screen)
    expDelay = 0.5

    # initial (blank) flip to sync up timing better
    mywin.flip()
    expClock.reset()

    for i in range(len(study_list)):
        # add entries to dataframe
        datadf.loc[trial, 'subj'] = subj
        datadf.loc[trial, 'block'] = block
        datadf.loc[trial, 'trial'] = trial
        datadf.loc[trial, 'image'] = study_list[i]
        datadf.loc[trial, 'ptime'] = stim
        trial += 1

        # wait until start of trial
        while expClock.getTime() < expDelay + i*trialDur - slack:
            core.wait(.0001)

        # blank phase
        mywin.logOnFlip(level=logging.EXP, msg=f'blank on {i}')
        mywin.flip()

        # get read to draw image to screen
        study_img[i].draw()

        # wait for blank
        while expClock.getTime() < expDelay + i*trialDur + blankDur - slack:
            core.wait(.0001)

        # display image
        mywin.logOnFlip(level=logging.EXP, msg=f'stimulus on {i}')
        mywin.flip()
        while expClock.getTime() < expDelay + i*trialDur + blankDur + stimDur - slack:
            core.wait(.0001)

        # image off
        mywin.logOnFlip(level=logging.EXP, msg=f'stimulus off {i}')
        mywin.flip()
    datadf.to_csv('study_data.csv', index=False)
    return datadf


def test_phase(study_list, test_list, subj, block, mywin):
    """This function performs the test phase of the experiment and return the recorded data as a dataframe"""

    # create a blank dataframe
    dataVars = ['subj', 'block', 'trial', 'image', 'choice', 'RT', 'ans', 'badkeys', 'badRT', 'nbadkeys']
    datadf = pd.DataFrame(columns=dataVars)

    # reading in image
    test_img = [[]] * len(test_list)
    r = 600; c = 800; ar = r / c
    for i in range(len(test_list)):
        test_img[i] = visual.ImageStim(win=mywin, image=test_list[i], size=[.5, .5 * ar], contrast=1.0, ori=0)

    # printing messages to participants and experimenters
    msg = visual.TextStim(win=mywin,
                          text='You will be presented with images, please indicate '
                               'whether they are old (press "d") or new (press "k")',
                          color='black', font='times', height=.1, pos=[0.0, 0.0])
    msg.autoDraw = False
    msg.draw()
    mywin.flip();
    core.wait(8.0)

    msg1 = visual.TextStim(win=mywin,
                           text='old (press "d")',
                           color='black', font='times', height=.1, pos=[-0.4, -0.3])
    msg2 = visual.TextStim(win=mywin,
                           text='new (press "k")',
                           color='black', font='times', height=.1, pos=[+0.4, -0.3])
    msg1.autoDraw = True
    msg2.autoDraw = True
    mywin.flip(); core.wait(1.0)

    # create clocks
    expClock = core.Clock()  # full experiment clock

    # set logger
    logging.console.setLevel(logging.WARNING)
    logging.setDefaultClock(expClock)
    lastLog = logging.LogFile('Homework10_Li.log', level=logging.INFO, filemode='w')

    # display the stimulus
    mywin.flip()
    expClock.reset()

    # start testing phase
    trial = 0
    for i in range(len(test_list)):
        # add entries to dataframe
        datadf.loc[trial, 'subj'] = subj
        datadf.loc[trial, 'block'] = block
        datadf.loc[trial, 'trial'] = trial
        datadf.loc[trial, 'image'] = test_list[i]
        if test_list[i] in study_list:
            datadf.loc[trial, 'ans'] = 'old'
        else:
            datadf.loc[trial, 'ans'] = 'new'

        # get read to draw image to screen
        test_img[i].draw()

        # display image
        mywin.logOnFlip(level=logging.EXP, msg=f'stimulus on {i}')
        mywin.flip()
        expClock.reset()

        # check for key press and record response time
        loop = True
        badkey = False
        nbadkeys = 0
        badkeys = []
        badrt = []

        while loop:
            keys = event.getKeys(timeStamped=expClock)

            if keys:
                if keys[0][0] in ['d', 'k', 'q']:
                    loop = False
                    choice = keys[0][0]
                    rt = keys[0][1]
                    # add entries to dataframe
                    datadf.loc[trial, 'choice'] = choice
                    datadf.loc[trial, 'RT'] = rt
                else:
                    badkey = True
                    badkeys.append(keys[0][0])
                    badrt.append(keys[0][1])
                    nbadkeys += 1

            core.wait(0.0001)

        mywin.logOnFlip(level=logging.EXP, msg=f'stimulus off {i}')
        mywin.flip()

        if badkey:
            print('bad key')
            # add entries to dataframe
            datadf.loc[trial, 'badkeys'] = badkeys
            datadf.loc[trial, 'badRT'] = badrt
            datadf.loc[trial, 'nbadkeys'] = nbadkeys
        else:
            print()

        if keys[0][0] == 'q':
            break
        trial += 1
    datadf.to_csv('test_data.csv', index=False)
    return datadf


def main(mywin):
    # set mouse to invisible
    mouse = event.Mouse(win=mywin, visible=False)
    # call functions to perform the experiment and collect data
    s_list, t_list = load_image(dr, subj, lens)
    study_phase(s_list, subj, stim, bint, rf, block, mywin)
    test_phase(s_list, t_list, subj, block, mywin)
    mouse.setVisible(True)


if __name__ == '__main__':
    try:
        dr = './OBJECTSALL'
        bint = 0.5
        rf = 1 / 60  # refresh time in sec for 60Hz
        block = 0
        subj, lens, stim = param()
        mywin = visual.Window(size=[1440, 800], screen=0, fullscr=True, allowGUI=True, monitor="testMonitor",
                              units='height', color='white')
        main(mywin)

        mywin.close()
        core.quit()

    except Exception as ex:
        mywin.close()
        print(ex)
        core.quit()
