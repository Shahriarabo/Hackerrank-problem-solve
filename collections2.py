from collections import defaultdict

# Read input
n, m = map(int, input().split())
group_a = defaultdict(list)

# Populate group A
for i in range(n):
    word = input()
    group_a[word].append(i + 1)  # Adding 1 to index to match 1-based indexing

# Process group B
for _ in range(m):
    word = input()
    if word in group_a:
        print(" ".join(map(str, group_a[word])))
    else:
        print("-1")
