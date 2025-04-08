# Makefile for simulated data analysis
include config.mk

.PHONY: all
all: model_1_amplitude_noise model_1_constant_noise model_3

priors.json: $(DATAFILE)
	bayesbeat_estimate_priors $(DATAFILE) priors.json --parameter domega


.PHONY: model_1_constant_noise model_1 model_3

model_1_constant_noise: priors.json
	bayesbeat_build model_1_constant_noise.ini --submit

model_1_amplitude_noise: priors.json
	bayesbeat_build model_1.ini --submit

model_3: priors.json
	bayesbeat_build model_3.ini --submit
