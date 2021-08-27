import time
import os
from custom_ppt import *

def Gesture2Command(class_lists, given_motion):
    for class_list in class_lists:
        class_list.g2c(given_motion)

ppt_exepath = "C:\\Program Files (x86)\\HNC\\Office 2018\\HOffice100\\Bin\HShow.exe"
media_exepath = "C:\\Program Files\\DAUM\\PotPlayer"

pptpath = "C:\\Users\\User\\Downloads\\Prj_aMotion (1).pptx"
mediapath = "C:\\Python\\Pyqt5\\Gesture2Command\\test_datas\\amumu1.mp4"

link = "www.naver.com"

class_lists = []

class_lists.append(StartEnd('K', ppt_exepath, pptpath))

class_lists.append(NextSlide('L'))

class_lists.append(PreviousSlide('zero'))

class_lists.append(AddMedia('one', media_exepath, mediapath))

class_lists.append(AddLink('two', link))

Gesture2Command(class_lists, 'K')
time.sleep(1)
Gesture2Command(class_lists, 'K')
time.sleep(1)
Gesture2Command(class_lists, 'L')
time.sleep(1)
Gesture2Command(class_lists, 'L')
time.sleep(1)
Gesture2Command(class_lists, 'zero')
time.sleep(1)
Gesture2Command(class_lists, 'K')
time.sleep(1)
Gesture2Command(class_lists, 'one')
time.sleep(4)
Gesture2Command(class_lists, 'one')
time.sleep(1)
Gesture2Command(class_lists, 'two')
time.sleep(5)
#Gesture2Command(class_lists, 'two')