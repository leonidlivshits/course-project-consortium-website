#!/bin/sh

export PROMETHEUS_MULTIPROC_DIR=/tmp/prometheus
mkdir -p "$PROMETHEUS_MULTIPROC_DIR"
find "$PROMETHEUS_MULTIPROC_DIR" -maxdepth 1 -type f -name '*.db' -delete
