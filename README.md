# Backend FastAPI Projects

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109%2B-009688.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

A collection of experimental backend projects built with FastAPI for learning and practice purposes. Each project demonstrates different concepts, patterns, and real-world implementations.

---

## About This Repository

This repository contains various backend projects developed using FastAPI framework. Each project is self-contained and focuses on specific backend concepts, from basic CRUD operations to advanced microservices architecture.

**Purpose:**
- Practice and improve FastAPI skills
- Experiment with different backend patterns
- Build production-ready API structures
- Document learning progress and implementations

---

## Repository Structure

```
backend-fastapi-projects/
│
├── project-01-basic-api/
│
├── project-02-auth-system/
│
├── project-03-ecommerce-api/
│
└── ...
```

---


Browse the repository folders to explore individual projects. Each project has its own README with specific setup instructions and implementation details.

---

## Technologies Used

### Core
- **FastAPI** - Modern Python web framework
- **Pydantic** - Data validation and serialization
- **SQLAlchemy** - ORM for database operations
- **Alembic** - Database migrations

### Databases
- **MySql** - Primary relational database
- **Redis** - Caching and session storage

### Authentication & Security
- **JWT** - Token-based authentication
- **OAuth2** - Social login integration
- **Bcrypt** - Password hashing

### Testing & Quality
- **Pytest** - Testing framework
- **Coverage.py** - Code coverage
- **Black** - Code formatting
- **Flake8** - Linting

### DevOps & Deployment
- **Docker** - Containerization
- **Docker Compose** - Multi-container orchestration
- **Nginx** - Reverse proxy
- **GitHub Actions** - CI/CD

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip or Poetry for package management
- PostgreSQL or other database (project-dependent)
- Redis (optional, for certain projects)

### General Setup Steps

1. **Clone the repository:**
```bash
git clone https://github.com/ZeyadGabr1/backend-fastapi-projects.git
cd backend-fastapi-projects
```

2. **Navigate to a specific project:**
```bash
cd [project-folder-name]
```

3. **Follow the project's README:**

Each project has its own README with specific setup instructions, dependencies, and configuration details. Refer to the individual project documentation for:
- Installation steps
- Environment configuration
- Database setup
- Running the application
- API documentation links

---

## Development Guidelines

### Code Style
- Follow PEP 8 guidelines
- Use type hints for all functions
- Write docstrings for modules, classes, and functions
- Format code with Black
- Lint with Flake8

### Git Workflow
- Create feature branches from `main`
- Write descriptive commit messages
- Submit pull requests for review
- Keep commits atomic and focused

### Testing
- Write tests for all endpoints
- Aim for 80%+ code coverage
- Include integration tests
- Test error cases and edge cases

---

## Learning Resources

- [FastAPI Official Documentation](https://fastapi.tiangolo.com/)
- [FastAPI Best Practices](https://github.com/zhanymkanov/fastapi-best-practices)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Alembic Tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

---

## Contributing

Contributions, suggestions, and feedback are welcome! Feel free to:
- Report bugs or issues
- Suggest new project ideas
- Improve existing implementations
- Add documentation

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or discussions:
- Open an issue in this repository
- Email: [zeyad.ossama.dev@gmail.com]

---

## Acknowledgments

Built with FastAPI and inspired by the amazing Python community.

**Happy Coding!**
