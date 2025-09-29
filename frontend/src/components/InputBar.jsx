// src/components/InputBar.jsx
import React, { useEffect, useRef, useState } from "react";

export default function InputBar({ onSubmit, disabled }) {
  const [value, setValue] = useState("");
  const textareaRef = useRef(null);

  // 입력 길이에 따라 자동 높이 조절
  useEffect(() => {
    const el = textareaRef.current;
    if (!el) return;
    el.style.height = "auto";
    el.style.height = `${el.scrollHeight}px`;
  }, [value]);

  const submit = () => {
    const text = value.trim();
    if (!text) return;
    onSubmit?.(text);
    setValue("");
  };

  const onKeyDown = (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      submit();
    }
  };

  return (
    <div className="inputBar">
      <textarea
        ref={textareaRef}
        className="input"
        placeholder="예) 네이버 뉴스에서 ‘AI’ 키워드 기사 상위 20건 수집해줘"
        rows={1}
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={onKeyDown}
      />
      <button className="send" onClick={submit} disable={disabled} aria-label="전송">
        ➤
      </button>
    </div>
  );
}
