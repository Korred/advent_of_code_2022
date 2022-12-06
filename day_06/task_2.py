signal = list(open("input.txt", "r").read().strip())
window_size = 14

# sliding window approach
for i in range(len(signal) - window_size + 1):
    if len(set(signal[i : i + window_size])) == window_size:
        print(f"First start-of-message marker after: {i + window_size} characters")
        break
