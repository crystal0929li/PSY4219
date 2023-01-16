#
# test16.py    test sounds
#

import psychtoolbox as ptb
from psychopy import core, sound

dur = 0.25

mySound1 = sound.Sound('A',   secs=dur, octave=4)
mySound2 = sound.Sound('Afl', secs=dur, octave=3)
mySound3 = sound.Sound('B',   secs=dur, octave=3)
mySound4 = sound.Sound('C',   secs=dur, octave=4)
mySound5 = sound.Sound('Csh', secs=dur, octave=5)

now = ptb.GetSecs(); mySound1.play(when=now)
core.wait(1)
now = ptb.GetSecs(); mySound2.play(when=now)
core.wait(1)
now = ptb.GetSecs(); mySound3.play(when=now)
core.wait(1)
now = ptb.GetSecs(); mySound4.play(when=now)
core.wait(1)
now = ptb.GetSecs(); mySound5.play(when=now)
core.wait(1)

mySound1 = sound.Sound('A',   secs=dur, octave=4)
mySound2 = sound.Sound('Csh', secs=dur, octave=4)
mySound3 = sound.Sound('E',   secs=dur, octave=4)
mySound4 = sound.Sound('Gsh', secs=dur, octave=4)
now = ptb.GetSecs();
mySound1.play(when=now)
mySound2.play(when=now)
mySound3.play(when=now)
mySound4.play(when=now)




