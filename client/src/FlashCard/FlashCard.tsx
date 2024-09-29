import { useState, useEffect } from "react";
import Card from "../Components/Card";
import './FlashCard.css';
import DashNavbar from "../Components/navbar";
import Timer from "../Components/Timer";

interface Flashcard {
  question: string;
  answer: string;
}

export default function FlashCard() {
  const [flashcards, setFlashcards] = useState<Flashcard[]>([]);
  const [currentCardIndex, setCurrentCardIndex] = useState<number>(0);
  const [isFlipped, setIsFlipped] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const [university, setUniversity] = useState<string>("");
  const [course, setCourse] = useState<string>("");
  const [formSubmitted, setFormSubmitted] = useState<boolean>(false);

  // Fetch flashcards from API
  useEffect(() => {
    const fetchFlashcards = async () => {
      try {
        setLoading(true);
        const response = await fetch(`http://127.0.0.1:8000/flashcards?university=${university}&course=${course}`, {
          method: 'GET',
          headers: {
            'Content-type': 'application/json',
          }
        });
        if (!response.ok) {
          throw new Error('Failed to fetch flashcards');
        }
        const data: Flashcard[] = await response.json();
        setFlashcards(data);
        setLoading(false);
      } catch (error) {
        setError('Error fetching flashcards: ' + error);
        setLoading(false);
      }
    };

    if (formSubmitted) {
      fetchFlashcards();
    }
  }, [formSubmitted, university, course]);

  function nextCard() {
    if (currentCardIndex < flashcards.length - 1) {
      setCurrentCardIndex(currentCardIndex + 1);
      setIsFlipped(false);
    }
  }

  function prevCard() {
    if (currentCardIndex > 0) {
      setCurrentCardIndex(currentCardIndex - 1);
      setIsFlipped(false);
    }
  }

  function flipCard() {
    setIsFlipped(!isFlipped);
  }

  const handleFormSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setFormSubmitted(true);  // Trigger the fetchFlashcards effect
  };

  if (!formSubmitted) {
    return (
      <div>
        <h2>Create a Deck of Flashcards</h2>
        <form onSubmit={handleFormSubmit}>
          <label>
            University:
            <input 
              type="text" 
              value={university} 
              onChange={(e) => setUniversity(e.target.value)} 
              required 
            />
          </label>
          <label>
            Course:
            <input 
              type="text" 
              value={course} 
              onChange={(e) => setCourse(e.target.value)} 
              required 
            />
          </label>
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }

  if (loading) {
    return <p>Loading flashcards...</p>;
  }

  if (error) {
    return <p>{error}</p>;
  }

  return (
    <>
      <div>
        <DashNavbar />
      </div>
      <div className="flashcard-container">
        {flashcards.length > 0 ? (
          <>
            <Card
              card={flashcards[currentCardIndex]}
              isFlipped={isFlipped}
              flipcard={flipCard}
            />
            <div className="button-container">
              <button onClick={prevCard} disabled={currentCardIndex === 0}>
                &lt;
              </button>
              <button
                onClick={nextCard}
                disabled={currentCardIndex === flashcards.length - 1}
              >
                &gt;
              </button>
            </div>
          </>
        ) : (
          <p>No flashcards available.</p>
        )}
      </div>
      <div>
        <Timer />
      </div>
    </>
  );
}