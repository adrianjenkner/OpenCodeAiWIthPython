from opencode_ai_with_python.main import main


def test_main(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello from OpenCode AI With Python!\n"
