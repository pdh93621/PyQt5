import os
import custom_ppt
import time
import winreg

command_lists = ['StartEnd', 'NextSlide', 'PreviousSlide', 'AddMedia', 'AddLink']
motion_lists = ['zero', 'one', 'two', 'three', 'four', 'five', 'K', 'L']

def find_exe(file):
    extension = '.' + file.split('.')[-1]
    exe = winreg.QueryValue(winreg.HKEY_CLASSES_ROOT, extension)
    created_key = winreg.CreateKey(winreg.HKEY_CLASSES_ROOT, exe)
    exepath = winreg.QueryValue(created_key, 'DefaultIcon')
    exepath = exepath.split(',')[0]
    if exepath[0] in ["'",'"']:
        exepath = eval(exepath)
    return exepath

def Gesture2Command(class_lists, given_motion):
    for class_list in class_lists:
        class_list.g2c(given_motion)

def list2para(custom):
    if custom[0] in command_lists[1:3]:
        temp = [custom[0], custom[1:]]
        
    elif custom[0] == command_lists[3] or custom[0] == command_lists[0]:
        exepath = find_exe(custom[-1])
        custom[-1] = custom[-1].replace('/', '\\')
        temp = [custom[0], custom[1:-2], exepath, custom[-1]]

    elif custom[0] == command_lists[4]:
        temp = [custom[0], custom[1:-1], custom[-1]]

    return temp

PATH_BASE = os.path.dirname(__file__)
ppt_elements_path = os.path.join(PATH_BASE, 'ppt_elements')
ppt_elements = os.listdir(ppt_elements_path)
#print(ppt_elements)

customPPT = 'customPPT.txt'
#ppt_environment_setting = 'ppt_environment_setting.txt'

with open(os.path.join(ppt_elements_path, customPPT)) as f:
    customs = [list2para(l[:-1].split('|')) for l in f.readlines()]

# with open(os.path.join(ppt_elements_path, ppt_environment_setting)) as f:
#     settingevi = f.readline().split('|')[1:]

# for custom in customs:
#     if custom[0] == "StartEnd":
#         custom.append(settingevi[0].replace('/', '\\'))
#         custom.append(settingevi[1].replace('/', '\\'))

#print(customs)
#print(settingevi)

class_lists = []

for custom in customs:
    class_lists.append(getattr(custom_ppt, custom[0])(*custom[1:]))

#print(class_lists)

#Gesture2Command(class_lists, customs[0][1])

print(class_lists[0].is_open_ppt)
print(class_lists[0].pptpath)
print(class_lists[0].exepath)

i = 0
while i < 6:
    Gesture2Command(class_lists, customs[0][1])
    time.sleep(2)
    Gesture2Command(class_lists, customs[3][1])
    time.sleep(2)
    i += 1