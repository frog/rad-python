# RAD Python

A starting point for containerized Python 3 applications.  Based on RAD Container:  https://github.com/frog/rad-container

# Getting Started
To begin developing your Python 3 application, you must have the latest version of Docker installed on your system.  If you are using an older version of Docker, please uninstall it and use the appropriate installer from the docker website.

https://docs.docker.com/engine/installation/

Once Docker is installed on your machine, follow the steps below to begin developing your application.  This is intended for local development, and will map your project root directory into the container and auto restart the application when changes are made.

1.  Navigate to your project root directory and copy the contents of this repository to that location.
2.  Create a copy of `make_env.dist` and rename it to `make_env`.  Update with your project specific information.
3.  'make build'
4.  'make shell'
5.  'pip install -r requirements.txt'
6.  'python3 app.py'

# Success

1.  If successful, you will see "Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)" in your console.
2.  In a web browser, navigate to 'http://localhost:5000' and you will see "Hello world!".

# Environment Variables

You may pass additional environment variables to your application by including them in your `make_env` file.  Follow these steps to add new environment variables.

1.  Add your environment variable to your `make_env` file inside the DOCKER_ENV specification.  Remember, the last line does not get a trailing slash.
2.  Destroy your existing container and rebuild it using `make build`.
3.  Run and re-attach to your updated container using `make shell`.