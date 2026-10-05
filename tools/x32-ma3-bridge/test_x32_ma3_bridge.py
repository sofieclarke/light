#!/usr/bin/env python3
"""Unit tests for the bridge. Run: python3 test_x32_ma3_bridge.py"""
import struct
import unittest

from x32_ma3_bridge import Mapper, label_address, osc_message, osc_parse


def cfg(**ma3):
    return {
        "x32": {"ip": "127.0.0.1"},
        "ma3": ma3,
        "faders": [
            {"x32": "/dca/1/fader", "ma3_page": 1, "ma3_exec": 201},
            {"x32": "/dca/2/fader", "ma3_page": 0, "ma3_exec": 202},
            {"x32": "/ch/01/mix/fader", "ma3_page": 3, "ma3_exec": 301, "range": [20, 80]},
            {"x32": "/main/st/mix/fader", "ma3_cmd": "Master 2.1 At {value}"},
        ],
        "buttons": [
            {"x32": "/dca/1/on", "ma3_page": 1, "ma3_exec": 201},
            {"x32": "/dca/2/on", "ma3_cmd": "Go+ Sequence 1"},
        ],
    }


class Osc(unittest.TestCase):
    def test_round_trip(self):
        msg = osc_message("/Page1/Fader201", 42.5, 7, "hello")
        self.assertEqual(len(msg) % 4, 0)
        self.assertEqual(osc_parse(msg), [("/Page1/Fader201", [42.5, 7, "hello"])])

    def test_known_bytes(self):
        # /xremote with no arguments, as every X32 client sends it
        self.assertEqual(osc_message("/xremote"), b"/xremote\0\0\0\0,\0\0\0")

    def test_query_without_type_tags(self):
        self.assertEqual(osc_parse(b"/dca/1/fader\0\0\0\0"), [("/dca/1/fader", [])])

    def test_bundle(self):
        a, b = osc_message("/dca/1/fader", 0.5), osc_message("/dca/1/on", 1)
        bundle = b"#bundle\0" + b"\0" * 8 + struct.pack(">i", len(a)) + a + struct.pack(">i", len(b)) + b
        self.assertEqual(osc_parse(bundle), [("/dca/1/fader", [0.5]), ("/dca/1/on", [1])])


class Mapping(unittest.TestCase):
    def test_fader_scales_to_ma3_range(self):
        m = Mapper(cfg())
        self.assertEqual(m.translate("/dca/1/fader", [0.75]), [("/Page1/Fader201", [75.0])])

    def test_duplicates_are_dropped(self):
        m = Mapper(cfg())
        m.translate("/dca/1/fader", [0.5])
        self.assertEqual(m.translate("/dca/1/fader", [0.5]), [])

    def test_page_zero_means_current_page(self):
        self.assertEqual(Mapper(cfg()).translate("/dca/2/fader", [1.0]), [("/Fader202", [100.0])])

    def test_custom_range(self):
        self.assertEqual(Mapper(cfg()).translate("/ch/01/mix/fader", [0.5]), [("/Page3/Fader301", [50.0])])

    def test_prefix_and_int(self):
        m = Mapper(cfg(prefix="gma3", value_type="int"))
        self.assertEqual(m.translate("/dca/1/fader", [0.333]), [("/gma3/Page1/Fader201", [33])])

    def test_fader_command(self):
        self.assertEqual(Mapper(cfg()).translate("/main/st/mix/fader", [0.5]),
                         [("/cmd", ["Master 2.1 At 50.0"])])

    def test_button_is_a_tap_either_way(self):
        m = Mapper(cfg())
        tap = [("/Page1/Key201", [1]), ("/Page1/Key201", [0])]
        self.assertEqual(m.translate("/dca/1/on", [0]), tap)
        self.assertEqual(m.translate("/dca/1/on", [1]), tap)

    def test_button_command(self):
        self.assertEqual(Mapper(cfg()).translate("/dca/2/on", [1]), [("/cmd", ["Go+ Sequence 1"])])

    def test_unmapped_is_ignored(self):
        self.assertEqual(Mapper(cfg()).translate("/ch/02/mix/fader", [0.5]), [])

    def test_mapping_needs_a_target(self):
        with self.assertRaises(ValueError):
            Mapper({"x32": {"ip": "x"}, "faders": [{"x32": "/dca/1/fader"}]})

    def test_label_address(self):
        self.assertEqual(label_address("/dca/1/fader"), "/dca/1/config/name")
        self.assertEqual(label_address("/ch/01/mix/fader"), "/ch/01/config/name")
        self.assertEqual(label_address("/main/st/mix/fader"), "/main/st/config/name")


if __name__ == "__main__":
    unittest.main()
