#!/bin/bash
# Athena Global Defense System Deployment Script

echo "Starting Athena Global Defense System deployment..."
echo "=================================================="

# Set the base directory
export ATHENA_HOME="$HOME/athena-global-defense"

# Run the Python deployment script
python3 "$ATHENA_HOME/deploy.py"

echo "=================================================="
echo "Deployment initiated! All apps are starting..."
echo "Protecting 16,000 mainframes across all sectors."
echo "=================================================="