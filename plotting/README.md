# Producing figures

The figures are produced in various notebooks:

- [Notebook for producing Figure 4](./plot_signals.ipynb)


```{important}
If running these locally, make sure you have downloaded the data release.
See [Downloading the data release](results/README.md#downloading-the-data-release).
```

## Reproducing all figures

The `Makefile` include in this directory can used to reproduce the figures
in the paper. To do so, run the following command in the directory:

```
make
```

**Note:** using `make` requires `nbconvert` to be installed.

The `Makefile` also includes a rule for making a flat `zip` file with all the plots:

```
make figures.zip
```
