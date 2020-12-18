#!/usr/bin/python


'''
Intel License
'''

import argparse
import os
import subprocess
import shutil

'''
For generating API document, this will copy java files located in webrtc stack to android client sdk repo
'''

THIS = os.path.dirname(os.path.abspath(__file__))
STACK_ANDROID_PATH='src/talk/ics/sdk/base/android/java/com/intel/webrtc/base'
STACK_AUDIO_PATH='src/third_party/webrtc/modules/audio_device/android/java/src/com/intel/webrtc/base'
ANDROID_REPO_PATH=os.path.join(THIS, '../src/sdk/base/src/main/java/com/intel/webrtc/base/')
DOXYGEN_PATH = os.path.join(THIS, 'doxygen')

FOUND_STACK = False

def cleanEnv():
    os.chdir(os.path.join(THIS, '..'))
    cmd = ['./gradlew', 'clean']
    subprocess.call(cmd)

    if os.path.exists(os.path.join(THIS, 'html')):
        shutil.rmtree(os.path.join(THIS, 'html'))

def genDoc():
    os.chdir(DOXYGEN_PATH)
    cmd = ['doxygen', 'doxygen_android.conf']
    subprocess.call(cmd)

if __name__ == '__main__':
    cleanEnv()
    genDoc()
    if not FOUND_STACK:
        print '\n ------------------------------'
        print ' | No webrtc stack found      |'
        print ' | Please use -stack_location |'
        print ' | to set webrtc stack path   |'
        print ' ------------------------------\n'
