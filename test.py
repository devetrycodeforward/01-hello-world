def test_message(capsys):
    """
    Check that running your code should print out "Hello, World"
    """
    
    import hello
    out, err = capsys.readouterr()
    assert out == "Hello, world!\n", "Your code should have printed out 'Hello, World!, but I didn't see any output..."

