import os
import csv
from datetime import datetime, date

JOB_DIR = "input_jobs"
RESUME_DIR = "input_resumes"
KB_DIR = "input_kb"
OUTPUT_DIR = "outputs"
TRACKER_DIR = "tracker"

KEYWORDS = [
    "python", "machine learning", "data preprocessing", "github", "git",
    "api", "prompt engineering", "sql", "communication", "problem solving",
    "oop", "database", "jupyter", "pandas", "numpy", "deep learning",
    "html", "css", "flask", "streamlit", "resume", "interview"
]

def ensure_folders():
    for folder in [JOB_DIR, RESUME_DIR, KB_DIR, OUTPUT_DIR, TRACKER_DIR]:
        os.makedirs(folder, exist_ok=True)

def read_text_files(folder):
    combined_text = ""
    file_list = []
    file_count = 0
    for filename in os.listdir(folder):
        if filename.lower().endswith(".txt"):
            path = os.path.join(folder, filename)
            with open(path, "r", encoding="utf-8") as file:
                combined_text += f"\n\n--- FILE: {filename} ---\n"
                combined_text += file.read()
            file_list.append(filename)
            file_count += 1
    return combined_text, file_count, file_list

def save_text(path, content):
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)

def extract_keywords(text):
    text_lower = text.lower()
    found = []
    for keyword in KEYWORDS:
        if keyword in text_lower:
            found.append(keyword)
    return found

def compare_skills(job_skills, resume_skills):
    matched = [skill for skill in job_skills if skill in resume_skills]
    missing = [skill for skill in job_skills if skill not in resume_skills]
    score = 0 if not job_skills else round((len(matched) / len(job_skills)) * 100, 2)
    return matched, missing, score

def show_menu(file_list, label):
    print(f"\n--- Select {label} ---")
    for i, f in enumerate(file_list):
        print(f"  {i+1}. {f}")
    choice = input("Enter number (or press Enter for all): ").strip()
    return choice

def generate_job_analysis(job_text, job_skills):
    report = "Job Analysis Report\n===================\n\n"
    report += f"Total skills/keywords found: {len(job_skills)}\n\n"
    report += "Skills/keywords found in job posters:\n"
    for skill in job_skills:
        report += f"  - {skill}\n"
    return report

def generate_skill_gap_report(job_skills, resume_skills, matched, missing, score):
    report = "Skill Gap Report\n================\n\n"
    report += f"Match Score: {score}%\n\n"
    if score >= 75:
        report += "Status: STRONG MATCH - You are well prepared!\n\n"
    elif score >= 50:
        report += "Status: MODERATE MATCH - Some improvement needed.\n\n"
    else:
        report += "Status: WEAK MATCH - Significant preparation required.\n\n"
    report += "Matched Skills:\n"
    for skill in matched:
        report += f"  + {skill}\n"
    report += "\nMissing Skills:\n"
    for skill in missing:
        report += f"  - {skill}\n"
    return report

def generate_resume_suggestions(job_skills, missing):
    output = "Tailored Resume Suggestions\n===========================\n\n"
    output += "Suggested improvements based on job requirements:\n\n"
    for skill in job_skills:
        output += f"  - Add or improve resume evidence related to: {skill}\n"
    output += "\nSuggested Resume Bullet Points:\n"
    output += "  - Developed Python-based academic projects with clear documentation.\n"
    output += "  - Used GitHub for project version control and README-based documentation.\n"
    output += "  - Applied machine learning algorithms on real datasets.\n"
    output += "  - Performed data preprocessing using Pandas and NumPy.\n"
    output += "  - Built and deployed web apps using Streamlit.\n"
    if missing:
        output += "\nSkills to Learn Before Applying:\n"
        for skill in missing:
            output += f"  * {skill} - add projects or courses to demonstrate this\n"
    return output

def generate_interview_questions(job_skills, kb_text):
    questions = "Interview Questions\n===================\n\n"
    questions += "Technical Questions (based on job requirements):\n"
    for skill in job_skills:
        questions += f"  - Explain your understanding of {skill}.\n"
        questions += f"  - How have you used {skill} in a project?\n"
    questions += "\nHR and Behavioral Questions:\n"
    questions += "  - Tell me about yourself.\n"
    questions += "  - Why are you interested in this role?\n"
    questions += "  - Describe your best academic/project work.\n"
    questions += "  - What are your strengths and weaknesses?\n"
    questions += "  - Why should we select you?\n"
    questions += "  - Where do you see yourself in 5 years?\n"
    questions += "\nQuestions from Knowledge Base:\n"
    kb_lines = [line.strip("- ").strip() for line in kb_text.splitlines() if line.strip() and not line.startswith("Topic")]
    for line in kb_lines[:10]:
        questions += f"  - How would you explain: {line}?\n"
    return questions

def get_reminder_urgency(date_str):
    if not date_str:
        return ""
    try:
        target = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = date.today()
        diff = (target - today).days
        if diff < 0:
            return "OVERDUE"
        elif diff == 0:
            return "TODAY"
        elif diff == 1:
            return "TOMORROW"
        elif diff <= 7:
            return "THIS WEEK"
        else:
            return f"In {diff} days"
    except:
        return ""

def create_or_update_tracker():
    path = os.path.join(TRACKER_DIR, "applications.csv")
    if not os.path.exists(path):
        with open(path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "application_id", "company", "role", "source", "status",
                "applied_date", "interview_date", "follow_up_date", "next_action", "notes"
            ])
            writer.writerow([
                "APP-001", "Sample Company", "AI Intern", "Job Poster",
                "Not Applied", "", "", "", "Tailor resume and apply", "Sample row"
            ])
    return path

def generate_reminders():
    tracker_path = os.path.join(TRACKER_DIR, "applications.csv")
    reminders = "Application Reminders\n=====================\n"
    reminders += f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n"
    if not os.path.exists(tracker_path):
        return "No tracker file found."
    with open(tracker_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            app_id = row.get("application_id", "")
            company = row.get("company", "")
            role = row.get("role", "")
            status = row.get("status", "")
            interview_date = row.get("interview_date", "")
            follow_up_date = row.get("follow_up_date", "")
            next_action = row.get("next_action", "")
            if status.lower() == "interview scheduled":
                urgency = get_reminder_urgency(interview_date)
                reminders += f"[{urgency}] {app_id}: Interview at {company} for {role} on {interview_date}\n"
                reminders += f"  Next action: {next_action}\n\n"
            elif status.lower() == "not applied":
                reminders += f"[ACTION NEEDED] {app_id}: Not applied yet for {role} at {company}.\n"
                reminders += f"  Action: Tailor resume and apply soon.\n\n"
            elif status.lower() == "applied":
                urgency = get_reminder_urgency(follow_up_date)
                reminders += f"[{urgency}] {app_id}: Applied to {company}. Follow up on {follow_up_date}.\n\n"
    return reminders

def run_agent():
    ensure_folders()
    print("\n====================================")
    print("  CareerPrep Job-Hunting Agent")
    print("====================================\n")

    job_text, job_count, job_files = read_text_files(JOB_DIR)
    resume_text, resume_count, resume_files = read_text_files(RESUME_DIR)
    kb_text, kb_count, kb_files = read_text_files(KB_DIR)

    if job_count == 0 or resume_count == 0 or kb_count == 0:
        print("Please add .txt files in input_jobs, input_resumes, and input_kb folders.")
        return

    print(f"Found {job_count} job poster(s): {job_files}")
    print(f"Found {resume_count} resume file(s): {resume_files}")
    print(f"Found {kb_count} KB file(s): {kb_files}")

    job_skills = extract_keywords(job_text)
    resume_skills = extract_keywords(resume_text)
    matched, missing, score = compare_skills(job_skills, resume_skills)

    print(f"\nMatch Score: {score}%")
    print(f"Matched Skills: {matched}")
    print(f"Missing Skills: {missing}")

    job_report = generate_job_analysis(job_text, job_skills)
    gap_report = generate_skill_gap_report(job_skills, resume_skills, matched, missing, score)
    resume_suggestions = generate_resume_suggestions(job_skills, missing)
    interview_questions = generate_interview_questions(job_skills, kb_text)

    create_or_update_tracker()
    reminders = generate_reminders()

    final_report = "CareerPrep Job-Hunting Agent - Final Report\n"
    final_report += f"Generated on: {datetime.now()}\n"
    final_report += "=" * 45 + "\n\n"
    final_report += job_report + "\n"
    final_report += gap_report + "\n"
    final_report += resume_suggestions + "\n"
    final_report += interview_questions + "\n"
    final_report += reminders + "\n"

    save_text(os.path.join(OUTPUT_DIR, "job_analysis_report.txt"), job_report)
    save_text(os.path.join(OUTPUT_DIR, "skill_gap_report.txt"), gap_report)
    save_text(os.path.join(OUTPUT_DIR, "tailored_resume_suggestions.txt"), resume_suggestions)
    save_text(os.path.join(OUTPUT_DIR, "interview_questions.txt"), interview_questions)
    save_text(os.path.join(OUTPUT_DIR, "final_agent_report.txt"), final_report)
    save_text(os.path.join(TRACKER_DIR, "reminders.txt"), reminders)

    print("\nAgent completed successfully!")
    print("All outputs saved in outputs/ and tracker/ folders.")

if __name__ == "__main__":
    run_agent()
