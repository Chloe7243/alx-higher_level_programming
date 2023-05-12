#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    len_args = len(sys.argv) - 1
    if len_args > 0:
        if len_args == 1:
            print("1 argument:")
        else:
            print(f"{len_args} arguments:")
            for i, arg in enumerate(sys.argv):
                if i == 0:
                    continue
                print(f"{i}: {arg}")
    else:
        print("0 arguments.")
