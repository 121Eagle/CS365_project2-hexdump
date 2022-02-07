from argparse import ArgumentParser


def main():
    args = ArgumentParser(
            description="display file contents in headecimal and ascii"
            )

    args.add_argument(
            "file",
            type=str,
            help="a file that is parsed by the system"
            )

    open_file_and_parse(args.parse_args().file)


def open_file_and_parse(filename: str) -> None:
    """
    Function takes in a filename and then proceeds
    to open it and begin the act of dumping the hex
    ----
    Input: filename of file to be dumped
    ----
    Output: Null
    """
    with open(filename, 'rb') as f:
        pass
    return None


def _parse_file(Data: file) -> None:
    """
    parses the data of the file for as long as there is data
    to parse
    """
    pass


def _format_text_portion(data: bytes) -> str:
    pass


if __name__ == "__main__":
    main()
