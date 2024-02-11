import os, shutil

curDir = os.path.dirname(__file__)
home = os.path.dirname(os.path.dirname(curDir))

src = home + "/src/"
dest = home + "/dest/"
formats = home + "/sorter/formats/"

tmp_file = open(formats + "document.txt", "r")
document_formats = tmp_file.readlines()
tmp_file.close()

def run():
    if not os.path.exists(dest + "documents/"):
        os.mkdir(dest + "documents/")

    for home, subDirs, files in os.walk(src):
        for f in files:
            print("checking", f, "...\n")
            tmp = False
            for d in document_formats:
                d = d.strip("\n")
                print("Checking", d, "...\n")
                if d in f:
                    shutil.move(src + f, dest + "documents/" + f)
                    tmp = True
                    break
            if tmp:
                print(f, "is successfully moved in 'documents'.\n")
            else:
                print(f, "couldn't be moved in 'documents'.\n")
