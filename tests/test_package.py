"""Smoke tests confirming the package and its modules import correctly."""

import importlib

import pytest

import pca

MODULES = ["pca", "linalg_utils"]


def test_version_is_defined() -> None:
    assert isinstance(pca.__version__, str)
    assert pca.__version__.count(".") == 2


@pytest.mark.parametrize("module", MODULES)
def test_module_imports(module: str) -> None:
    assert importlib.import_module(f"pca.{module}") is not None
