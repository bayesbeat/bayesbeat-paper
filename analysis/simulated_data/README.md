# Simulated data analyses

## Makefile

The `Makefile` in this directory contains commands to reproduce all of the analyses.
The settings are configured in `config.mk`

All analyses can be submitted by running

```
make
```

in this directory. Alternatively, there are individual commands for each step:

- `make <path/to/datafile>`: generate the datafile. Note, the file is included so this shouldn't need to be run.
- `make priors.json`: estimate the `deomega` priors for each injections
- `make model_1_constant_noise`: submit analyses with model 1 and constant noise
- `make model_1_amplitude_noise`: submit analyses with model 1 and amplitude and constant noise
- `make model_3`: submit analyses with model 3 and amplitude and constant noise

Below we explain how to manually run each of the steps.

## Generating data

Data is generated using `bayesbeat_generate_injections`. This takes an ini file
with an `Injection` and a `Noise` section

```python
bayesbeat_generate_injections injections.ini --n-injections 8 --filename data/injections.hdf5
```

Unless specified in `[Injection]`, parameters will be drawn uniformly from the specified prior bounds.

The noise is controlled via the `Noise` section which includes different amplitudes for the different types of noise.

See `injections.ini` for an example ini file.

### Specific injection files

The specific injections were generated using `generate_injections.sh`.
This script produces 50 injections. It also produces plots for each injection

## Analyzing

Analyzing injections is identical to analyzing simulated data; you only need to change the path to the data file.

### Priors

The priors were generated using

```
bayesbeat_estimate_priors <path/to/data/file/> --parameter domega --minimum-domega-width 0.2
```
