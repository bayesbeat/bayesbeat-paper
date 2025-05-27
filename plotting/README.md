# Producing figures

The figures are produced in various notebooks:

- [Signal model comparison](./plot_signals.ipynb)
- [Results from analyzing simulated data](./plot_real_data_results.ipynb) - this includes plots in the appendices
- [Results from analyzing real data](./plot_real_data_results.ipynb) - this includes plots in the appendices
- [Loss plots](./plot_loss.ipynb)
- [Reparameterization plot (Appendix A)](./plot_reparameterizations.ipynb)
- [Inference cost (Appendix C)](.//plot_inference_cost.ipynb)


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
