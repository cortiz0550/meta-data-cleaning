import os.path
import csv
import glob
import pandas as pd


already_recorded_folder = "C:\\Users\\E33100\\OneDrive - SRI International\\My Stuff\\General Qx Surveys\\Meta Data\\Already Recorded Datasets"
datasets_folder = "C:\\Users\\E33100\\OneDrive - SRI International\\My Stuff\\General Qx Surveys\\Meta Data\\Original Datasets\\"
trimmed_folder = "C:\\Users\\E33100\\OneDrive - SRI International\\My Stuff\\General Qx Surveys\\Meta Data\\Trimmed Datasets\\"
datasets = glob.glob(os.path.join(datasets_folder, "*.csv"))

# These are the fields we want to track across all data we download.
fields_to_keep = ["Progress",
				  "Duration (in seconds)",
				  "Finished",
				  "RecordedDate",
				  "ResponseId",
				  "LocationLatitude",
				  "LocationLongitude",
				  "DistributionChannel",
				  "UserLanguage",
				  "meta_info_Browser",
				  "meta_info_Version",
				  "meta_info_Operating System",
				  "meta_info_Resolution"]

# We loop through each dataset, and then remove any columns we don't want.
# Next we save each trimmed dataset to a new folder, which can be added to our "hot" folder for tracking.
for dataset in datasets:
	print(dataset)
	trimmed_name = dataset
	title = dataset.split("\\")[-1]
	csv_df = pd.read_csv(dataset)
	trimmed_df = csv_df[csv_df.columns & fields_to_keep]
	trimmed_df = trimmed_df.drop([0, 1])
	
	# Save the trimmed csv to a new folder to be used for analysis
	trimmed_df.to_csv(os.path.join(trimmed_folder, title))

	# This moves the original datasets into an archive folder so we are not continuously adding them to our "hot" folder.
	# This will save time as we get more datasets to input.
	if(os.path.exists(trimmed_name)):
		os.replace(dataset, os.path.join(already_recorded_folder, title))


