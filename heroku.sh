#!/bin/bash
gunicorn app:app --daemon
python3 worker.py