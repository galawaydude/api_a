import random
from locust import HttpUser, task, between

class BlogUser(HttpUser):
    wait_time = between(1, 5)  # Wait 1-5 seconds between tasks

    def on_start(self):
        """On start, create a post to work with."""
        self.client.post("/posts", json={
            "title": "Initial Post",
            "author": "Locust",
            "content": "This is a test post."
        })

    @task(3)
    def get_posts(self):
        """Get all posts or a specific post."""
        # Get all posts
        self.client.get("/posts")

        # Get a specific post (assuming IDs start from 1)
        post_id = random.randint(1, 10) 
        self.client.get(f"/posts/{post_id}", name="/posts/[id]")

    @task(2)
    def create_post(self):
        """Create a new post."""
        self.client.post("/posts", json={
            "title": f"New Post by {random.randint(1, 100)}",
            "author": "Locust",
            "content": "Some random content."
        })

    @task(1)
    def update_post(self):
        """Update an existing post."""
        post_id = random.randint(1, 10)
        self.client.put(f"/posts/{post_id}", json={
            "title": "Updated Title",
            "author": "Locust Updater",
            "content": "This content has been updated."
        }, name="/posts/[id]")
