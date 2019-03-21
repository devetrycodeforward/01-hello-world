def test_message(capsys):
    """
    Check that running your code should print out "Hello, World!"
    """
    
    import hello
    out, err = capsys.readouterr()
    assert "Hello, World!" in out, "Your code should have printed out 'Hello, World!, but it doesn't look like it did..."
