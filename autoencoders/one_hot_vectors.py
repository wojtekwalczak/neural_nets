"""
A simple auto-encoder, which learns binary representation for 8 one-hot vectors 
of length 8 each.

Input vectors                        Learned representation
---------------------------------    ----------------------
[ 1.  0.  0.  0.  0.  0.  0.  0.] => [ 0.  0.  1.]
[ 0.  1.  0.  0.  0.  0.  0.  0.] => [ 1.  0.  1.]
[ 0.  0.  1.  0.  0.  0.  0.  0.] => [ 0.  0.  0.]
[ 0.  0.  0.  1.  0.  0.  0.  0.] => [ 0.  1.  1.]
[ 0.  0.  0.  0.  1.  0.  0.  0.] => [ 1.  1.  1.]
[ 0.  0.  0.  0.  0.  1.  0.  0.] => [ 0.  1.  0.]
[ 0.  0.  0.  0.  0.  0.  1.  0.] => [ 1.  0.  0.]
[ 0.  0.  0.  0.  0.  0.  0.  1.] => [ 1.  1.  0.]

"""

import random
import numpy as np
import tensorflow as tf

# Input definition
input_size, hidden_size = 8, 3
X = tf.placeholder(tf.float32, [8, input_size])

# Weights & bias for hidden layer
W_input_to_hidden = tf.Variable(tf.truncated_normal([input_size, hidden_size]))
b_hidden = tf.Variable(tf.truncated_normal([hidden_size]))

# Weights & bias for output layer 
W_hidden_to_output = tf.Variable(tf.truncated_normal([hidden_size, input_size]))
b_output = tf.Variable(tf.truncated_normal([input_size]))

# Compute hidden layer & output layer
hidden = tf.nn.sigmoid(tf.nn.xw_plus_b(X, W_input_to_hidden, b_hidden))
output = tf.nn.softmax(tf.nn.xw_plus_b(hidden, W_hidden_to_output, b_output))

# Loss function: mean squared error
error = tf.sqrt(tf.reduce_mean(tf.square(X - output)))
train_op = tf.train.AdamOptimizer(learning_rate=0.01).minimize(error)

# Drop scientific notation
np.set_printoptions(suppress=True)
np.set_printoptions(precision=1)

# Input vectors
eye = np.eye(8, dtype=np.float32)

with tf.Session() as sess:
    sess.run(tf.initialize_all_variables())
    for i in range(50000):
        cur_eye = sorted(eye, key=lambda k: random.random())
        _, cur_error = sess.run([train_op, error], feed_dict={X: cur_eye})
        print('{}: {}\r'.format(i, cur_error, end=" "))

    print('Querying hidden layer for learned representation (encoding):')
    inputs = sess.run([hidden], feed_dict={X: eye})[0]
    for orig, encoded in zip(eye, inputs):
        print('{} => {}'.format(orig, encoded))

    print('\nQuerying output layer (decoding):')
    outputs = sess.run([output], feed_dict={hidden: np.array(inputs)})[0]
    for encoded, decoded in zip(inputs, outputs):
        print('{} => {}'.format(encoded, decoded))

