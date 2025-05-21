PATHS_FILE=paths.yml
DATA_RELEASE_NAME=bayesbeat_inference_results
ZENODO_DOI=10.5281/zenodo.15479247

$(DATA_RELEASE_NAME): collate_results.py
	python collate_results.py $(PATHS_FILE) --symlink --output-dir $(DATA_RELEASE_NAME)


$(DATA_RELEASE_NAME).zip: $(DATA_RELEASE_NAME)
	zip -r $(DATA_RELEASE_NAME).zip $(DATA_RELEASE_NAME)

.PHONY: fetch_data_release
fetch_data_release:
	zenodo_get $(ZENODO_DOI) --dest $(DATA_RELEASE_NAME)
	unzip $(DATA_RELEASE_NAME).zip

.PHONY: all clean
all: $(DATA_RELEASE_NAME).zip

clean:
	rm -rf $(DATA_RELEASE_NAME) $(DATA_RELEASE_NAME).zip
