.PHONY: all
all: build

../results/bayesbeat_inference_results:
	cd ../results && make fetch_data_release

.PHONY: build
build: ../results/bayesbeat_inference_results
	bash build.sh


.PHONY: clean
clean:
	rm -rf _build
	rm -rf _source
