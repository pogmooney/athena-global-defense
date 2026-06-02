#!/usr/bin/env python3
"""Master Deployment Script for All Areas Of Work Suite"""

import subprocess
import sys
import os
import json
import hashlib
import base64
import random
import string
import time
import requests
import logging
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
# The athena module is in the ../athena-global-defense directory
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "..", "athena-global-defense")))

# Import from core Athena system
from athena import WorkerData, DataPurificationEngine, DistributedStorage, DistributedThinkTank

# List of apps to deploy
APPS = [
    "agriculture",
    "forestry",
    "fishing",
    "mining",
    "manufacturing",
    "utilities",
    "construction",
    "wholesale",
    "transportation",
    "hospitality",
    "information",
    "finance",
    "professional",
    "public",
    "education",
    "healthcare",
    "arts",
    "other_services",
    "all_areas_of_work",
    "custom_area_of_work"
]

def run_app(app_name):
    """Run a single app"""
    print(f"\n{'='*60}")
    print(f"DEPLOYING {app_name.upper().replace('_', ' ')} - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*60}")
    
    try:
        # Run the app from its subdirectory
        result = subprocess.run(
            ["python3", f"apps/{app_name}/app.py"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        if result.returncode == 0:
            print(f"✓ {app_name} deployed successfully")
            return True
        else:
            print(f"✗ {app_name} deployment failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ {app_name} error: {e}")
        return False

def main():
    """Main deployment function"""
    print("\nDEPLOYING ALL AREAS OF WORK SUITE")
    print("=" * 60)
    
    success_count = 0
    failure_count = 0
    
    for app in APPS:
        if run_app(app):
            success_count += 1
        else:
            failure_count += 1
    
    print("\n" + "=" * 60)
    print(f"DEPLOYMENT COMPLETE: {success_count}/{len(APPS)} apps deployed successfully")
    print(f"Successful: {success_count}, Failed: {failure_count}")
    print("=" * 60)

if __name__ == "__main__":
    main()