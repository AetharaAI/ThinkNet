import { motion } from "framer-motion";

export default function NamePage() {
  return (
    <main className="flex flex-col items-center justify-center min-h-screen p-6 text-[#e0e0e0] bg-gradient-to-br from-[#0b0c2a] via-[#4b0082] to-[#0b0c2a]">
      <motion.h1
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
        className="text-3xl font-bold mb-8"
      >
        🌟 Name Your Aethara
      </motion.h1>
    </main>
  );
}
