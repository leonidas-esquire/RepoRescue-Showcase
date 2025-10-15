from src.main import main

def test_main(capsys):
    """Tests the main function."""
    main()
    captured = capsys.readouterr()
    assert captured.out == "Welcome to the Repo Rescue™ Showcase!\n"

