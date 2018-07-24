import argparse
import time
from .new_note import new_note
from .add_link import add_link

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-nf', '--new_file', help=' Create a note file.', action='store_true')
    parser.add_argument('-al', '--add_link', help=' Add a new link.', action='store_true')
    parser.add_argument('-at', '--add_tag', help='Add a new tag.', action='store_true')
    parser.add_argument('-r', '--read', help='Read note file and show.', action='store_true')
    parser.add_argument('-l', '--links', help='Get all links and show.', action='store_true')
    parser.add_argument('-t', '--tags', help='Get all tags and show.', action='store_true')
    args = parser.parse_args()

    file_name = time.strftime('%d-%m-%Y')

    # -nf, --new_file
    if args.new_file: new_note(file_name)

    # -al, --add_link
    elif args.add_link: add_link(file_name)

    # -at, --add_tag
    elif args.add_tag: pass

    # -r, --read
    elif args.read: pass

    # -l, --links
    elif args.links: pass

    # -t, --tags
    elif args.tags: pass

if __name__ == '__main__':
    main()