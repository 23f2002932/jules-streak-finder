from typing import List

def longest_positive_streak(nums: List[int]) -> int:
    """
    Calculates the length of the longest run of consecutive values
    strictly greater than 0.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest positive streak.
    """
    max_streak = 0
    current_streak = 0

    for num in nums:
        if num > 0:
            # If the number is positive, extend the current streak
            current_streak += 1
        else:
            # If the number is zero or negative, the streak is broken
            # Update the max streak if the current one was longer
            max_streak = max(max_streak, current_streak)
            # Reset the current streak counter
            current_streak = 0

    # Final check after the loop finishes to account for a streak at the end
    max_streak = max(max_streak, current_streak)

    return max_streak
