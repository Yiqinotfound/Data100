OK_FORMAT = True
OK_FORMAT = True
OK_FORMAT = True
test = {   'name': 'q6d',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> all(np.isclose([sum(u[:, i] ** 2) for i in range(u.shape[1])], np.ones((u.shape[1],))))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(np.isclose([sum(vt[i, :] ** 2) for i in range(vt.shape[1])], np.ones((u.shape[1],))))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> len(s) == 13\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> (np.isclose(u @ np.diag(s) @ vt, df_standardized)).all()\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
