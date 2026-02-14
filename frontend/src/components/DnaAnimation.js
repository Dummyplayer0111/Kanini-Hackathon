import "./DnaAnimation.css";

const PAIR_COUNT = 32;

function DnaAnimation() {
  const pairs = Array.from({ length: PAIR_COUNT }, (_, i) => {
    const rotation = (i * 360) / PAIR_COUNT;
    const top = (i / PAIR_COUNT) * 100;
    return (
      <div
        key={i}
        className="dna-pair"
        style={{
          top: `${top}%`,
          transform: `rotateY(${rotation}deg)`,
        }}
      >
        <div className="dna-pair-inner">
          <div className="dna-dot dna-dot-left" />
          <div className="dna-connector" />
          <div className="dna-dot dna-dot-right" />
        </div>
      </div>
    );
  });

  // Floating ambient particles spread across full viewport
  const particles = Array.from({ length: 20 }, (_, i) => {
    const size = 2 + Math.random() * 5;
    const left = 5 + Math.random() * 90;
    const top = Math.random() * 100;
    const duration = 5 + Math.random() * 8;
    const delay = Math.random() * 6;
    const isBlue = i % 2 === 0;

    return (
      <div
        key={`p-${i}`}
        className="dna-particle"
        style={{
          width: size,
          height: size,
          left: `${left}%`,
          top: `${top}%`,
          background: isBlue
            ? "rgba(0, 180, 216, 0.5)"
            : "rgba(123, 47, 247, 0.4)",
          boxShadow: isBlue
            ? "0 0 8px rgba(0, 180, 216, 0.3)"
            : "0 0 8px rgba(123, 47, 247, 0.3)",
          animationDuration: `${duration}s`,
          animationDelay: `${delay}s`,
        }}
      />
    );
  });

  return (
    <div className="dna-container">
      <div className="dna-helix">{pairs}</div>
      {particles}
    </div>
  );
}

export default DnaAnimation;
