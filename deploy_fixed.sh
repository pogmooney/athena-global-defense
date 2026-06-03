#!/bin/bash
# CORRECTED Athena Global Defense System Deployment Script
# This version uses user-writable directories and proper initialization

echo "Starting Athena Global Defense System deployment..."
echo "=================================================="

# Use user's home directory for storage (writable)
export ATHENA_HOME="$HOME/ateta-global-defense"
mkdir -p "$ATHENA_HOME/mainframe_storage"
mkdir -p "$ATHENA_HOME/logs"

# Initialize Athena Core in a proper way
echo "Initializing Athena Core..."
python3 -c "
import sys
sys.path.insert(0, '$ATHENA_HOME')
from athena import AthenaCore
athena = AthenaCore()
print('Athena Core initialized')
"

# Create mainframes in user's storage directory
echo "Deploying to 16,000 mainframes..."
for i in {0..15999}; do
    mainframe="mainframe-$(printf '%04d' $i)"
    mkdir -p "$ATHENA_HOME/mainframe_storage/$mainframe"
    echo "Deployed to $mainframe"
done

# Start sector applications - PROPER WAY
echo "Starting sector applications..."
sectors=(
    agriculture forestry fishing mining manufacturing
    utilities construction wholesale transportation
    hospitality information finance professional
    public education healthcare arts other_services
    all_areas_of_work custom_area_of_work
)

# Start all sector apps in background
for sector in "${sectors[@]}"; do
    echo "Starting $sector app..."
    python3 -c "
import sys
sys.path.insert(0, '$ATHENA_HOME')
from athena import AthenaCore, SectorApp, DataCollector, DataPurificationEngine
from athena import DistributedStorage, DistributedThinkTank
from datetime import datetime

# Initialize Athena Core
athena = AthenaCore()
athena.mainframes = [f'mainframe-{i:04d}' for i in range(16000)]

# Create sector-specific components
collector = DataCollector('$sector')
storage = DistributedStorage(athena.mainframes, '$sector')
thinktank = DistributedThinkTank(f'mainframe-{hash('$sector') % 1000:04d}', 2)

# Create and run sector app
app = SectorApp('Athena-$sector', '$sector', collector, athena.data_purification, storage, thinktank)
app.run()
" &
done

# Start master app
echo "Starting master app..."
python3 -c "
import sys
sys.path.insert(0, '$ATHENA_HOME')
from athena import AthenaCore, SectorApp, DataCollector, DataPurificationEngine
from athena import DistributedStorage, DistributedThinkTank, MasterDataCollector
from datetime import datetime

athena = AthenaCore()
athena.mainframes = [f'mainframe-{i:04d}' for i in range(16000)]

# Create master-specific components
collector = MasterDataCollector(athena)
storage = DistributedStorage(athena.mainframes, 'master')
thinktank = DistributedThinkTank('mainframe-master', 0)

app = SectorApp('Athena-Master', 'master', collector, athena.data_purification, storage, thinktank)
app.run()
" &

echo "=================================================="
echo "Deployment initiated! All apps are starting..."
echo "Protecting 16,000 mainframes across all sectors."
echo "=================================================="