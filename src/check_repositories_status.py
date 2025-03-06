import pandas as pd
import os, logging

def setup_logger(log_file="process.log"):
	logging.basicConfig(
		filename=log_file,
		level=logging.INFO,
		format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filemode='a'
	)

def check_maven_build(repo_name):
	try:
		os.chdir(repo_name)
		status = os.system("mvn clean install")

		if status == 0:
			logging.info(f"Build for {repo_name} was successful.")
			return True
		else:
			logging.error(f"Build for {repo_name} failed. Status code: {status}")
			return False
	except Exception as e:
		logging.error(f"An error occurred while running Maven build for {repo_name}: {e}")
		return False
	finally:
		os.chdir("..")

def is_maven_project(repo_name):
	pom_file_path = os.path.join(repo_name, "pom.xml")
	exists = os.path.exists(pom_file_path) and os.path.isfile(pom_file_path)
	logging.info(f"{repo_name} is {'a' if exists else 'not a'} Maven project.")
	return exists

def main():
	
	# Logging configuration
	setup_logger()
	logging.info("Starting process...")
		
	# Assign data
	repository_path = "data/repositories/jsoup-master"

	logging.info(f"Processing repository: {repository_path}")

	if is_maven_project(repository_path):
		check_maven_build(repository_path)
	else:
		logging.warning("not Maven")

if __name__ == "__main__":
    main()