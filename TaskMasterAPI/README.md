# TaskMasterAPI

TaskMasterAPI is a project that provides an API for managing tasks and users. The project allows users to create accounts, add tasks, update them, and delete them, with full control over user permissions.

## Features

### User Management
- Create new user accounts.
- Update user information.
- Delete user accounts.

### Task Management
- Add new tasks with a title, description, and deadline.
- View tasks.
- Update tasks.
- Delete tasks.

### Security
- Use of OAuth2 for securing API access.
- Password encryption using bcrypt.

## Technologies Used

- **FastAPI**: A fast and efficient framework for building APIs with Python.
- **SQLAlchemy**: An ORM library for interacting with databases.
- **SQLite**: A lightweight and fast database for local development.
- **JWT (JSON Web Tokens)**: For securing API access.
- **Pydantic**: For data validation and creating data models.

## How to Run

### 1. Install Requirements
Install the required packages using the following command:

```bash
pip install -r requirements.txt
```

### 2. Run the Server
Start the server using the following command:

```bash
uvicorn main:app --reload
```

### 3. Access the API
You can access the API at:

```
http://127.0.0.1:8000/ or http://127.0.0.1:8000/docs
```

## Endpoints

### Users
- **Create a New User:** `POST /user/create`
- **Get User Information:** `GET /user/{id}`
- **Update User Information:** `PUT /user/update/{id}`
- **Delete User:** `DELETE /user/delete/{id}`

### Tasks
- **Add a New Task:** `POST /task/add`
- **Get Task Information:** `GET /task/{id}`
- **Update a Task:** `PUT /task/update/{id}`
- **Delete a Task:** `DELETE /task/delete/{id}`

### Authentication
- **Get Token:** `POST /token`

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the project.
2. Create a new branch:
   ```bash
   git checkout -b feature/YourFeatureName
   ```
3. Make your changes and add them:
   ```bash
   git add .
   ```
4. Commit your changes:
   ```bash
   git commit -m 'Add some feature'
   ```
5. Push your changes to the branch:
   ```bash
   git push origin feature/YourFeatureName
   ```
6. Open a Pull Request.

## License
This project is licensed under the **MIT License**. For more details, please see the `LICENSE` file.

## Contact
If you have any questions or inquiries, please contact:

- **Email:** zeyad.gabr12222009@gmail.com
- **GitHub:** https://github.com/ZeyadGabr1

---
