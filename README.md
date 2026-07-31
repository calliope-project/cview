# Calligraph: Calliope model result graphing and visualisation tool

`Calligraph` is a tool to interactively explore and visualise Calliope model results.

> [!IMPORTANT]
> Note that this is pre-release software and there are likely to bugs. Please [report issues and feedback on GitHub](https://github.com/calliope-project/calligraph)!

> [!CAUTION]
> Calligraph only works with Calliope 0.7 or higher. If you are running Calliope 0.6 or lower, use the built-in visualisation tools instead.

## Installation

`pip install calligraph`

## Use

Save a solved Calliope model to a NetCDF file with `model.to_netcdf()` or by using the appropriate settings with the Calliope command-line interface. Then run `calligraph` in the command line:

```shell
$ calligraph your_model_results.nc
```

This launches Calligraph's web interface in the default web browser on your system. To use a custom port, supply the `--port PORTNUMBER` option; if you do not want the default web browser to open, specify `-nb` or `--no-browser`.

To experiment with the built-in urban-scale model:

```python
import calliope
m = calliope.examples.urban_scale(time_subset=None)
m.run()
m.to_netcdf("urban_scale.nc")
```

Then:

```shell
$ calligraph urban_scale.nc
```

## Development

Development environments are managed with [pixi](https://pixi.sh/), which installs
Python, the binary dependencies and the development tooling from a committed lockfile:

```shell
git clone git@github.com:calliope-project/calligraph.git
cd calligraph
pixi install
```

Then:

```shell
pixi run check         # lint, formatting and tests
pixi run test          # tests only
pixi run format        # apply formatting
pixi run docs-serve    # documentation, with live reload
pixi run build         # build the wheel and source distribution
```

`pixi run pre-commit-install` sets up the git hooks, which run the same lint and
formatting checks on commit.

The default environment is Python 3.12. `pixi run -e py310 …` and `-e py311` are the
other supported versions, and CI runs all three.
