def sliding_window(arr):
    n = len(arr)
    l = 0  # left pointer
    result = 0  # or float('-inf'), '', [], depending on the problem

    # Optional: data structure to track state in the window
    window = {}

    for r in range(n):  # right pointer
        # 1. Expand: add arr[r] to window
        # Update window state here (e.g., count freq, sum, set)
        # Example: window[arr[r]] = window.get(arr[r], 0) + 1

        # 2. While the window violates condition — shrink from the left
        while condition_not_satisfied(window):
            # Remove arr[l] from window
            # Example: window[arr[l]] -= 1
            # if window[arr[l]] == 0: del window[arr[l]]
            l += 1

        # 3. Update result if needed
        result = max(result, r - l + 1)  # or sum, min, etc.

    return result
