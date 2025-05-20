# Data

We provide two data files:

- `PyTotalAnalysis_2024_02_23.mat`: this contains the real data obtained using the GeNS techniques
- `simulated_data.hdf5`: this contains the simulated data used in the paper. See the [simulated data documentation](../analysis/simulated_data/README.md#generating-data) for details on how the data was generated.


## Reading the data

A ringdown can be loaded from the datafiles using a function included in `bayesbeat`

```python
from bayesbeat.data import get_data

x_data, y_data, frequency, _ = get_data(data_file, index=index)
```
where `index` specifies which of the ringdowns to load.