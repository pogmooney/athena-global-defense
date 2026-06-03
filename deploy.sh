#!/bin/bash
# Athena Global Defense System Deployment Script
# Three ways to deploy:
#   1. bash deploy.sh       (this script)
#   2. python3 deploy.py    (Python deployer)
#   3. python3 athena.py    (main entry point)

set -e

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
export ATHENA_HOME="$SCRIPT_DIR"

echo "============================================================"
echo "ATHENA GLOBAL DEFENSE SYSTEM - DEPLOYMENT"
echo "============================================================"

python3 "$SCRIPT_DIR/athena.py"

echo "============================================================"
echo "Deployment complete."
echo "============================================================"