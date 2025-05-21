# Results

This directory contains scripts for producing the data release files.

## Producing the data release

The data release is produced using the `Makefile` included in this directory.
This automatically collects the results as specified in the `paths.yml` file
into a single directory that is then compressed into a single ZIP file.

To collate the results and produce the ZIP file, run:

```
make
```

To just collate the results run:

```
make bayesbeat_inference_results
```

**Note: this step must be run before running any of the plotting notebooks

### Result collation

The results are collated into a single file using the `collate_results.py`
scripts which is run from the command line

```bash
python collate_results.py paths.yml --symlink --output-dir bayesbeat_inference_results
```

The `--symlink` options ensures the results are linked rather than copied and `--output-dir`
specifies the name of the output directory. The script also supports a `--flatten` option which
removed the nested directories.

## Downloading the data release

The data release can be downloaded directly from Zenodo or using [`zenodo_get`](https://github.com/dvolgyes/zenodo_get).
The `Makefile` includes a command to do this:

```
make fetch_data_release
```

**Note:** this command will overwrite any results already collected using the steps
described above.


Alternatively, one can run the steps manually:

```
zenodo_get 10.5281/zenodo.15479247
```

Once downloaded, unzip the data release using e.g. zip:

```
unzip bayesbeat_inference_results.zip
```

For details about the data release structure, see the [Zenodo record](10.5281/zenodo.15479247)
