## Deployed app Link : https://calculationappio-subkiplvp4cyhkylmr9zdk.streamlit.app/

# Loyalty Point Calculator Demo
## Project Overview
This project is designed to demonstrate the calculation of loyalty points for an online gaming platform. The application uses a predefined formula to calculate points based on player activities such as depositing money, withdrawing money, and playing games. The formula is designed to reward players for their engagement on the platform. The project is implemented using Streamlit to create an interactive user interface.
## Assignment Goals
### Part A: Calculating Loyalty Points
Slot-Based Calculation:

Calculates player loyalty points for specific slots:
2nd October Slot S1 (12am - 12pm)
16th October Slot S2 (12pm - 12am)
18th October Slot S1 (12am - 12pm)
26th October Slot S2 (12pm - 12am)
Overall Monthly Points:

Calculates total loyalty points earned by all players during October.
Ranks players based on their loyalty points, using the number of games played as a tiebreaker.
Averages:

Average deposit amount.
Average deposit amount per user for the month.
Average number of games played per user.

### Part B: Leaderboard Bonus Distribution
The company allocates a ₹50,000 bonus pool for the top 50 players based on their loyalty points. A hybrid distribution system is proposed, considering both:

Loyalty points earned.
Number of games played.
### Part C: Evaluating and Improving the Formula
Discusses the fairness of the existing formula.
Proposes enhancements to improve player engagement and reward consistency, such as:
Consistency bonuses (daily login streaks, weekend bonuses).
Skill-based rewards (win rate, tournament participation).
Dynamic weighting for different engagement levels.

## Features of the Application
### Interactive Interface:

Players can be selected from a dropdown list to view detailed calculations of their loyalty points.

### Customizable Calculations:

Each player's activity (deposits, withdrawals, games played) is used to compute their points.

### Point Breakdown:

Deposit points, withdrawal points, net deposit points, and game points are calculated and displayed.

### Expandable Dataset:

Includes data for 20 players, which can be expanded as needed.

## Technical Details
### Formula for Loyalty Points
Loyalty points are calculated using the following formula:
Loyalty Points = (0.01 × Deposit Amount) 
               + (0.005 × Withdrawal Amount) 
               + (0.001 × max(Number of Deposits - Number of Withdrawals, 0))
               + (0.2 × Number of Games Played)

### Implementation Stack
Programming Language: Python
Framework: Streamlit (for UI)
Data Handling: Pandas (for tabular data processing)

## How to Run the Application
### Prerequisites
Python 3.7 or higher
Streamlit installed (pip install streamlit)
### Steps to Run
Clone or download the project files.
Navigate to the project directory.
Save the main file as loyalty_demo.py.
Run the application:
streamlit run loyalty_demo.py

## Proposed Enhancements for the Formula
To make the loyalty point system more robust:

Add daily login streak bonuses to encourage regular activity.
Introduce win rate multipliers to reward skilled players.
Apply dynamic weightings for players based on their engagement level (e.g., beginner, intermediate, expert).
Award tournament participation bonuses for competitive gameplay.

## Example Dataset
This project comes with a sample dataset of 20 players. Each player's data includes:

Deposited and withdrawn amounts.
Number of deposits and withdrawals.
Number of games played.
The user can interact with the application to view calculations for any player.
