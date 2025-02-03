from src.funcions import es_primo

def test_primo_1():
    assert es_primo(1) == False

def test_es_primo_2():
    assert es_primo(2) == True

def test_es_primo_3():
    assert es_primo(13) == True

def test_es_primo_4():
    assert es_primo(31) == True

def test_es_primo_5():
    assert es_primo(20) == False