#!/bin/bash
exec poetry run uvicorn qqe.fapi:fastapp --reload
