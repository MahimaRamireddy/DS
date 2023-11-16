input_strings = ["iiitdm-kancheepuram", "iiitdm-cse-dept", "iiitdm-ece-dept", "iiitdm-me-dept"]

def longest_common_prefix(strings):
    if not strings:
        return ""

    min_length = min(len(s) for s in strings)
    common_prefix = ""

    for i in range(min_length):
        current_char = strings[0][i]
        if all(s[i] == current_char for s in strings):
            common_prefix += current_char
        else:
            break

    return common_prefix

result = longest_common_prefix(input_strings)
print(result)