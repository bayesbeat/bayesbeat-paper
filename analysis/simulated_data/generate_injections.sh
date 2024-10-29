#!/usr/bin/env python
NINJ=50
FILENAME="data/injections_dataset.hdf5"
FIGURE_DIR="figures"
echo Generating $NINJ injections and saving to $FILENAME

bayesbeat_generate_injections \
    injections_config.ini \
    --n-injections $NINJ \
    --filename $FILENAME \
    --seed 42

echo Producing data plots and saving to: $FIGURE_DIR
for i in $(seq 0 $((NINJ-1))); do
    bayesbeat_plot_data \
        $FILENAME \
        --index $i \
        --filename $FIGURE_DIR/data_$i.png
done
