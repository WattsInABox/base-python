from invoke import task

use_pty = False
try:
    import pty
    use_pty = True
except:
    print("tasks/base.py: not using pty since your platform does not support it.")

@task
def assemble(ctx):
    pass

@task
def build(ctx):
    return ctx.run("docker-compose build")

@task
def coverage(ctx, container="dev"):
    return ctx.run(f"docker-compose run --rm {container} pytest --cov=app ../test/python")

@task
def deploy(ctx, container="dev"):
    coverage(ctx, container)
    return test_python(ctx, container)

@task
def start(ctx):
    return ctx.run("docker-compose up --remove-orphans -d namenode datanode")

@task
def stop(ctx):
    return ctx.run("docker-compose down")

@task
def test_prep(ctx):
    pass

@task
def test_python(ctx, filter="*", verbose=False, container="dev"):
    command = f"docker-compose run --rm {container} pytest"

    if filter != '*':
        command += f' -k "{filter}"'

    # verbose mode option
    command += " -s -vv" if verbose else ""
    # add the directory where our test files are kept
    command += f" /usr/src/test/python"

    print(command)
    return ctx.run(command, pty=use_pty)

@task
def test(ctx, filter="*", verbose=False):
    """Can pass a filter to specify certain tests to be run
        ex: invoke test --filter=TestCircle
        ex: invoke test --filter=TestC*le
        ex: invoke test --filter=TestSquare,TestC*le

        Can specify verbose output:
        ex: invoke test --verbose=True

        Can turn offline mode off. This slows down tests but allows downloads of new maven plugins / versions
        ex: invoke test --no-offline
    """
    test_python(ctx, filter, verbose)


@task
def install(ctx):
    return docker.install_required_docker_images(ctx)

@task
def run(ctx):
    # runs the default application with default parameters
    return ctx.run("java -cp target/*.jar com.disney.ali.Driver")
