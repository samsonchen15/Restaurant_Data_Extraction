# Extraction of Restaurant Data from Zomato

`Data_Extraction.py` is a Python script that is designed to extract restaurant data from Zomato and process it into three separate datasets in `.csv` file format. These datasets, which contain various restaurant-related information, are then stored in the `data` folder. The `requirements.txt` consists a list of packages that are required for the Python script to run.

## How to Run

To execute the Python file on your local computer, you'll need to clone the repository and store the file on your local drive.

### Prerequisites

Before you get started, ensure that your computer has the following prerequisites installed:
- [Git](https://git-scm.com/downloads)
- [Python](https://www.python.org/downloads/)

### Instructions

#### Navigate to the Repository Directory:

Launch Git Bash and specify the directory where you want the cloned directory to be located. You can either input `cd` followed by the folder location or conveniently drag and drop the folder into the Git Bash window.
```
$ cd <repository_directory>
```

#### Clone Repository to Local Drive:

This command will download all the files from the repository to your specified local directory.
```
$ git clone https://github.com/samsonchen15/Restaurant_Data_Extraction.git
```

#### Install Dependencies:

The Python script relies on external packages. Execute the following command to install all the required packages listed in the `requirements.txt` file
```
$ pip install -r requirements.txt
```

#### Run Python Script:
Execute the following command to run the source code. The status of the data extraction process will be displayed in the terminal window.

```
$ python Data_Extraction.py
```

## Deployment

The Python script can be deployed on a range of cloud service platforms, including Amazon Web Services (AWS) and Google Cloud Platform (GCP). It can harness the capabilities of cloud computing to streamline and optimize the data extraction process. Some of the key capabilities include:

**Scalability:** Ability to easily scale computing power up or down as needed. This allows the script to handle varying workloads efficiently, even at peak usage, without the constraints of physical hardware.

**Reliability and Availability**: Enable the script to operate seamlessly without being affected by hardware failures or downtime, ensuring consistent and dependable performance. 

**Automated Scheduling**: Schedule and execute code remotely and at regular intervals, ensuring the data remains consistently up-to-date while minimizing the need for manual intervention.

**Data Storage**: Provide various data storage solutions, e.g. SQL Database, to store the extracted data directly in these services for easy access and retrieval.

## Cloud Components

**1) Cloud Data Source**: Establish a connection to an external website, from which the Python script extracts information.

**2) Data Storage**: Provide a cloud-based solution to store data extracted by the script

**3) Computing Resources**: Virtual machines to execute Python script and handle the data extraction process.

**4) Scheduled Task Manager**: Schedule the script to run at regular intervals, with minimal manual intervention.

**5) Monitoring & Logging**:  To track the script performance, errors, and resource utilization.

