import unittest

from service_monitoring import ServiceMonitoring


class TestServiceMonitoring(unittest.TestCase):

    def test_get_data(self):
        data = ServiceMonitoring._get_data()
        assert isinstance(data, list)

    def test_get_status(self):
        health_check_status = {'Service_name': 3}
        data = [['0.0.0.0', 'Service_name', '20%', '50%']]
        data = ServiceMonitoring._get_status(data, health_check_status)
        assert len(data[0]) == 5
        assert data[0][4] == 'healthy'


if __name__ == '__main__':
    unittest.main()
