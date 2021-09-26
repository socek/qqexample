#!/bin/bash
exec poetry run celery -A cworker worker
