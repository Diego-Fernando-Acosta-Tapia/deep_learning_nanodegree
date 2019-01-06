{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "version": "0.3.2",
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "metadata": {
        "id": "pq0dguu5a6kj",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "outputId": "f522518d-38f0-4157-8626-31ae3d4454de"
      },
      "cell_type": "code",
      "source": [
        "\"\"\"\n",
        "Set the values to `strides` and `ksize` such that\n",
        "the output shape after pooling is (1, 2, 2, 1).\n",
        "\"\"\"\n",
        "import tensorflow as tf\n",
        "import numpy as np\n",
        "\n",
        "# `tf.nn.max_pool` requires the input be 4D (batch_size, height, width, depth)\n",
        "# (1, 4, 4, 1)\n",
        "x = np.array([\n",
        "    [0, 1, 0.5, 10],\n",
        "    [2, 2.5, 1, -8],\n",
        "    [4, 0, 5, 6],\n",
        "    [15, 1, 2, 3]], dtype=np.float32).reshape((1, 4, 4, 1))\n",
        "X = tf.constant(x)\n",
        "\n",
        "def maxpool(input):\n",
        "    # TODO: Set the ksize (filter size) for each dimension (batch_size, height, width, depth)\n",
        "    ksize = [1, 4, 4, 1]\n",
        "    # TODO: Set the stride for each dimension (batch_size, height, width, depth)\n",
        "    strides = [1, 2, 2, 1]\n",
        "    # TODO: set the padding, either 'VALID' or 'SAME'.\n",
        "    padding = \"SAME\"\n",
        "    # https://www.tensorflow.org/versions/r0.11/api_docs/python/nn.html#max_pool\n",
        "    return tf.nn.max_pool(input, ksize, strides, padding)\n",
        "    \n",
        "out = maxpool(X)\n",
        "print(out)"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Tensor(\"MaxPool_11:0\", shape=(1, 1, 1, 1), dtype=float32)\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}