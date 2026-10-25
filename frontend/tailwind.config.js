/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        accent: {
          DEFAULT: "#E2E8F0",
          muted: "#94A3B8",
          highlight: "#3B82F6",
        },
        dark: {
          900: "#0A0A0A",
          800: "#121212",
          700: "#1A1A1A",
          600: "#242424",
          500: "#2E2E2E",
        },
      },
      backgroundImage: {
        'cinematic-gradient': 'radial-gradient(circle at center, #1A1A1A 0%, #0A0A0A 100%)',
      },
    },
  },
  plugins: [],
}
