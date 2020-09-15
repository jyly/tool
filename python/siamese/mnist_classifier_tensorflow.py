import tensorflow as tf
from keras.datasets import mnist
import numpy as np
def create_pairs(x, digit_indices,num_classes):
    '''Positive and negative pair creation.
    Alternates between positive and negative pairs.
    '''
    pairs = []
    labels = []
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        for i in range(n):
            z1, z2 = digit_indices[d][i], digit_indices[d][i + 1]
            pairs += [[x[z1], x[z2]]]
            inc = random.randrange(1, num_classes)
            dn = (d + inc) % num_classes
            z1, z2 = digit_indices[d][i], digit_indices[dn][i]
            pairs += [[x[z1], x[z2]]]
            labels += [1, 0]
    return np.array(pairs), np.array(labels)

def create_pairs_incre(x, digit_indices,num_classes):
    '''Positive and negative pair creation.
    Alternates between positive and negative pairs.
    '''
    pairs = []
    labels = []
    print([len(digit_indices[d]) for d in range(num_classes)])
    n = min([len(digit_indices[d]) for d in range(num_classes)]) - 1
    for d in range(num_classes):
        for i in range(n):
            for j in range(i+1,n+1):
                z1, z2 = digit_indices[d][i], digit_indices[d][j]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*2)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*3)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*4)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                np.random.seed(i*10+j*5)
                inc = np.random.randint(1, num_classes)
                dn = (d + inc) % num_classes
                z1, z2 = digit_indices[d][i], digit_indices[dn][i]
                pairs += [[x[z1], x[z2]]]

                labels += [1, 0, 0, 0, 0, 0]

    return np.array(pairs), np.array(labels)



(train_data, train_target), (test_data, test_target) = mnist.load_data()
train_data = train_data.astype('float32')
test_data = test_data.astype('float32')
train_data /= 255
test_data /= 255
input_shape = train_data.shape[1:]

digit_indices = [np.where(train_target == i)[0] for i in range(0,num_classes)]
train_pairs, train_label = create_pairs(train_data, digit_indices,num_classes)

digit_indices = [np.where(test_target == i)[0] for i in range(0,num_classes)]
test_pairs, test_label = create_pairs(test_data, digit_indices,num_classes)