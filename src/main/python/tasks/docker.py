from invoke import task

@task
def list_containers(ctx):
    return ctx.run("docker ps -a -q")

# @todo
@task
def remove_all_containers(ctx):
    pass

# @todo
@task
def remove_all_images(ctx):
    pass

@task
def remove_dangling_containers(ctx):
    return ctx.run("docker container prune")

@task
def remove_dangling_images(ctx):
    return ctx.run("docker image prune")

# @todo
@task
def remove_networks(ctx):
    pass

# @todo
@task
def remove_volumes(ctx):
    pass

@task
def stop_containers(ctx):
    processes_result = list_containers(ctx)
    processes = processes_result.stdout.splitlines()

    if processes:
        return ctx.run("docker stop {0}".format(' '.join(processes)))

@task
def install_required_docker_images(ctx):
    return ctx.run("docker-compose build")

@task
def implode(ctx):
    stop_containers(ctx)
    remove_all_containers(ctx)
    remove_all_images(ctx)
    remove_networks(ctx)
    remove_volumes(ctx)
