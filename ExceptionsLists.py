'''
    Given a list of 10 names, complete the program that outputs the name specified by
    the list index entered by the user. Use a try block to output the name and an
    except block to catch any IndexError. Output the message from the exception object
    if an IndexError is caught. Output the first element in the list if the invalid
    index is negative or the last element if the invalid index is positive.

    Note: Python allows using a negative index to access a list, as long as the magnitude of
    the index is smaller than the size of the list.

    Ex: If the input of the program is:
        5
    the program outputs:
        Name: Jane

    Ex: If the input of the program is:
        12
    the program outputs:
        Exception! list index out of range
        The closest name is: Johnny

    Ex: If the input of the program is:
        -2
    the program outputs:
        Name: Tyrese

    Ex: If the input of the program is:
        -15
    the program outputs:
        Exception! list index out of range
        The closest name is: Ryley
'''

names = ['Ryley', 'Edan', 'Reagan', 'Henry', 'Caius', 'Jane', 'Guto', 'Sonya', 'Tyrese', 'Johnny']
index = int(input())

try:
    print(names[index])

except IndexError:
    print('Exception! list index out of range')
    if index > len(names) - 1:
        print('The closes name is:', names[-1])
    elif index < len(names):
        print('The closes name is:', names[0])
