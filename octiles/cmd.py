import sys
from octiles.commands import eq_command, dedup_command, help_command


def cmd():
    if len(sys.argv) < 2:
        help_command()
        return

    command = sys.argv[1]
    arguments = sys.argv[2:]
    match command:
        case 'eq': eq_command(*arguments)
        case 'dedup': dedup_command(*arguments)
        case _: help_command()
