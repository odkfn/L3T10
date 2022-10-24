Project Title: silverbyskyline

Description: This website consists of the L3T10 capstone task for HyperionDev. It is based around the (ex) band silverbyskyline and features one of their songs ("Seeds") on the homepage.  Users must be logged in to see this.

Installation: There are two facets to the installation of this - viewing the site via the virtual environment, or viewing it via the containerised docker image.  The virtual environment instructions pertain to Mac.

VIRTUAL ENVIRONMENT (for Mac):
1.  Open Terminal;
2.  Navigate to the project folder which contains "runserver.sh" (using the cd command);
3.  Type "sh runserver.sh" into the terminal and press enter;
4.  You will see a message "starting server at http://127.0.0.1:8000/";
5.  Copy and paste the above into an internet browser to begin using the site.


DOCKER FILE:
1.  Navigate to https://hub.docker.com/ and create a Docker Hub account;
2.  Download Docker desktop and install from https://www.docker.com/products/docker-desktop then login;
3.  Navigate to the folder with the Dockerfile using cd;
4.  Execute the two commands in commands.txt in terminal, which are:
    docker build --tag my-project .  # This creates the docker image and calls it my Project
    docker run --publish 8000:8000 my-project  # This "containerises" the image, and runs it on port 8000
5.  Navigate to 127.0.0.1:8000/ in the browser to view the site!
