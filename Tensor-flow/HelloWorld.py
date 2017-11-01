import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')

tf.contrib.data.Dataset.from_tensor_slices
dataset1 = tf.contrib.data.Dataset.from_tensor_slices(tf.random_uniform([4, 20]))
print(dataset1.output_types)  # ==> "tf.float32"
print(dataset1.output_shapes)  # ==> "(10,)"

sess = tf.Session()
print(sess.run(hello))