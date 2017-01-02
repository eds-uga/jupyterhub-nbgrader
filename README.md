# Resources for JupyterHub and nbgrader

This is meant to be a singular repository for resources related to running and updating [JupyterHub](https://github.com/jupyterhub/jupyterhub) with the [nbgrader](https://github.com/jupyter/nbgrader) extension.

Right now, it doesn't contain a whole lot, but it does have scripts that serve as useful templates for migrating an *existing* JupyterHub deployment to a new course (e.g. a new semester).

### What it does

 - Updates the current Anaconda environment, and specifically the JupyterHub and nbgrader applications.
 - Creates the system users needed and configures them with the nbgrader extension.
 - Deletes previous users (and their home directories) on the system.

### What it doesn't do (yet)

 - Modify the `nbgrader_config.py` file in any way.
 - Modify the `jupyterhub_config.py` file in any way.
 - Create, delete, or otherwise edit any nbgrader courses.
 - Use GitHub authentication.

Pull requests are welcome, as are any links to JupyterHub / nbgrader integration resources. Getting these two to play nicely together is a messy process; I'm hoping this will help clean it up a bit!