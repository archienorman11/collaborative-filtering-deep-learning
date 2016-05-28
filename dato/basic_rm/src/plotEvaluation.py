import matplotlib.pyplot as plt
import numpy as np


data1 = np.genfromtxt('../output/item_sim_evaluation.csv', delimiter=',', skip_header=1)
data2 = np.genfromtxt('../output/rank_fact_evaluation.csv', delimiter=',', skip_header=1)
data3 = np.genfromtxt('../output/pop_evaluation.csv', delimiter=',', skip_header=1)


def plot_map(k):

    fig = plt.figure()

    ax1 = fig.add_subplot(111)
    ax1.set_title("mAP Evaluation")
    ax1.set_ylabel('Mean Avg. Precision')
    ax1.set_xlabel('Top-mapmapK')

    ax1.plot(data1[:k, 0], data1[:k, 1], c='r', label='item-sim')
    ax1.plot(data2[:k, 0], data2[:k, 1], c='b', label='rank-fact')
    ax1.plot(data3[:k, 0], data3[:k, 1], c='g', label='pop')

    ax1.legend()

    plt.show()


def plot_recall(k):

    fig = plt.figure()
    ax1 = fig.add_subplot(111)

    ax1.set_title("Recall Evaluation")
    ax1.set_ylabel('Recall')
    ax1.set_xlabel('Top-K')

    ax1.plot(data1[:k, 0], data1[:k, 2], c='r', label='item-sim')
    ax1.plot(data2[:k, 0], data2[:k, 2], c='b', label='rank-fact')
    ax1.plot(data3[:k, 0], data3[:k, 2], c='g', label='pop')

    ax1.legend(loc=2)

    plt.show()



if __name__ == '__main__':

    plot_map(10)
    plot_recall(10)

