# Derivations — Principal Component Analysis From Scratch

This document records the mathematical derivations underpinning the implementation,
written out in full before the corresponding code.

## Summary of results

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

## Stage 1: Covariance from scratch

_To be completed._

## Stage 2: Eigendecomposition PCA

_To be completed._

## Stage 3: Choosing k

_To be completed._

## Stage 4: SVD solver

_To be completed._

## Stage 5: Compression and reconstruction

_To be completed._

## Stage 6: Eigenfaces

_To be completed._

## Stage 7: Packaging

_To be completed._
