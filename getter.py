import argparse
import core
import visual
import interactive

parser = argparse.ArgumentParser(
    description="A multi-workflow YouTube downloader")
modes = parser.add_mutually_exclusive_group()
modes.add_argument("-c", "--core", action="store_true",
                   help="traditional one-shot getter")
modes.add_argument("-i", "--interactive",
                   action="store_true", help="interactive getter")
modes.add_argument("-v", "--visual", action="store_true", help="visual getter")
parser.add_argument("-l", "--location", action="store_true",
                    help="determine the final output destination")
parser.add_argument("-f", "--format", action="store_true",
                    help="determine the output format")
parser.add_argument("-s", "--search", type=str,
                    help="the string to search or url to download from")
# parser.add_argument("-s", "--spleet", type=str, nargs="*",
#                     help="spleet the downloaded file into stems. Currently not implemented.")
args = parser.parse_args()

if args.core:
  # TODO: add format choosing
  if args.search == None:
    parser.error("--core requires --search not Null")
  core.main(searchString=args.searchString)

if args.visual:
  visual.main()

if args.interactive:
  interactive.main()