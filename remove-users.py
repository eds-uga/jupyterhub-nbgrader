"""
Creates a bunch of new users on the system, passwords and all.
"""
import argparse
import os
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'JHub Remove Users',
        epilog = 'lol moar pyth0nz', add_help = 'How to use',
        prog = 'python remove-users.py <args>')

    # Optional parameters.
    parser.add_argument("-f", "--folder", default = "/home",
        help = "Folder of usernames for deletion. [DEFAULT: /home/]")
    parser.add_argument("-e", "--except", nargs = "*",
        default = ["magsol", "squinn", "csciadmin"],
        help = "Usernames to retain.")

    args = vars(parser.parse_args())

    # Get a list of all the directories in the specified user dir.
    directories = [f for f in os.listdir(args['folder']) \
        if os.path.isdir(os.path.join(args['folder'], f))]

    # Loop through the directory names, deleting those NOT in the safe list.
    n = 0
    for d in directories:
        if d in args['except']: continue

        # Delete the user!
        command = "userdel -fr {}".format(d)
        print(command)
        subprocess.run(command.split())
        n += 1

    print("{} user{} deleted.".format(n, '' if n == 1 else 's'))
