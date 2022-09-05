# Docker Resources

- I've used **Docker Tutorial for Beginners** [**a YouTube course**](https://www.youtube.com/watch?v=3c-iBn73dDE) from TechWorld with Nana YT channel.

- I've also watched this 10 Hours [**Extensive Docker Tutorial**](https://www.youtube.com/watch?v=PrusdhS2lmo&t=20196s) by [Ahmed Sami](https://www.linkedin.com/in/ahmed-sami-a173138/).

# What I've Learned:
1- **docker ps**: List running containers.

```bash
$ docker ps -a # list ALL containers (Stopped and Running).
$ docker container ls # List running containers.
```

2- **docker run**: Pulls an image from internet -or locally- and create a container and run it.

```bash
$ docker run --name alpinec alpine:latest # Create a container from alpine image locally or from Docker Hub and give it a name of alpinec.
$ docker run --name alpine-old alpine:3.15 # This will take mush less time (Docker optimization advantage) because of the similarity between the two versions (same layers).
$ docker run -d alpine # runs a new container in detached mode.
```

3- **docker start <name>**: Start a stopped container using its name or ID.

4- **docker stop <name>**: Stop a running container using its name or ID.

```bash
$ docker start alpinec # start a container named alpinec.
$ docker stop 066 # stop a container, its ID starts with 066 (alpinec).
```

5- **docker images**: List all local images.

```bash
$ docker image ls # List all local images.
```

6- **Port Mapping**: How to map a port frm host machine to a container.

```bash
$ docker run -p 6000:6379 -d redis # create and run a container from redis image and mapping port 6000 on the host (laptop) to 6379 port on the container.
$ docker run -p 6001:6379 -d redis:5.0 # we can run two containers at the same time with same port opened but we open two different ports on host.
$ curl http://localhost:6001 # to see that both containers are running fine.
$ curl http://localhost:6000 # to see that both containers are running fine.
```

7- **docker logs**: show the logs of a container.

```bash
$ docker logs mongoc # logs a container named mongoc.
$ docker logs 6ac # logs a container, its ID is 6ac.
```

8- **docker exec**: enter a running container terminal.

```bash
$ docker exec -it mongoc bash # Enter bash of mongoc container to debug.
$ docker exec -it 6ac bash # Enter bash of mongoc container by its ID to debug.
```

9- **docker network**: handle docker networks.

```bash
$ docker network ls # Lists all networks.
$ docker network create mongo-network # create a new network named mongo-network.
```

