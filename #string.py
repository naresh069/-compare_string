def compare_strings(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    common_letters = set(str1) & set(str2)
    count = sum(min(str1.count(letter), str2.count(letter)) for letter in common_letters)

    return count

str1, str2 = input().split()
result = compare_strings(str1, str2)
print(result)