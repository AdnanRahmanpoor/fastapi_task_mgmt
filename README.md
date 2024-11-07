# Task Management API using FastAPI

This is a simple Task Management API built with FastAPI that allows users to create, read, update, and delete tasks. It demonstrates essential FastAPI features like CRUD operations, request validation with Pydantic models AND query parameter filtering.

## Features

- **CRUD Operations**: Create, read, update, and delete tasks.
- **Request Validation**: Ensures input data is valid using Pydantic models.
- **Query Parameters**: Filter tasks by status and priority.

## Learning Focus

This project covers the fundamentals of FastAPI, including:
- Setting up path operations for CRUD functionality
- Using Pydantic models for data validation

## Project Structure

```plaintext
task_management_api/
├── app/
│   ├── main.py               # Main entry point of the application
│   ├── models.py             # Task data models (Pydantic)
│   ├── schemas.py            # Data validation schemas
│   ├── database.py           # In-memory database setup and CRUD functions
│
└── requirements.txt          # Dependencies for the project
```

## Getting Started

### Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/AdnanRahmanpoor/fastapi_task_mgmt.git
    cd fastapi_task_mgmt
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the FastAPI application with Uvicorn:

    ```bash
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to access the interactive API documentation (Swagger UI).

## API Endpoints

### Task Model

Each task has the following attributes:

- **id** (int): Unique identifier for the task.
- **title** (str): Title of the task.
- **description** (str, optional): Description of the task.
- **status** (enum): Status of the task, default is "Pending" (`Pending`, `In Progress`, or `Completed`).
- **priority** (int): Priority of the task, default is "Medium" (`1`, `2`, or `3` for low, medium, high respectively).

### Endpoints

| Method | Endpoint             | Description                    |
|--------|-----------------------|--------------------------------|
| GET    | `/tasks`             | List all tasks (with optional filters for `status` and `priority`) |
| GET    | `/tasks/{task_id}`    | Get a specific task by `task_id` |
| POST   | `/tasks`             | Create a new task              |
| PUT    | `/tasks/{task_id}`    | Update an existing task by `task_id` |
| DELETE | `/tasks/{task_id}`    | Delete a task by `task_id`     |

### Example Usage

#### Creating a Task

**POST** `/tasks`

Request Body:
```json
{
    "title": "Complete documentation",
    "description": "Finish the API documentation",
    "status": "Pending",
    "priority": 2
}
```

#### Getting a Task

**GET** `/tasks/1`

Response:
```json
{
    "id": 1,
    "title": "Complete documentation",
    "description": "Finish the API documentation",
    "status": "Pending",
    "priority": 2
}
```

#### Filtering Tasks

**GET** `/tasks?status=Pending&priority=2`

This will return tasks with a `status` of `Pending` and a `priority` of `2` (Medium).

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.