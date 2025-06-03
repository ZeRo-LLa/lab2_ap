import random

def generate_custom_input(
    filename='lab7/input.txt',
    haystack_size=100_000,
    needle='privit',
    insert_every=5000
):
    
    open(filename, 'w').close()
    words = ["hello", "privit", "python", "search", "index", "value", "data", "result", "code", "function"]
    
    haystack = []
    chars_written = 0

    while chars_written < haystack_size:
        if chars_written % insert_every < len(needle) and chars_written + len(needle) < haystack_size:
            haystack.append(needle)
            chars_written += len(needle)
        else:
            word = random.choice(words)
            haystack.append(word)
            chars_written += len(word)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(''.join(haystack) + '\n')
        f.write(needle + '\n')

    print(f"Файл {filename} створено. Розмір тексту: {chars_written} символів.")

generate_custom_input()
