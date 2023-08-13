#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    len_s = len(sentence)
    f_char = None if len_s == 0 else sentence[0]
    return len_s, f_char


if __name__ == "__main__":
    sentence = "At school, I learnt C!"
    length, first = multiple_returns(None)
    print("Length: {:d} - First character: {}".format(length, first))
