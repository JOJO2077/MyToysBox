import os
import base64

flag = True
p = b"H:/MITE/.minecraft/assets"


def fileMap(path):
    parents = os.listdir(path)
    for parent in parents:
        child = os.path.join(path, parent)
        childout = ''
        if (flag):
            childout = os.path.join(path,
                                    base64.b64encode(os.path.split(parent)[1]))
        else:
            childout = os.path.join(path,
                                    base64.b64decode(os.path.split(parent)[1]))

        if os.path.isdir(child):
            fileMap(child)
        else:
            with open(child, 'rb+') as f:
                bit = f.read(1)
                f.seek(0)
                f.write(bytes(chr(127-ord(bit))))
            os.rename(childout, child)


fileMap(p)
