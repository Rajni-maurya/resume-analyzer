// static/js/app.js
document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("analyze-form");
  const analyzeBtn = document.getElementById("analyze-btn");
  const loader = document.getElementById("loader-area");
  const resultArea = document.getElementById("result-area");
  const alertBox = document.getElementById("alert-box");
  const wText = document.getElementById("w_text");
  const wTextVal = document.getElementById("w_text_val");

  wText.addEventListener("input", () => {
    wTextVal.textContent = parseFloat(wText.value).toFixed(2);
  });

  form.addEventListener("submit", async function(e) {
    e.preventDefault();
    alertBox.innerHTML = "";
    resultArea.style.display = "none";
    loader.style.display = "block";
    analyzeBtn.disabled = true;

    const fd = new FormData(form);
    try {
      const resp = await fetch("/analyze", {
        method: "POST",
        body: fd
      });
      const data = await resp.json();
      if (!data.ok) {
        alertBox.innerHTML = <div class="alert alert-danger">${data.error || "Analysis failed"}</div>;
      } else {
        // show results
        document.getElementById("resume-preview").textContent = data.resume_preview || "";
        document.getElementById("resume-skills").textContent = (data.resume_skills && data.resume_skills.join(", ")) || "—";
        document.getElementById("job-skills").textContent = (data.job_skills && data.job_skills.join(", ")) || "—";
        document.getElementById("text-sim").innerHTML = <strong>Text similarity:</strong> ${(data.text_similarity*100).toFixed(2)}%;
        document.getElementById("skill-percent").innerHTML = <strong>Skill match:</strong> ${data.skill_summary.skill_match_pct}%;
        document.getElementById("matched-list").textContent = Matched: ${data.skill_summary.matched.join(", ") || "—"};
        const final = data.final_score;
        // simple circular score
        const circle = <div class="score-circle">${final}</div>;
        document.getElementById("score-circle").innerHTML = circle;
        // missing skills
        const miss = data.skill_summary.missing || [];
        document.getElementById("missing-skills").textContent = miss.length ? Missing (from JD): ${miss.join(", ")} : "";
        resultArea.style.display = "block";
        alertBox.innerHTML = <div class="alert alert-success">Analysis complete</div>;
      }
    } catch (err) {
      console.error(err);
      alertBox.innerHTML = <div class="alert alert-danger">Error: ${err.message}</div>;
    } finally {
      loader.style.display = "none";
      analyzeBtn.disabled = false;
    }
  });
});
