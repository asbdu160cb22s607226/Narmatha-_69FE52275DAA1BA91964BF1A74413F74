from app import create_app

def test_health():
    app = create_app()
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json["status"] == "ok"


def test_analyze_endpoint():
    app = create_app()
    client = app.test_client()
    resp = client.post("/api/analyze", json={"text": "I feel happy and excited"})
    assert resp.status_code == 200
    body = resp.get_json()
    assert "analysis" in body and "actions" in body
    assert body["actions"]
