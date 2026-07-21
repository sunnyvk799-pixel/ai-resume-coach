import { useState } from "react";
import { api } from "../services/api";
import type { ChatResponse } from "../types/api";

interface ChatBoxProps {
  documentId: string;
}

export default function ChatBox({ documentId }: ChatBoxProps) {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleAsk() {
    if (!question.trim()) {
      alert("Please enter a question.");
      return;
    }

    try {
      setLoading(true);

      const response = await api.post<ChatResponse>("/chat", {
        question: question,
        document_id: documentId,
      });

      setAnswer(response.data.answer);
    } catch (error: any) {
      console.error(error);

      if (error.response) {
        alert(JSON.stringify(error.response.data));
      } else {
        alert("Chat request failed.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="mt-8 rounded-lg bg-white p-6 shadow-lg">
      <h2 className="mb-4 text-2xl font-bold">
        Ask AI About Your Resume
      </h2>

      <textarea
        rows={4}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Example: How can I improve my resume?"
        className="w-full rounded-lg border p-3"
      />

      <button
        onClick={handleAsk}
        disabled={loading}
        className="mt-4 rounded-lg bg-green-600 px-6 py-3 font-semibold text-white hover:bg-green-700"
      >
        {loading ? "Thinking..." : "Ask AI"}
      </button>

      {answer && (
        <div className="mt-6 rounded-lg bg-gray-100 p-4">
          <h3 className="mb-2 text-lg font-semibold">
            AI Response
          </h3>

          <p className="whitespace-pre-wrap">
            {answer}
          </p>
        </div>
      )}
    </div>
  );
}