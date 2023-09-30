# Sweeft-Digital-Project

# Project Title

A brief description of what this project does and who it's for

# Book Giveaway Service API Documentation

Welcome to the Book Giveaway Service API documentation. This API allows registered users to offer books for free and also take books that are offered by others. Non-registered users can view the list of available books. The project includes user registration, book management, and supporting resources like book authors, genres, condition, images or posters.

## Table of Contents
- [Authentication](#authentication)
- [Endpoints](#endpoints)
  - [User Management](#user-management)
  - [Book Management](#book-management)
  - [Resource Management](#resource-management)

## Authentication

To use this API, you need to authenticate your requests. Authentication is performed using API keys. Please contact the administrator to obtain your API key.

Include your API key in the header of your requests as follows:


## Endpoints

### User Management

#### Register a User
- **Endpoint**: `/api/register`
- **Method**: `POST`
- **Description**: Register a new user.
- **Request Body**:
  - `username`: User's username
  - `email`: User's email address
  - `password`: User's password

#### Login
- **Endpoint**: `/api/login`
- **Method**: `POST`
- **Description**: Log in a user and obtain an access token.
- **Request Body**:
  - `username`: User's username
  - `password`: User's password
- **Response**:
  - `access_token`: JWT access token for authentication

### Book Management

#### Add a Book
- **Endpoint**: `/api/books`
- **Method**: `POST`
- **Description**: Add a new book to the system.
- **Request Body**:
  - `title`: Title of the book
  - `author_id`: ID of the book author
  - `genre_id`: ID of the book genre
  - `condition`: Condition of the book (e.g., new, used)
  - `image_url`: URL of the book's image or poster
- **Response**:
  - `book_id`: ID of the newly added book

#### List Available Books
- **Endpoint**: `/api/books`
- **Method**: `GET`
- **Description**: Get a list of available books for non-registered users.

#### Get Book Details
- **Endpoint**: `/api/books/{book_id}`
- **Method**: `GET`
- **Description**: Get detailed information about a specific book.
- **Parameters**:
  - `book_id`: ID of the book
- **Response**:
  - `title`: Title of the book
  - `author`: Author of the book
  - `genre`: Genre of the book
  - `condition`: Condition of the book
  - `image_url`: URL of the book's image or poster

### Resource Management

#### List Authors
- **Endpoint**: `/api/authors`
- **Method**: `GET`
- **Description**: Get a list of book authors.

#### List Genres
- **Endpoint**: `/api/genres`
- **Method**: `GET`
- **Description**: Get a list of book genres.

## Conclusion

This API provides a Book Giveaway Service, allowing users to offer and request books. It also offers comprehensive user, book, author, and genre management capabilities. For more details on each endpoint and how to use them, please refer to the respective sections above.

If you have any questions or need assistance, please contact our support team.

Happy reading!
