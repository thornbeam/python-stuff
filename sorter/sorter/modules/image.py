import os, shutil

curDir = os.path.dirname(__file__)
home = os.path.dirname(os.path.dirname(curDir))

src = home + "/src/"
dest = home + "/dest/"
formats = home + "/sorter/formats/"

tmp_file = open(formats + "image.txt", "r")
image_formats = tmp_file.readlines()
tmp_file.close()

def run():
    if not os.path.exists(dest + "images/"):
        os.mkdir(dest + "images/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("checking", f, "...\n")
            tmp = False
            for d in image_formats:
                d = d.strip("\n")
                print("Checking", d, "...\n")
                if d in f:
                    shutil.move(src + f, dest + "images/" + f)
                    tmp = True
                    break
            if tmp:
                print(f, "is successfully moved in 'images'.\n")
            else:
                print(f, "couldn't be moved in 'images'.\n")
