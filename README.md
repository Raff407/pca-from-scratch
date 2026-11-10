# Principal Component Analysis From Scratch

[![CI](https://github.com/Raff407/pca-from-scratch/actions/workflows/ci.yml/badge.svg)](https://github.com/Raff407/pca-from-scratch/actions/workflows/ci.yml)
![Python](https://img.shields.io/badge/python-3.12%20%7C%203.13-blue)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-in%20development-orange)

A NumPy-only implementation of Principal Component Analysis using both eigendecomposition of the covariance matrix and singular value decomposition, applied to visualisation, image compression and eigenfaces.

> **Status:** in development. The repository structure, tooling and test infrastructure are in place; implementation is proceeding stage by stage according to the roadmap below.

## Contents

- [Overview](#overview)
- [Features](#features)
- [Mathematical background](#mathematical-background)
- [Roadmap](#roadmap)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
- [Experiments](#experiments)
- [Design principles](#design-principles)
- [References](#references)
- [License](#license)

## Overview

Principal Component Analysis finds an orthogonal basis in which the variance of the data is concentrated in as few directions as possible. This project implements a `PCA` estimator with `fit`, `transform`, `inverse_transform`, `fit_transform` and `explained_variance_ratio_`, using two independent solvers that are tested against each other and against scikit-learn (up to the sign ambiguity of eigenvectors).

The estimator is then applied to progressively richer problems: two-dimensional visualisation of Iris, the effect of feature scaling on Wine, compression and reconstruction of handwritten digits, and the classical eigenfaces method for face representation and nearest-neighbour matching.

## Features

- Covariance-based solver using `np.linalg.eigh` on the symmetric covariance matrix
- SVD-based solver on the centred data matrix (no explicit covariance)
- Explained-variance ratios, scree plots and selection of k by variance threshold
- Reconstruction via `inverse_transform` and reconstruction-error analysis
- Eigenfaces on the Olivetti faces dataset with nearest-neighbour matching
- Sign alignment utilities for deterministic comparison of components

## Mathematical background

Let $X \in \mathbb{R}^{n \times d}$ contain $n$ samples.

| Step | Definition |
|---|---|
| Centre | $X_c = X - \bar{x}$ |
| Covariance | $C = \frac{1}{n-1} X_c^\top X_c$ |
| Eigendecomposition | $C = V \Lambda V^\top$ |
| Projection | $Z = X_c V_k$ |
| Reconstruction | $\hat{X} = Z V_k^\top + \bar{x}$ |
| Explained variance ratio | $\lambda_i / \sum_j \lambda_j$ |
| SVD route | $X_c = U \Sigma V^\top,\quad \lambda_i = \sigma_i^2 / (n-1)$ |

Full derivations are recorded in [`docs/derivations.md`](docs/derivations.md).

## Roadmap

- [ ] **Stage 1: Covariance from scratch.** Centring and covariance matching `np.cov` to 1e-10.
- [ ] **Stage 2: Eigendecomposition PCA.** Iris projected to two dimensions; components and variance ratios tested against scikit-learn.
- [ ] **Stage 3: Choosing k.** Scree plot, cumulative explained variance, standardised vs raw features on Wine.
- [ ] **Stage 4: SVD solver.** Equivalence with the eigen solver; timing and numerical-conditioning comparison.
- [ ] **Stage 5: Compression and reconstruction.** Digits and MNIST reconstructions for varying k; principal axes visualised as images.
- [ ] **Stage 6: Eigenfaces.** Mean face, top eigenfaces, held-out reconstruction and nearest-neighbour matching accuracy against k.
- [ ] **Stage 7: Packaging.** Validated public API; ≥ 80% coverage.

## Project structure

```text
pca-from-scratch/
├── .github/workflows/ci.yml   # Lint, format check and tests on Python 3.12 / 3.13
├── data/                      # Downloaded datasets (git-ignored)
├── docs/derivations.md        # Mathematical derivations
├── experiments/               # Reproducible scripts that generate figures
├── figures/                   # Saved plots referenced in this README
├── src/
│   └── pca/
│       ├── __init__.py      # Package metadata
│       ├── pca.py           # PCA estimator with eigendecomposition and SVD solvers, transform and inverse_transform
│       └── linalg_utils.py  # Centring, covariance and eigenvector sign alignment
├── tests/                     # pytest suite
├── pyproject.toml             # Packaging and tool configuration
└── uv.lock                    # Locked dependency versions
```

## Getting started

### Prerequisites

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)

### Installation

```bash
git clone https://github.com/Raff407/pca-from-scratch.git
cd pca-from-scratch
uv sync
```

### Running the tests

```bash
uv run pytest
```

### Linting and formatting

```bash
uv run ruff check .
uv run ruff format .
```

## Experiments

Each script in [`experiments/`](experiments/) is deterministic given its seed and writes its output to [`figures/`](figures/).

- `iris_projection.py` — two-dimensional projection coloured by class
- `wine_scaling.py` — effect of standardisation on the principal components
- `digits_compression.py` — reconstruction quality against number of components
- `eigenfaces.py` — eigenfaces and nearest-neighbour face matching

Results and figures will be added to this section as each stage is completed.

## Design principles

- **From scratch.** The algorithm itself uses only Python and NumPy. scikit-learn (and, where noted, PyTorch) is used solely as a reference implementation in tests and for loading datasets.
- **Test-driven.** Each stage begins with a failing test against a hand-computed value or a reference implementation. Target coverage is at least 80%.
- **No mutation.** Public functions return new arrays and objects and never modify their inputs.
- **Reproducible.** Every stochastic routine and experiment accepts an explicit random seed.
- **Validated boundaries.** Public functions check input shapes and dtypes and fail with clear error messages.

## References

1. J. Shlens — *A Tutorial on Principal Component Analysis* (2014). <https://arxiv.org/abs/1404.1100>
2. M. P. Deisenroth, A. A. Faisal, C. S. Ong — *Mathematics for Machine Learning*, ch. 4 and 10. <https://mml-book.github.io>
3. M. Turk, A. Pentland — *Eigenfaces for Recognition*, Journal of Cognitive Neuroscience 3(1), 1991.
4. G. Strang — MIT 18.06 Linear Algebra. <https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/>
5. scikit-learn — Decomposition user guide. <https://scikit-learn.org/stable/modules/decomposition.html#pca>

## License

Released under the [MIT License](LICENSE).
