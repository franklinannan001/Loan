# Credit Decision Evaluator

A lightweight Python command-line application that evaluates loan or credit eligibility based on an applicant's credit score, monthly income (in KSH), and payment history.

## Features

* **Interactive CLI Prompts:** Collects applicant details including name, credit score, monthly income, and missed payments.
* **Input Validation:** Ensures credit scores fall within the standard 300–850 range and prevents negative values for income or missed payments.
* **Tiered Risk Assessment:** Automatically categorizes applicants into four distinct lending tiers.
* **Clean Formatting:** Outputs neatly formatted currency figures (`KSH`) and personalized decision messages.

## Decision Logic

The application evaluates applicants using the following rules:

| Decision Tier | Criteria | Outcome Message |
| :--- | :--- | :--- |
| **Rejected** | Credit score `< 580`, monthly income `< KSH 15,000`, or missed payments `> 2` | *Application does not meet requirements.* |
| **Excellent Terms** | Credit score `>= 750` (and passes rejection checks) | *You qualify for our best rate.* |
| **Standard Terms** | Credit score `650 – 749` (and passes rejection checks) | *Approved at standard rate.* |
| **High-Interest Terms** | Credit score `580 – 649` (and passes rejection checks) | *Approved, but at a higher rate.* |

> **Note:** Inputs outside valid ranges (e.g., credit score `< 300` or `> 850`, or non-numeric entries) will exit gracefully without generating a decision.

## Prerequisites

* **Python 3.10 or higher** (required for structural pattern matching via `match`/`case`).

## Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd your-repo-name
   ```

2. **Run the script:**
   ```bash
   python main.py
   ```
   *(Replace `main.py` with your actual filename if different.)*

## Usage Example

```text
What is your name: jane doe
What is your credit score: 760
What is your monthly income: 45000
How many missed payments do you have: 0
Jane Doe has a credit score of 760 with KSH 45,000.00 income — Excellent Terms. You qualify for our best rate.
```

## Project Structure

* `main()` — Handles user input, exception catching, and formatted output.
* `get_decision()` — Validates input boundaries and determines the approval tier.
* `get_message()` — Maps the decision tier to a user-friendly status message.
