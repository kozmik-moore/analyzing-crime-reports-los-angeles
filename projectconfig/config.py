from pathlib import Path
from os.path import join

# Directory paths
root_dir = Path('..')
data_dir = Path(join(root_dir, 'data'))
asset_dir = Path(join(root_dir, 'assets'))
notebook_dir = Path(join(root_dir, 'notebooks'))
script_dir = Path(join(root_dir, 'scripts'))

# File paths
raw_data_path = join(data_dir, 'raw', 'crimes.csv')
processed_data_path = join(data_dir, 'processed', 'crimes_processed.csv')
crime_desc_table_orig = join(data_dir, 'generated', 'crime_descriptions_orig.md')
crime_desc_table_new = join(data_dir, 'generated', 'crime_descriptions_new.md')
victim_sex_table = join(data_dir, 'generated', 'victim_sex_records.md')