#PALIN- The Next Palindrome - aided by Editorial https://spojeditorials.wordpress.com/2016/09/22/palin-the-next-palindrome/
#Status: Works, but NZEC error- May need Big integer equivalent

"""
Finds the subsequent palindrome of a given number. Eg: 808 -> 818
1223 -> 2222

Problem: https://www.spoj.com/problems/PALIN/
"""
def reverse_string(inp):
    return "".join(list(reversed(inp)))


def up_palin_even(inp, half_string, back_half, midpt, val):
    second_half = reverse_string(half_string)

    while True:
        up_string = (reverse_string(second_half) + second_half)
        if int(up_string) > val:
            print(up_string)
            break

        if second_half[0] != '9':
            #print("here")
            second_half = str(int(int(second_half)+ (10**midpt)))
        else:
            for i in range(1, midpt+1):
                if second_half[i] == '9':
                    continue
                else:
                    second_half = str(int(int(second_half) + (10**(midpt-i))))


def up_palin_odd(inp, half_string, back_half, mid_digit, midpt, val):
    second_half = reverse_string(half_string)

    while True:
        up_string = (reverse_string(second_half) + mid_digit + second_half)
        if int(up_string) > val:
            print(up_string)
            break

        if mid_digit != '9':
            mid_digit = str(int(int(mid_digit) + 1))
        else:
            for i in range(1, midpt+1):
                if second_half[i] == '9':
                    continue
                else:
                    second_half = str(int(int(second_half) + (10**(midpt-i))))






def palin_even(inp, mag):
    val = int(inp)
    midpt = (mag/2) -1
    half_string = inp[0:int(midpt + 1)]
    back_half = inp[int(midpt+1):]
    #we now have mirrored the string across its center
    up_palin_even(inp, half_string, back_half, midpt, val)


def palin_odd(inp, mag):
    val = int(inp)
    midpt = int((mag/2) - 0.5)
    mid_digit = inp[int(midpt)]
    half_string = inp[0:int(midpt)]
    back_half = inp[int(midpt+1):]
    up_palin_odd(inp, half_string, back_half, mid_digit, midpt, val)




t = int(input())

q = 0
while q < t:
    q += 1
    current_inp = input()
    mag = len(current_inp)
    if mag%2 == 0:
        palin_even(current_inp, mag)
    else:
        palin_odd(current_inp, mag)
