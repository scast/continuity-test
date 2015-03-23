from fabric.api import env, run, task, local
from dockerfabric.apiclient import docker_fabric, container_fabric
from dockermap.api import DockerClientWrapper, MappingDockerClient
from continuity import bootstrap_environment
from continuity import tasks as continuity

@task
def production():
    """Remote production environment"""
    env.docker = docker_fabric()
    bootstrap_environment('production')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.forward_agent = True
    env.map_client = container_fabric(env.container_map)
    env.run = run
    env.roledefs = {
        'web': ['{user}@{site_url}'.format(**env)],
    }


@task
def development():
    """Remote staging/development environment"""
    env.docker = docker_fabric()
    bootstrap_environment('development')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.forward_agent = True
    env.map_client = container_fabric(env.container_map)
    env.run = run
    env.roledefs = {
        'web': ['{user}@{site_url}'.format(**env)],
    }

@task
def testing():
    """Local testing environment"""
    env.docker = DockerClientWrapper('unix://var/run/docker.sock')
    bootstrap_environment('testing')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.map_client = MappingDockerClient(env.container_map,
                                         env.container_config,
                                         clients={'__default__': env.container_config})
    env.run = local

@task
def locally():
    """Local development environment"""
    env.docker = DockerClientWrapper('unix://var/run/docker.sock')
    bootstrap_environment('local')
    env.project_path = '/home/{user}/jenkins-test'.format(**env)
    env.map_client = MappingDockerClient(env.container_map,
                                         env.container_config,
                                         clients={'__default__': env.container_config})
    env.run = local
