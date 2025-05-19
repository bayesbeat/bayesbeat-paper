# Producing figures

The figures in the paper a produced using the various notebooks included in this
directory. They can either be run individually, or using the provided `Makefile`:

```
make
```

**Note:** using `make` requires `nbconvert` to be installed.

The `Makefile` also includes a rule for making a flat `zip` file with all the plots:

```
make figures.zip
```
