
# import packages
import argparse
import graphlab as gl

########################################################################################################################


# loads data
def load_data():

    # load data
    data = gl.SFrame.read_csv('../../../data/nowplaying/nowplaying_2016_04_06.csv', delimiter=',', verbose=False)

    # return data
    return data


########################################################################################################################


# loads subset
def load_subset():

    # load subset
    subset = gl.SFrame.read_csv('../../../data/nowplaying_subset.csv', delimiter=',', verbose=False)

    # return subset
    return subset


########################################################################################################################


# gets total number of tweets in the full dataset and subset
def tweet_total(data, subset):

    # get total number of tweets in the full dataset and subset
    tweets_data = len(data.__getitem__('user_id'))
    tweets_subset = len(subset.__getitem__('user_id'))
    print 'Total number of tweets in the full dataset: {}'.format(tweets_data)
    print 'Total number of tweets in the subset: {}'.format(tweets_subset)


########################################################################################################################


# gets total number of users in the full dataset and subset
def user_total(data, subset):

    # get total number of users in the full dataset and subset
    users_data = data.__getitem__('user_id')
    users_subset = subset.__getitem__('user_id')
    users_data = users_data.unique()
    users_subset = users_subset.unique()
    print 'Total number of users in the full dataset: {}'.format(len(users_data))
    print 'Total number of users in the subset: {}'.format(len(users_subset))


########################################################################################################################


# gets total number of artists in the full dataset
def artist_total(data):

    # get total number of artists in the full dataset
    artists = data.__getitem__('artist')
    artists = artists.unique()
    print 'Total number of artists in the full dataset: {}'.format(len(artists))


########################################################################################################################


# gets total number of tracks in the full dataset
def track_total(data):

    # gets total number of tracks in the full dataset
    tracks = data.__getitem__('track')
    tracks = tracks.unique()
    print 'Total number of tracks in the full dataset: {}'.format(len(tracks))


########################################################################################################################


# gets user stats from the full dataset
def user_stat(data):

    # get user stats from the full dataset
    user_data = (data.groupby('user_id', {'count': gl.aggregate.COUNT('user_id')}).sort('count', ascending=False))
    user_data.save('../output/user_2016_04_06.csv')


########################################################################################################################


# gets source stats from the full dataset
def source_stat(data):

    # get source stats from the full dataset
    source_data = (data.groupby('source', {'count': gl.aggregate.COUNT('source')}).sort('count', ascending=False))
    source_data.save('../output/source_2016_04_06.csv')


########################################################################################################################


# gets artist stats from the full dataset
def artist_stat(data):

    # get artist stats from the full dataset
    artist_data = (data.groupby('artist', {'count': gl.aggregate.COUNT('artist')}).sort('count', ascending=False))
    artist_data.save('../output/artist_2016_04_06.csv')


########################################################################################################################


# gets track stats from the full dataset
def track_stat(data):

    # get track stats from the full dataset
    track_data = (data.groupby('track', {'count': gl.aggregate.COUNT('track')}).sort('count', ascending=False))
    track_data.save('../output/track_2016_04_06.csv')


########################################################################################################################


# gets artist track stats from the full dataset
def artist_track_stat(data):

    # get artist track stats from the full dataset
    artist_track_data = (data.groupby('artist',
                       {'track': gl.aggregate.SELECT_ONE('track')},
                       {'artist count': gl.aggregate.COUNT('artist')},
                       {'track count': gl.aggregate.COUNT('track')}
                       ).sort('artist count', ascending=False))
    artist_track_data.save('../output/artist_track_2016_04_06.csv')


########################################################################################################################


# gets filtered users with 3 or more tweets
def user_filtered(data):

    # get user id item id from the full dataset
    user_id_item_id = data.select_columns(['user_id', 'item_id'])
    # save user id item id to file
    user_id_item_id.save('../output/user_id_item_id_2016_04_06.csv')

    # load user id item id file
    load_uid_iid = gl.SFrame.read_csv('../output/user_id_item_id_2016_04_06.csv', delimiter=',', verbose=False)
    # load user count 3 file, file containing users with 3 or more tweets but not containing the item column
    load_user_count_3 = gl.SArray('../output/user_count_3_2016_04_06.csv')

    # filter user id item id file by user count 3 file
    filtered_user_count_3 = load_uid_iid.filter_by(load_user_count_3, 'user_id').sort('user_id', ascending=False)
    # save user id item id containing users with 3 or more tweets
    filtered_user_count_3.save('../output/filtered_user_count_3_2016_04_06.csv')


########################################################################################################################


# main function
def main(analysis):

    # load data and subset
    data = load_data()
    subset = load_subset()

    if analysis == 'tweet_total':
        # get total number of tweets in the full dataset and subset
        tweet_total(data, subset)
    elif analysis == 'user_total':
        # get total number of users in the full dataset and subset
        user_total(data, subset)
    elif analysis == 'artist_total':
        # get total number of artists in the full dataset
        artist_total(data)
    elif analysis == 'track_total':
        # get total number of tracks in the full dataset
        track_total(data)

    if analysis == 'user_stat':
        # get user stats
        user_stat(data)
    elif analysis == 'source_stat':
        # get source stats
        source_stat(data)
    elif analysis == 'artist_stat':
        # get artist stats
        artist_stat(data)
    elif analysis == 'track_stat':
        # get track stats
        track_stat(data)
    elif analysis == 'artist_track_stat':
        # get artist track stats
        artist_track_stat(data)
    elif analysis == 'user_filtered':
        # get users with 3 or more tweets
        user_filtered(data)


########################################################################################################################


# runs main function
if __name__ == '__main__':

    # parse script argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--analysis', type=str, dest='analysis', metavar='analysis type',
                        help='analysis type', required=True)
    args = parser.parse_args()

    # call main function with the script argument as parameter
    main(args.analysis)


########################################################################################################################
