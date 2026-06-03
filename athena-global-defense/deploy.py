#!/usr/bin/env python3
import os
import sys
sys.path.insert(0, os.environ['ATHENA_HOME'])
from athena import AthenaCore, SectorApp, DataCollector, DataPurificationEngine, DistributedStorage, DistributedThinkTank, MasterDataCollector

athena = AthenaCore()
athena.mainframes = [f'mainframe-{i:04d}' for i in range(16000)]

sectors = [
    "agriculture", "forestry", "fishing", "mining", "manufacturing",
    "utilities", "construction", "wholesale", "transportation",
    "hospitality", "information", "finance", "professional", "public",
    "education", "healthcare", "arts", "other_services",
    "all_areas_of_work", "custom_area_of_work"
]

for sector in sectors:
    collector = DataCollector(sector)
    storage = DistributedStorage(athena.mainframes, sector, athena.encryption_key)
    thinktank = DistributedThinkTank(f'mainframe-{hash(sector) % 1000:04d}', 2, athena.encryption_key)
    app = SectorApp(f'Athena-{sector}', sector, collector, athena.data_purification, storage, thinktank)
    app.run()

# Master app
collector = MasterDataCollector(athena)
storage = DistributedStorage(athena.mainframes, "master", athena.encryption_key)
thinktank = DistributedThinkTank("mainframe-master", 0, athena.encryption_key)
app = SectorApp("Athena-Master", "master", collector, athena.data_purification, storage, thinktank)
app.run()