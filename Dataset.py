from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import gzip
import os

import numpy
from six.moves import urllib
from six.moves import xrange  # pylint: disable=redefined-builtin

class Dataset(object):
  def __init__(self, images, labels):
#    assert images.shape[0] == labels.shape[0],(
#      'images.shape: %s labels.shape:%s' % (image.shape, labels.shape))
   
    self._num_examples = images.shape[0]
    self._images = images
    self._labels = labels
    self._epochs_completed = 0
    self._index_in_epoch = 0
 
  @property
  def images(self):
    return self._images
 
  @property
  def labels(self):
    return self._labels

  @property
  def num_examples(self):
    return self._num_examples

  @property
  def epochs_completed(self):
    return self._epochs_completed

  def next_batch(self, batch_size):
    """Return the next `batch_size` examples from this dataset."""
    start = self._index_in_epoch
    self._index_in_epoch += batch_size
    if self._index_in_epoch > self._num_examples:
      self._epochs_completed += 1
      perm = np.arange(self._num_examples)  
      np.random.shuffle(perm)
      self._images = self._images[perm]
      self._labels = self._labels[perm]
      start = 0
      self._index_in_epoch = batch_size 
      assert batch_size <= self._num_examples
    end = self._index_in_epoch
    return self._images[start:end], self._labels[start:end]


