import './Card.css';

interface CardProps {
  card: {
    question: string;
    answer: string;
  };
  isFlipped: boolean;
  flipcard: () => void;
}

export default function Card({ card, isFlipped, flipcard }: CardProps) {
  return (
    <div className={`card ${isFlipped ? 'flipped' : ''}`} onClick={flipcard}>
      <div className="inner-card">
        <div className="front-card">
          <p>{card.question}</p>
        </div>
        <div className="back-card">
          <p>{card.answer}</p>
        </div>
      </div>
    </div>
  );
}