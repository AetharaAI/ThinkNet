import { useState } from "react";
import { motion } from "framer-motion";
import { changeMood } from "../lib/api"
export default function TonePage() {
  const [tone, setTone] = useState(50);

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6 text-[#e0e0e0] bg-gradient-to-br from-[#0b0c2a] via-[#4b0082] to-[#0b0c2a]">
      <motion.h1
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="text-3xl font-bold mb-8"
      >
        🌌 Adjust Tone Sensitivity
      </motion.h1>

      <div className="flex flex-col items-center space-y-6 w-full max-w-md">
        <input
          type="range"
          min="0"
          max="100"
          value={tone}
          onChange={(e) => setTone(parseInt(e.target.value))}
          className="w-full"
        />
        <span className="text-lg">Current Sensitivity: {tone}%</span>
        <button
          className="bg-gradient-to-r from-indigo-600 to-purple-700 px-6 py-2 rounded-lg hover:scale-105 transition"
          onClick={() => changeMood('logicmodel', `tone_sensitivity:${tone}`).then(() => alert('Tone Sensitivity Updated!'))}
        >
          Save Tone
        </button>
      </div>
    </main>
  );
}
