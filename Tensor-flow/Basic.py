#Multiplies matrix a by matrix b, producing a * b.

#The inputs must, following any transpositions, be tensors of rank >= 2 where the inner 2 dimensions specify valid matrix multiplication arguments, and any further outer dimensions match.

#Both matrices must be of the same type. The supported types are: float16, float32, float64, int32, complex64, complex128.

from __future__ import print_function
import tensorflow as tf

a = tf.constant(2)
b = tf.constant(3)

with tf.Session() as sess:
    print("a=2, b=3")
    print("Addition with constants: " % sess.run(a+b))

# 2-D tensor `a`
a = tf.constant([1, 7, 2, 3, 4, 5, 6], shape=[4, 2, 2, 3])


with tf.Session() as sess:
    result = sess.run(a)
    print(result)
    # ==> [[ 12.]]