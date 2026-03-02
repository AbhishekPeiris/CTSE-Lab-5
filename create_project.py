import os

project_name = "microservices-lab"

folders = [
    "item-service",
    "order-service",
    "payment-service",
    "api-gateway"
]

files = {
    "docker-compose.yml": "",
    "item-service/main.py": "",
    "item-service/requirements.txt": "",
    "item-service/Dockerfile": "",
    "order-service/main.py": "",
    "order-service/requirements.txt": "",
    "order-service/Dockerfile": "",
    "payment-service/main.py": "",
    "payment-service/requirements.txt": "",
    "payment-service/Dockerfile": "",
    "api-gateway/nginx.conf": "",
    "api-gateway/Dockerfile": ""
}

# Create root folder
os.makedirs(project_name, exist_ok=True)

# Create subfolders
for folder in folders:
    os.makedirs(os.path.join(project_name, folder), exist_ok=True)

# Create empty files
for file_path in files:
    full_path = os.path.join(project_name, file_path)
    with open(full_path, "w") as f:
        f.write("")

print("Project structure created successfully!")