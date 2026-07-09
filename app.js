// ==========================================================================
// GitHub Projects Database (Pre-configured from repository indexing)
// ==========================================================================
const projectsData = [
  {
    id: "ai-business-analyst-demo",
    title: "AI-Business-Analyst-Demo",
    description: "An AI-powered business analyst demo leveraging language models to automate complex reporting, analysis, and dashboard generation.",
    category: "AI & ML",
    language: "TypeScript",
    langColor: "#3178c6",
    link: "https://github.com/johnparente97/AI-Business-Analyst-Demo",
    tech: ["TypeScript", "LLM APIs", "JSON Data Modeling"],
    value: "Demonstrates practical integration of generative AI into business analysis workflows, automating data interpretation and turning raw metrics into stakeholder-ready summaries."
  },
  {
    id: "aep-customer-identity-pipeline",
    title: "aep-customer-identity-pipeline",
    description: "Customer identity resolution pipeline tailored for Adobe Experience Platform (AEP), consolidating cross-device profiles into single customer schemas.",
    category: "Pipelines",
    language: "JavaScript",
    langColor: "#f1e05a",
    link: "https://github.com/johnparente97/aep-customer-identity-pipeline",
    tech: ["JavaScript", "AEP API", "Identity Resolution"],
    value: "Solves critical customer identity gaps by merging fragmented event streams, enabling marketers and analysts to view accurate client journey profiles."
  },
  {
    id: "aep-web-tracking-lab",
    title: "aep-web-tracking-lab",
    description: "Implementation sandbox for web tracking SDKs, capturing customer touchpoints, clicks, and page behaviors for analytics databases.",
    category: "Pipelines",
    language: "HTML",
    langColor: "#e34c26",
    link: "https://github.com/johnparente97/aep-web-tracking-lab",
    tech: ["HTML", "JavaScript", "Adobe SDKs"],
    value: "Validates tracking structures, data layers, and custom event tracking. Reduces data reconciliation errors before production deployment."
  },
  {
    id: "python-banking-suite",
    title: "Python-Banking-Suite",
    description: "Modular banking simulator designed to manage savings, compound interest calculations, and CD account growth with high precision.",
    category: "Software Development",
    language: "Python",
    langColor: "#3572A5",
    link: "https://github.com/johnparente97/Python-Banking-Suite-Managing-Savings-CD-Accounts-with-Modular-Design",
    tech: ["Python", "OOP", "Financial Math"],
    value: "Built with modular design principles (OOP). Provides clear code structures that automate interest projections and demonstrate software architecture fundamentals."
  },
  {
    id: "geo-retail-analytics",
    title: "Geo-Retail-Analytics-Footwear",
    description: "Geographic retail analytics notebook tracking regional sales volumes, consumer trends, and stock adjustments for athletic footwear.",
    category: "Data Analytics",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/Geo-Retail-Analytics-Regional-Sales-and-Trends-in-Athletic-Footwear",
    tech: ["Jupyter Notebook", "Pandas", "Matplotlib", "Geopandas"],
    value: "Applies supply chain and marketing insights to regional sales data. Creates visual geographic maps highlighting product demand hotspots."
  },
  {
    id: "ecommerce-strategic-analysis",
    title: "E-Commerce-Strategic-Analysis",
    description: "Advanced analysis optimizing client portfolios, spend behaviors, and product pricing models to maximize profit margin.",
    category: "Data Analytics",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/E-Commerce-Strategic-Analysis-for-Client-and-Profit-Optimization",
    tech: ["Python", "Pandas", "Profit Modeling"],
    value: "Models supplier costs and customer purchase size to identify off-contract leakage. Directly reflects skills used in procurement and spend reconciliation."
  },
  {
    id: "quickserve-ordering-system",
    title: "QuickServe-Ordering-System",
    description: "Interactive ordering and transaction system simulation built to optimize customer flow, checkout speed, and kitchen queue processing.",
    category: "Software Development",
    language: "Python",
    langColor: "#3572A5",
    link: "https://github.com/johnparente97/QuickServe-Ordering-System",
    tech: ["Python", "Queue Simulation", "UI"],
    value: "Utilizes event-based design to model physical business operations, validating optimization of supply chain logistics at point of sale."
  },
  {
    id: "patterns-search-data-stocks",
    title: "Search-Trends-Stock-Forecasting",
    description: "Time-series study correlating Google search volume patterns against stock price variations to generate predictive forecasting signals.",
    category: "Data Analytics",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/Patterns-in-Search-Data-and-Stock-Prices-for-Strategic-Forecasting",
    tech: ["Jupyter Notebook", "Prophet", "Statsmodels", "Pandas"],
    value: "Leverages predictive modeling (Prophet) to reveal seasonal search trends and their market implications, helping businesses anticipate consumer focus shifts."
  },
  {
    id: "crypto-clustering-pca",
    title: "CryptoClustering-K-Means-PCA",
    description: "Machine learning application classifying cryptocurrency market performance using Principal Component Analysis (PCA) and K-Means clustering.",
    category: "AI & ML",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/CryptoClustering-K-Means-PCA-Driven-Cryptocurrency-Market-Analysis",
    tech: ["Python", "Scikit-Learn", "K-Means", "PCA"],
    value: "Simplifies high-dimensional market data into clear clusters. Proves ability to deploy statistical techniques to segment financial assets."
  },
  {
    id: "email-guardian-ml",
    title: "Email-Guardian-ML-Filter",
    description: "Supervised machine learning pipeline evaluating text token frequencies to classify and filter spam emails.",
    category: "AI & ML",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/Email-Guardian-Harnessing-Machine-Learning-to-Filter-the-Inbox",
    tech: ["Python", "NLP", "Naive Bayes", "Scikit-Learn"],
    value: "Implements security and automation in communications. Turns unstructured text data into actionable routing decisions using machine learning."
  },
  {
    id: "employee-attrition-network",
    title: "Employee-Attrition-Neural-Network",
    description: "Deep learning neural network modeling employee attributes to predict turnover probabilities and appropriate department placement.",
    category: "AI & ML",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/Employee-Attrition-Department-Prediction-Neural-Network",
    tech: ["TensorFlow", "Keras", "Deep Learning"],
    value: "Provides HR and operations teams with predictive attrition foresight. Enables preventative retention actions by flagging departments at risk."
  },
  {
    id: "spam-ham-classification",
    title: "Spam-or-Ham-Text-Classification",
    description: "Natural Language Processing (NLP) text classification model targeting SMS data to identify messages as ham or spam.",
    category: "AI & ML",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/Spam-or-Ham-Text-Message-Classification-with-Machine-Learning",
    tech: ["Python", "NLP", "TF-IDF", "Random Forest"],
    value: "Demonstrates text preprocessing, feature engineering (TF-IDF vectorizer), and model evaluation metrics for business automation."
  },
  {
    id: "sourcing-movie-data",
    title: "Sourcing-Movie-Data-With-APIs",
    description: "Data collection engine connecting to external REST APIs, downloading metadata, cleaning schemas, and outputting clean database records.",
    category: "Pipelines",
    language: "Jupyter Notebook",
    langColor: "#DA5B0B",
    link: "https://github.com/johnparente97/Sourcing-Movie-Data-With-APIs",
    tech: ["API Integration", "JSON Extraction", "Pandas"],
    value: "Showcases ETL (Extract, Transform, Load) pipelines. Translates nested API payloads into flat, normalized tables prepared for dashboarding."
  },
  {
    id: "solana-case-study",
    title: "Solana-Case-Study",
    description: "Thorough market research and technical evaluation of the Solana blockchain framework, network costs, and scalability metrics.",
    category: "Data Analytics",
    language: "Rich Text Format",
    langColor: "#2a2d38",
    link: "https://github.com/johnparente97/Solana-Case-Study",
    tech: ["Market Analysis", "Blockchain Research", "Strategy"],
    value: "Highlights strategic technology evaluation skills. Explains complex blockchain performance data to help operators assess adoption opportunities."
  }
];

// ==========================================================================
// Initialization & Core Logic
// ==========================================================================
document.addEventListener("DOMContentLoaded", () => {
  initTheme();
  renderProjects(projectsData);
  initProjectFilters();
  initProjectSearch();
  initContactForm();
  initIntersectionObserver();
});

// ==========================================================================
// Theme Management
// ==========================================================================
function initTheme() {
  const themeToggleBtn = document.getElementById("theme-toggle");
  if (!themeToggleBtn) return;
  
  // Load saved theme or fall back to system preference
  const savedTheme = localStorage.getItem("portfolio-theme");
  const prefersLight = window.matchMedia("(prefers-color-scheme: light)").matches;
  
  const currentTheme = savedTheme || (prefersLight ? "light" : "dark");
  document.body.setAttribute("data-theme", currentTheme);
  
  themeToggleBtn.addEventListener("click", () => {
    const isDark = document.body.getAttribute("data-theme") !== "light";
    const nextTheme = isDark ? "light" : "dark";
    document.body.setAttribute("data-theme", nextTheme);
    localStorage.setItem("portfolio-theme", nextTheme);
  });
}

// ==========================================================================
// Render Project Cards
// ==========================================================================
function renderProjects(projects) {
  const grid = document.getElementById("projects-grid");
  if (!grid) return;
  
  grid.innerHTML = "";
  
  if (projects.length === 0) {
    grid.innerHTML = `
      <div style="grid-column: 1/-1; text-align: center; padding: 3rem; color: var(--text-secondary);">
        <p>No projects found matching your criteria. Try adjusting your search query.</p>
      </div>
    `;
    return;
  }
  
  projects.forEach(project => {
    const card = document.createElement("article");
    card.className = "project-card glass-card";
    card.setAttribute("tabindex", "0");
    card.setAttribute("role", "button");
    card.setAttribute("aria-label", `View details of project ${project.title}`);
    
    card.innerHTML = `
      <span class="project-category">${project.category}</span>
      <h3 class="project-title">${project.title}</h3>
      <p class="project-desc">${project.description}</p>
      <div class="project-meta">
        <span class="project-lang">
          <span class="lang-color" style="background-color: ${project.langColor}"></span>
          ${project.language}
        </span>
        <span class="project-link">
          Details &rarr;
        </span>
      </div>
    `;
    
    // Open detail modal on click or Enter keypress
    const openModal = () => showProjectModal(project);
    card.addEventListener("click", openModal);
    card.addEventListener("keydown", (e) => {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        openModal();
      }
    });
    
    grid.appendChild(card);
  });
}

// ==========================================================================
// Project Filters
// ==========================================================================
let activeCategory = "All";
let searchQuery = "";

function initProjectFilters() {
  const filterBtns = document.querySelectorAll(".filter-btn");
  
  filterBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      // Update UI active state
      filterBtns.forEach(b => b.classList.remove("active"));
      btn.classList.add("active");
      
      // Update filter criteria
      activeCategory = btn.getAttribute("data-filter");
      applyFilters();
    });
  });
}

function initProjectSearch() {
  const searchInput = document.getElementById("project-search");
  if (!searchInput) return;
  
  searchInput.addEventListener("input", (e) => {
    searchQuery = e.target.value.toLowerCase().trim();
    applyFilters();
  });
}

function applyFilters() {
  const filtered = projectsData.filter(project => {
    const matchesCategory = activeCategory === "All" || project.category === activeCategory;
    const matchesSearch = project.title.toLowerCase().includes(searchQuery) ||
                          project.description.toLowerCase().includes(searchQuery) ||
                          project.tech.some(t => t.toLowerCase().includes(searchQuery)) ||
                          project.language.toLowerCase().includes(searchQuery);
                          
    return matchesCategory && matchesSearch;
  });
  
  renderProjects(filtered);
}

// ==========================================================================
// Project Modal / Dialog Control
// ==========================================================================
function showProjectModal(project) {
  let dialog = document.getElementById("project-details-modal");
  
  if (!dialog) {
    dialog = document.createElement("dialog");
    dialog.id = "project-details-modal";
    dialog.className = "project-modal";
    document.body.appendChild(dialog);
  }
  
  const techTagsHtml = project.tech.map(t => `<span class="modal-tech-tag">${t}</span>`).join("");
  
  dialog.innerHTML = `
    <div class="modal-header">
      <span class="modal-category">${project.category}</span>
      <button class="modal-close-btn" aria-label="Close modal">&times;</button>
    </div>
    <h3 class="modal-title">${project.title}</h3>
    <p class="modal-desc">${project.description}</p>
    
    <div class="modal-value-box">
      <h4>Business Value & Impact</h4>
      <p>${project.value}</p>
    </div>
    
    <div class="modal-footer">
      <div class="modal-tech">
        ${techTagsHtml}
      </div>
      <a href="${project.link}" target="_blank" rel="noopener noreferrer" class="btn btn-primary" style="padding: 0.5rem 1rem; font-size: 0.85rem;">
        View Repository
      </a>
    </div>
  `;
  
  // Close buttons and backdrop click handlers
  const closeBtn = dialog.querySelector(".modal-close-btn");
  closeBtn.addEventListener("click", () => dialog.close());
  
  dialog.addEventListener("click", (e) => {
    if (e.target === dialog) {
      dialog.close();
    }
  });
  
  // Escape key close comes natively with <dialog>
  dialog.showModal();
}

// ==========================================================================
// Contact Form Handler
// ==========================================================================
function initContactForm() {
  const form = document.getElementById("contact-form");
  const statusDiv = document.getElementById("form-status");
  if (!form || !statusDiv) return;
  
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    
    // Get fields
    const name = document.getElementById("form-name").value.trim();
    const email = document.getElementById("form-email").value.trim();
    const message = document.getElementById("form-message").value.trim();
    
    if (!name || !email || !message) {
      showStatus("Please fill in all fields.", "error");
      return;
    }
    
    // Simulate submission (save to localStorage)
    const submissions = JSON.parse(localStorage.getItem("portfolio-inquiries") || "[]");
    submissions.push({ name, email, message, date: new Date().toISOString() });
    localStorage.setItem("portfolio-inquiries", JSON.stringify(submissions));
    
    showStatus("Message sent successfully! Thank you for reaching out.", "success");
    form.reset();
  });
  
  function showStatus(text, type) {
    statusDiv.textContent = text;
    statusDiv.className = `form-status ${type}`;
    
    setTimeout(() => {
      statusDiv.style.display = "none";
    }, 5000);
  }
}

// ==========================================================================
// Intersection Observer for Animate-On-Scroll & Stats Counter
// ==========================================================================
function initIntersectionObserver() {
  const statsElements = document.querySelectorAll(".impact-num");
  let animated = false;
  
  const statsObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (entry.isIntersecting && !animated) {
        animateCounters();
        animated = true;
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });
  
  const snapshotSection = document.querySelector(".impact-snapshot");
  if (snapshotSection) {
    statsObserver.observe(snapshotSection);
  }
  
  // Fade in animation for other elements
  const fadeElements = document.querySelectorAll(".glass-card, .timeline-item, .section-title");
  
  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
      }
    });
  }, { threshold: 0.05 });
  
  fadeElements.forEach(el => {
    el.style.opacity = "0";
    el.style.transform = "translateY(20px)";
    el.style.transition = "opacity 0.6s ease-out, transform 0.6s ease-out";
    fadeObserver.observe(el);
  });
}

function animateCounters() {
  const stats = [
    { id: "stat-accounts", target: 50, suffix: "+" },
    { id: "stat-spend", target: 10, prefix: "$", suffix: "M+" },
    { id: "stat-rebates", target: 150, prefix: "$", suffix: "K+" },
    { id: "stat-crm", target: 100, suffix: "+" },
    { id: "stat-social", target: 42.5, suffix: "K+" }
  ];
  
  stats.forEach(stat => {
    const el = document.getElementById(stat.id);
    if (!el) return;
    
    let current = 0;
    const isFloat = stat.target % 1 !== 0;
    const duration = 1500; // ms
    const frameRate = 1000 / 60; // 60 fps
    const totalFrames = Math.round(duration / frameRate);
    const increment = stat.target / totalFrames;
    
    let frame = 0;
    
    const count = () => {
      frame++;
      current += increment;
      
      if (frame >= totalFrames) {
        current = stat.target;
        clearInterval(timer);
      }
      
      let formattedVal = isFloat ? current.toFixed(1) : Math.floor(current);
      el.textContent = `${stat.prefix || ""}${formattedVal}${stat.suffix}`;
    };
    
    const timer = setInterval(count, frameRate);
  });
}
