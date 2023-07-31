# TO DO list

# Task Management Application

This is a simple task management application built using Django. It allows users to create, view, update, and delete tasks.

## Project Description

The Task Management Application provides a user-friendly interface to manage tasks efficiently. Users can create tasks with a title, description, due date, and status. They can also update the task details and mark tasks as completed when finished. The application provides pagination for easy navigation through tasks and includes a search feature to filter tasks by their ID.

## Setup and Local Installation

To set up and run the application locally, follow these steps:

1. **Clone the repository:** Start by cloning this GitHub repository to your local machine using the following command:

``` git clone git@github.com:heyman242/backend-intern-assignment.git```
  
2. Navigate to the project directory:

 ```cd ums_project```

3. **Create a virtual environment:** It is recommended to use a virtual environment to keep the project dependencies isolated. Create a new virtual environment by running the following command:

 ``` python3 -m venv env ```

4. Activate the virtual environment:

 ```source env/bin/activate (for macos / linux)```
 ```.\env\Scripts\activate (for windows)```

5. **Install dependencies:** Install the project dependencies listed in the requirements.txt file by running the following command:

 ```pip install -r requirements.txt```

6. **Run database migrations:** Apply the database migrations to set up the necessary database schema. Run the following command:

 ```python3 manage.py makemigrations```
 ```python3 manage.py migrate```

7. **Start the development server:** Start the Django development server by running the following command:

 ```python3 manage.py runserver```

8. **Access the application: Open a web browser and navigate to ```http://localhost:8000/tasks``` or ```http://127.0.0.1:8000/tasks``` to access the Task Management Application.

Usage
Create a new task by filling in the title, description, due date, and selecting the status. Click the "Create" button to add the task.
View the list of tasks on the home page, with pagination for easy navigation.
Update a task by clicking the "Update" link next to the task you want to modify. Make the necessary changes and click "Save" to update the task details.
Delete a task by clicking the "Delete" button next to the task you want to remove.


