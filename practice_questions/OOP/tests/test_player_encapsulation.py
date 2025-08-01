from unittest.mock import patch

from app.player_encapsulation import Player


def test_player_instance():
    player1 = Player()
    assert isinstance(player1, Player)


def test_health_is_private():
    player1 = Player()
    player1.__health = 10
    assert player1.__health != player1._Player__health


def test_player_str():
    player1 = Player()
    assert str(player1) == "Player Object"


def test_initial_health_is_zero():
    player1 = Player()
    assert player1._Player__health == 0


@patch("app.player_encapsulation.input")
def test_health_points_rejects_above_100(mock_obj, capfd):
    mock_obj.side_effect = ["101", "50"]
    player1 = Player()
    result = player1.health_points()
    o, _ = capfd.readouterr()
    assert "Healing maxed out!" in o
    assert result == 50


@patch("app.player_encapsulation.input")
def test_health_points_rejects_zero_or_less(mock_obj, capfd):
    player1 = Player()
    mock_obj.side_effect = ["0", "20"]
    result = player1.health_points()
    o, _ = capfd.readouterr()
    assert "No change in health points are you sure?" in o
    assert result == 20


@patch("app.player_encapsulation.input")
def test_health_points_adds_and_caps(mock_obj, capfd):
    player1 = Player()
    mock_obj.side_effect = ["120", "100"]
    result = player1.health_points()
    o, _ = capfd.readouterr()
    assert "Healing maxed out!" in o
    assert result == 100


@patch("app.player_encapsulation.input")
def test_damage_points_rejects_above_100(mock_obj, capfd):
    player1 = Player()
    player1._Player__health = 100
    mock_obj.side_effect = ["101", "50"]
    result = player1.damage_points()
    o, _ = capfd.readouterr()
    assert "Damage input above 100 please enter numbers 100 or below." in o
    assert result == 50


@patch("app.player_encapsulation.input")
def test_damage_points_blocks_when_health_zero(mock_obj, capfd):
    p1 = Player()
    mock_obj.return_value = "50"
    p1.damage_points()
    o, _ = capfd.readouterr()
    assert "Opponent's health already  at 0 please fill up HP." in o


@patch("app.player_encapsulation.input")
def test_damage_points_reduces_health_properly(mock_obj):
    p1 = Player()
    p1._Player__health = 50
    mock_obj.return_value = "30"
    p1.damage_points()
    assert p1._Player__health == 20


@patch("app.player_encapsulation.input")
def test_damage_points_triggers_fainted_message_at_zero(mock_obj, capfd):
    p1 = Player()
    p1._Player__health = 10
    mock_obj.return_value = "10"
    p1.damage_points()
    o, _ = capfd.readouterr()
    assert "Opponent has fainted" in o
    assert p1._Player__health == 0


@patch("app.player_encapsulation.input")
def test_sequence_healing(mock_obj):
    p1 = Player()
    mock_obj.side_effect = ["50", "30", "20"]

    p1.health_points()
    assert p1._Player__health == 50

    p1.damage_points()
    assert p1._Player__health == 20

    p1.health_points()
    assert p1._Player__health == 40
