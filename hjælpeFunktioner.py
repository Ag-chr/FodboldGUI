import pickle


def gem(filename, item):
    outfile = open(filename, 'wb')
    pickle.dump(item, outfile)
    outfile.close()


def moneySortedList():
    return dict(sorted(fodboldtur.items(), key=lambda item: item[1]))

def nameSortedList():
    pass

