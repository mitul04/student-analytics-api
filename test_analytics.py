from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_students_summary_exact_values():
    response = client.get("/analytics/students-summary")

    assert response.status_code == 200

    data = response.json()

    assert data["total_students"] == 27
    assert float(data["average_cgpa"]) == 8.33
    assert float(data["min_cgpa"]) == 6.8
    assert float(data["max_cgpa"]) == 9.6

    assert data["branch_count"] == {
        "CSE": 6,
        "ECE": 5,
        "EEE": 4,
        "RAI": 4,
        "CE": 4,
        "ME": 4,
    }


def test_branchwise_summary():
    response = client.get("/analytics/branchwise-summary")

    assert response.status_code == 200

    data = response.json()

    expected_counts = {
        "CSE": 6,
        "ECE": 5,
        "EEE": 4,
        "RAI": 4,
        "CE": 4,
        "ME": 4,
    }

    actual_counts = {
        branch: details["total_students"]
        for branch, details in data.items()
    }

    assert actual_counts == expected_counts

    for details in data.values():
        assert details["min_cgpa"] <= details["average_cgpa"]
        assert details["average_cgpa"] <= details["max_cgpa"]


def test_cgpa_distribution_exact_values():
    response = client.get("/analytics/cgpa-range-count")

    assert response.status_code == 200

    data = response.json()

    assert data["total_students"] == 27
    assert data["0_6"] == 0
    assert data["6_7"] == 2
    assert data["7_8"] == 7
    assert data["8_9"] == 10
    assert data["9_10"] == 8


def test_cgpa_distribution_for_valid_branch():
    response = client.get(
        "/analytics/cgpa-range-count",
        params={"branch": "CSE"},
    )

    assert response.status_code == 200

    data = response.json()

    assert data["branch"] == "CSE"
    assert data["total_students"] == 6

    assert {
        "0_6": data["0_6"],
        "6_7": data["6_7"],
        "7_8": data["7_8"],
        "8_9": data["8_9"],
        "9_10": data["9_10"],
    } == {
        "0_6": 0,
        "6_7": 0,
        "7_8": 0,
        "8_9": 2,
        "9_10": 4,
    }


def test_cgpa_distribution_rejects_unknown_branch():
    response = client.get(
        "/analytics/cgpa-range-count",
        params={"branch": "ZZZ"},
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Branch not found"


def test_top_performers_exact_values():
    response = client.get(
        "/analytics/top-performers",
        params={"limit": 10},
    )

    assert response.status_code == 200

    data = response.json()

    expected = [
        ("Uma", "RAI", 9.6),
        ("Xander", "CSE", 9.6),
        ("Yara", "ECE", 9.6),
        ("Fiona", "CSE", 9.5),
        ("Alice", "CSE", 9.2),
        ("Oscar", "RAI", 9.2),
        ("Charlie", "RAI", 9.1),
        ("Laura", "CSE", 9.0),
        ("Michael", "ECE", 8.8),
        ("Ian", "RAI", 8.7),
    ]

    actual = [
        (item["name"], item["branch"], float(item["cgpa"]))
        for item in data
    ]

    assert actual == expected


def test_bottom_performers_exact_values():
    response = client.get(
        "/analytics/bottom-performers",
        params={"limit": 10},
    )

    assert response.status_code == 200

    data = response.json()

    expected = [
        ("Ethan", "ME", 6.8),
        ("Quentin", "ME", 6.9),
        ("Victor", "CE", 7.1),
        ("Diana", "CE", 7.2),
        ("Kevin", "ME", 7.4),
        ("Penelope", "CE", 7.5),
        ("Sam", "ECE", 7.7),
        ("Dell", "ECE", 7.89),
        ("Hannah", "EEE", 7.9),
        ("Wendy", "ME", 8.0),
    ]

    actual = [
        (item["name"], item["branch"], float(item["cgpa"]))
        for item in data
    ]

    assert actual == expected


def test_top_performers_branch_filter():
    response = client.get(
        "/analytics/top-performers",
        params={"branch": "CSE", "limit": 3},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3
    assert all(item["branch"] == "CSE" for item in data)

    assert [
        (item["name"], float(item["cgpa"]))
        for item in data
    ] == [
        ("Xander", 9.6),
        ("Fiona", 9.5),
        ("Alice", 9.2),
    ]


def test_top_performers_rejects_invalid_limit():
    response = client.get(
        "/analytics/top-performers",
        params={"limit": 0},
    )

    assert response.status_code == 422



def test_bottom_performers_branch_filter():
    response = client.get(
        "/analytics/bottom-performers",
        params={"branch": "CSE", "limit": 3},
    )

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 3
    assert all(item["branch"] == "CSE" for item in data)

    assert [
        (item["name"], float(item["cgpa"]))
        for item in data
    ] == [
        ("Mitul", 8.11),
        ("Rachel", 8.6),
        ("Laura", 9.0),
    ]
