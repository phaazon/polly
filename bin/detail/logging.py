# Copyright (c) 2015, Ruslan Baratov
# All rights reserved.

import os

class Logging:
  def __init__(self, polly_temp_dir, verbose, discard):
    self.verbose = verbose
    self.discard = discard
    self.log_path = os.path.join(polly_temp_dir, 'log.txt')
    self.log_file = open(self.log_path, 'w')
