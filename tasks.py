from invoke import task


@task
def start(ctx):
    ctx.run("python3 src/index.py")


@task
def test(ctx):
    ctx.run("pytest src")

@task
def test(ctx):
    ctx.run("pytest src")
    
@task
def initdb(ctx):
    ctx.run("python3 src/database/initialize_database.py")


