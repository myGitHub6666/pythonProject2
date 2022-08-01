import sys
# script, encoding, error = sys.argv


def my_print(line, my_encoding, *args, **kwargs):
    # args = ["fdsf", "badf", "ew"]
    # kargs = {"test_key": 1, "ker2": 2}
    if 'test_key' in kwargs.keys():
        print(kwargs['test_key'])

    print(kwargs)
    if 'key2' in kwargs.keys():
        print(kwargs["key2"])


def test():
    my_print(line=1, my_encoding="utf-8", test_key="new_key", key2='key2222222')


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding=encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)




# languages = open("languages.txt", encoding = "utf-8")

# main(languages, encoding, error)
test()