import { useState } from "react";
import { motion } from "framer-motion";
import { generateFromBrain } from "../lib/api";

export default function AskPage() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");

  const handleAsk = async () => {
    try {
      const res = await generateFromBrain(prompt, 5001); // Replace 5001 with your emotion brain port or main brain port
      setResponse(res.data.response);
    } catch (error) {
      console.error(error);
      setResponse("Aethara is thinking... Please try again.");
    }
  };

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6 text-[#e0e0e0] bg-gradient-to-br from-[#0b0c2a] via-[#4b0082] to-[#0b0c2a]">
      <motion.h1
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="text-3xl font-bold mb-8"
      >
        💬 Ask Aethara Anything
      </motion.h1>

      <textarea
        placeholder="Type your question..."
        className="w-full max-w-lg h-32 p-4 rounded-lg bg-gray-800 border border-indigo-600 mb-4"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        onClick={handleAsk}
        className="bg-gradient-to-r from-indigo-600 to-purple-700 px-6 py-2 rounded-lg hover:scale-105 transition mb-6"
      >
        Ask Aethara
      </button>

      {response && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8 }}
          className="bg-gray-900 p-6 rounded-lg max-w-lg text-center border border-indigo-700"
        >
          <p>{response}</p>
        </motion.div>
      )}
    </main>
  );
}
