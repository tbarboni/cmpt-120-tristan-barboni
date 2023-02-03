from datetime import datetime # import your libraries here.
log_file = str("log-file-" + datetime.today().strftime('%Y-%m-%d')+".log") # the name of the log file to write to.


def log(text, log_file=log_file):
    log_file = open(log_file, "a")  # open up the log file in the correct mode.
    # create a string that has the current date and time in the beginning of the text.
    log_file.write(datetime.today().strftime('%Y-%m-%d %H:%M:%S ') + text + "\n")# Ensure the string ends with a new line character.
    # append the text to the end of the file.
    log_file.close()  # close the file.
    return None


def dump(log_file=log_file):
    '''
    This function prints out each line in the log file to the console
    '''
    log_file = open(log_file, "r")  # open up the log file in the correct mode.
    file_list = [] #List for file to be iterated in.
    log_file.read(file_list=log_file)  # read the file into a list.
    for n in file_list: # iterate through each item in the list and print out the results.
        print(n)
    log_file.close()# close the file.
    return None
