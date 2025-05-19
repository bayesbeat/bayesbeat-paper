# Real data analyses

## Makefile

The `Makefile` in this directory contains commands to reproduce all of the analyses.
The settings are configured in `config.mk`

All analyses can be submitted by running

```
make
```

in this directory. Alternatively, there are individual commands for each step:

- `make priors.json`: estimate the `deomega` priors for each injections
- `make model_1_constant_noise`: submit analyses with model 1 and constant noise
- `make model_1_amplitude_noise`: submit analyses with model 1 and amplitude and constant noise
- `make model_3`: submit analyses with model 3 and amplitude and constant noise
