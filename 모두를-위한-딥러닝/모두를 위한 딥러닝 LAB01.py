%tensorflow_version 1.x
import tensorflow as tf

import tensorflow.compat.v1 as tf
tf.diable_v2_behavior()



hello = tf.constant("Hello, Tensorflow!") #.constant()
sess = tf.Session() #.Session()
print(sess.run(hello)) #.run()
'''
b'Hello, Tensorflow!'
'''



node1 = tf.constant(3.0, tf.float32)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)  #.add()

sess = tf.Session()
print("sess.run(node1, node2): ", sess.run([node1, node2])) 
print("sess.run(node3): ", sess.run(node3))
'''
sess.run(node1, node2):  [3.0, 4.0]
sess.run(node3):  7.0
'''



a_node = tf.placeholder(tf.float32) #.placeholeder()와 feed_dict={a:a_data}
b_node = tf.placeholder(tf.float32)
add_node = a_node + b_node

print(sess.run(add_node, feed_dict={a_node:2, b_node:13}))
'''
15.0
'''
