def rev_string(astring):
    """Return reverse of string.

    You may NOT use the reversed() function!
    """

    # START SOLUTION

    out = ""

    for i in range((len(astring) - 1), -1, -1):
        out += astring[i]

    return out


print rev_string("apple")