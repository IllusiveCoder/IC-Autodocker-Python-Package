# IC-Autodocker-Python-Package

[[_TOC_]]

## Description
This project is for people, who want to learn Docker. It is planned, as portable version of my other project. It comes with many supportative functions for the beginning. Planned is an instructual guide, which is guiding through the installation and explains how to use the package.

## Further updates
Are planned for the near future!

## Further informations
### Functions:
Installation:
- complete_installation
- installation_docker
- installation_vscode

Container:
- create_container
- edit_container
- delete_container
- start_container
- run_container
- stop_container
- restart_container
- change_containername
- list_of_all_containers

Images:
- create_image
- delete_image
- change_imagename
- list_of_images

More commands:
- touch_dockerfile_node
- touch_dockerfile
- setDestination

## Examples
Example 1:
```
import ICAutoDocker from ICAutoDockerPackage  as IC

IC.touch_dockerfile_node()

```
Example 2:
```
import ICAutoDocker from ICAutoDockerPackage  as IC

IC.create_image("User","whale")
IC.create_container("whale")
IC.run_container("whale", "3000")
```

[GitHub Style Guide for Readme.md files](https://docs.github.com/de/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#headings)
