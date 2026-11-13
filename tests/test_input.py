from systems_abstract import get_positive_float


def test_invalid_then_valid_input(monkeypatch, capsys):
    inputs = iter(["abc", "12.50"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Price: $")

    assert result == 12.50

    output = capsys.readouterr().out
    assert "Please enter a valid number, e.g. 12.50" in output


def test_negative_then_valid_input(monkeypatch, capsys):
    inputs = iter(["-5", "12.50"])

    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = get_positive_float("Price: $")

    assert result == 12.50

    output = capsys.readouterr().out
    assert "Please enter a number greater than zero." in output


def test_valid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "25.50")

    result = get_positive_float("Price: $")

    assert result == 25.50
