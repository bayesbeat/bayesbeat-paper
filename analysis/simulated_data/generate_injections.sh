#!/usr/bin/env python
FILENAME=$1
NINJ=$2
FIGURE_DIR="figures/simulated_data/"
PARAMETERS="parameters.json"
echo Generating $NINJ injections and saving to $FILENAME

bayesbeat_generate_injections \
    injections_config.ini \
    --n-injections $NINJ \
    --filename $FILENAME \
    --parameters $PARAMETERS \
    --seed 42

echo Producing data plots and saving to: $FIGURE_DIR
for i in $(seq 0 $((NINJ-1))); do
    bayesbeat_plot_data \
        $FILENAME \
        --index $i \
        --filename $FIGURE_DIR/data_$i.png
done
