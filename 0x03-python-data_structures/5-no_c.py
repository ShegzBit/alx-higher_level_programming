#!/usr/bin/python3
def no_c(my_string):
    if my_string is None:
        return None
    my_string = "".join([x for x in my_string if (not (x in "cC"))])
    return my_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
    print(no_c(None))
