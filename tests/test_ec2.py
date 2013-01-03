import unittest
import mock


class EC2TestCase(unittest.TestCase):
    def test_choice(self):
        instance = mock.Mock(id="1")
        reservation = mock.Mock(instances=[instance])
        with mock.patch("random.choice") as choice:
            from pantera import chaos
            ec2 = chaos.EC2("ac", "sec")
            ec2.conn = mock.Mock()
            choice.return_value = reservation
            vm = ec2.choice()
        self.assertEqual("1", vm)

    def test_connect(self):
        with mock.patch("boto.ec2.connection.EC2Connection") as ec2con:
            from pantera import chaos
            ec2 = chaos.EC2("ac", "sec")
            ec2.connect()
            ec2con.assert_called_with("ac", "sec")
