#!/bin/bash
# Upgrade script for JupyterHub. To be used between classes.
# MUST BE RUN WITH FULL ROOT PERMISSIONS.

# Test if command line argument is being used.
if [ $# -eq 0 ]
    then
        echo "Supply a list of students (one username per line)."
        echo "Also, be sure to run with ROOT PERMISSIONS."
        exit 0
fi

# Test if running as root.
if [ "$(id -u)" != "0" ]; then
    echo "You must run this script as ROOT."
    exit 0
fi

# 1: Update the base Python install, including JupyterHub itself.
conda update -y conda
conda update -y --all
pip install -U jupyterhub
pip install -U nbgrader

# 2: Remove the previous JupyterHub configuration.
rm /etc/jupyterhub/jupyterhub.sqlite 

# 3: Remove all the previous users of the system (except for admin users).
# Luckily, we have a script for this.
python remove-users.py

# 4: Create all the needed users and install the nbgrader extension.
# Luckily, we have a self-contained script to do this for us.
python add-users.py -f $1

# Start it up!
nohup jupyterhub -f /etc/jupyterhub/jupyterhub.py &
