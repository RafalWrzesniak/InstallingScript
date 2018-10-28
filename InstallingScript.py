import time
import os
#import reachArgs

red = '\033[91m' + '\033[1m'
end = '\033[0m'
bold = '\033[1;34m' + '\033[1m'
ex_cod = 0
conf_file_path = ''
repository_path = ''
report_path = ''
help_usage = ''
# to delete
#conf_file_path = 'C:\\Users\\Student\\Desktop'
#repository_path = 'C:\\Users\\Student\\Desktop\\Target'
#report_path = 'C:\\Users\\Student\\Desktop'


# Get current time and date func
def get_time():
    localtime = time.localtime(time.time())
    cur_time = ''
    for i in range(0, 6):
        cur_time += str(localtime[i])
        if i < 2:
            cur_time += '-'
        elif i == 2:
            cur_time += '_'
        elif i < 5:
            cur_time += ';'
    return cur_time


# Get configuration file path
conf_file_path = input('Type configuration file path:\n')
if conf_file_path == '':
    conf_file_path = 'C:\\Users\\Rafal\\Desktop'
try:
    os.chdir(conf_file_path)
except Exception as e:
    print(e)
    print('Configuration file path set to default')
    conf_file_path = r'C:\\Users\\Rafal\\Desktop'
print('Configuration file path: ' + conf_file_path)

# Get repository path
repository_path = input('Type repository path:\n')
if repository_path == '':
    repository_path = 'F:\\Rafał\\Instalki\\Code Blocks'
try:
    os.chdir(repository_path)
except Exception as e:
    print(e)
    print('Repository path set to default')
    repository_path = 'F:\\Rafał\\Instalki\\Code Blocks'
print('Repository folder path: ' + repository_path)

# Get report file path
report_path = input('Type report file path:\n')
if report_path == '':
    report_path = 'C:\\Users\\Rafal\\Desktop'
try:
    os.chdir(report_path)
except Exception as e:
    print(e)
    print('Report file path set to default')
    report_path = 'C:\\Users\\Rafal\\Desktop'
print('Report file path: ' + report_path)

# help
help_usage = input('Help? [T/F]\n')
if help_usage == 'T':
    print('Here is help')
else:
    print('-')

# Creating file list to be install
os.chdir(conf_file_path)  # reachArgs.conf_file_path
try:
    file_conf = open('ConfFile.txt', 'r')
    target_list = file_conf.readlines()
    for i in range(len(target_list)):
        if target_list[i].endswith('\n'):
            target_list[i] = target_list[i][0:-1]
    file_conf.close()
except Exception as e:
    print(e)
    target_list = []
# print(target_list)

# Check if files exist
os.chdir(repository_path)
f = open('restart.txt', 'w')
f.close()
files_list = os.listdir(repository_path)
for name in target_list:
    if name not in files_list and name != 'restart':
        print(red + 'File "' + name + '" not found. It will not be installed' + end)
        target_list.remove(name)


# Check if os restart interrupted installation
try:
    restart_info = open('restart_info.txt', 'r')
    leng = restart_info.readlines()
    restart_info.close()
    target_list = target_list[len(leng):]
except Exception as e:
    print('Running for the first time')
prt_target_list = [name for name in target_list if name != 'restart']
print('Files to install: ' + str(prt_target_list))


# Run files
for name in target_list:
    if name != 'restart':
        try:
            start_time = get_time()
            print('Installing file "' + bold + name + end + '"')
            #ex_cod = os.system(msiexec /i repository_path + '\\' + name)
            print('"' + bold + name + end + '" installed')
            restart_info = open('restart_info.txt', 'a')
            restart_info.write('1\n')
            restart_info.close()
            stop_time = get_time()
        except Exception as e:
            print(e)
            print(red + 'Failed to install "' + name + '"' + end)
            ex_cod = 2
            sto_time = get_time()

        rep_file = open(report_path + '\\' + get_time() + '_Report.txt', 'a')
        if ex_cod == 0:
            rep_file.write(name + ', ' + start_time + ', ' + stop_time + ', ' + 'SUCCESS\n')
        else:
            rep_file.write(name + ', ' + start_time + ', ' + stop_time + ', ' + 'FAILED\n')
        rep_file.close()

    else:
        restart_info = open('restart_info.txt', 'a')
        restart_info.write('1\n')
        restart_info.close()
        print(red + 'Restarting system..' + end)
        # os.system("shutdown /r")
os.system("del restart_info.txt")
print(bold + '\nInstallation completed\n' + end)
