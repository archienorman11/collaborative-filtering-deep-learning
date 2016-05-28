
# import packages
import math
import argparse
import graphlab as gl

########################################################################################################################


# loads data
def load_data():

    # load data
    data = gl.SFrame.read_csv('../../../data/nowplaying_subset.csv', delimiter=',', verbose=False)

    train_data, test_data = gl.recommender.util.random_split_by_user(data, max_num_users=int(math.floor(data.shape[0]/4)))
    # train_data, test_data = gl.recommender.util.random_split_by_user(data, max_num_users=5000)

    # return train and test data
    return train_data, test_data


########################################################################################################################


# evaluates model
def evaluate_model(model, model_name, test_data):

    # map and recall evaluation for top-K items
    evaluation = gl.recommender.util.compare_models(test_data, [model], model_names=[model_name])

    # save model evaluation to file
    evaluation[0]['precision_recall_overall'].save('../output/{0}_evaluation.csv'.format(model_name), format='csv')

    # return model evaluation
    return evaluation


########################################################################################################################


# runs item similarity model
def item_sim(train_data, test_data):

    # create item similarity recommender
    rm = gl.item_similarity_recommender.create(train_data)

    # make recommendations
    recs = rm.recommend()

    # save recommendations to file
    recs.save('../output/item_sim_recs.csv', format='csv')

    # get similar items
    sim_items = rm.get_similar_items()

    # save similar items to file
    sim_items.save('../output/item_sim_sim_items.csv', format='csv')

    # evaluate model
    evaluate_model(rm, 'item_sim', test_data)


########################################################################################################################


# runs factorization recommender for ranking model
def rank_fact(train_data, test_data):

    # create ranking factorization recommender
    rm = gl.ranking_factorization_recommender.create(train_data)

    # make recommendations
    recs = rm.recommend()

    # save recommendations to file
    recs.save('../output/rank_fact_recs.csv', format='csv')

    # get similar items
    sim_items = rm.get_similar_items()

    # save similar items to file
    sim_items.save('../output/rank_fact_sim_items.csv', format='csv')

    # evaluate model
    evaluate_model(rm, 'rank_fact', test_data)


########################################################################################################################


# runs popularity-based recommender model
def pop(train_data, test_data):

    # create popularity recommender
    rm = gl.popularity_recommender.create(train_data)

    # make recommendations
    recs = rm.recommend()

    # save recommendations to file
    recs.save('../output/pop_recs.csv', format='csv')

    # get similar items
    sim_items = rm.get_similar_items()

    # save similar items to file
    sim_items.save('../output/pop_sim_items.csv', format='csv')

    # evaluate model
    evaluate_model(rm, 'pop', test_data)


########################################################################################################################


# main function
def main(basic_rm):

    # load train and test data
    train_data, test_data = load_data()

    # if basic recommender equals to 'item_sim'
    if basic_rm == 'item_sim':
        # run item sim function
        item_sim(train_data, test_data)
    # if basic recommender equals to 'rank_fact'
    elif basic_rm == 'rank_fact':
        # run rank function
        rank_fact(train_data, test_data)
    # if basic recommender equals to 'pop'
    elif basic_rm == 'pop':
        # run pop function
        pop(train_data, test_data)


########################################################################################################################


# runs main function
if __name__ == '__main__':

    # parse script argument
    parser = argparse.ArgumentParser()
    parser.add_argument('-b_rm', '--basic_rm', type=str, dest='basic_rm', metavar='basic recommender name',
                        help='basic recommender name', required=True)
    args = parser.parse_args()

    # call main function with the script argument as parameter
    main(args.basic_rm)


########################################################################################################################
