import docker

# Initialize the Docker client
client = docker.from_env()

# Pull the desired image (optional if already available)
image_name = "ubuntu:latest"
client.images.pull(image_name)

# Create and run a container
container = client.containers.run(
    image_name,
    "/bin/bash",  # This ensures the container starts with a shell
    detach=True,
    tty=True  # Allocates a pseudo-TTY
)

print(f"Container {container.short_id} is created and running.")

# Run a command inside the container
command = "echo 'pip install numpy'"
exec_result = container.exec_run(command)

# Print the output of the command
print(f"Command output: {exec_result.output.decode()}")

# Stop and remove the container
container.stop()
print(f"Container {container.short_id} is stopped")
