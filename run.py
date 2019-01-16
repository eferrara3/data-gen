from line_maker import LineMaker




while True:
    try:
        time = int(input('enter time to simulate (integer value):'))
        break
    except:
        print('')
        print('******')
        print('error:')
        print('you must enter a valid integer for time.')
        print('')
        print('******')
    else:
        continue


def fails(to_file):
    if len(to_file) > 0:
        return False
    else:
        return True


to_file = input('enter desired output file name:')
while fails(to_file) is True:
    print('')
    print('******')
    print('error:')
    print('you must enter a valid file name.')
    print('')
    print('******')
    to_file = input('enter desired output file name:')


to_file_nm = 'results/' + to_file + '.csv'
print('')
print('')
print('running ...')
LineMaker().file_write(time, to_file_nm)


print('')
print(f'data-gen complete! check {to_file_nm} in the data-gen folder for result.')
