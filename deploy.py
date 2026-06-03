#!/usr/bin/env python3
"""
Athena Global Defense System - Standalone Deployer
Runs all 20 sector apps + master app with proper initialization.
Equivalent to running athena.py directly.
"""
import os
import sys

# Add project root to path so imports work from anywhere
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from athena import (AthenaCore, SectorApp, DataCollector, DataPurificationEngine,
                    DistributedStorage, DistributedThinkTank, MasterDataCollector,
                    SecurityLevel)

def deploy():
    print("=" * 60)
    print("ATHENA GLOBAL DEFENSE SYSTEM - DEPLOYER")
    print("=" * 60)

    athena = AthenaCore()
    athena.mainframes = [f'mainframe-{i:04d}' for i in range(16000)]
    print(f"Initialized {len(athena.mainframes)} mainframes")

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
        thinktank = DistributedThinkTank(
            f'mainframe-{hash(sector) % 1000:04d}',
            SecurityLevel.SECRET,
            athena.encryption_key
        )
        app = SectorApp(f'Athena-{sector}', sector, collector,
                        athena.data_purification, storage, thinktank)
        athena.apps[sector] = app
        print(f"Created sector app: {sector}")

    # Master app
    master_collector = MasterDataCollector(athena)
    master_storage = DistributedStorage(athena.mainframes, "master", athena.encryption_key)
    master_thinktank = DistributedThinkTank(
        "mainframe-master", SecurityLevel.TOP_SECRET, athena.encryption_key
    )
    master_app = SectorApp("Athena-Master", "master", master_collector,
                           athena.data_purification, master_storage, master_thinktank)
    athena.apps["master"] = master_app
    print("Created master app")

    print("\nRunning all sector applications...")
    from concurrent.futures import ThreadPoolExecutor, as_completed
    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = {executor.submit(app.run): name for name, app in athena.apps.items()}
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                print(f"Error running {futures[future]}: {e}")

    print("\n" + "=" * 60)
    print("ATHENA SYSTEM ACTIVE AND PROTECTING GLOBAL WORKFORCE")
    print("=" * 60)

if __name__ == "__main__":
    deploy()