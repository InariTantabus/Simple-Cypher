import sys, os, random

to_trans = "if you can read this youre insane" # Phrase to translate
c_base = 10 # Base to set to. 0 means translate from cypher to english. Base has to be an int and can't be higher than 10 or lower than 0.
char_edge = "!" # First cypher letter to allow. '|' is always included. Larger bases require character to be closer to the start of cypher_letters.

base_letters = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cypher_letters = ['|', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')']

def numberToBase(num, base): # I did not write this
    if num == 0:
        return [0]
    digits = []
    while num:
        digits.append(int(num % base))
        num //= base
    return digits[::-1] # [::-1] reverses the order of the list

def baseListToNumber(num):
    output = 0
    for i, v in enumerate(num):
        if v == 10:
            pass
        else:
            output += v*(10**(len(num)-i-1))
    return output

def baseListToNumber2(num): # I did not write this
    strings = [str(integer) for integer in num]
    a_string = "".join(strings)
    an_integer = int(a_string)
    
    return an_integer

def translate(to_trans, c_base, char_edge='!'):
    if to_trans:
        if c_base == 0: # I don't want to work on this yet
            temp_base = []
            temp_base.append(to_trans[1:to_trans.index(' ')])
            temp_num_base = []
            for i in temp_base[0]:
                temp_num_base.append(cypher_letters.index(i))
            c_base = baseListToNumber(temp_num_base)
            
            to_trans = to_trans[to_trans.index(' ')+1:]
            char_edge = to_trans[0]
            to_trans = to_trans[to_trans.index(' | ')+3:]
            temp_string = to_trans[:to_trans.index(' ')]
            
            cypher_letters_to_use = []
            for i, v in enumerate(cypher_letters):
                if i > c_base + cypher_letters.index(char_edge) - 1:
                    break
                if i >= cypher_letters.index(char_edge):
                    cypher_letters_to_use.append(v)
            cypher_letters_to_use.insert(0, cypher_letters_to_use[-1])
            cypher_letters_to_use.pop(-1)
            
            output_list = []
            while to_trans:
                temp_list = []
                for i in temp_string:
                    temp_list.append(cypher_letters_to_use.index(i))
                temp_num = baseListToNumber2(temp_list)
                output_list.append(int(str(temp_num), c_base))
                if ' | ' in to_trans:
                    if to_trans.index(' | ') == to_trans.index(' '):
                        to_trans = to_trans[to_trans.index(' | ')+3:]
                        temp_string = to_trans[:to_trans.index(' ')]
                        output_list.append(0)
                    else:
                        to_trans = to_trans[to_trans.index(' ')+1:]
                        temp_string = to_trans[:to_trans.index(' ')]
                elif ' ' in to_trans:
                    to_trans = to_trans[to_trans.index(' ')+1:]
                    if ' ' in to_trans:
                        temp_string = to_trans[:to_trans.index(' ')]
                    else:
                        temp_string = to_trans[:-1]
                else: 
                    break
            
            output = ''
            for i in output_list:
                output += base_letters[i]
            
            return output
        
        elif c_base % 1 == 0 and c_base >= 1 and c_base <=10: # Checking if c_base is a valid input
            temp_list = []
            for i in to_trans:
                if i in base_letters:
                    temp_list.append(base_letters.index(i))
            temp_based_list = []
            for i in temp_list:
                temp_based_list.append(numberToBase(i, c_base))
                
            cypher_letters_to_use = []
            for i, v in enumerate(cypher_letters):
                if i > c_base + cypher_letters.index(char_edge) - 1:
                    break
                if i >= cypher_letters.index(char_edge):
                    cypher_letters_to_use.append(v)
            cypher_letters_to_use.insert(0, cypher_letters_to_use[-1])
            cypher_letters_to_use.pop(-1)
                
            output = '-'
            based_base = numberToBase(c_base, 10)
            for i, v in enumerate(based_base):
                if v == 0:
                    output += ')'
                else:
                    output += '{}'.format(cypher_letters[v])
            output += ' {} | '.format(char_edge)
                    
            for i in temp_based_list:
                if i == [0]:
                    output += '|'
                else:
                    for v in i:
                        output += cypher_letters_to_use[v]
                output += ' '
            output = output[:-1] + '-'
                
            return output

print(translate(to_trans, c_base, char_edge))