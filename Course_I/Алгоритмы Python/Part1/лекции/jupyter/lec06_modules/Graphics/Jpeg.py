import sys


def g_load(file):
    print("file {} loaded as JPEG".format(file))
    return None


if __name__ == "__main__":
    print("Test  Jpeg.py")
    print("Command line arguments: ", sys.argv)
    print(g_load("test.jpeg"))
