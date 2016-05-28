# get vocabulary from the data. then concatenate all data as text for each track.
# finally, obtain the tf-idf of each track or document against the vocab..
# at the end we need to have a TxV matrix where T is the number of tracks and
# the V is the vocabulary size.


# import packages
import time
import graphlab as gl
import numpy as np
import pandas as pd
from numpy import genfromtxt
from graphlab import SArray
from io import StringIO


########################################################################################################################


# loads data
def loadData():

    # load data
    print ("starting to load the data...")

    start = time.time()

    track_data = gl.SFrame.read_csv('../data/musicbrainz/track_data.csv', delimiter=',', verbose=False, header=True)

    track_record_tags = gl.SFrame.read_csv('../data/musicbrainz/track_record_tags.csv', delimiter=',', verbose=False, header=True)

    track_artist_tags = gl.SFrame.read_csv('../data/musicbrainz/track_artist_tags.csv', delimiter=',', verbose=False, header=True)

    end = time.time()

    # return data
    print("data loaded in %d ...", start-end)

    return track_data, track_record_tags, track_artist_tags


########################################################################################################################


# loads data
def aggregateData(filename):

    # load data
    print ("aggregating the data...")

    start = time.time()

    aggregatedData = filename.groupby("gid", operations = {

                    "tags": gl.aggregate.CONCAT("tag_label", "tag_label.1"),
                    "artists": gl.aggregate.SELECT_ONE("artistname"),
                    "track_names": gl.aggregate.SELECT_ONE("trackname")

                    })

    end = time.time()

    # return data
    print("aggregated in %d ...", start-end)

    return aggregatedData


########################################################################################################################


if __name__ == '__main__':

    print ("initialising...")

    track_data, track_record_tags, track_artist_tags = loadData()

    # track_data.save('track_data'), track_record_tags.save('track_record_tags'), track_artist_tags.save('track_artist_tags')

    print ("merging...")

    start = time.time()

    merged = track_data.join(track_record_tags, on='gid', how='left')

    print ("first merge complete...")

    data_matrix = merged.join(track_artist_tags, on='gid', how='left')

    end = time.time()

    print ("completed merge in %d, now printing...", start-end)

    print(data_matrix)

    data_matrix.save('../data/musicbrainz/matrix')

    # data_matrix.save('data/musicbrainz/matrix.csv', format='csv')

    aggregatedData = aggregateData(data_matrix)

    # print(aggregatedData)

    aggregatedData.save('../data/musicbrainz/aggregatedData')

    aggregatedData.save('../data/musicbrainz/aggregatedData.csv', format='csv')

    # sed 's/[^a-zA-Z0-9,-.]/ /g' aggregatedData.csv > removePunctuation.csv

    # temp1 = pd.read_csv("data/musicbrainz/removePunctuation.csv", skipinitialspace=True)

    # temp1 = np.genfromtxt("../data/musicbrainz/removePunctuation.csv", delimiter=",", filling_values=None)

    temp = SArray('../data/musicbrainz/removePunctuation.csv')

    docs_tfidf = gl.text_analytics.tf_idf(temp)

    print (docs_tfidf)

    docs_tfidf.save('../data/musicbrainz/docs_tfidf')

    docs_tfidf.save('../data/musicbrainz/docs_tfidf.csv', format='csv')




########################################################################################################################


    # print ("starting to load the data...\n")
    #
    # df1 = pd.read_csv("data/musicbrainz/track_artist_tags.csv", sep=';')
    #
    # df2 = pd.read_csv("data/musicbrainz/track_data.csv", sep=';')
    #
    # print ("...loading complete, now merging \n")
    #
    # merged = df1.merge(df2, on="gid", how="outer").fillna("")
    #
    # print ("...merged \n")
    #
    # merged.to_csv("data/musicbrainz/merged.csv", index=False)
    #
    # print ("...exported to csv \n")


########################################################################################################################


    # sed 's/[^a-zA-Z0-9,-.]/ /g' aggregatedData.csv > removePunctuation.csv
    # sed '/^$/d;s/[[:blank:]]//g' removePunctuation.csv > test1.csv
