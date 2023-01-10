import subprocess
import getpass
import os
import requests

class ICAutoDocker():
    
    """Package for executingDocker commands in Python 3.
    Required libraries: subprocess, getpass, os,  requests"""
    # Links für Windows-Version
    URLVSCODE = "https://az764295.vo.msecnd.net/stable/c3511e6c69bb39013c4a4b7b9566ec1ca73fc4d5/VSCodeUserSetup-x64-1.67.2.exe"
    URLDOCKER = "https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe"

    # Standards
    ProgramFiles = ["Docker.exe", "VSCode.exe"]
    Username = getpass.getuser()
    Destination = f'C:\\Users\\{Username}\\Downloads\\'
    #-------------------------------------------------Container Commands------------------------------------------------------#

    def complete_installation():
        """Installation of Docker and VS Code."""
        try:
            filepathDocker = ICAutoDocker.setDestination(0)
            filepathVSCode = ICAutoDocker.setDestination(1)
            downloadDocker = requests.get(
                ICAutoDocker.URLDOCKER, allow_redirects=True)
            downloadVSCode = requests.get(
                ICAutoDocker.URLVSCODE, allow_redirects=True)
            with open(filepathDocker, "wb") as Docker, open(filepathVSCode, "wb") as VSCode:
                Docker.write(downloadDocker.content)
                VSCode.write(downloadVSCode.content)
            subprocess.call(filepathDocker + " batch.exe", shell=True)
            subprocess.call(filepathVSCode + " batch.exe", shell=True)
        except:
            raise "ERROR, Download wasn't successful!"

    def installation_docker():
        """Installation of Docker."""
        try:
            filepath = ICAutoDocker.setDestination(0)
            download = requests.get(
                ICAutoDocker.URLDOCKER, allow_redirects=True)
            with open(filepath, "wb") as file:
                file.write(download.content)
            subprocess.call(filepath + " batch.exe", shell=True)
        except:
            raise "ERROR, Download wasn't successful!"

    def installtion_vscode():
        """Installation of VS Code."""
        try:
            filepath = ICAutoDocker.setDestination(1)
            download = requests.get(
                ICAutoDocker.URLVSCODE, allow_redirects=True)
            with open(filepath, "wb") as file:
                file.write(download.content)
            subprocess.call(filepath + " batch.exe", shell=True)
        except:
            raise "ERROR, Download wasn't successful!"
            
    def create_container(containername):
        """Creation of container with name.
        Example: ICAutoDocker.create_container("whalecontainer")"""
        os.system(f"docker create {containername}")

    def edit_container(containername):
        """Editing of a specific container.
        Example: ICAutoDocker.edit_container("whalecontainer")"""
        os.system(f"docker update {containername}")

    def delete_container(containername):
        """Deletion of a specific container.
        Example: ICAutoDocker.delete_container("whalecontainer")"""
        os.system(f"docker rm /{containername}")

    def start_container(containername):
        """Starting a container.
        Example: ICAutoDocker.start("whalecontainer")
        """
        os.system(f"docker start {containername}")
            
    def run_container(containername:str, Port:str):
        """Running a specific container, optionally with port.
        Example: ICAutoDocker.run("whalecontainer","3000")"""
        if not Port:
            os.system(f"docker run {containername}")
        else:
            os.system(f"docker run -p {Port}:{Port} {containername}")

    def stop_container(containername):
        """Stopping  the running container.
        Example: ICAutoDocker.stop_container("whalecontainer")"""
        os.system(f"docker stop {containername}")

    def restart_container(containername):
        """Restarting a container.
        Example: ICAutoDocker.restart_container("whalecontainer")"""
        os.system(f"docker restart {containername}")

    def change_containername(containername, newcontainername):
        """Renaming containers.
        Example: ICAutoDocker.change_containername("whalecontainer", "whalecontainer2")"""
        os.system(f" docker rename {containername} {newcontainername}")

    def list_of_containers():
        """Showing list of all containers.
        Example: ICAutoDocker.list_of_containers()"""
        os.system("docker ps")
    #-------------------------------------------------Image Commands----------------------------------------------------------#

    def create_image(username, imagename):
        """Creating image for container.
        Example: ICAutoDocker.create_image("User", "whaleImage")"""
        os.system(f"docker build {username}/{imagename}")

    def delete_image(imagename):
        """Deleting image.
        Example: ICAutoDocker.delete_image("whaleImage")"""
        os.system(f"docker rmi {imagename}")

    def change_imagename(imagename,newimagename):
        """Renaming image.
        Example: ICAutoDocker.change_imagename("whaleImage", "whaleImage2")"""
        os.system(f"docker tag {imagename} {newimagename}")

    def list_of_images():
        """Lists all  images.
        Example: ICAutoDocker.list_of_images()"""
        os.system("docker images")
    #-------------------------------------------------Other Commands----------------------------------------------------------#

    def touch_dockerfile_node():
        """Creating example docker project with NodeJS.
        Official example from docker website.
        Example: ICAutoDocker.touch_dockerfile_node()"""
        os.system("touch Dockerfile")
        dockerfile = open("Dockerfile", "w")
        dockerfile.write("""FROM node:16
        # Create app directory
        WORKDIR /usr/src/app

        # Install app dependencies
        # A wildcard is used to ensure both package.json AND package-lock.json are copied
        # where available (npm@5+)
        COPY package*.json ./

        RUN npm install
        # If you are building your code for production
        # RUN npm ci --only=production

        # Bundle app source
        COPY . .

        EXPOSE 8080
        CMD [ "node", "server.js" ]
        """)
        dockerfile.close()

    def touch_dockerfile():
        """Creating dockerfile.
        Example: ICAutoDocker.touch_dockerfile()"""
        os.system("touch Dockerfile")
        
    def setDestination(Input):
        """Setting destination for filepath. (Destination is download folder)"""
        filepath = ICAutoDocker.Destination + \
            ICAutoDocker.ProgramFiles[Input]
        return filepath