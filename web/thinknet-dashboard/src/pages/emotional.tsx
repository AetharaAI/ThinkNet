import { useState } from "react";
import { motion } from "framer-motion";
import { changeMood } from "../lib/api"; //
export default function EmotionalPage() {
  const [resonance, setResonance] = useState(50);

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6 text-[#e0e0e0] bg-gradient-to-br from-[#0b0c2a] via-[#4b0082] to-[#0b0c2a]">
      <motion.h1
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="text-3xl font-bold mb-8"
      >
        🌠 Set Emotional Resonance
      </motion.h1>

      <div className="flex flex-col items-center space-y-6 w-full max-w-md">
        <input
          type="range"
          min="0"
          max="100"
          value={resonance}
          onChange={(e) => setResonance(parseInt(e.target.value))}
          className="w-full"
        />
        <span className="text-lg">Current Resonance: {resonance}%</span>
      <button
          className="bg-gradient-to-r from-indigo-600 to-purple-700 px-6 py-2 rounded-lg hover:scale-105 transition"
          onClick={() => changeMood('emotionmodel', `resonance:${resonance}`).then(() => alert('Emotional Resonance Updated!'))}
>
  Save Setting
</button>
      </div>
    </main>
  );
}
