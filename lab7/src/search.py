def compute_lps(pattern):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(haystack, needle):
    if not needle:
        return []

    lps = compute_lps(needle)
    result = []

    i = 0
    j = 0

    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == len(needle):
                result.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return result


def recipes_from_file(filename):
    recipes = {}
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            if ':' in line:
                parts = line.strip().split(':', 1)
                if len(parts) == 2:
                    key, value = parts
                    recipes[key.strip()] = value.strip()
    return recipes


recipes = recipes_from_file('lab7/src/recipes.txt')
inventory = input("Your inventory: ").strip()

craftable_items = []

for ingredients, item in recipes.items():
    if kmp_search(inventory, ingredients):
        craftable_items.append(item)

if craftable_items:
    print("Can create:")
    for item in craftable_items:
        print("-", item)
else:
    print("Nothing can be crafted.")
