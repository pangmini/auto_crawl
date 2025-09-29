import React, { useState } from "react";
import InputBar from "./components/InputBar";
import { submitPrompt } from "./services/api";
import "./App.css";

export default function App() {
  const [loading, setLoading] = useState(false);
  const [serverMsg, setServerMsg] = useState("");

  const handleSubmit = async (text) => {
    setLoading(true);
    setServerMsg("");
    try {
      const data = await submitPrompt(text); // ← 백엔드로 전송
      setServerMsg(data.message);            // ← 응답 반영
    } catch (e) {
      setServerMsg(`오류: ${e.message}`);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <main className="hero">
        <h1 className="title">auto_crawl</h1>
        <p className="subtitle">원하는 수집/분석 목표를 입력해 시작하세요</p>

        {loading && <p>전송 중…</p>}
        {!loading && serverMsg && (
          <pre style={{ whiteSpace: "pre-wrap" }}>{serverMsg}</pre>
        )}

        <div className="inputDock">
          <InputBar onSubmit={handleSubmit} />
          <p className="hint">Enter: 전송 · Shift+Enter: 줄바꿈</p>
        </div>
      </main>
    </div>
  );
}
