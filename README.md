# Blog API Project

A full-featured Blog API built with **Django REST Framework**, using **JWT authentication**, **PostgreSQL**, and **Docker**. This project supports user management, roles, posts, categories, tags, comments, and likes with role-based permissions for admin and managers.

---

## Features

- User registration, login, logout
- JWT-based authentication
- Custom user profiles
- Role-based permissions (admin, manager, regular user)
- CRUD operations for posts, categories, tags
  - Only admin/manager can create/update/delete categories and tags
- Likes and comments functionality
- Pagination for posts
- Dockerized for easy setup
- PostgreSQL database support
- Production-ready with Gunicorn

---

## Tech Stack

- **Backend:** Django, Django REST Framework
- **Database:** PostgreSQL
- **Authentication:** JWT (Simple JWT)
- **Containerization:** Docker
- **Image Handling:** Pillow

---

## Getting Started

### Prerequisites

- Docker and Docker Compose installed
- Git installed

### Clone the repository


git clone https://github.com/Jemmal35/Blog-App-API.git
cd blog-api


Environment Variables

# Create a .env file in the root folder:
    SECRET_KEY=your_secret_key
    DEBUG=True
    DB_NAME=blog_db
    DB_USER=postgres
    DB_PASSWORD=postgres_password
    DB_HOST=db
    DB_PORT=5432

# Build and Run Docker Containers
    docker-compose up --build
    - The API will be accessible at: http://localhost:8000/

# Apply Migrations
    docker-compose exec web python manage.py migrate

# Create Superuser
    docker-compose exec web python manage.py createsuperuser

# API Endpoints
## Accounts
| Method | Endpoint                                | Description               |
| ------ | --------------------------------------- | ------------------------- |
| POST   | `/auth/api/v1/register/`                | User registration         |
| POST   | `/auth/api/v1/login/`                   | Obtain JWT token          |
| POST   | `/auth/api/v1/logout/`                  | Logout (invalidate token) |
| POST   | `/auth/api/v1/refresh/`                 | Refresh JWT token         |
| GET    | `/auth/api/v1/profile/`                 | Retrieve user profile     |
| PUT    | `/auth/api/v1/profile/update/`          | Update user profile       |
| PUT    | `/auth/api/v1/profile/change-password/` | Change password           |

## Role Management (Admin Only)
| Method | Endpoint                                   | Description                   |
| ------ | ------------------------------------------ | ----------------------------- |
| PUT    | `/auth/api/v1/admin/users/<user_id>/role/` | Update user role (admin only) |


## Blog
| Method           | Endpoint                            | Description                                 |
| ---------------- | ----------------------------------- | ------------------------------------------- |
| GET, POST        | `/api/v1/posts/`                    | List all posts / Create a new post          |
| GET, PUT, DELETE | `/api/v1/posts/<id>/`               | Retrieve, update, or delete a single post   |
| GET, POST        | `/api/v1/posts/<post_id>/comments/` | List or add comments for a post             |
| POST             | `/api/v1/posts/<post_id>/like/`     | Like or unlike a post                       |
| GET, POST        | `/api/v1/category/`                 | List all categories / Create a new category |
| GET, PUT, DELETE | `/api/v1/category/<id>/`            | Retrieve, update, or delete a category      |
| GET, POST        | `/api/v1/tag/`                      | List all tags / Create a new tag            |
| GET, PUT, DELETE | `/api/v1/tag/<id>/`                 | Retrieve, update, or delete a tag           |

- JWT token must be included in the Authorization header: Bearer <your-token>

# Roles and Permissions
    -- Admin
        Full access to all resources
        Can manage users, roles, categories, tags, posts, comments
    -- Manager
        Can manage categories, tags, and moderate posts/comments
    -- Regular User
        Can create, read, update, delete own posts
        Can like and comment

# License
    This project is for study and personal learning purposes.