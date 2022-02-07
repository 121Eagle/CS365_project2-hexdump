from argparse import ArgumentParser


def main():
    args = ArgumentParser(
            discription="display file contents in headecimal and ascii"
            )

    args.add_argument(
            "file",
            type=str,
            help="a file that is parsed by the system"
            )


if __name__ == "__main__":
    main()
