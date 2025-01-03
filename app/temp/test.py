import docker
import subprocess

# Initialize the Docker client
client = docker.from_env()

# Pull the desired image (optional if already available)
image_name = "python:3.9"  # Use a Python-based image
client.images.pull(image_name)

# Create and run a container
container = client.containers.run(
    image_name,
    "/bin/bash",  # This ensures the container starts with a shell
    detach=True,
    tty=True  # Allocates a pseudo-TTY
)

print(f"Container {container.short_id} is created and running.")

# Input command (e.g., installing numpy)
input_command = "pip install bjdaf"

# Run the input command inside the container
exec_result = container.exec_run(input_command)

# Print the output of the command
print(f"Command output: {exec_result.output.decode()}")

# Check if numpy was installed successfully
#exec_result = container.exec_run("python -c 'import numpy; print(numpy.__version__)'")

# Print the numpy version
#print(f"Installed numpy version: {exec_result.output.decode().strip()}")

# Stop and remove the container
container.stop()
container.remove()
print(f"Container {container.short_id} is stopped and removed.")
