# PCA From Scratch

Principal Component Analysis written by hand in Python with NumPy, to understand how it actually works.

## The idea

You have data with lots of features and want to squash it down to a few while losing as little information as possible. PCA does this by finding the directions in which the data is most spread out, then describing each point using only those directions.

1. **Centre** the data: subtract the mean of each feature.
2. **Covariance matrix**: work out how every pair of features varies together.
3. **Eigenvectors** of that matrix are the directions of spread (the principal components). Their eigenvalues say how much spread each one captures.
4. **Sort** the components by eigenvalue and keep the top `k`.
5. **Project** the centred data onto those `k` directions.

The only library shortcut is `np.linalg.eigh` for the eigenvectors. Everything else is written by hand.

## Plan

- [ ] Steps 1 to 5 on the Iris dataset (4 features), plotted in 2D and coloured by species
- [ ] Plot how much of the total variance each component explains
- [ ] Check the result against `sklearn.decomposition.PCA` (components may differ in sign, which is fine)
- [ ] *Optional:* compress images of handwritten digits and see how many components it takes to make them recognisable

## Data

Iris: 150 flowers, 4 measurements each, 3 species. Built into scikit-learn or available as a CSV on Kaggle.

## Running

```bash
pip install -r requirements.txt
python pca.py
```

## Status

Not started.
