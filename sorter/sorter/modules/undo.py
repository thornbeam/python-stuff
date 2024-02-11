import os, shutil

curDir = os.path.dirname(__file__)
home = os.path.dirname(os.path.dirname(curDir))

src = home + "/src/"
dest = home + "/dest/"

images = dest + "image/"
documents = dest + "document/"
audios = dest + "audio/"
videos = dest + "video/"

def run():
    for homeDir, subDirs, files in os.walk(images):
        for f in files:
            shutil.move(images + f, src + f)
    for homeDir, subDirs, files in os.walk(documents):
        for f in files:
            shutil.move(documents + f, src + f)
    for homeDir, subDirs, files in os.walk(audios):
        for f in files:
            shutil.move(audios + f, src + f)
    for homeDir, subDirs, files in os.walk(videos):
        for f in files:
            shutil.move(videos + f, src + f)
