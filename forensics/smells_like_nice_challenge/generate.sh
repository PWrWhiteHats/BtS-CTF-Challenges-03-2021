#!/usr/bin/env bash
cd files && \
python generate_image.py && \
python -m pysstv --mode Robot36 flag.png flag.wav && \
python generate_challenge.py