#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    flist = dir(hidden_4)
    for i in range(len(flist)):
        if (flist[i][0] != '_' and flist[i][1] != '_'):
            print("{}".format(flist[i]))
