from fastapi import APIRouter
from app.schemas import ScamCheckRequest, ScamCheckResponse

router = APIRouter()


def get_advice(risk_level: str):
    if risk_level == "High":
        return "Do not click any links or share personal information. Verify through official channels."
    if risk_level == "Medium":
        return "Be careful. Confirm the message source before taking action."
    return "No major warning signs detected, but still verify unexpected messages."


def detect_scam(message: str):
    text = message.lower()

    red_flags = []
    scam_type = "Unknown"
    score = 0

    if any(word in text for word in ["won", "winner", "prize", "reward", "congratulations"]):
        red_flags.append("Promises unexpected money or rewards")
        scam_type = "Prize Scam"
        score += 3

    if any(word in text for word in ["click", "link", "claim", "verify", "login"]):
        red_flags.append("Asks user to click a link or verify details")
        score += 2

    if any(word in text for word in ["urgent", "now", "immediately", "limited time", "today"]):
        red_flags.append("Creates urgency or pressure")
        score += 2

    if any(word in text for word in ["pin", "password", "otp", "account number", "mpesa pin"]):
        red_flags.append("Requests sensitive personal or financial information")
        scam_type = "Phishing Scam"
        score += 4

    if any(word in text for word in ["job", "vacancy", "recruitment", "pay registration fee"]):
        red_flags.append("Mentions job opportunity or recruitment")
        scam_type = "Fake Job Scam"
        score += 2

    if score >= 6:
        risk_level = "High"
    elif score >= 3:
        risk_level = "Medium"
    else:
        risk_level = "Low"

    if not red_flags:
        red_flags.append("No obvious scam patterns detected")

    return {
        "risk_level": risk_level,
        "scam_type": scam_type,
        "red_flags": red_flags,
        "advice": get_advice(risk_level),
    }


@router.post("/analyze", response_model=ScamCheckResponse)
def analyze_message(request: ScamCheckRequest):
    return detect_scam(request.message)