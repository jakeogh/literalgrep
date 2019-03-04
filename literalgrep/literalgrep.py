#!/usr/bin/env python3
import sys
import ast
import click

@click.command()
@click.argument('match')
@click.option('--verbose', is_flag=True)
def literalgrep(match, verbose):
    match = ast.literal_eval('b"""' + match + '"""')
    assert isinstance(match, bytes)
    if verbose: print("match:", match, file=sys.stderr)
    found = False
    for line in sys.stdin.buffer.read().split(b'\n')[:-1]:
        if verbose: print("line:", line, file=sys.stderr)
        if match in line:
            found = True
            sys.stdout.buffer.write(line + b'\n')
        if found:
            quit(0)
        quit(1)

if __name__ == '__main__':
    literalgrep()

