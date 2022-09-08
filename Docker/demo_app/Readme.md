# Simple Static Website
This is a simple app to sharpen my skill in docker.
## Mode Demo


https://user-images.githubusercontent.com/83673888/188954352-6b8eeb9f-3a52-43ae-81b5-119aafdefece.mp4


## How To Try This App
* Clone this repo to get all the code and files.
```bash
$ cd ./DevOps_Learning_Journey/Docker/demo_app
$ docker-compose up # this command will create 3 containers and run them.
```

* To see the website go to this URL **https://localhost:3000**
* To see the database and check if the app is connected, go to this URL **https://localhost:8080**
* Now, you can edit the name, email and intersts in the website and see the changes in the mongo-express database page.


## Python fun part
I've used selenium to open the website and database URLs and edit some fields automatically.
Before that, I had to open the links myself and edit the fields and then check the dataset to see if the app is connected to the database.

pretty boring right :)<br>
Now with one command all of it is done within seconds.



## Resources and Note
1. I have used this amazing [**YouTube tutorial**](https://www.youtube.com/watch?v=3c-iBn73dDE) by [nana janashia](https://www.linkedin.com/in/nana-janashia/) to build my project.
2. I've added GitHub Actions workflow, so that when I commit new change to the app, an Action will get triggered and build a container and push it to my Docker hub account.

If you like this project, I appreciate you starring this repo.<br>
Please feel free to fork the content and contact me on my [LinkedIn account](https://www.linkedin.com/in/abdassalam-ahmad/) if you have any questions.
