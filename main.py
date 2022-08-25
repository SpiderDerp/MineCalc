import click


__author__ = "SpiderDerp"

@click.group()
def main():
    """
    Simple CLI for calculating things related to Minecraft!
    """
    pass

@main.command()
@click.argument('coords', nargs=2)
def ow2ne(coords):
    """This converts Overworld coordinates to Nether Coordinates\n
    Example: python main.py ow2ne x z"""

    coords_params = {
        'x': float(coords[0]),
        'z': float(coords[1])
    }

    response = "X: {}\nZ: {}".format(coords_params['x']/8, coords_params['z']/8)

    click.echo(response) 

@main.command()
@click.argument('coords', nargs=2)
def ne2ow(coords):
    """This converts Nether coordinates to Overworld Coordinates\n
    Example: python main.py ne2ow x z"""

    coords_params = {
        'x': float(coords[0])*8,
        'z': float(coords[1])*8
    }

    response = "X: {}\nZ: {}".format(coords_params['x'], coords_params['z'])

    click.echo(response)

if __name__ == "__main__":
    main()