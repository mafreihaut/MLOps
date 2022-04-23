<p align = "center" draggable=”false” ><img src="https://user-images.githubusercontent.com/37101144/161836199-fdb0219d-0361-4988-bf26-48b0fad160a3.png"
     width="200px"
     height="auto"/>
</p>



# <h1 align="center" id="heading">Part 1: AWS "Hello World"</h1>

For this assignment, our goal will be to run python on a cloud server on Amazon Web Services(AWS). We will essentially be using AWS as a virtual machine. The AWS cloud server we'll be using today is called Elastic Compute Cloud (EC2).

We'll first start by creating a repository and modifying it on our local machine. We'll then launch an EC2 instance (server) with a specific configuration so we can access it publicly. From there, we'll add our files that we modified to server and test it.

We'll work locally first. Make sure you `exit` out of your current `SSH` connection.
![image](https://user-images.githubusercontent.com/72572922/164942902-2437a623-f73c-478d-b92d-fdf1662cded4.png)



Create a `conda` virtual environment using the following code block

``` bash
conda create -n aws_fastapi python=3.8
```

![image](https://user-images.githubusercontent.com/72572922/164943060-02a71406-73fd-4ea4-ae06-5163812d77cf.png)

Activate the environment using the following code block

``` bash
conda activate aws_fastapi
```

![image](https://user-images.githubusercontent.com/72572922/164943075-aa6f66cc-68bb-46a6-bd59-054049d3bd7c.png)

Install FastAPI using the following code block

``` bash
pip install fastapi
```

![image](https://user-images.githubusercontent.com/72572922/164943085-a806dcdf-a7cf-432e-be9c-efd2e0bb0855.png)

Install uvicorn using the following code block

``` bash
pip install uvicorn
```

![image](https://user-images.githubusercontent.com/72572922/164943092-07bf364a-2c26-4a08-ab51-ed989b2502f3.png)

Save all the `pip` requirements using the following code block

``` bash
pip freeze > requirements.txt
```

![image](https://user-images.githubusercontent.com/72572922/164943122-cac80461-cdba-4130-9026-e45033ec1db6.png)

Open VS Code in your current conda environment

![image](https://user-images.githubusercontent.com/72572922/164943215-3c8cb8b9-5147-40b5-8858-f4020395a4dc.png)
