#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.3),
    on Mon Apr 25 19:30:40 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.3'
expName = 'stroopselfmade'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/sebastiansaueruser/github-repos/Pavlovia/stroop-selfmade/stroopselfmade_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "Willkommen_2"
Willkommen_2Clock = core.Clock()
Willkommen = visual.TextStim(win=win, name='Willkommen',
    text='Willkommen zu dieser Studie.\n\nHier sind die Instruktionen: ...\n\nWeiter mit jeder Taste.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
willkommen_weiter = keyboard.Keyboard()

# Initialize components for Routine "Main"
MainClock = core.Clock()
stimuli = visual.TextStim(win=win, name='stimuli',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
resp = keyboard.Keyboard()

# Initialize components for Routine "outro"
outroClock = core.Clock()
OutroText = visual.TextStim(win=win, name='OutroText',
    text='Danke! \n\nTschüss.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Willkommen_2"-------
continueRoutine = True
# update component parameters for each repeat
willkommen_weiter.keys = []
willkommen_weiter.rt = []
_willkommen_weiter_allKeys = []
# keep track of which components have finished
Willkommen_2Components = [Willkommen, willkommen_weiter]
for thisComponent in Willkommen_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
Willkommen_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "Willkommen_2"-------
while continueRoutine:
    # get current time
    t = Willkommen_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=Willkommen_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *Willkommen* updates
    if Willkommen.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        Willkommen.frameNStart = frameN  # exact frame index
        Willkommen.tStart = t  # local t and not account for scr refresh
        Willkommen.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(Willkommen, 'tStartRefresh')  # time at next scr refresh
        Willkommen.setAutoDraw(True)
    
    # *willkommen_weiter* updates
    waitOnFlip = False
    if willkommen_weiter.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        willkommen_weiter.frameNStart = frameN  # exact frame index
        willkommen_weiter.tStart = t  # local t and not account for scr refresh
        willkommen_weiter.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(willkommen_weiter, 'tStartRefresh')  # time at next scr refresh
        willkommen_weiter.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(willkommen_weiter.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(willkommen_weiter.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if willkommen_weiter.status == STARTED and not waitOnFlip:
        theseKeys = willkommen_weiter.getKeys(keyList=None, waitRelease=False)
        _willkommen_weiter_allKeys.extend(theseKeys)
        if len(_willkommen_weiter_allKeys):
            willkommen_weiter.keys = _willkommen_weiter_allKeys[-1].name  # just the last key pressed
            willkommen_weiter.rt = _willkommen_weiter_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Willkommen_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Willkommen_2"-------
for thisComponent in Willkommen_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('Willkommen.started', Willkommen.tStartRefresh)
thisExp.addData('Willkommen.stopped', Willkommen.tStopRefresh)
# check responses
if willkommen_weiter.keys in ['', [], None]:  # No response was made
    willkommen_weiter.keys = None
thisExp.addData('willkommen_weiter.keys',willkommen_weiter.keys)
if willkommen_weiter.keys != None:  # we had a response
    thisExp.addData('willkommen_weiter.rt', willkommen_weiter.rt)
thisExp.addData('willkommen_weiter.started', willkommen_weiter.tStartRefresh)
thisExp.addData('willkommen_weiter.stopped', willkommen_weiter.tStopRefresh)
thisExp.nextEntry()
# the Routine "Willkommen_2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
loop1 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Stimuli.xlsx'),
    seed=None, name='loop1')
thisExp.addLoop(loop1)  # add the loop to the experiment
thisLoop1 = loop1.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
if thisLoop1 != None:
    for paramName in thisLoop1:
        exec('{} = thisLoop1[paramName]'.format(paramName))

for thisLoop1 in loop1:
    currentLoop = loop1
    # abbreviate parameter names if possible (e.g. rgb = thisLoop1.rgb)
    if thisLoop1 != None:
        for paramName in thisLoop1:
            exec('{} = thisLoop1[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Main"-------
    continueRoutine = True
    # update component parameters for each repeat
    stimuli.setColor(letterColor, colorSpace='rgb')
    stimuli.setText(word)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    # keep track of which components have finished
    MainComponents = [stimuli, resp]
    for thisComponent in MainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    MainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "Main"-------
    while continueRoutine:
        # get current time
        t = MainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=MainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stimuli* updates
        if stimuli.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stimuli.frameNStart = frameN  # exact frame index
            stimuli.tStart = t  # local t and not account for scr refresh
            stimuli.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stimuli, 'tStartRefresh')  # time at next scr refresh
            stimuli.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left','right','down'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in MainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Main"-------
    for thisComponent in MainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    loop1.addData('stimuli.started', stimuli.tStartRefresh)
    loop1.addData('stimuli.stopped', stimuli.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for loop1 (TrialHandler)
    loop1.addData('resp.keys',resp.keys)
    loop1.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        loop1.addData('resp.rt', resp.rt)
    loop1.addData('resp.started', resp.tStartRefresh)
    loop1.addData('resp.stopped', resp.tStopRefresh)
    # the Routine "Main" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'loop1'


# ------Prepare to start Routine "outro"-------
continueRoutine = True
routineTimer.add(3.500000)
# update component parameters for each repeat
# keep track of which components have finished
outroComponents = [OutroText]
for thisComponent in outroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
outroClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "outro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = outroClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=outroClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *OutroText* updates
    if OutroText.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        OutroText.frameNStart = frameN  # exact frame index
        OutroText.tStart = t  # local t and not account for scr refresh
        OutroText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(OutroText, 'tStartRefresh')  # time at next scr refresh
        OutroText.setAutoDraw(True)
    if OutroText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > OutroText.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            OutroText.tStop = t  # not accounting for scr refresh
            OutroText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(OutroText, 'tStopRefresh')  # time at next scr refresh
            OutroText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in outroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "outro"-------
for thisComponent in outroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('OutroText.started', OutroText.tStartRefresh)
thisExp.addData('OutroText.stopped', OutroText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
