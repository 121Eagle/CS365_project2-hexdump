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
    for bytes_counted in count(step=16):
        byte_values = data.read(16)


def string_processing(Data: bytes) -> str:
    """
    Returns a string value that is what the bytes are as interpreted
    as a string
    """
    pass


def hexdata_print(data: bytes) -> list[int]:

    return [int(byte, base=16) for byte in data]


def _format_text_portion(data: bytes) -> str:
    pass


if __name__ == "__main__":
    main()
