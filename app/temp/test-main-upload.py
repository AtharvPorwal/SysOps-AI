import docker
import tarfile
import io
import os

def create_and_run_container(image_name="python:3.9"):
    client = docker.from_env()
    try:
        client.images.pull(image_name)
        container = client.containers.run(
            image_name,
            "/bin/bash",
            detach=True,
            tty=True
        )
        print(f"Container {container.short_id} is created and running.")
        return container
    except docker.errors.APIError as e:
        print(f"Error creating container: {e}")
        return None

def run_command_in_container(container, command):
    try:
        exec_result = container.exec_run(command)
        print(f"Command output:\n{exec_result.output.decode()}")
    except docker.errors.APIError as e:
        print(f"Error running command in container: {e}")

def stop_and_remove_container(container):
    try:
        container.stop()
        container.remove()
        print(f"Container {container.short_id} is stopped and removed.")
    except docker.errors.APIError as e:
        print(f"Error stopping or removing container: {e}")

def upload_file_to_container(container, local_file_path, container_path):
    try:
        tar_stream = io.BytesIO()
        with tarfile.open(fileobj=tar_stream, mode='w') as tar:
            tar.add(local_file_path, arcname=os.path.basename(local_file_path))
        tar_stream.seek(0)
        container.put_archive(container_path, tar_stream)
        print(f"File {local_file_path} uploaded to {container_path} in the container.")
    except FileNotFoundError:
        print(f"Error: File {local_file_path} does not exist.")
    except docker.errors.APIError as e:
        print(f"Error uploading file to container: {e}")

def main():
    container = create_and_run_container()
    if not container:
        print("Failed to start Docker container.")
        return

    try:
        while True:
            input_command = input("Enter command to run in Docker container (type 'end' to exit): ")
            if input_command.lower() == "end":
                print("Ending the session...")
                break
            elif input_command.lower().startswith("upload "):
                parts = input_command.split(" ")
                if len(parts) == 3:
                    local_file_path, container_path = parts[1], parts[2]
                    upload_file_to_container(container, local_file_path, container_path)
                else:
                    print("Error: Invalid command format. Use 'upload <local_file_path> <container_path>'.")
            else:
                run_command_in_container(container, input_command)
    finally:
        stop_and_remove_container(container)

if __name__ == "__main__":
    main()