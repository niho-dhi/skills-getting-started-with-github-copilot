def test_get_activities_returns_expected_payload(client):
    # Arrange
    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200

    payload = response.json()
    assert "Chess Club" in payload
    assert payload["Chess Club"]["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert payload["Chess Club"]["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]


def test_get_activities_includes_frontend_fields(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()
    programming_class = payload["Programming Class"]

    assert set(programming_class) == {
        "description",
        "schedule",
        "max_participants",
        "participants",
    }
    assert isinstance(programming_class["participants"], list)