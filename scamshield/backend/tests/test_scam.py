from app.routes.scam import detect_scam


def test_high_risk_prize_scam():
    result = detect_scam(
        "Congratulations! You have won KES 50,000. Click this link now."
    )

    assert result["risk_level"] == "High"
    assert result["scam_type"] == "Prize Scam"


def test_low_risk_normal_message():
    result = detect_scam("Hi, please send me the meeting notes when free.")

    assert result["risk_level"] == "Low"