
# ABOUT
**data-gen** is a Python3 application that generates random sales data over time for any size set of categories. It takes in a text file containing lists of the desired categories and category values, assigns a dollar amount for cost and retail, and outputs a csv file of the number of units sold and returned as well as the associated dollar value over time. The cost and retail amount remain the same over time while the units sold and returned vary.



# SET-UP & RUN
0. Make sure python3 is installed and up to date.
1. Download the repository into any directory.
2. Edit '*cat_file.txt*' as needed.
3. From the command-line, navigate to the directory and execute `python3 run.py`.
4. Enter the desired units of time and the output file name.
5. The output will be saved to the 'results' directory.

### Notes:
- There is no overwrite warning. Specifying an existing filename will replace it.
- Only integer values are allowed when specifying time.
- The length of the output file must be at least one character long.
- Dollar values per item will be between $5 and $100. Units sold and returned per time increment will be between 5 and 10,000. This can be changed in the price_maker method within



# EXAMPLE
'*example_data.csv*' shows the results for 10 units of time. 
[Link](https://github.com/eferrara3/data-gen/blob/master/results/example_data.csv)



# HOW IT WORKS
1. '*file_read.py*' uses `Parser()` to define the state for each line in '*cat_file.txt*' with `Enum`. It parses and cleans the lists and stores each list as an entry in a dictionary object using the asterisk line as the key.
2. '*line_maker.py*' initiates and instance of the `Parser()` class through `LineMaker()`. It iterates through each dictionary entry to assemble a tuple of the variable length cartesian product. The `random` module create the assigned static and variable values for each tuple. A file is written to the 'results' directory using the `csv` module.
3. '*run.py*' prompts for the time required and the desired output file name (with some exception handling), and then runs the `LineMaker()` method using those values.
