import unittest
import mock


class TerminateTestCase(unittest.TestCase):
    def test_choice(self):
        instance = mock.Mock(id="1")
        reservation = mock.Mock(instances=[instance])
        with mock.patch("random.choice") as choice:
            from pantera import chaos
            terminate = chaos.Terminate("ac", "sec")
            terminate.conn = mock.Mock()
            choice.return_value = reservation
            vm = terminate.choice()
        self.assertEqual("1", vm)

    def test_connect(self):
        with mock.patch("boto.ec2.connection.EC2Connection") as ec2con:
            from pantera import chaos
            terminate = chaos.Terminate("ac", "sec")
            terminate.connect()
            ec2con.assert_called_with("ac", "sec")

    def test_terminate(self):
        from pantera import chaos
        vms = ["1"]
        conn = mock.Mock()
        conn.terminate_instances.return_value = vms
        choice = mock.Mock()
        choice.return_value = "1"
        terminate = chaos.Terminate("access", "secret")
        terminate.connect = mock.Mock()
        terminate.conn = conn
        terminate.choice = choice
        destroyed = terminate.terminate()
        self.assertListEqual(vms, destroyed)

    def test_execute(self):
        from pantera import chaos
        terminate = chaos.Terminate("access", "secret")
        terminate.terminate = mock.Mock()
        terminate.execute()
        terminate.terminate.assert_called_with()
