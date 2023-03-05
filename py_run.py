import docker


def execute():
    client = docker.from_env()
    client.containers.run("ubuntu:latest", "echo hello world")
