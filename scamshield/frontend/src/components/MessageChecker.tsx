import { useState } from "react";
import { analyzeMessage } from "../api/scamApi";
import type { ScamResponse } from "../types/scam";

function MessageChecker() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState<ScamResponse | null>(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async () => {
    if (!message.trim()) return;

    setLoading(true);
    const data = await analyzeMessage(message);
    setResult(data);
    setLoading(false);
  };

  return (
    <div>
      <h1>ScamShield</h1>
      <p>Paste a suspicious message below.</p>

      <textarea
        rows={6}
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Paste suspicious message here..."
      />

      <br />

      <button onClick={handleAnalyze}>
        {loading ? "Analyzing..." : "Analyze Message"}
      </button>

      {result && (
        <div>
          <h2>Result</h2>
          <p><strong>Risk:</strong> {result.risk_level}</p>
          <p><strong>Scam Type:</strong> {result.scam_type}</p>
          <p><strong>Advice:</strong> {result.advice}</p>

          <h3>Red Flags</h3>
          <ul>
            {result.red_flags.map((flag, index) => (
              <li key={index}>{flag}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default MessageChecker;