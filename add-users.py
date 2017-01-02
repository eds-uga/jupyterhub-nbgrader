"""
Creates a bunch of new users on the system, passwords and all.
"""
import argparse
import os
import subprocess

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'JHub Add Users',
        epilog = 'lol moar pyth0nz', add_help = 'How to use',
        prog = 'python add-users.py <args>')

    # Required parameters.
    parser.add_argument("-f", "--file", required = True,
        help = "Line of usernames to add to the system.")

    # Optional parameters.
    parser.add_argument("-o", "--openssl", choices = ['1', 'apr1', 'crypt'],
        default = "1", help = "Form of password encryption to use. [DEFAULT: 1]")

    args = vars(parser.parse_args())

    # Read in all the usernames.
    f = open(args['file'], "r")
    usernames = [u.strip() for u in f.readlines()]
    f.close()

    # For each username, create a user with an encrypted password.
    print("{} users found.".format(len(usernames)))
    for username in usernames:
        username = username.strip()

        # Generate an encrypted password based on their username.
        command = "openssl passwd -{} {}".format(args['openssl'], username)
        print(command)
        pwd = subprocess.run(command.split(), stdout = subprocess.PIPE)

        # Create the user.
        command = "useradd -s /bin/bash -m -N -g students -p {} {}".format(pwd.stdout.strip().decode(), username)
        print(command)
        subprocess.run(command.split())

        # Install and configure the nbgrader Jupyter extension *as the user*.
        os.chdir("/home/{}".format(username))
        command1 = "sudo -H -u {} nbgrader extension install assignment_list --user".format(username)
        print(command1)
        command2 = "sudo -H -u {} mkdir /home/{}/.jupyter".format(username, username)
        print(command2)
        command3 = "sudo -H -u {} nbgrader extension activate assignment_list".format(username)
        print(command3)
        command4 = "sudo -H -u {} fc-cache".format(username)
        print(command4)

        subprocess.run(command1.split())
        subprocess.run(command2.split())
        subprocess.run(command3.split())
        subprocess.run(command4.split())

    print("All done!")
