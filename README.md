# CareerPrep Job-Hunting Agent

A file-driven AI agent that helps students manage their job search workflow.

## Student Info
- Name: Amna Arshad
- Roll Number: 22F-3170
- Section: BAI-8A

## How to Run

1. Clone this repository:
git clone https://github.com/amna-arshad7/job-hunting-agent

2. Go into the folder:
cd job-hunting-agent

3. Run the agent:
python app.py

## What This Agent Does
- Reads job posters from input_jobs/
- Reads resume from input_resumes/
- Reads interview notes from input_kb/
- Generates skill gap report
- Generates resume tailoring suggestions
- Generates interview questions from KB
- Maintains application tracker with CSV
- Generates reminders with urgency levels

## Folder Structure
- input_jobs/ — Real job descriptions (Systems Limited, Arbisoft)
- input_resumes/ — Student resume
- input_kb/ — Interview preparation notes
- outputs/ — All generated reports
- tracker/ — Application CSV and reminders
- samples/ — Sample files for testing

## Output Files Generated
- outputs/job_analysis_report.txt
- outputs/skill_gap_report.txt
- outputs/tailored_resume_suggestions.txt
- outputs/interview_questions.txt
- outputs/final_agent_report.txt
- tracker/applications.csv
- tracker/reminders.txt

## Unique Features Added
- Reminder urgency system (OVERDUE / TODAY / TOMORROW / THIS WEEK)
- Match score with status (STRONG / MODERATE / WEAK)
- Real job data from Systems Limited and Arbisoft Pakistan
- Resume suggestions with specific bullet points
