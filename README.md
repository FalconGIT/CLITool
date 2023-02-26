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

<instances> - List all the instances running with optional instances names as filter

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

```python
python service_monitoring.py instances IdService TimeService

|     | IP          | Service     | CPU   | Memory   | Status   |
|----:|:------------|:------------|:------|:---------|:---------|
|  10 | 10.58.1.85  | TimeService | 87%   | 71%      | healthy  |
|  12 | 10.58.1.86  | IdService   | 82%   | 18%      | healthy  |
|  14 | 10.58.1.40  | IdService   | 14%   | 3%       | healthy  |
|  24 | 10.58.1.38  | TimeService | 81%   | 90%      | healthy  |
|  25 | 10.58.1.117 | IdService   | 34%   | 95%      | healthy  |
|  29 | 10.58.1.14  | IdService   | 94%   | 13%      | healthy  |
|  42 | 10.58.1.133 | IdService   | 12%   | 7%       | healthy  |
|  45 | 10.58.1.58  | TimeService | 23%   | 11%      | healthy  |
|  49 | 10.58.1.96  | IdService   | 72%   | 22%      | healthy  |

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

	
## Assumption

The following are the assumptions made while building the CLI Tool

	1. Health Status - If there are less than 2 instances running for a service, the status is unhealthy		
	2. Max Traffic the cox server can handle - Currently we are hitting the APIs every 5 seconds to refresh the monitoring status (the time interval can be configured in the config file)
	3. Based on assumption 2 where cpx server can handle multiple requests or load, we are not persisting the data in any persistent data store or cache

	
## Improvements

The following improvements can be made to the CLI Tool in the future based on the additional requirements that may pop up

	1. Persiting the cpx server endpoints data in a cache and refreshing the cache every 5 seconds.		
	2. New Services added or exisitng services if went down can be found by comparing the historic data from cache. This can be used for Alerting if any services are down
	3. GUI - Instead of CLI montioring, a dashboard can be built for better user experience.
