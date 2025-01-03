# Use an official Python image as the base
FROM python:3.10

# Install tmux and other utilities
RUN apt-get update && apt-get install -y \
    tmux \
    bash \
    curl \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Set up a working directory for the container
WORKDIR /app

# Copy Python files into the container
COPY . /app

# Default command to start tmux and run the Python script in separate windows
CMD ["tmux", "new-session", "-d", "python3", "terminal1.py", ";", "split-window", "-h", "python3", "terminal2.py", ";", "attach-session"]
