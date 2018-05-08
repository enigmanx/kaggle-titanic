import tensorflow as tf
from dataset import Dataset


input_ = tf.placeholder(shape=[None, 3], dtype=tf.float32)
output_ = tf.placeholder(shape=[None, 1], dtype=tf.float32)
ds = Dataset()

