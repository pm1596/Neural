#change
# Parameters
learning_rate = 0.01
training_iters = 1000
#batch_size = 100
display_step = 50

# Network Parameters
no_input = 1024 # matrix dataset input (adj_mat shape: 32*32)
no_classes = 2 # output classes -(dense/sparse)
dropout = 0.75 # Dropout, probability to keep units

# tf computation graph input
x = tf.placeholder(tf.float32, [None, no_input])   # input matrices
y = tf.placeholder(tf.float32, [None, no_classes]) # labels
keep_prob = tf.placeholder(tf.float32) #dropout (keep probability)
