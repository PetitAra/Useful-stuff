from project3.tokenization import tokenizator

def test_tokenizator():
    string= 'My name is John'
    assert len(tokenizator(string))==len(string.split(" "))