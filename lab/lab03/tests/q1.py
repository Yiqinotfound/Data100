OK_FORMAT = True
OK_FORMAT = True
test = {   'name': 'q1',
    'points': None,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(answer1, list)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all([isinstance(elt, str) for elt in answer1])\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(answer1) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all([elt in calls['OFFENSE'].values for elt in answer1])\nTrue", 'hidden': False, 'locked': False},
                                   {   'code': ">>> set([a.strip().upper() for a in answer1]) == set(['THEFT FELONY (OVER $950)', 'THEFT FROM PERSON', 'THEFT MISD. (UNDER $950)'])\nTrue",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
