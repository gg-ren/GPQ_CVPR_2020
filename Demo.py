from utils.GPQ_network import *
from utils.Functions import *
from utils import cifar10 as ci10
from utils.RetrievalTest import *


def demo():

    G_x, Q_x = ci10.prepare_data(data_dir, False)

    l_S = csr_matrix(scipy.io.loadmat(cifar10_label_sim_path)['label_Similarity'])
    l_S = l_S.todense()

    Net = GPQ(training=training_flag)
    feature = Net.F(x)
    Z = Net.Z

    saver = tf.train.Saver(tf.global_variables())

    with tf.Session(config=config) as sess:
        saver.restore(sess, model_load_path)
        mAP = PQ_retrieval(sess, x, training_flag, feature, Z, n_book, G_x, Q_x, l_S, True, TOP_K=n_DB)
        print(model_load_path+" mAP: %.4f"%(mAP))


if __name__ == '__main__':
    demo()

