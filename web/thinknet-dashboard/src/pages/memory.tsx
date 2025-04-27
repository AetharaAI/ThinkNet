import { useState } from "react";
import { motion } from "framer-motion";
import { learnMemory } from "../lib/api";
export default function MemoryPage() {
  const [memory, setMemory] = useState("");

  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6 text-[#e0e0e0] bg-gradient-to-br from-[#0b0c2a] via-[#4b0082] to-[#0b0c2a]">
      <motion.h1
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="text-3xl font-bold mb-8"
      >
        🪐 Teach Aethara New Memory
      </motion.h1>

      <textarea
        placeholder="Type something you want Aethara to remember..."
        className="w-full max-w-lg h-40 p-4 rounded-lg bg-gray-800 border border-indigo-600 mb-6"
        value={memory}
        onChange={(e) => setMemory(e.target.value)}
      />

      <button
        className="bg-gradient-to-r from-indigo-600 to-purple-700 px-6 py-2 rounded-lg hover:scale-105 transition"
        onClick={() => learnMemory(memory).then(() => alert('Memory Uploaded Successfully!'))}
      >
      Save Memory
      </button>
    </main>
  );
}
