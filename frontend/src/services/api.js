const API_BASE = process.env.REACT_APP_API_BASE || 'http://localhost:8000';

export async function submitPrompt(prompt){
  const res = await fetch(
    API_BASE ? `${API_BASE}/api/submit` : `/api/submit`,
    {
      method: 'POST', 
      headers : {"Content-Type": "application/json"},
      body: JSON.stringify({prompt})
    }
  );
  if (!res.ok) {
    const errorText = await res.text();
    throw new Error(`HTTP ${res.status} - ${errorText}`);
  }
  return res.json();
}