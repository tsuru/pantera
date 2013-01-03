import unittest
import mock


class StopTestCase(unittest.TestCase):
    def test_choice(self):
        instance = mock.Mock(id="1")
        reservation = mock.Mock(instances=[instance])
        with mock.patch("random.choice") as choice:
            from pantera import chaos
            stop = chaos.Stop("ac", "sec")
            stop.conn = mock.Mock()
            choice.return_value = reservation
            vm = stop.choice()
        self.assertEqual("1", vm)

    def test_connect(self):
        with mock.patch("boto.ec2.connection.EC2Connection") as ec2con:
            from pantera import chaos
            stop = chaos.Stop("ac", "sec")
            stop.connect()
            ec2con.assert_called_with("ac", "sec")

    def test_stop(self):
        from pantera import chaos
        vms = ["1"]
        conn = mock.Mock()
        conn.stop_instances.return_value = vms
        choice = mock.Mock()
        choice.return_value = "1"
        stop = chaos.Stop("access", "secret")
        stop.connect = mock.Mock()
        stop.conn = conn
        stop.choice = choice
        destroyed = stop.stop()
        self.assertListEqual(vms, destroyed)

    def test_execute(self):
        from pantera import chaos
        stop = chaos.Stop("access", "secret")
        stop.stop = mock.Mock()
        stop.execute()
        stop.stop.assert_called_with()
