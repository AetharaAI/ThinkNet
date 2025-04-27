// src/components/MoodController.tsx

"use client";

import { useState } from "react";
import { motion } from "framer-motion";
import { changeMood } from "../lib/api";

const brainRoles = [
  { label: "Creative Brain", value: "creativemodel" },
  { label: "Emotional Brain", value: "emotionmodel" },
  { label: "Technical Brain", value: "technicalmodel" },
  { label: "Logical Brain", value: "logicmodel" },
  { label: "Linguistic Brain", value: "linguisticmodel" },
];

export default function MoodController() {
  const [selectedBrain, setSelectedBrain] = useState("");
  const [newBias, setNewBias] = useState("");
  const [statusMessage, setStatusMessage] = useState("");

  const handleMoodChange = async () => {
    if (!selectedBrain || !newBias) {
      setStatusMessage("Please select a brain and enter a new bias.");
      return;
    }
    try {
      await changeMood(selectedBrain, newBias);
      setStatusMessage(`Bias updated for ${selectedBrain}!`);
      setNewBias("");
    } catch (error) {
      console.error(error);
      setStatusMessage("Error updating bias. Check server connection.");
    }
  };

  return (
    <motion.div
      className="bg-gradient-to-br from-indigo-800 via-purple-700 to-indigo-900 p-6 rounded-xl shadow-xl max-w-lg mx-auto my-10"
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
    >
      <h2 className="text-2xl font-bold mb-4 text-center">Mood Controller</h2>

      <select
        className="w-full p-2 rounded-md mb-4 bg-gray-900 border border-purple-400 text-white"
        value={selectedBrain}
        onChange={(e) => setSelectedBrain(e.target.value)}
      >
        <option value="">Select Brain</option>
        {brainRoles.map((brain) => (
          <option key={brain.value} value={brain.value}>
            {brain.label}
          </option>
        ))}
      </select>

      <input
        className="w-full p-2 rounded-md mb-4 bg-gray-900 border border-blue-400 text-white"
        placeholder="Enter new mood bias..."
        value={newBias}
        onChange={(e) => setNewBias(e.target.value)}
      />

      <button
        className="w-full py-2 rounded-md bg-gradient-to-r from-pink-500 to-purple-600 hover:scale-105 transition-transform"
        onClick={handleMoodChange}
      >
        Update Mood
      </button>

      {statusMessage && (
        <p className="mt-4 text-center text-sm text-purple-300">{statusMessage}</p>
      )}
    </motion.div>
  );
}
