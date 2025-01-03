import docker

def create_and_run_container(image_name="python:3.9", memory_limit="2g", cpus="2"):
    """
    Creates and runs a Docker container based on the given image name,
    with specified memory and CPU parameters.
    Returns the container object.
    """
    client = docker.from_env()

    # Pull the image if not already available
    client.images.pull(image_name)

    # Run the container with resource limits and install sudo and lshw
    container = client.containers.run(
        image_name,
        "/bin/bash -c 'apt-get update && apt-get install -y sudo lshw && /bin/bash'",  # Install sudo and lshw
        detach=True,
        tty=True,
        mem_limit=memory_limit,
        cpuset_cpus=cpus
    )
    print(f"Container {container.short_id} is created and running with {memory_limit} memory and {cpus} CPUs.")
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
    # Set memory and CPU limits as per the user's preference
    memory_limit = "2g"  # Example: 2GB memory
    cpus = "2"  # Example: 2 CPU cores

    container = create_and_run_container(memory_limit=memory_limit, cpus=cpus)

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
