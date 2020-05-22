#!/usr/bin/python3
import argparse
from components import core

from functools import partial

parser = argparse.ArgumentParser(
    description="A multi-workflow YouTube downloader")

modes = parser.add_mutually_exclusive_group()
modes.add_argument("-c", "--core", type=str, nargs="*",
                   help="traditional one-shot getter. Provide a searchstring or youtube URL to download")
modes.add_argument("-i", "--interactive",
                   action="store_true", help="interactive getter")
modes.add_argument("-v", "--visual", action="store_true", help="visual getter")
modes.add_argument("-hot", "--hotkey",
                   action="store_true", help="getter hotkey mode")

parser.add_argument("-d", "--dest", type=str,
                    help="determine the final output destination")
parser.add_argument("-f", "--format", type=str,
                    help="determine the output format")
parser.add_argument("--shutdown", action="store_true",
                    help="shutdown the system after downloads are complete. only supported in core right now")
# parser.add_argument("-s", "--spleet", type=str, nargs="*",
#                     help="spleet the downloaded file into stems. Currently not implemented.")

args = parser.parse_args()

if args.core:
  searchString = core.getArgs(args.core)
  core.main(searchString=searchString, format=args.format,
            dest=args.dest, shutdown=args.shutdown)

elif args.visual:
  from components import visual
  fun = visual.main
  if args.dest:
    fun = partial(fun, destination=args.dest)
  fun()

elif args.interactive:
  from components import interactive
  interactive.main(format=args.format, dest=args.dest)

elif args.hotkey:
  from components import hotkey
  hotkey.main(format=args.format, destination=args.dest)

else:
  parser.print_help()
