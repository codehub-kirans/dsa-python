##################################################################
##
##                       DOCUMENTATION
##
##################################################################
#
#
# @file	validateSubsequence.py
# @version	1
# @author	Kiran S | R&D Manager
# @short	validateSubsequence implementation
# validateSubsequence implementation
#
# <p>
# See GIT for detailed history.
# <p>
# Copyright (c) 2022 Kiran S. All rights reserved.
#
##################################################################

def validateSubsequence(array,sequence):
    seqIdx = 0
    for i in range (len(array)):
        if seqIdx == len(sequence):
            return True
        if array[i] == sequence[seqIdx]:
            seqIdx += 1

    return seqIdx == len(sequence)

print ("Found Subsequence") if (validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10])) else print("Not Found Subsequence")


