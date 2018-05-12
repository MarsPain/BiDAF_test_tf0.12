# test1
# import tensorflow as tf
#
# # temp = tf.tile([1,2,3],[2])
# # temp2 = tf.tile([[1,2],[3,4],[5,6]],[2,3])
# #
# # with tf.Session() as sess:
# #     print(sess.run(temp))
# #     print(sess.run(temp2))
#
# t1 = [[[1, 2, 3], [1, 2, 3], [1, 2, 3]], [[4, 5, 6], [4, 5, 6], [4, 5, 6]]]
# t2 = [[[7, 8, 9], [7, 8, 9], [7, 8, 9]], [[10, 11, 12], [10, 11, 12], [10, 11, 12]]]
# xx = tf.concat(2, [t1, t2])
# with tf.Session() as sess:
#     print(sess.run(xx))

# test2
import tensorflow as tf

a = tf.random_normal((100, 100))
b = tf.random_normal((100, 500))
c = tf.matmul(a, b)
sess = tf.InteractiveSession()
sess.run(c)

# test3
# import tensorflow as tf
#
# with tf.device('gpu'):
#     a = tf.constant([1.0, 2.0, 3.0], shape=[3], name='a')
#     b = tf.constant([1.0, 2.0, 3.0], shape=[3], name='b')
# with tf.device('gpu'):
#     c = a + b
#
# # 注意：allow_soft_placement=True表明：计算设备可自行选择，如果没有这个参数，会报错。
# # 因为不是所有的操作都可以被放在GPU上，如果强行将无法放在GPU上的操作指定到GPU上，将会报错。
# sess = tf.Session(config=tf.ConfigProto(allow_soft_placement=True, log_device_placement=True))
# # sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# sess.run(tf.global_variables_initializer())
# print(sess.run(c))