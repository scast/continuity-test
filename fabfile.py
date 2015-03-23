from fabric.api import env, run
from dockerfabric.apiclient import docker_fabric
from dockermap.api import DockerClientWrapper, MappingDockerClient
from continuity import bootstrap_environment
from continuity import tasks as continuity

@bootstrap_environment('production')
def production():
    """Remote production environment"""
    env.forward_agent = True
    env.docker = docker_fabric()
    env.run = run
    env.roledefs = {
        'web': ['{user}@{site_url}'.format(**env)],
    }


@bootstrap_environment('development')
def development():
    """Remote staging/development environment"""
    env.forward_agent = True
    env.docker = docker_fabric()
    env.run = run
    env.roledefs = {
        'web': ['{user}@{site_url}'.format(**env)],
    }

@bootstrap_environment('testing')
def testing():
    """Local testing environment"""
    env.docker = DockerClientWrapper('unix://var/run/docker.sock')
    env.run = local

@bootstrap_environment('local')
def locally():
    """Local development environment"""
    env.docker = DockerClientWrapper('unix://var/run/docker.sock')
    env.run = local
