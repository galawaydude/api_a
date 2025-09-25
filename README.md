# Blog Post API

This is a simple REST API for a blog post application built with Python and FastAPI.

## How to Build and Run

1.  **Build the Docker Image:**
    ```sh
    docker build -t blog-api .
    ```

2.  **Run the Docker Container:**
    ```sh
    docker run -d -p 8000:8000 --name blog-api-container blog-api
    ```

The API will be accessible at `http://localhost:8000`.
