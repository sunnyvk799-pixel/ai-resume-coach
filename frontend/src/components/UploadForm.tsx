import { useState } from "react";
import { api } from "../services/api";
import type { AnalyzeResponse } from "../types/api";
import ChatBox from "./ChatBox";

export default function UploadForm() {
  const [resume, setResume] = useState<File | null>(null);
  const [jobDescription, setJobDescription] = useState<File | null>(null);

  const [result, setResult] = useState<AnalyzeResponse | null>(null);
  const [documentId, setDocumentId] = useState("");

  const [loading, setLoading] = useState(false);

  async function handleAnalyze() {
    if (!resume || !jobDescription) {
      alert("Please upload both files.");
      return;
    }

    const formData = new FormData();
    formData.append("resume", resume);
    formData.append("job_description", jobDescription);

    try {
      setLoading(true);

      const response = await api.post<AnalyzeResponse>(
        "/analyze",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );

      setResult(response.data);
      setDocumentId(response.data.document_id);

    } catch (error: any) {
      console.error(error);

      if (error.response) {
        alert(JSON.stringify(error.response.data));
      } else {
        alert("Analysis failed.");
      }
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="max-w-3xl mx-auto mt-10 space-y-8 rounded-lg bg-white p-8 shadow-lg">

      <h1 className="text-4xl font-bold text-center">
        AI Resume Coach
      </h1>

      <div>
        <label className="block font-semibold mb-2">
          Resume PDF
        </label>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) => setResume(e.target.files?.[0] ?? null)}
        />
      </div>

      <div>
        <label className="block font-semibold mb-2">
          Job Description PDF
        </label>

        <input
          type="file"
          accept=".pdf"
          onChange={(e) =>
            setJobDescription(e.target.files?.[0] ?? null)
          }
        />
      </div>

      <button
        onClick={handleAnalyze}
        disabled={loading}
        className="w-full rounded-lg bg-blue-600 py-3 text-white font-semibold hover:bg-blue-700"
      >
        {loading ? "Analyzing..." : "Analyze Resume"}
      </button>

      {result && (
        <div className="rounded-lg bg-gray-100 p-6">

          <h2 className="text-2xl font-bold">
            ATS Score: {result.ats_score}
          </h2>

          <div className="mt-6">

            <h3 className="text-lg font-semibold text-green-700">
              Matched Skills
            </h3>

            <ul className="mt-2 list-disc list-inside">
              {result.matched_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>

          </div>

          <div className="mt-6">

            <h3 className="text-lg font-semibold text-red-700">
              Missing Skills
            </h3>

            <ul className="mt-2 list-disc list-inside">
              {result.missing_skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>

          </div>

        </div>
      )}

      {documentId && (
        <ChatBox documentId={documentId} />
      )}

    </div>
  );
}