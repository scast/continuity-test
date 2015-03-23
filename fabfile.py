from fabric.api import env, run, task, local
from dockerfabric.apiclient import docker_fabric
from dockermap.api import DockerClientWrapper, MappingDockerClient
from continuity import bootstrap_environment
from continuity import tasks as continuity

@task
def production():
    """Remote production environment"""
    bootstrap_environment('production')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.forward_agent = True
    env.docker = docker_fabric()
    env.run = run
    env.roledefs = {
        'web': ['{user}@{site_url}'.format(**env)],
    }


@task
def development():
    """Remote staging/development environment"""
    bootstrap_environment('development')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.forward_agent = True
    env.docker = docker_fabric()
    env.run = run
    env.roledefs = {
        'web': ['{user}@{site_url}'.format(**env)],
    }

@task
def testing():
    """Local testing environment"""
    bootstrap_environment('testing')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.docker = DockerClientWrapper('unix://var/run/docker.sock')
    env.run = local

@task
def locally():
    """Local development environment"""
    bootstrap_environment('local')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.docker = DockerClientWrapper('unix://var/run/docker.sock')
    env.run = local
