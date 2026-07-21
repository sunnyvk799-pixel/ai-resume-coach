export interface AnalyzeResponse {
  ats_score: number;
  matched_skills: string[];
  missing_skills: string[];
  document_id: string;
}

export interface ChatResponse {
  answer: string;
  sources: string[];
}