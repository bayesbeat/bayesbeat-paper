#!/bin/bash
rm -f analysis plotting results data
ln -s ../analysis analysis
ln -s ../plotting plotting
ln -s ../results results
ln -s ../data data
jupyter-book build .
