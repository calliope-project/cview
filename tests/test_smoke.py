"""Checks that the installed package is usable at all.

These would fail on a broken `[project.scripts]` entry point, on an undeclared
dependency that happens to be missing from a fresh environment, and on an import
error anywhere in the eager `import calligraph.ui` chain that `__init__.py` runs
— all failures that only show up after a release otherwise, since nothing else
in CI imports the package.
"""

from click.testing import CliRunner

import calligraph
from calligraph.cli import calligraph_cli


def test_version_is_reported():
    """`__version__` moved to `_version.py` so hatchling can read it without importing
    the package; `__init__.py` must keep re-exporting it, because `click.version_option`
    and the docs both read it from there."""
    assert calligraph.__version__


def test_cli_help():
    """The entry point resolves and click can build the command."""
    result = CliRunner().invoke(calligraph_cli, ["--help"])
    assert result.exit_code == 0
    assert "PATH" in result.output


def test_cli_requires_an_existing_path():
    """`path` is `click.Path(exists=True)`, so a missing file must fail before the
    server starts rather than opening a browser onto nothing."""
    result = CliRunner().invoke(calligraph_cli, ["does-not-exist.nc"])
    assert result.exit_code != 0
