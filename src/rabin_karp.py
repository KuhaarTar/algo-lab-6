
def rabin_karp_matcher(haystack: str, needle: str) -> list:
    """
    Implemented rabin-karp algorithm function
    :param haystack: Input text
    :param needle: searching string
    :return: Array of occurrence indexes needle in haystack
    """
    base = 256
    prime = 101
    text_length = len(haystack)
    pattern_length = len(needle)
    hash_ = pow(base, pattern_length - 1) % prime
    pattern_hash = 0
    text_hash = 0
    result = []

    for i in range(pattern_length):
        pattern_hash = (base * pattern_hash + ord(needle[i])) % prime
        text_hash = (base * text_hash + ord(haystack[i])) % prime

    for start_index in range(text_length - pattern_length + 1):
        if pattern_hash == text_hash:
            match = True
            for i in range(pattern_length):
                if needle[i] != haystack[start_index + i]:
                    match = False
                    break
            if match:
                result.append(start_index)

        if start_index < text_length - pattern_length:
            text_hash = (text_hash - hash_ * ord(haystack[start_index])) % prime
            text_hash = (
                                text_hash * base + ord(haystack[start_index + pattern_length])
                        ) % prime
            text_hash = (text_hash + prime) % prime

    return result
