OK_FORMAT = True
OK_FORMAT = True
OK_FORMAT = True
test = {   'name': 'q4',
    'points': 4,
    'suites': [   {   'cases': [   {'code': '>>> res_q4.shape == (26, 4)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> set(res_q4.columns) == set(['runtimeBin', 'averageRating', 'averageNumVotes', 'total'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> res_q4["runtimeBin"].min() == 50.0\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> res_q4["runtimeBin"].max() == 370.0\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
