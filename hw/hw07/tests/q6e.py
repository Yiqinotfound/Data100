OK_FORMAT = True
OK_FORMAT = True
OK_FORMAT = True
test = {   'name': 'q6e',
    'points': 2,
    'suites': [   {   'cases': [   {'code': '>>> first_2_pcs.shape == (51, 2)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> all(first_2_pcs.columns == ['pc1', 'pc2'])\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> all(np.isclose(first_2_pcs.loc[0], [-2.9386, 0.7964], atol=1e-4))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(np.isclose(first_2_pcs.loc[46], [-0.2960, -1.5452], atol=1e-4))\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> all(np.isclose(first_2_pcs.loc[28], [0.9442, -1.5338], atol=1e-4))\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
