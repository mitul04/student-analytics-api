from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_nonexisting_student():
    response = client.get("/students/26XX001")

    assert response.status_code == 404


def test_get_existing_student():
    response = client.get("/students/26CS001")

    assert response.status_code == 200


def test_create_student_missing_required_field():
    payload = {
        "id": "26XX001",
        "name": "Test Student",
        "branch": "CS",
        # cgpa is missing
    }

    response = client.post("/students/", json=payload)

    assert response.status_code == 422


def test_create_student_rejects_extra_field():
    payload = {
        "id": "26XX001",
        "name": "Test Student",
        "branch": "CS",
        "cgpa": 8.5,
        "age": 22  # Not defined in StudentCreate
    }

    response = client.post("/students/", json=payload)

    assert response.status_code == 422


def test_create_and_retrieve_student():
    student_id = "26XX001"

    payload = {
        "id": student_id,
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 8.5
    }

    created = False

    try:
        response = client.post("/students/", json=payload)

        # Record whether the API actually created the student.
        created = response.status_code in (200, 201)

        assert response.status_code == 200
        assert response.json()["id"].strip() == student_id
        assert response.json()["name"] == "Test Student"

        # Verify that the record can be retrieved.
        retrieved = client.get(f"/students/{student_id}")

        assert retrieved.status_code == 200
        assert retrieved.json()["student"]["name"] == "Test Student"

    finally:
        # Clean up even if an assertion fails.
        if created:
            client.delete(f"/students/{student_id}")


def test_duplicate_student_id():
    student_id = "26XX001"

    payload = {
        "id": student_id,
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 8.5
    }

    created = False

    try:
        first_response = client.post("/students/", json=payload)
        created = first_response.status_code == 200

        assert first_response.status_code == 200

        # Submit the exact same student again.
        second_response = client.post("/students/", json=payload)

        assert second_response.status_code == 400
        assert second_response.json()["detail"] == "Student ID already exists"

    finally:
        if created:
            client.delete(f"/students/{student_id}")


def test_create_student_with_invalid_cgpa():
    payload = {
        "id": "26XX001",
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 11.0
    }

    response = client.post("/students/", json=payload)

    assert response.status_code == 422


def test_create_student_with_nonexistent_branch():
    payload = {
        "id": "26XX001",
        "name": "Test Student",
        "branch": "AIDS",
        "cgpa": 8.5
    }

    response = client.post("/students/", json=payload)

    assert response.status_code == 404
    assert response.json()["detail"] == "Branch not found"


def test_put_nonexistent_student():
    payload = {
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 8.5
    }

    response = client.put(
        "/students/26XX001",
        json=payload
    )

    assert response.status_code == 404


def test_patch_nonexistent_student():
    payload = {
        "cgpa": 8.5
    }

    response = client.patch(
        "/students/26XX001",
        json=payload
    )

    assert response.status_code == 404


def test_delete_nonexistent_student():
    response = client.delete("/students/26XX001")

    assert response.status_code == 404


def test_put_existing_student():
    student_id = "26XX001"

    original = {
        "id": student_id,
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 7.0
    }

    updated = {
        "name": "Updated Student",
        "branch": "CSE",
        "cgpa": 8.5
    }

    created = False

    try:
        response = client.post("/students/", json=original)
        created = response.status_code == 200

        assert response.status_code == 200

        response = client.put(
            f"/students/{student_id}",
            json=updated
        )

        assert response.status_code == 200

        body = response.json()
        assert body["name"] == "Updated Student"
        assert body["branch"].strip() == "CSE"
        assert float(body["cgpa"]) == 8.5

    finally:
        if created:
            client.delete(f"/students/{student_id}")


def test_patch_existing_student():
    student_id = "26XX001"

    original = {
        "id": student_id,
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 7.0
    }

    updated = {
        "name": "Updated Student",
        "cgpa": 8.5
    }

    created = False

    try:
        response = client.post("/students/", json=original)
        created = response.status_code == 200

        assert response.status_code == 200

        response = client.patch(
            f"/students/{student_id}",
            json=updated
        )

        assert response.status_code == 200

        body = response.json()

        assert body["branch"] == "CSE"
                
        assert body["name"] == "Updated Student"
        assert float(body["cgpa"]) == 8.5

    finally:
        if created:
            client.delete(f"/students/{student_id}")


def test_delete_existing_student():
    student_id = "26XX001"

    payload = {
        "id": student_id,
        "name": "Test Student",
        "branch": "CSE",
        "cgpa": 7.0
    }

    created = False
    deleted = False

    try:
        response = client.post("/students/", json=payload)
        created = response.status_code == 200

        assert response.status_code == 200

        response = client.delete(f"/students/{student_id}")

        assert response.status_code == 200
        deleted = True

        response = client.get(f"/students/{student_id}")
        assert response.status_code == 404

    finally:
        # Delete only if creation succeeded but deletion did not.
        if created and not deleted:
            client.delete(f"/students/{student_id}")

