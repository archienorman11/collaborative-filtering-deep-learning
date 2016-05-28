import pandas as pd
import numpy as np
from collections import defaultdict
from collections import Counter

import csv

np.set_printoptions(threshold=np.nan)

data = []
clean_data = []
d = {}

########################################################################################################################


def openData(filename):

    print ("loading datset from file %s" % filename)

    with open(filename) as infile:

        for line in infile:

            line = line.strip()

            line = line.split(',')

            data.append(line)

    return data


########################################################################################################################


def openPanda(data):

    pandaData = pd.DataFrame(data) # , dtype=string

    pandaData.columns = ['user_id', 'mb_track_id']

    cleanData = pandaData.groupby('user_id', as_index=True).agg(lambda x: tuple(x))

    return cleanData


########################################################################################################################


def writePanda(pandaData):

    with open("../data/output.csv", "wb") as f:

        writer = csv.writer(f)

        writer.writerows(e)


########################################################################################################################

if __name__ == '__main__':

    iterateData = openData("../data/user-track.csv")

    print ("loading complete, now writing to file")

    e = []

    for k, v in iterateData:

        d.setdefault(k, []).append(v)

    for key, value in d.items():

        e.append((key, len(filter(bool, value)), value))

    writePanda(e)




    #CLEAN
    # sed 's/[^a-zA-Z0-9,-]/ /g' pre/output.csv > pre/clean_output.csv
