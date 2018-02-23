class Values:
    def __init__(self, num_list = None):
        self.num_list = num_list
        self.difference()
        self.min_max()
        self.sum_list()
    
    def difference(self):
        from list_module.max_difference import max_difference
        self.max_diff = max_difference(self.num_list)
    
    def min_max(self):
        from list_module.min_max_list import min_max_list
        self.max_mi = min_max_list(self.num_list)
    
    def sum_list(self):
        from list_module.sum_list import (sum_list, EmptyError,
                                          DictionaryError)
        self.sum_l = sum_list(self.num_list)
