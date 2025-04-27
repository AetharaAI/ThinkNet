import { motion } from "framer-motion";
import Link from "next/link";

export default function CosmicTile({ title, link }: { title: string; link: string }) {
  return (
    <Link href={link}>
      <motion.div
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        className="p-6 bg-gradient-to-br from-[#0b0c2a] via-[#5b3cc4] to-[#0b0c2a] border border-[#5b3cc4] hover:border-[#ff914d] rounded-2xl shadow-xl cursor-pointer text-center transition duration-300"
      >
        <h2 className="text-xl font-bold">{title}</h2>
      </motion.div>
    </Link>
  );
}
