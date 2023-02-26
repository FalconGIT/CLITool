# Service Monitoring CLI Tool

ServiceMonitoring is a Python command line program for querying the Cloud Provider X (CPX).

## Installation

Use the Below Steps to install the requirements

```bash
1. Create a Virtual environment
		
		python -m venv venv

2. Activate the virtual environment
		
		cd venv
		cd Scripts
		activate

3. Install the required modules from requirements.txt
		
		pip install -r requirements.txt

4. To run the CLI tool
		python service_monitoring.py <command>

		For help on the commands, please enter python service_monitoring.py --help
```

## Commands Usage

<instances> - List all the instances running

```python
python service_monitoring.py instances


|     | IP          | Service            | CPU   | Memory   | Status   |
|----:|:------------|:-------------------|:------|:---------|:---------|
|   0 | 10.58.1.64  | IdService          | 33%   | 33%      | healthy  |
|   1 | 10.58.1.105 | RoleService        | 18%   | 46%      | healthy  |
|   2 | 10.58.1.12  | PermissionsService | 34%   | 33%      | healthy  |
|   3 | 10.58.1.47  | PermissionsService | 92%   | 85%      | healthy  |
|   4 | 10.58.1.80  | RoleService        | 24%   | 79%      | healthy  |
|   5 | 10.58.1.74  | TicketService      | 0%    | 66%      | healthy  |
|   6 | 10.58.1.77  | UserService        | 74%   | 36%      | healthy  |
|   7 | 10.58.1.30  | IdService          | 30%   | 96%      | healthy  |
|   8 | 10.58.1.68  | GeoService         | 75%   | 28%      | healthy  |

```

memory -  Return the average Memory of the particular service if the service is provided else return all the services. It's sorted in terms of Memory in descending order

```python
python service_monitoring.py memory

| Service            |   Memory |
|:-------------------|---------:|
| StorageService     |  61.8125 |
| GeoService         |  57.1176 |
| AuthService        |  56.4706 |
| TimeService        |  53.5    |
| RoleService        |  53.44   |
| MLService          |  53.1875 |
| IdService          |  52.6667 |
| TicketService      |  51.25   |
| PermissionsService |  46.5    |
| UserService        |  45.1    |

python service_monitoring.py memory PermissionsService 

| Service            |   Memory |
|:-------------------|---------:|
| PermissionsService |     45.9 |
```

cpu-  Return the average CPU of the particular service if the service is provided else return all the services. It's sorted in terms of CPU in descending order

```python
python service_monitoring.py cpu

| Service            |     CPU |
|:-------------------|--------:|
| UserService        | 63.4    |
| PermissionsService | 53.5    |
| MLService          | 49.1875 |
| TicketService      | 46.5    |
| GeoService         | 45.8235 |
| RoleService        | 44.64   |
| TimeService        | 41      |
| IdService          | 40.6667 |
| AuthService        | 40.3529 |
| StorageService     | 39.5625 |

python service_monitoring.py cpu PermissionsService 

| Service            |   CPU |
|:-------------------|------:|
| PermissionsService |  38.7 |
```

unhealthy - Return services with status unhealthy


```python
python service_monitoring.py unhealthy

No Unhealthy Services. All services have more than 2 instances up and running
