"""CSC148 Assignment 1: Sample tests

=== CSC148 Fall 2019 ===
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for the Assignment.

Warning: This is an extremely incomplete set of tests!

Note: this file is to only help you; you will not submit it when you hand in
the assignment.

Author: Anshul Agrawal
"""
from io import StringIO
from simulation import GroceryStoreSimulation

CONFIG_FILE = '''{
  "regular_count": 1,
  "express_count": 0,
  "self_serve_count": 0,
  "line_capacity": 1
}
'''

EVENT_FILE = '''10 Arrive Tamara Bananas 7
5 Arrive Jugo Bread 3 Cheese 3
'''


def test_simulation() -> None:
    """Test two events and single checkout simulation."""
    gss = GroceryStoreSimulation(StringIO(CONFIG_FILE))
    stats = gss.run(StringIO(EVENT_FILE))
    assert stats == {'num_customers': 2, 'total_time': 18, 'max_wait': 8}

def test_config_111_10_events_mixtures() -> None:
    config_file = open('input_files/config_111_10.json')
    sim = GroceryStoreSimulation(config_file)
    config_file.close()
    event_file = open('input_files/events_mixtures.txt')
    sim_stats = sim.run(event_file)
    event_file.close()
    assert sim_stats == {'num_customers': 16, 'total_time': 390, 'max_wait': 266}

def test_config_111_10_events_one_close() -> None:
    config_file = open('input_files/config_111_10.json')
    sim = GroceryStoreSimulation(config_file)
    config_file.close()
    event_file = open('input_files/events_one_close.txt')
    sim_stats = sim.run(event_file)
    event_file.close()
    assert sim_stats == {'num_customers': 4, 'total_time': 21, 'max_wait': 18}

def test_config_001_10_events_base() -> None:
    # All lines close before all customers arrive causing infinite loop.
    pass

def test_config_001_10_events_mixtures() -> None:
    # All lines close before all customers arrive causing infinite loop.
    pass

def test_config_001_10_events_one_close() -> None:
    # All lines close before all customers arrive causing infinite loop.
    pass

def test_config_001_10_events_one() -> None:
    config_file = open('input_files/config_001_10.json')
    sim = GroceryStoreSimulation(config_file)
    config_file.close()
    event_file = open('input_files/events_one.txt')
    sim_stats = sim.run(event_file)
    event_file.close()
    assert sim_stats == {'num_customers': 1, 'total_time': 72, 'max_wait': 62}

def test_config_001_10_events_one_at_a_time() -> None:
    config_file = open('input_files/config_001_10.json')
    sim = GroceryStoreSimulation(config_file)
    config_file.close()
    event_file = open('input_files/events_one_at_a_time.txt')
    sim_stats = sim.run(event_file)
    event_file.close()
    assert sim_stats == {'num_customers': 3, 'total_time': 24, 'max_wait': 6}

def test_config_001_10_events_two() -> None:
    config_file = open('input_files/config_001_10.json')
    sim = GroceryStoreSimulation(config_file)
    config_file.close()
    event_file = open('input_files/events_two.txt')
    sim_stats = sim.run(event_file)
    event_file.close()
    assert sim_stats == {'num_customers': 2, 'total_time': 31, 'max_wait': 21}

# def test_events_mixtures_all() -> None:
#     configs = [
#         'config_111_01.json',
#         'config_111_10.json',
#         'config_300_01.json',
#         'config_300_10.json',
#         'config_333_01.json',
#         'config_333_10.json',
#         'config_642_05.json',
#     ]
#     results = []
#     for config_file in configs:
#         file = open('input_files/' + config_file)
#         sim = GroceryStoreSimulation(file)
#         file.close()
#         event_file = open('input_files/events_mixtures.txt')
#         sim_stats = sim.run(event_file)
#         event_file.close()
#         results.append(sim_stats)
#     for result in results:
#         print(result)

if __name__ == '__main__':
    import pytest
    pytest.main(['a1_sample_test.py'])
