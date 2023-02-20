# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 19:42:01 2022

@author: Mark Cassidy

OBS Web Scoket Commands:
'PressInputPropertiesButton', 'GetHotkeyList', 'OpenInputInteractDialog', 
'SaveSourceScreenshot', 'GetVersion', 'SetInputName', 'SetSceneName', 
'GetStats', 'TriggerStudioModeTransition', 'SetInputAudioSyncOffset', 
'GetSceneCollectionList', 'BroadcastCustomEvent', 'Sleep', 
'SetSceneSceneTransitionOverride', 'CallVendorRequest', 
'CreateSceneCollection', 'SetStudioModeEnabled', 'TriggerHotkeyByName', 
'OpenVideoMixProjector', 'TriggerHotkeyByKeySequence', 'GetPersistentData', 
'SetSceneItemIndex', 'SetPersistentData', 'SetCurrentSceneCollection', 
'SetInputMute', 'SetCurrentPreviewScene', 'SetCurrentProgramScene', 
'OpenSourceProjector', 'GetProfileList', 'SetCurrentProfile', 'RemoveProfile', 
'CreateProfile', 'GetProfileParameter', 'SetProfileParameter', 
'GetInputPropertiesListPropertyItems', 'GetInputAudioBalance', 
'GetStreamServiceSettings', 'GetVideoSettings', 'SetVideoSettings', 
'SetInputAudioBalance', 'SetInputVolume', 'SetStreamServiceSettings', 
'GetInputDefaultSettings', 'GetSpecialInputs', 'GetInputKindList', 
'GetRecordDirectory', 'GetInputMute', 'GetCurrentPreviewScene', 
'GetReplayBufferStatus', 'GetSourceActive', 'GetSourceScreenshot', 
'GetSourcePrivateSettings', 'SetSourcePrivateSettings', 
'SetSourceFilterEnabled', 'GetInputList', 'GetSceneList', 'GetGroupList', 
'SetInputSettings', 'GetCurrentProgramScene', 'GetSceneItemId', 'RemoveScene', 
'CreateScene', 'GetSceneSceneTransitionOverride', 'RemoveInput', 'CreateInput', 
'GetSceneItemLocked', 'GetInputSettings', 'ToggleInputMute', 
'SetCurrentSceneTransition', 'GetInputVolume', 'GetInputAudioSyncOffset', 
'GetInputAudioMonitorType', 'SetInputAudioMonitorType', 'StartVirtualCam', 
'GetInputAudioTracks', 'SetInputAudioTracks', 'GetTransitionKindList', 
'GetSceneItemTransform', 'GetSceneTransitionList', 'GetVirtualCamStatus', 
'GetCurrentSceneTransition', 'SetCurrentSceneTransitionDuration', 
'SetCurrentSceneTransitionSettings', 'GetCurrentSceneTransitionCursor', 
'SetTBarPosition', 'StopOutput', 'ToggleOutput', 'GetSourceFilterList', 
'GetSourceFilterDefaultSettings', 'CreateSourceFilter', 'RemoveSourceFilter', 
'SetSourceFilterName', 'GetSourceFilter', 'StopRecord', 'ToggleRecord', 
'SetSourceFilterIndex', 'SetSourceFilterSettings', 'SetSceneItemTransform', 
'GetSceneItemList', 'GetGroupSceneItemList', 'CreateSceneItem', 
'RemoveSceneItem', 'DuplicateSceneItem', 'GetSceneItemEnabled', 
'SetSceneItemEnabled', 'SetSceneItemLocked', 'GetSceneItemIndex', 
'StartReplayBuffer', 'GetSceneItemBlendMode', 'SetSceneItemBlendMode', 
'GetSceneItemPrivateSettings', 'SetSceneItemPrivateSettings', 'StopVirtualCam', 
'ToggleVirtualCam', 'StopReplayBuffer', 'ToggleReplayBuffer', 
'SaveReplayBuffer', 'GetLastReplayBufferReplay', 'GetOutputList', 
'GetOutputStatus', 'StartOutput', 'GetOutputSettings', 'SetOutputSettings', 
'GetStreamStatus', 'StopStream', 'ToggleStream', 'StartStream', 
'SendStreamCaption', 'GetRecordStatus', 'StartRecord', 'ToggleRecordPause', 
'PauseRecord', 'ResumeRecord', 'SetMediaInputCursor', 'GetMediaInputStatus', 
'OffsetMediaInputCursor', 'TriggerMediaInputAction', 'GetStudioModeEnabled', 
'OpenInputPropertiesDialog', 'OpenInputFiltersDialog', 'GetMonitorList'
"""

import asyncio
import simpleobsws
#import keyboard
import tkinter as tk
from functools import partial

client=simpleobsws.WebSocketClient("ws://localhost:4455",password="wNyFZf1UUPKVrPX0")

async def change_scene(setscenename):
    await client.connect()
    await client.wait_until_identified()

    ret_sc = await client.call(simpleobsws.Request("SetCurrentProgramScene",{"sceneName":str(setscenename)}))
    
    print(format(ret_sc))
    
    await client.disconnect()
    
async def toggle_mute(togglemuteaudio):
    await client.connect()
    await client.wait_until_identified()

    ret_au = await client.call(simpleobsws.Request('ToggleInputMute',{"inputName":str(togglemuteaudio)}))
    
    print(format(ret_au))
    
    await client.disconnect()
    window.after(0,toggle_mute)

#asyncio.create_task(change_scene("iPad_Webcam"))
#asyncio.create_task(toggle_mute("Scarlett_Audio"))

def button_lookup(bttn,lst):
    return str(button_dict["Button"+str(bttn)][lst])

#Define GUI buttons
button_dict={
    "Button1":["OBS Webcam Only","client.call('SetCurrentScene',\"Webcam_Only\")"],
    "Button2":["OBS iPad and Webcam","client.call(request.SetCurrentScene(\"iPad_Webcam\"))"],
    "Button3":["OBS Show Desktop","client.call(request.SetCurrentScene(\"Desktop_Only\"))"],
    "Button4":["OBS Toggle Mute","asyncio.create_task(toggle_mute(\"Scarlett_Audio\"))"],
    "Button5":["Zoom Mute","key_press('f13')"],
    #"Button6":["OBS TEST WEBCAM","key_press('f15')"]
    }

#Create GUI Window
window=tk.Tk()
for i in range(1):
    for j in range(len(button_dict)):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        btn=tk.Button(window,text=button_dict["Button"+str(j+1)][0], command=partial(eval,button_dict["Button"+str(j+1)][1],{"asyncio":asyncio,"toggle_mute":toggle_mute}))
        btn.grid(row=i,column=j)
        print(button_dict["Button"+str(j+1)][1])
window.title("OBS Control Centre")

#Set GUI always on top
window.after(0,toggle_mute)
window.wm_attributes("-topmost", 1)
window.mainloop()