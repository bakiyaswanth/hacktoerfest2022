string = input('Enter a string')
index = int(input('Enter the index to remove the character'))
def remove_at(string,index):
    before = string[: index :]
    after = string[index+1: :]
    return before+after
print(remove_at(string,index))
