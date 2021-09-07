# Problem 9c
from lcs_dp import lcs_dp
from lcs_rec import lcs_rec
import time
import random
import json
import string


def writeToFile(arr, name):
    with open('{}.json'.format(name), 'w', encoding='utf-8') as f:
        json.dump(arr, f, indent=4)


if __name__ == '__main__':

    X = ""
    Y = ""
    i = 0
    rec_times = []
    dp_times = []

    # Length of X and Y is equal to i.
    while i < 32:
        chars = string.ascii_lowercase  # "ab"
        X += random.choice(chars)
        Y += random.choice(chars)
        t = time.process_time()
        print("Recursive LCS: ", lcs_rec(X, Y, len(X), len(Y)))
        time_rec = time.process_time() - t
        rec_times.append(time_rec)
        t = time.process_time()
        print("DP LCS: ", lcs_dp(X, Y))
        time_dp = time.process_time() - t
        dp_times.append(time_dp)
        print("Time recursive: {} \nTime DP: {}".format(time_rec, time_dp))
        print("{} Finished Round {} {}".format(5*"-", i+1, 5*"-"), "\n")
        i += 1

    writeToFile(rec_times, "Recursive_Times")
    writeToFile(dp_times, "DP_Times")

    """

    For strings consisting of two unique characters, the recursive algorithm seems to slow when the strings lengths are around 28 to 32. 
    For strings consisting of more than two unique characters, the recursive algorithm seems to slow when string length is around 13-15.

    The worst case time complexity of the recursive approach is O(2^n+m).
    This corresponds with my findings, as iterative rounds usually takes 4 times longer than the previous. 
    See the pictures in the repo for examples, or run this file with your own settings.

    """
