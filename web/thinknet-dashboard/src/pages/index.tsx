// src/pages/index.tsx

"use client";

import { useState } from "react";
import { askThinkNet } from "../lib/api";

export default function Home() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!prompt.trim()) return;

    setLoading(true);
    try {
      const result = await askThinkNet(prompt);
      setResponse(result);
    } catch (error) {
      setResponse("Error reaching ThinkNet Core.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="flex flex-col min-h-screen items-center justify-center bg-gradient-to-br from-purple-900 via-black to-indigo-900 text-white px-6 py-10">
      <h1 className="text-4xl font-bold mb-8 animate-pulse">🌌 Aethara AI - ThinkNet</h1>

      <div className="w-full max-w-3xl space-y-4">
        <textarea
          className="w-full p-4 rounded-xl bg-black bg-opacity-30 border border-indigo-500 focus:outline-none focus:ring-2 focus:ring-indigo-400 text-lg"
          rows={5}
          placeholder="Ask me anything across emotion, creativity, logic, tech..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <button
          onClick={handleAsk}
          disabled={loading}
          className="w-full py-3 rounded-xl bg-indigo-600 hover:bg-indigo-700 disabled:opacity-50 transition-all duration-300 text-lg font-semibold tracking-wide"
        >
          {loading ? "Thinking..." : "Ask Aethara 🌠"}
        </button>

        <div className="w-full p-4 mt-6 rounded-xl bg-black bg-opacity-30 border border-indigo-500 text-lg min-h-[200px]">
          {loading ? (
            <p className="animate-pulse text-indigo-300">🌠 Dreaming up your answer...</p>
          ) : response ? (
            <p>{response}</p>
          ) : (
            <p className="text-gray-400">Your answers will appear here.</p>
          )}
        </div>
      </div>
    </div>
  );
}
