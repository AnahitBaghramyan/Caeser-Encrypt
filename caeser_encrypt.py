# function that reads from file with the given path and returns all the text
def read_from_file(source_path: str):
    with open(source_path, mode='r') as tx:
        while (line := tx.read()):
            return line


# function that creates a file and writes in that file the given text
def write_to_file(dest_path: str, line: str):
    with open(dest_path, mode='x+') as dest:
        dest.write(line)


# function that encrypts the given text
# (only changes the letters and leaves the numbers and symbols same)
# also keeps the spaces and tabs in the same places and quantities
def encrypt(initial_text, shift: int):
    if isinstance(shift, int):
        result = ""
        for i in range(len(initial_text)):
            char = initial_text[i]
            if char.isalpha():
                if (char.isupper()):
                    result += chr((ord(char) + int(shift) - 65) % 26 + 65)
                else:
                    result += chr((ord(char) + int(shift) - 97) % 26 + 97)
            else:
                result += char
        return result
    else:
        print('Please insert a value only containing 0-9')

# function that calls all previous functions with checking some conditions


def caeser_encrypt(source: str, dest: str, shift: int):
    encrypted_code = ''
    scanned_text = ''
    # this validation is done for checking the given path of the source path
    # if it is right it reads from that file,
    # saves the text in the variable scanned_text
    # then calls the encrypt function
    # as an argument takes encrypted_code variable
    # and saves the encrypted text in variable encrypted_code
    # if the path isn't true prints message for user
    try:
        scanned_text = read_from_file(source)
        encrypted_code = encrypt(scanned_text, shift)
    except FileNotFoundError:
        print("Enter a valid source path")
    # this condition at first checks if the there is an ecrypted code
    # if there is it checks whether there exists any file with that given path
    # if there exists if handles an error and sends message to user
    # if there doesn't exist any file it calls write_to_file functions
    # which creates and writes the given text in destination file
    if encrypted_code:
        try:
            write_to_file(dest, encrypted_code)
        except FileExistsError:
            print('File already exists.  Clean up!')
    else:
        return


if __name__ == '__main__':
    caeser_encrypt()
