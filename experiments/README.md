# Experiments

Standalone scripts that reproduce the figures in the project README. Each script
accepts a `--seed` argument and saves its output to `../figures/`.

Run any script with:

```bash
uv run python experiments/<script>.py --seed 0
```

## Planned scripts

- `iris_projection.py` — two-dimensional projection coloured by class
- `wine_scaling.py` — effect of standardisation on the principal components
- `digits_compression.py` — reconstruction quality against number of components
- `eigenfaces.py` — eigenfaces and nearest-neighbour face matching
