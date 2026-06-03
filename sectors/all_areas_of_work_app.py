#!/usr/bin/env python3
"""Athena All_areas_of_work Sector Application"""

from athena import SectorApp

class All_areas_of_workApp(SectorApp):
    def __init__(self):
        super().__init__(name="Athena-all_areas_of_work", sector="all_areas_of_work", 
                        data_collector=None, data_purifier=None, 
                        data_storage=None, thinktank=None)
    
    def run(self):
        print(f"Running all_areas_of_work sector app...")
        # Implementation specific to this sector
        super().run()

if __name__ == "__main__":
    app = All_areas_of_workApp()
    app.run()
