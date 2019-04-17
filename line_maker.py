import random
import csv
from file_read import Parser

### change the name of the categories file here if needed ###
edit_file = 'cat_file.txt'




class LineMaker(object):

# initialize
    def __init__(self):
        self.categories=Parser().run(edit_file)

# take in two lists, cartesian product, return tuple
    def combo_maker(self, l1, l2):
        loop_list = []
        for first in l1:
            if len(l2) == 0:
                loop_list.append(first)
                continue
            for second in l2:
                if type(second) is tuple:
                    a = first,
                    loop_list.append(second + a)
                else:
                    a = second,first
                    loop_list.append(a)
        return loop_list

# loop with combo_maker to return all combinations as list of tuples
    def dict_parse(self, dict):
        combos = []
        for val_list in dict.values():
            combos = self.combo_maker(val_list, combos)
        return combos

# make a random price per item for each combination
    def price_maker(self, combos_list, run_time):
        w_lines = []
        t_line = []
        for combo in combos_list:
            unit_retail = random.randint(500,1000)
            unit_cost = random.randint(100,unit_retail)/100.0
            unit_retail = unit_retail/100.0
            t_cursor = 1
            while t_cursor <= run_time:
                units_sold = random.randint(5,10000)
                units_returned = random.randint(0,units_sold)
                income = round((unit_retail * units_sold),2)
                returned = round((unit_retail * units_returned),2)
                t_tup = t_cursor,unit_retail,unit_cost,units_sold,units_returned,income,returned
                t_line = combo + t_tup
                w_lines.append(t_line)
                t_cursor += 1
        return w_lines

# write file lines
    def file_write(self, run_time, w_file_name):
        # run combo_maker and price_maker
        combos_list = self.dict_parse(self.categories)
        w_lines = self.price_maker(combos_list, run_time)
        # make header line using categories specified
        h_line = []
        for key in self.categories.keys():
            h_line.append(key)
        quantify = 'time','unit_retail','unit_cost','units_sold','units_returned','income_$','return_$'
        h_line = tuple(h_line) + quantify
        w_lines = [h_line] + w_lines
        w_file_name = w_file_name
        with open(w_file_name, mode='w') as w_csv:
            writer = csv.writer(w_csv, delimiter=',', quoting=csv.QUOTE_NONE)
            for l in w_lines:
                writer.writerow(l)
