OK_FORMAT = True
OK_FORMAT = True
OK_FORMAT = True
test = {   'name': 'q4b',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> isinstance(sent, pd.DataFrame)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> sent.shape == (7517, 1)\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> tuple(sent.columns)  == ("polarity", )\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> sent.index.name == "token"\nTrue', 'hidden': False, 'locked': False},
                                   {'code': ">>> list(sent.index[5000:5005]) == ['paranoids', 'pardon', 'pardoned', 'pardoning', 'pardons']\nTrue", 'hidden': False, 'locked': False},
                                   {'code': ">>> np.allclose(sent['polarity'].head(), [-1.5, -0.4, -1.5, -0.4, -0.7])\nTrue", 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
