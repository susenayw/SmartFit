import LoginButtons from "../components/Button";
import { Link } from "react-router-dom";

function LandingPage() {
  return (
    <main 
      className="w-full h-screen fixed inset-0 bg-cover bg-center bg-no-repeat"
      style={{ backgroundImage: "url('/images/landing-page-background.png')" }}
    >
      <div className="absolute inset-0" aria-hidden="true" />

      <header className="absolute top-0 right-0 p-4 sm:p-6 z-10">
        <nav className="flex gap-2 sm:gap-3" aria-label="Main Navigation">
          <Link to="/signup">
            <LoginButtons name="Sign up" />
          </Link>
          <Link to="/login">
            <LoginButtons name="Login" />
          </Link>
        </nav>
      </header>

      <section className="absolute inset-x-0 top-1/2 -translate-y-1/2 bg-white/60 backdrop-blur-sm py-8 sm:py-12 px-6 sm:px-12 z-10">
        <h1 className="font-special-gothic-expanded-one text-5xl sm:text-6xl md:text-8xl text-black mb-3 transition-all duration-700 opacity-100 translate-y-0">
          SmartFit
        </h1>
        <h2 className="text-lg sm:text-xl md:text-2xl font-bold text-black mb-2 transition-all duration-700 delay-150 opacity-100 translate-y-0">
          Meet SmartFit: Your Personal Digital Health Coach.
        </h2>
        <p className="text-sm sm:text-base font-semibold text-black/75 transition-all duration-700 delay-300 opacity-100 translate-y-0">
          Tailored nutrition and fitness plans powered by AI, designed to adapt as you grow.
        </p>
      </section>
    </main>
  );
}

export default LandingPage;