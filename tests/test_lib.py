from toto.lib import who_am_i



def test_who_am_i():


    name = who_am_i()

    assert "Yannis" in name
    assert type(name) == str
