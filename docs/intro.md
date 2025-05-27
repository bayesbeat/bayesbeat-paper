# Use of Bayesian Inference to Diagnose Issues in Experimental Measurements of Mechanical Disk Resonators

This is the data release for the paper 'Use of Bayesian Inference to Diagnose Issues in Experimental Measurements of Mechanical Disk Resonators', which can be found [here](https://arxiv.org/abs/2505.17346).


```{admonition} Work in progress
This page is still a work in progress and will be updated once the article is published.
```

## Cloning the git repository

The git repository that contains all the files to reproduce the analyses can
be cloned using

```
git clone git@github.com:mj-will/bayesbeat-paper.git
```

## Configuring the environment

After cloning the repository, run the following command from the command line:

```bash
conda env create environment.yml
```
For instructions on how to install `conda` see [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).

## Ringdown Data

In the [data](data/README.md) section we described the ringdown data included in the data release and how it can be read using
functions provided in `bayesbeat`

## Analyses

We provide scripts to reproduce all of the analyses described in the paper. These are divided between:

- [Analyses using simulated data(analysis/simulated_data/README.md)
- [Analyses using real data](analysis/gens_data/README.md)

See each section for further details.

## Results

We provided notebooks to reproduce all of the results and figures in the paper.

### Downloading results

The results produced for the paper in available via Zenodo at this DOI:

They can also be downloaded using the `download_results.sh` script in the root directory of the repository:

```bash
bash download_results.sh
```

### Reproducing figures

See [this page](plotting/README.md) for instructions on how to reproduce the
results.
