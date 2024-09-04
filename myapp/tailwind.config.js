/** @type {import('tailwindcss').Config} */
module.exports = {
  darkMode: 'class',
  content: [
    './templates/**/*.html'
  ],
  theme: {
    extend: {
      fontFamily : {
        angsana : ["Angsana New"],
        notosansthai : ["Noto Sans Thai"]
      }
    },
  },
  plugins: [],
}

