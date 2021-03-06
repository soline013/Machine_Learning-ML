%tensorflow_version 1.x
import tensorflow as tf

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()



#H(x) = Wx + b
x_train = [1, 2, 3]
y_train = [1, 2, 3]
w = tf.Variable(tf.random_normal([1]), name='weight') #.Variable(): 변수
b = tf.Variable(tf.random_normal([1]), name='bias') #.random_normal(Shapes)
hypothesis = x_train * w + b

#Cost(W,b)=∑...
cost = tf.reduce_mean(tf.square(hypothesis - y_train)) #.reduce_mean(): 평균 #.square()

#Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01) #.GradientDescentOptimizer()
train = optimizer.minimize(cost) #.minimize()

sess = tf.Session()
sess.run(tf.global_variables_initializer()) #.global_variables_initializer()

for step in range(2001):
  sess.run(train)
  if step % 20 == 0:
    print("step:", step, "cost:", sess.run(cost), "w:", sess.run(w), "b:", sess.run(b))
'''
step: 1920 cost: 1.6264777e-06 w: [1.0014813] b: [-0.00336703]
step: 1940 cost: 1.4772226e-06 w: [1.0014116] b: [-0.00320888]
step: 1960 cost: 1.341712e-06 w: [1.0013454] b: [-0.00305814]
step: 1980 cost: 1.2185493e-06 w: [1.0012822] b: [-0.00291448]
step: 2000 cost: 1.106765e-06 w: [1.0012219] b: [-0.00277757]
'''



#H(x) = Wx + b
x = tf.placeholder(tf.float32, shape=[None])
y = tf.placeholder(tf.float32, shape=[None])
w = tf.Variable(tf.random_normal([1]), name='weight')
b = tf.Variable(tf.random_normal([1]), name='bias')
hypothesis = x * w + b

#Cost(W,b)=∑...
cost = tf.reduce_mean(tf.square(hypothesis - y))

#Gradient Descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

for step in range(2001):
  cost_val, w_val, b_val, _ = sess.run([cost, w, b, train],
      feed_dict={x: [2, 2.1, 2.2], y: [11, 12, 13]})
  if step % 20 == 0:
    print("step:", step, "cost:", cost_val, "w:", w_val, "b:", b_val)

#11.97 = 2.1 * 4.7 + 2.1
#y = x * w + b
'''
step: 1920 cost: 0.15351407 w: [5.20387] b: [1.0842893]
step: 1940 cost: 0.15336299 w: [5.2062306] b: [1.0793244]
step: 1960 cost: 0.153212 w: [5.20859] b: [1.0743623]
step: 1980 cost: 0.15306108 w: [5.210948] b: [1.0694033]
step: 2000 cost: 0.15291019 w: [5.2133045] b: [1.0644472]
'''
