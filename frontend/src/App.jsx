import { useState } from "react"


function App() {
  const [name, setName] = useState("")
  const [error, setError] = useState("")
  const [showForm, setShowForm] = useState(true)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [email, setEmail] = useState("")
  const [jobTitle, setJobTitle] = useState("")
  const [resume, setResume] = useState(null)
  const [jobDescription, setJobDescription] = useState("")
  const [showRecommendation, setShowRecommendation] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError("")


    if (!name || !email || !jobTitle || !resume || !jobDescription) {
      setError("Please fill all fields before analyzing the resume.")
      return
    }
    if (resume && resume.type !== "application/pdf") {
      setError("Please upload a PDF resume only.")
      return
    }
    if (resume.size > 5 * 1024 * 1024) {
      setError("Resume file size must be less than 5 MB.")
      return
    }
    const formData = new FormData()

    formData.append("name", name)
    formData.append("email", email)
    formData.append("job_title", jobTitle)
    formData.append("resume", resume)
    formData.append("job_description", jobDescription)
    setLoading(true)



    try {
      const response = await fetch("http://127.0.0.1:8000/analyze-resume", {
        method: "POST",
        body: formData,
      })

      const data = await response.json()

      console.log("API Response:", data)
      if (!response.ok) {
        console.error("Validation Error:", data.detail)
        setError(
          typeof data.detail === "string"
            ? data.detail
            : "Unable to analyze the resume. Please try again."
        )

        return
      }
      setResult(data)
      setShowForm(false)

    } catch (error) {
      console.error("Error:", error)
      setError("Something went wrong. Please try again.")
    }

    finally {
      setLoading(false)
    }
  }
  const getScoreStatus = (score) => {
    if (score <= 40) {
      return {
        label: "Low Match",
        message: "Your resume has a low match with this job description.",
        badge: "bg-red-50 border-red-200 text-red-700",
        dot: "bg-red-500",
      }
    }

    if (score <= 70) {
      return {
        label: "Moderate Match",
        message: "Your resume partially matches the requirements of this job.",
        badge: "bg-yellow-50 border-yellow-200 text-yellow-700",
        dot: "bg-yellow-500",
      }
    }

    return {
      label: "Strong Match",
      message: "Your resume strongly matches the requirements of this job.",
      badge: "bg-green-50 border-green-200 text-green-700",
      dot: "bg-green-500",
    }
  }
  return (
    <div className="min-h-screen bg-gray-100 py-10 px-4">
      <div className="max-w-3xl mx-auto bg-white rounded-2xl shadow-lg p-8">

        <h1 className="text-3xl font-bold text-center text-gray-800">
          AI Resume Analyzer
        </h1>

        <p className="text-center text-gray-500 mt-2 mb-8">
          Analyze your resume against a job description
        </p>
        {result && (
          <div className="mt-10 border-t pt-8">

            <h2 className="text-2xl font-bold text-gray-800 text-center">
              Resume Analysis Result
            </h2>

            <div className="bg-white border rounded-2xl p-8 shadow-sm flex flex-col items-center">

              <h2 className="text-xl font-bold text-gray-800 mb-6">
                Overall Match Score
              </h2>

              <div className="relative w-40 h-40">

                <svg
                  className="w-40 h-40 transform -rotate-90"
                  viewBox="0 0 120 120"
                >
                  {/* Background Circle */}
                  <circle
                    cx="60"
                    cy="60"
                    r="50"
                    strokeWidth="10"
                    fill="none"
                    className="stroke-gray-200"
                  />

                  {/* Progress Circle */}
                  <circle
                    cx="60"
                    cy="60"
                    r="50"
                    strokeWidth="10"
                    fill="none"
                    strokeLinecap="round"
                    className="stroke-blue-600 transition-all duration-1000"
                    strokeDasharray="314"
                    strokeDashoffset={
                      314 - (314 * result.scores.final_score) / 100
                    }
                  />
                </svg>

                {/* Score in center */}
                <div className="absolute inset-0 flex items-center justify-center">
                  <span className="text-3xl font-bold text-gray-800">
                    {result.scores.final_score}%
                  </span>
                </div>


              </div>

              <p className="mt-5 text-gray-500 text-sm text-center">
                Resume compatibility with this job description
              </p>
              {(() => {
                const status = getScoreStatus(result.scores.final_score)

                return (
                  <div className="mt-5 flex flex-col items-center">
                    <div
                      className={`inline-flex items-center gap-2 px-4 py-2 border rounded-full ${status.badge}`}
                    >
                      <span
                        className={`w-2.5 h-2.5 rounded-full ${status.dot}`}
                      ></span>

                      <span className="text-sm font-semibold">
                        {status.label}
                      </span>
                    </div>

                    <h2 className="mt-3 text-sm text-gray-500 text-center max-w-md">
                      {status.message}
                    </h2>
                  </div>
                )
              })()}

            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-5">

              {/* Skill Score */}
              <div className="bg-white border rounded-xl p-5 shadow-sm">
                <div className="flex justify-between mb-2">
                  <h3 className="font-semibold text-gray-700">
                    Skill Score
                  </h3>

                  <span className="font-bold text-blue-600">
                    {result.scores.skill_score}%
                  </span>
                </div>

                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div
                    className="bg-blue-600 h-3 rounded-full transition-all duration-700"
                    style={{
                      width: `${result.scores.skill_score}%`,
                    }}
                  ></div>
                </div>
              </div>


              {/* TF-IDF Score */}
              <div className="bg-white border rounded-xl p-5 shadow-sm">
                <div className="flex justify-between mb-2">
                  <h3 className="font-semibold text-gray-700">
                    TF-IDF Score
                  </h3>

                  <span className="font-bold text-purple-600">
                    {result.scores.tfidf_score}%
                  </span>
                </div>

                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div
                    className="bg-purple-600 h-3 rounded-full transition-all duration-700"
                    style={{
                      width: `${result.scores.tfidf_score}%`,
                    }}
                  ></div>
                </div>
              </div>


              {/* Semantic Score */}
              <div className="bg-white border rounded-xl p-5 shadow-sm">
                <div className="flex justify-between mb-2">
                  <h3 className="font-semibold text-gray-700">
                    Semantic Score
                  </h3>

                  <span className="font-bold text-green-600">
                    {result.scores.semantic_score}%
                  </span>
                </div>

                <div className="w-full bg-gray-200 rounded-full h-3">
                  <div
                    className="bg-green-600 h-3 rounded-full transition-all duration-700"
                    style={{
                      width: `${result.scores.semantic_score}%`,
                    }}
                  ></div>
                </div>
              </div>

            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-6">

              {/* Matched Skills */}
              <div className="bg-white border rounded-2xl p-6 shadow-sm">

                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-lg font-bold text-gray-800">
                    Matched Skills
                  </h3>

                  <span className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm font-semibold">
                    {result.skill_analysis.matched_skills.length}
                  </span>
                </div>

                <div className="flex flex-wrap gap-2">

                  {result.skill_analysis.matched_skills.map((skill, index) => (
                    <span
                      key={index}
                      className="bg-green-50 text-green-700 border border-green-200 px-3 py-2 rounded-lg text-sm font-medium"
                    >
                      ✓ {skill}
                    </span>
                  ))}

                </div>

              </div>


              {/* Missing Skills */}
              <div className="bg-white border rounded-2xl p-6 shadow-sm">

                <div className="flex items-center justify-between mb-4">
                  <h3 className="text-lg font-bold text-gray-800">
                    Missing Skills
                  </h3>

                  <span className="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm font-semibold">
                    {result.skill_analysis.missing_skills.length}
                  </span>
                </div>

                <div className="flex flex-wrap gap-2">

                  {result.skill_analysis.missing_skills.map((skill, index) => (
                    <span
                      key={index}
                      className="bg-red-50 text-red-700 border border-red-200 px-3 py-2 rounded-lg text-sm font-medium"
                    >
                      + {skill}
                    </span>
                  ))}

                </div>

              </div>

            </div>

            <button
              onClick={() => setShowRecommendation(!showRecommendation)}
              className="mt-6 w-full bg-purple-600 text-white font-semibold py-3 rounded-xl hover:bg-purple-700 transition"
            >
              {showRecommendation
                ? "Hide AI Recommendation"
                : "✨ Get AI Career Recommendation"}
            </button>

            {showRecommendation && (
              <div className="mt-6 bg-white border rounded-2xl shadow-sm overflow-hidden">

                {/* Header */}
                <div className="bg-purple-50 border-b px-6 py-5">
                  <div className="flex items-center gap-3">

                    <div className="w-10 h-10 bg-purple-600 text-white rounded-full flex items-center justify-center text-lg">
                      AI
                    </div>

                    <div>
                      <h3 className="text-xl font-bold text-gray-800">
                        AI Career Recommendation
                      </h3>

                      <p className="text-sm text-gray-500">
                        Personalized insights based on your resume and target role
                      </p>
                    </div>

                  </div>
                </div>


                {/* Recommendation Content */}
                <div className="p-6">

                  <div className="bg-gray-50 border rounded-xl p-5">
                    <div className="text-gray-700 whitespace-pre-line leading-7">
                      {result.ai_recommendation}
                    </div>
                  </div>

                </div>

              </div>
            )}
            <button
              onClick={() => {
                setShowForm(true)
                setResult(null)
                setShowRecommendation(false)
                setError("")
              }}
              className="mt-6 w-full bg-blue-600 text-white font-semibold py-3 rounded-xl hover:bg-blue-700 transition"
            >
              Analyze Another Resume
            </button>

          </div>
        )}

        {showForm && (
          <form onSubmit={handleSubmit} className="space-y-5">

            {/* Name */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Full Name
              </label>
              <input
                type="text"
                placeholder="Enter your name"
                value={name}
                onChange={(e) => setName(e.target.value)}
                className="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Email */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Email
              </label>
              <input
                type="email"
                placeholder="Enter your email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Job Title */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Job Title
              </label>
              <input
                type="text"
                placeholder="e.g. Machine Learning Engineer"
                value={jobTitle}
                onChange={(e) => setJobTitle(e.target.value)}
                className="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            {/* Resume */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Upload Resume
              </label>
              <input
                type="file"
                accept=".pdf"
                onChange={(e) => setResume(e.target.files[0])}
                className="w-full border border-gray-300 rounded-lg px-4 py-3"
              />
            </div>

            {/* Job Description */}
            <div>
              <label className="block text-sm font-medium text-gray-700 mb-2">
                Job Description
              </label>
              <textarea
                rows="7"
                placeholder="Paste the job description here..."
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
                className="w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
              ></textarea>
            </div>
            {error && (
              <p className="text-red-600 text-sm font-medium">
                {error}
              </p>
            )}

            {/* Button */}
            <button
              type="submit"
              disabled={loading}
              className="w-full bg-blue-600 text-white font-semibold py-3 rounded-lg hover:bg-blue-700 transition disabled:bg-gray-400 disabled:cursor-not-allowed"
            >
              {loading ? "Analyzing Resume..." : "Analyze Resume"}
            </button>

          </form>
        )}
      </div>
    </div>
  )
}

export default App