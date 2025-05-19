# bayesbeat-paper

Code to reproduce the analyses and results in 'Use of Bayesian Inference to Diagnose Issues in Experimental Measurements of Mechanical Disk Resonators'.

## Data

The simulated and real data are provided in the `data` directory.

## Analyses

Scripts for the analysis of real and simulated data are in separate directories

* `analysis/gens_data`: analysis of real GeNS data
* `analysis/simulated_data` analysis of simulated data

Each directory contains instructions for running the analyses.


### Installation

A conda environment with the required dependencies can be created using the `YAML` file
in the base directory of the repository:

```
conda env create environment.yaml
```

## Figures

Notebooks to reproduce all of the figures in the paper are available in the `plotting`
directory.
