import os
import re
import shutil

# Cleanup function
def ini(fileName):

    # Source directory
    dirOld = os.path.dirname(fileName)
    print(dirOld + " || Source directory")

    # RegEx Artist and Name from song.ini
    for lineBuf in open(fileName, 'r'):
        reArtist = RegExArtist.search(lineBuf)
        if reArtist:
            artist = ((reArtist.group(1)))
        reSong = RegExSong.search(lineBuf)
        if reSong:
            song = ((reSong.group(1)))
    title = (artist + ' - ' + song)
    title = title.replace(":", "-")
    title = title.replace("?", "")
    title = title.replace("*", "")

    # New directory
    dirNew = os.path.dirname(os.path.realpath(__file__)) + '\Cleaned up songs/' + title

    # Ignore desktop.ini file funciton
    def ignoreFiles(file): 
        def _ignore_(path, names): 
            ignored = [file] 
            if file in names: 
                ignored.append(file) 
            return set(ignored) 
        return _ignore_ 
    
    # Copy files to new directory
    if not os.path.exists(dirNew):
        shutil.copytree(dirOld, dirNew, ignore=ignoreFiles('desktop.ini'))
        print(dirNew + " || New directory created")
    else:
        print(dirNew + " || New directory already exist")

########## Starting Process ##########
# RegEx Patterns
RegExArtist = re.compile('(?i)artist*\s*=\s*(.+)')
RegExSong = re.compile('(?i)name*\s*=\s*(.+)')

# Walking thourhg subdirectories
rootdir = os.path.dirname(os.path.realpath(__file__)) + "\\songs"
for subdir, dirs, folders in os.walk(rootdir):
    for file in folders:
        if 'song.ini' in file:
            fileName = (os.path.join(subdir, file))
            ini(fileName)
print('Job Completed')