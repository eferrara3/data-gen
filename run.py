from line_maker import LineMaker
from time import sleep
from sys import exit



class Runner(object):

# request and store run time
    def ask_for_time(self):
        while True:
            try:
                self.run_time=int(input('enter time to simulate (integer value):'))
                break
            except:
                print('')
                print('******')
                print('error:')
                print('you must enter a valid integer for time.')
                print('')
                print('******')
            else:
                return self.run_time
                continue
        return self.run_time

# error catch for blank write file name
    def fails(self, to_file):
        if len(self.to_file) > 0:
            return False
        else:
            return True

# request and store write file name
    def ask_for_file(self):
        self.to_file = input('enter desired output file name:')
        while self.fails(self.to_file) is True:
            print('')
            print('******')
            print('error:')
            print('you must enter a valid file name.')
            print('')
            print('******')
            self.to_file = input('enter desired output file name:')
        return self.to_file

# print messages, run LineMaker
    def message_and_run(self):
        self.run_time = self.ask_for_time()
        self.to_file = self.ask_for_file()
        self.to_file_nm = 'results/' + self.to_file + '.csv'

        print('')
        print('')
        print('running ...')
        sleep(1)

        while True:
            try:
                LineMaker().file_write(self.run_time, self.to_file_nm)
                break
            except:
                print('')
                print('******')
                print('an error occured. please check the files and try again.')
                exit()

        print('')
        print(f'data-gen complete! check {self.to_file_nm} in the data-gen folder for result.')


Runner().message_and_run()
