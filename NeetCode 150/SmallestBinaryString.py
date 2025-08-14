def smallest_binary_string(dataSequence: str, maxSwaps: int) -> str:
    """
    Given:
        dataSequence : A binary string (only '0' and '1').
        maxSwaps     : Maximum number of adjacent swaps allowed.

    Goal:
        Return the lexicographically smallest string achievable
        by performing at most `maxSwaps` adjacent swaps.

    Approach:
        - The smallest binary string is achieved by moving '0's as far left as possible.
        - For each '0' in the string, swap it left past any '1's until:
            * We run out of allowed swaps, or
            * There are no more '1's immediately to the left.
        - Continue this process left-to-right until swaps are exhausted.
    """

    # Convert string to a list for easier swapping
    data = list(dataSequence)
    n = len(data)

    # Loop through each character in the string
    for i in range(n):
        if data[i] == '0':
            # This '0' can potentially be moved left to get a smaller string
            j = i  # current position of this '0'

            # Keep swapping left while:
            # - We aren't at the start of the string
            # - We still have swaps left
            # - The character to the left is '1' (since swapping with '0' doesn't help)
            while j > 0 and maxSwaps > 0 and data[j - 1] == '1':
                # Swap this '0' with the '1' to its left
                data[j], data[j - 1] = data[j - 1], data[j]

                # Move the index leftward
                j -= 1

                # One swap used
                maxSwaps -= 1

    # Join list back into a string for the result
    return ''.join(data)
