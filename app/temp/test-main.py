import docker
import os

def create_and_run_container(image_name="python:3.9"):
    """
    Creates and runs a Docker container based on the given image name.
    Returns the container object.
    """
    client = docker.from_env()
    client.images.pull(image_name)
    container = client.containers.run(
        image_name,
        "/bin/bash",  # This ensures the container starts with a shell
        detach=True,
        tty=True  # Allocates a pseudo-TTY
    )
    print(f"Container {container.short_id} is created and running.")
    return container

def run_command_in_container(container, command):
    """
    Runs a command inside the specified container and prints the output.
    """
    exec_result = container.exec_run(command)
    print(f"Command output:\n{exec_result.output.decode()}")

def stop_and_remove_container(container):
    """
    Stops and removes the specified Docker container.
    """
    container.stop()
    container.remove()
    print(f"Container {container.short_id} is stopped and removed.")

def main():
    """
    Main function to handle user input, run commands inside the Docker container,
    and end the session when the user types 'end'.
    """
    container = create_and_run_container()

    while True:
        # Take input from user
        input_command = input("Enter command to run in Docker container (type 'end' to exit): ")
        
        if input_command.lower() == "end":
            print("Ending the session...")
            break
        
        # Run the entered command inside the container
        run_command_in_container(container, input_command)

    # Stop and remove the container after exiting the loop
    stop_and_remove_container(container)

if __name__ == "__main__":
    main()
