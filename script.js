// Your paper data — 6 objects in an array
// Each object has: subject, college, stream, year, board
const papers = [
    { subject: "Physics", college: "St. Joseph's College", stream: "science", year: "2024", board: "PUC" },
    { subject: "Chemistry", college: "Christ College", stream: "science", year: "2023", board: "PUC" },
    { subject: "Mathematics", college: "St. Joseph's College", stream: "science", year: "2024", board: "PUC" },
    { subject: "Accountancy", college: "MES College", stream: "commerce", year: "2023", board: "PUC" },
    { subject: "Business Studies", college: "St. Joseph's College", stream: "commerce", year: "2024", board: "PUC" },
    { subject: "History", college: "Jyoti Nivas College", stream: "arts", year: "2023", board: "PUC" },
  ];
  
  // Tell JS which HTML elements to watch and which to fill
  const searchInput = document.getElementById("search");
  const streamFilter = document.getElementById("stream-filter");
  const container = document.getElementById("papers-container");
  
  // This function builds the HTML for ONE card and returns it as text
  function createCard(paper) {
    return `
      <div class="paper-card">
        <div class="card-subject">${paper.subject}</div>
        <div class="card-college">${paper.college}</div>
        <div class="card-meta">
          <span class="tag">${paper.stream}</span>
          <span class="tag">${paper.year}</span>
          <span class="tag">${paper.board}</span>
        </div>
      </div>
    `;
  }
  
  // This function filters the array and re-renders all cards
  function renderCards() {
    const searchTerm = searchInput.value.toLowerCase();
    const selectedStream = streamFilter.value;
  
    const filtered = papers.filter(function(paper) {
      const matchesSearch =
        paper.subject.toLowerCase().includes(searchTerm) ||
        paper.college.toLowerCase().includes(searchTerm) ||
        paper.year.includes(searchTerm);
  
      const matchesStream =
        selectedStream === "all" || paper.stream === selectedStream;
  
      return matchesSearch && matchesStream;
    });
  
    if (filtered.length === 0) {
      container.innerHTML = '<p class="no-results">No papers found.</p>';
    } else {
      container.innerHTML = filtered.map(createCard).join("");
    }
  }
  
  // Run once on page load to show all cards
  renderCards();
  
  // Every time the user types, re-run
  searchInput.addEventListener("input", renderCards);
  
  // Every time the dropdown changes, re-run
  streamFilter.addEventListener("change", renderCards);