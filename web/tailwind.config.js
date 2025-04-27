// tailwind.config.js

/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
      "./src/**/*.{js,ts,jsx,tsx}",
    ],
    theme: {
      extend: {
        colors: {
          cosmic: {
            light: "#c3b1e1",
            DEFAULT: "#6b21a8",
            dark: "#4c1d95",
          },
          space: {
            black: "#0b0c10",
            purple: "#6a0dad",
            indigo: "#4b0082",
          },
        },
        animation: {
          "pulse-slow": "pulse 4s cubic-bezier(0.4, 0, 0.6, 1) infinite",
        },
      },
    },
    plugins: [],
  }
  