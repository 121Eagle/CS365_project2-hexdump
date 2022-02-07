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
    pass


if __name__ == "__main__":
    main()
