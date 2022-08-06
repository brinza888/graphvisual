import click

from graph import Graph


@click.group()
@click.pass_context
def cli(ctx, **kwargs):
    ctx.ensure_object(dict)
    ctx.obj.update(kwargs)


@cli.command("random", help="Randomly generated graph")
@click.argument("N", required=True, type=click.INT)
@click.option("--fill", default=0.4, help="Edges fill factor", type=click.FLOAT)
@click.option("--weights", default=(1, 10), help="Weights range", type=click.Tuple((click.INT, click.INT)))
@click.pass_context
def random(ctx, n, fill, weights):
    if n == 0:
        click.echo("N must be positive number", err=True)
        return
    window = ctx.obj["window"]
    w_width, w_height = window.window_size
    g = Graph.random(n, w_width//2, w_height//2, w_width//2-50,
                     weights, fill)
    window.set_graph(g)


@cli.command("matrix", help="Graph generated from matrix")
@click.argument("N", required=True, type=click.INT)
@click.pass_context
def from_matrix(ctx, n):
    window = ctx.obj["window"]
    w_width, w_height = window.window_size

    matrix = []
    for i in range(n):
        r = list(map(int, click.prompt(f"{i}").split()))
        matrix.append(r)

    g = Graph.from_matrix(matrix, w_width//2, w_height//2, w_width//2-50)
    window.set_graph(g)


@cli.command("help", help="Show help")
@click.pass_context
def help_(ctx):
    click.echo(cli.get_help(ctx))
