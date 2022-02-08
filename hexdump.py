from argparse import ArgumentParser
from io import BufferedReader
from itertools import count


def main():
    args = ArgumentParser(
            description="display file contents in headecimal and ascii"
            )

    args.add_argument(
            "file",
            type=str,
            help="a file that is parsed by the system"
            )

    hexdump(args.parse_args().file)


def hexdump(filename: str) -> None:
    """
    Function takes in a filename and then proceeds
    to open it and begin the act of dumping the hex
    ----
    Input: filename of file to be dumped
    ----
    Output: Null
    """
    with open(filename, 'rb') as f:
        _parse_file(f)
    return None


def _parse_file(Data: BufferedReader) -> None:
    """
    parses the data of the file for as long as there is data
    to parse
    """
    totalLen = 0
    while True:
        x = Data.read(16)
        if x == b"":
            break
        print(f"{totalLen:08x} {hex_format(x)} {string_processing(x)}")
        totalLen += len(x)
    print(f"{totalLen:08x}")


def hex_format(Data: bytes) -> str:
    return f" {Data[:8].hex(' ', 1)}  {Data[8:].hex(' ', -1)} "


UNPRINTABLE_BYTES = bytearray(range(0, 32)) + bytes(range(127, 256))

TRANSFORMATION_TABLE = bytes.maketrans(
        UNPRINTABLE_BYTES,
        b"." * len(UNPRINTABLE_BYTES)
        )


def string_processing(Data: bytes) -> str:
    """
    Returns a string value that is what the bytes are as interpreted
    as a string
    """
    processed_string = Data.translate(
            TRANSFORMATION_TABLE
            ).decode(encoding="ascii")
    return f" |{processed_string}|"


def _format_text_portion(data: bytes) -> str:
    pass


if __name__ == "__main__":
    main()
