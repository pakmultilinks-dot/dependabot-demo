"""Tiny sample app for the Dependabot demo. Its dependencies are pinned to
deliberately old versions so Dependabot has real updates to propose."""
import requests
from dateutil import parser as date_parser


def main():
    print("requests version:", requests.__version__)
    print("parsed:", date_parser.parse("2026-10-23").date())


if __name__ == "__main__":
    main()
