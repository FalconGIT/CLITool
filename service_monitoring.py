import argparse
import os
import pandas as pd
import requests
import sys
import time

from config import *


class ServiceMonitoring:

    def __init__(self):
        parser = argparse.ArgumentParser(
            description='Command Line tool for checking the status of the instances and services',
            usage='''ServiceMonitoring <command> [<args>]

The Supported commands are:
   instances     List all the instances and its status
   cpu           Return average CPU of the particular service
   memory        Return average Memory of the particular service
   unhealthy     Return services with status unhealthy

Press CTRL + C for Keyboard interrupt
''')
        parser.add_argument("command", help="List the running instances, average CPU/Memory and unhealthy services")
        args = parser.parse_args(sys.argv[1:2])
        data = sys.argv[2:]
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)
        # using dispatch pattern to invoke method with same name
        getattr(self, args.command)(data)

    def cpu(self, data=None):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                server_data = self._get_data()
                df = pd.DataFrame(server_data, columns=data_headers)
                df['CPU'] = df['CPU'].apply(lambda x: float(x.split()[0].replace('%', '')))
                if data:
                    service = data[0]
                    df = df.loc[df['Service'] == service]
                    df = df.groupby('Service')['CPU'].mean().sort_values(ascending=False)
                else:
                    df = df.groupby('Service')['CPU'].mean().sort_values(ascending=False)
                sys.stdout.write(df.to_markdown())
                time.sleep(refresh_count_in_seconds)
        except KeyboardInterrupt:
            print("Keyboard Interrupt happened")

    def memory(self, data=None):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                server_data = self._get_data()
                df = pd.DataFrame(server_data, columns=data_headers)
                df['Memory'] = df['Memory'].apply(lambda x: float(x.split()[0].replace('%', '')))
                if data:
                    service = data[0]
                    df = df.loc[df['Service'] == service]
                    df = df.groupby('Service')['Memory'].mean().sort_values(ascending=False)
                else:
                    df = df.groupby('Service')['Memory'].mean().sort_values(ascending=False)
                sys.stdout.write(df.to_markdown())
                time.sleep(refresh_count_in_seconds)
        except KeyboardInterrupt:
            print("Keyboard Interrupt happened")

    def unhealthy(self, data=None):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                server_data = self._get_data()
                df = pd.DataFrame(server_data, columns=data_headers)
                df = df.loc[df['Status'] == "unhealthy"]
                if df.shape[0] == 0:
                    print("No Unhealthy Services. All services have more than 2 instances up and running")
                else:
                    sys.stdout.write(df.to_markdown())
                time.sleep(refresh_count_in_seconds)
        except KeyboardInterrupt:
            print("Keyboard Interrupt happened")
            
    def instances(self, data=None):
        try:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                data = self._get_data()
                df = pd.DataFrame(data, columns=data_headers)
                sys.stdout.write(df.to_markdown())
                time.sleep(refresh_count_in_seconds)
        except KeyboardInterrupt:
            print("Keyboard Interrupt happened")

    @staticmethod
    def _get_status(data, service_count_data):
        for i in data:
            service_count = service_count_data.get(i[1])
            if service_count < 2:
                i.append('unhealthy')
            else:
                i.append("healthy")
        return data

    @staticmethod
    def _get_data():
        response = requests.get(f'{base_url}/servers')
        servers = response.json()
        data = []
        health_check_status = {}
        for server in servers:
            server_response = requests.get(f"{base_url}/{server}").json()
            service = server_response.get('service')
            if service in health_check_status:
                health_check_status[service] += 1
            else:
                health_check_status[service] = 1
            data.append(
                [server, server_response.get('service'), server_response.get('cpu'), server_response.get('memory')])
        data = ServiceMonitoring._get_status(data, health_check_status)
        return data


if __name__ == '__main__':
    ServiceMonitoring()
