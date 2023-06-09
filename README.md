# Task Manager app

This is a simple Django application that allows you to create, modify and delete tasks from an SQLite database. Also, you will be able to get a list of all the existing tasks.

Django REST framework brings an easy way to build the backend of an application with good error handling.

In order to properly run this app, it is necessary to download or clone this repository and execute the following command from inside **django_app** directory:

```` python manage.py runserver````

Then from localhost:8000/tasks endpoint you will be able to manage any task through Django REST framework. You will see something like this:

<img width="1331" alt="image" src="https://github.com/gdiezve/task_manager/assets/49267946/8faed8a0-d88d-4361-9b2a-9bea9025dd81">

## Django REST framework usage

### Create task

To create a task, you can fill the information shown in *Content* box under *RAW DATA* tab following a json structure, or you can specify the desired values inside each box shown in *HTML form* tab and click **POST**, as shown below:

<img width="1331" alt="image" src="https://github.com/gdiezve/task_manager/assets/49267946/cf57373a-3d9b-4e5a-820d-85b634f667b1">

The new task will be created with the information and an ID.

### Modify task

You can also modify a task by going to localhost:8000/tasks/{id} and modify any of its data; in the example bellow, the status will be changed from **PENDING** to **INITIATED** by clicking **PUT** button:

<img width="1331" alt="image" src="https://github.com/gdiezve/task_manager/assets/49267946/78b6d803-1a26-4528-9919-5c62d48817c3">

### Delete task

To delete a task, you will only need to go to localhost:8000/tasks/{id} and click the **DELETE** red button from the top right corner of the page, as shown in previous screenshot.

## Other usages

This app can be used also from console or other API testing platforms as Postman. Here's an example of a POST request done with Postman to create a task:

<img width="852" alt="image" src="https://github.com/gdiezve/task_manager/assets/49267946/64d543c6-a4ba-45a8-aae2-8e61500e843c">
