from unittest.mock import patch

from app.player_encapsulation import Player

# Structural Tests


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


# Behavioural Tests


def test_initial_health_is_zero():
    player1 = Player()
    assert player1._Player__health == 0


@patch("app.player_encapsulation.input")
def test_health_points_rejects_above_100(mock_obj, capfd):
    mock_obj.return_value = "101"
    player1 = Player()
    result = player1.health_points()
    o, _ = capfd.readouterr()
    assert "Healing maxed out!" in o
    assert result == 0


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


def test_damage_points_rejects_above_100():
    pass


def test_damage_points_blocks_when_health_zero():
    pass


def test_damage_points_reduces_health_properly():
    pass


def test_damage_points_triggers_fainted_message_at_zero():
    pass
