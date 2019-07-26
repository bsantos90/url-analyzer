
# Docker Guest Talk - Ben Shaver - 26 July 2019

[repo](https://github.com/bpshaver/url-analyzer)

[slides](https://docs.google.com/presentation/d/1gH2uUkjkVVMvrq_lQY2fOn5ETEOmGYXCQEUbRZ7SyJ0/edit?usp=sharing)

## Docker Cheat Sheet




### Basic Docker terminology:
- host - your computer
- container - a running docker program containing user-defined code and processes
- image - executable file which starts a docker container
- dockerfile - text file which defines how an image will behave. it is a recipe.

### it commands we’ll use today
- `git checkout <BRANCH NAME>`
  - e.g. `git checkout master`

### Relevant bash commands
- `chmod`
- e.g. `chmod 700 <SOME FILE>`

### Docker commands
- `docker pull <DOCKER IMAGE>`
- `docker build -t <DOCKER IMAGE> .`
- `docker ps`
- `docker kill`
  - pro-tip: `docker kill $(ps -q)`
  - but we’ll always use ctrl+c
- `docker run <OPTIONS> <DOCKER IMAGE>`
- `-v` - share a folder b/w host and container
  - e.g. docker `run -v /data:/data`
- `-p` - expose port b/w and container
  - we won't discuss today, but this is relevant for hosting a web service or jupyter notebook from a container
  - e.g. `docker run -p 5000:5000`
  - e.g. `docker run -p 8888:8889` <- Why the difference here?
- `-it --rm`
  - ensures your container is interactive, and that it is removed when it is finished running
  - e.g. `docker run -it --rm python:3`

### Dockerfile keywords
- `FROM`
- `COPY`
- `RUN`
- `ENTRYPOINT`
