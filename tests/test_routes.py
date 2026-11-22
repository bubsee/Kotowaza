import unittest

from route_mapping import find_route, nodes


class VillageRoutesTest(unittest.TestCase):
    def test_all_waypoints_can_be_reached_from_each_other(self):
        for start, _ in nodes.values():
            for end, _ in nodes.values():
                with self.subTest(start=start, end=end):
                    route = find_route(start, end)
                    self.assertIsNotNone(route)
                    self.assertEqual(route[0], start)
                    self.assertEqual(route[-1], end)
