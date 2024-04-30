# 3D-Dashboard-Proxy

```bash
# the Python project structure is as follows:
# project/
# ├── Dockerfile
# ├── requirements.txt
# ├── main.py
```

With the provided project structure and Dockerfile, you can deploy the Python project using Docker without running the `test.py` script. Just build the Docker image and run the container as follows:

```bash
# Build the Docker image
docker build -t {{image_name}} .

# Run the Docker container
docker run {{image_name}}
```

Replace `{{image_name}}` with the desired name for your Docker image.
