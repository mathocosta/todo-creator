#!/usr/bin/env python3
# TODO: Colocar pra salvar os todos no Desktop
# Command line tool for creating TODOs
#
# usage: todo.py [-h] [-m] [-p {1,2,3}] title
#
# positional arguments:
#   title                 Title of todo.
#
# optional arguments:
#   -h, --help            show this help message and exit
#   -m, --message         Open editor to write the description of todo.
#   -p {1,2,3}, --priority {1,2,3}
#                         Sets an priority to todo, 1 for high, 2 for medium, 3
#                         for normal.

import argparse
import os

from codecs import open
from time import strftime

parser = argparse.ArgumentParser()

parser.add_argument("title", help="Title of todo.")
parser.add_argument("-m", "--message", action="store_true", help="Open editor to write the description of todo.")
parser.add_argument("-p", "--priority", default=3, type=int, choices=[1, 2, 3], help="Sets an priority to todo, 1 for high, 2 for medium, 3 for normal.")

args = parser.parse_args()

priority_classes = ("HIGH", "MEDIUM", "NORMAL")
body_template = """
Title: {0}
Priority: {1}
Created: {2}
- - -
    {3}
"""

current_time = strftime("%d.%m.%Y")
desktop_path = os.path.join(os.environ["USERPROFILE"], "Desktop")
filename = os.path.join(desktop_path, args.title.replace(" ", "_") + ".txt")

with open(filename, mode="w", encoding="utf-8") as file:
    if args.message:
        body = input("Body Text: ")
        file.write(body_template.format(
                args.title, priority_classes[args.priority - 1],
                current_time,
                body
            ))

    file.close()