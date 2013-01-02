import unittest
import mock


class ConnectTestCase(unittest.TestCase):
    def test_connect(self):
        with mock.patch("boto.ec2.connection.EC2Connection") as ec2con:
            from pantera import chaos
            chaos.connect("ac", "sec")
            ec2con.assert_called_with("ac", "sec")

