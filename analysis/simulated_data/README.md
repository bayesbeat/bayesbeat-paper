# Simulated data analyses

## Generating data

Data is generated using `bayesbeat_generate_injections`. This takes an ini file
with an `Injection` and a `Noise` section

```python
bayesbeat_generate_injections injections.ini --n-injections 8 --filename data/injections.hdf5
```

Unless specified in `[Injection]`, parameters will be drawn uniformly from the specfied prior bounds.

The noise is controlled via the `Noise` section which includes different amplitudes for the different types of noise.

See `injections.ini` for an example ini file.

## Analyzing

Analyzing injections is identical to analyzing simulated data; you only need to change the path to the data file.
