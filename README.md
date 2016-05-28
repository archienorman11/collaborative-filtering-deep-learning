
## Collaborative filtering project using Deep Learning

This is a group project developed as part of the [COMPGI15 - Information Retrieval and Data Mining](http://www.cs.ucl.ac.uk/teaching_learning/syllabus/mscml/gi15_information_retrieval_data_mining/) module at University College London.

---

### Group 10 Members

* [Santiago Gonzalez](https://github.com/santteegt) | hernan.toral.15@ucl.ac.uk | MSc WSBDA (Web Science and Big Data Analytics)
* [Archie Norman](https://github.com/archienorman11) | archie.norman.15@ucl.ac.uk | MSc WSBDA (Web Science and Big Data Analytics)
* [Sergiu Tripon](https://github.com/SergiuTripon) | sergiu.tripon.15@ucl.ac.uk | MSc WSBDA (Web Science and Big Data Analytics)

---

### Overview

1. [Report](https://github.com/santteegt/ucl-irdm-collaborative-filtering/raw/master/report/ucl_irdm_group_project_report.pdf) - downloads automatically
2. [Dataset](#dataset)
3. [System Requirements](#user-content-system-requirements)
4. [Set-up](#set-up)
  1. [Setting up GraphLab Create](#user-content-setting-up-graphlab-create)
5. [Running Analysis](#user-content-running-analysis)
6. [Running Basic Recommenders](#user-content-running-basic-recommenders)
7. [Running Collaborative Deep Learning Model](#user-content-running-collaborative-deep-learning-model)

---

### Dataset

This project makes use of the #nowplaying dataset which can be found [here](http://dbis-nowplaying.uibk.ac.at/). A subset of the #nowplaying dataset was extracted using Reservoir Sampling, because the original dataset was too large (13GB). More information on the sampling workflow can be found in the report, accompanying this assignment. The subset extracted is stored on GitHub at the following path:

```
# in csv format
data/nowplaying_subset.csv

# or in tar.gz format
data/nowplaying_subset.csv.tar.gz
```

[Go to top](#user-content-collaborative-filtering-project-using-deep-learning)

---

### System Requirements

```
Python 2.7.x - required by GraphLab Create
GraphLab-Create
```

[Go to top](#user-content-collaborative-filtering-project-using-deep-learning)

---

### Set-up

Fork this repository and then clone it by running the following command and entering your GitHub username and password:

```bash
git clone https://github.com/YOUR-USERNAME/ucl-irdm-collaborative-filtering
```

#### Setting up GraphLab Create

GraphLab Create is a machine learning framework provided by Dato. In order to use GraphLab Create a license is required. Dato's Academic Programme offers a 1-year free license of GraphLab Create. In order to obtain a license, click [here](https://dato.com/download/academic.html) and register using a @ucl.ac.uk or @cs.ucl.ac.uk account.

Once you have obtained a GraphLab Create license, forked and cloned the repo, follow the steps below to continue setting up GraphLab Create:

```bash
# navigate to ucl-irdm-collaborative-filtering folder
$ cd ucl-irdm-collaborative-filtering

# navigate to dato folder
$ cd dato

# create a new virtual environment with Python 2.7.x
$ virtualenv -p /usr/bin/python2.7 dato-env

# activate the virtual environment
$ source dato-env/bin/activate

# ensure pip is updated to the latest version
$ pip install --upgrade pip

# install your licensed copy of GraphLab Create
$ pip install --upgrade --no-cache-dir https://get.dato.com/GraphLab-Create/1.8.5/your registered email address here/your product key here/GraphLab-Create-License.tar.gz

# when finished, deactivate the virtual environment
$ deactivate

```

[Go to top](#user-content-collaborative-filtering-project-using-deep-learning)

---

### Running Analysis

To run the Analysis, you need to run the `analysis.py` file by following the steps below:

```bash
# navigate to dato folder
$ cd dato

# activate the virtual environment
$ source dato-env/bin/activate

# navigate to analysis folder
$ cd analysis

# navigate to src folder
$ cd src

# run the analysis.py file with the preferred parameter
# @param tweet_total - total number of tweets
# @param user_total - total number of users
# @param artist_total - total number of artists
# @param track_total - total number of tracks

# @param user_stat - user statistics
# @param source_stat - source statistics
# @param artist_stat - artist statistics
# @param track_stat - track statistics
# @param artist_track_stat - artist track statistics
# @param user_filtered - filtered user id item id containing users with 3 or more tweets

# runs the tweet_total() function, prints output to terminal
$ python2.7 analysis.py --analysis tweet_total
# runs the user_total() function, prints output to terminal
$ python2.7 analysis.py --analysis user_total
# runs the artist_total() function, prints output to terminal
$ python2.7 analysis.py --analysis artist_total
# runs the track_total() function, prints output to terminal
$ python2.7 analysis.py --analysis track_total

# runs the user_stat() function, saves output to file
$ python2.7 analysis.py --analysis user_stat
# runs the source_stat() function, saves output to file
$ python2.7 analysis.py --analysis source_stat
# runs the artist_stat() function, saves output to file
$ python2.7 analysis.py --analysis artist_stat
# runs the track_stat() function, saves output to file
$ python2.7 analysis.py --analysis track_stat
# runs the artist_track_stat() function, saves output to file
$ python2.7 analysis.py --analysis artist_track_stat
# runs the user_filtered() function, saves output to file
$ python2.7 analysis.py --analysis user_filtered

# when done, deactivate the virtual environment
$ deactivate
```

The `analysis.py` prints to terminal the following:

1. Total number of tweets in the full dataset
2. Total number of tweets in the subset
3. Total number of users in the full dataset
4. Total number of users in the subset
5. Total number of artists in the full dataset
6. Total number of tracks in the full dataset

The `analysis.py` script also saves the following files at the following paths:

**Note**: The date `2016_04_06` in the filenames below represents the date version of the #nowplaying dataset.

```
# user statistics, generated by user_stat() function
dato/analysis/output/user_2016_04_06.csv

# source statistics, generated by source_stat() function
dato/analysis/output/source_2016_04_06.csv

# artist statistics, generated by artist_stat() function
dato/analysis/output/artist_2016_04_06.csv

# track statistics, generated by track_stat() function
dato/analysis/output/track_2016_04_06.csv

# artist and track statistics, generated by artist_track_stat() function
dato/analysis/output/artist_track_2016_04_06.csv

# user id and item id from the full dataset, generated by user_filtered() function
# the file is too large to be upload to GitHub, therefore only the first 5 lines were
# uploaded to GitHub as an example
dato/analysis/output/user_id_item_id_2016_04_06.csv

# user ids of users with 3 or more tweets
dato/analysis/output/user_count_3_2016_04_06.csv

# filtered user id and item id of users with 3 or more tweets, generated by user_filtered() function
# the file is too large to be upload to GitHub, therefore only the first 5 lines were
# uploaded to GitHub as an example
dato/analysis/output/filtered_user_count_3_2016_04_06.csv
```

[Go to top](#user-content-collaborative-filtering-project-using-deep-learning)

---

### Running Basic Recommenders

Basic Recommenders available:

* Item Similarity Model
* Popularity-based Recommender Model
* Factorization Recommender for Ranking Model

```bash
# navigate to dato folder
$ cd dato

# activate the virtual environment
$ source dato-env/bin/activate

# navigate to basic_rm folder
$ cd basic_rm

# navigate to src folder
$ cd src

# run the basic_rm.py file with the preferred parameter
# @param item_sim for item_similarity
# @param rank_fact for factorization recommender for ranking
# @param pop for popularity-based recommender

# runs the item_sim() function
$ python2.7 basic_rm.py --basic_rm item_sim
# runs the rank_fact() function
$ python2.7 basic_rm.py --basic_rm rank_fact
# runs the pop() function
$ python2.7 basic_rm.py --basic_rm pop

# when done, deactivate the virtual environment
$ deactivate
```

The `basic_rm.py` script saves the following files at the following paths:

```
# item similarity model recommendations, generated by item_sim() function
dato/basic_rm/output/item_sim_recs.csv

# item similarity model similar items, generated by item_sim() function
dato/basic_rm/output/item_sim_sim_items.csv

# item similarity model evaluation, generated by item_sim() function
dato/basic_rm/output/item_sim_evaluation.csv

# factorization recommender for ranking model recommendations, generated by rank_fact() function
dato/basic_rm/output/rank_fact_recs.csv

# factorization recommender for ranking model similar items, generated by rank_fact() function
dato/basic_rm/output/rank_fact_sim_items.csv

# factorization recommender for ranking model evaluation, generated by rank_fact() function
dato/basic_rm/output/rank_fact_evaluation.csv

# popularity-based recommender model recommendations, generated by pop() function
dato/basic_rm/output/pop_recs.csv

# popularity-based recommender model similar items, generated by pop() function
dato/basic_rm/output/pop_sim_items.csv

# popularity-based recommender model evaluation, generated by pop() function
dato/basic_rm/output/pop_evaluation.csv
```

[Go to top](#user-content-collaborative-filtering-project-using-deep-learning)

---

### Running Collaborative Deep Learning Model

1. Execute the scripts `setup_cdl_linux` or the `setup_cdl_mac` depending on the OS you are using.
2. Execute the following commands in a command shell under the home directory of this code repository:

```bash
# navigate to cdl folder
$ cd cdl

# activate the virtual environment
$ source venv/bin/activate

# run the collaborative deep learning model
$ python src/run.py
```

[Go to top](#user-content-collaborative-filtering-project-using-deep-learning)

