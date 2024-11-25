import streamlit as st
import pandas as pd

# Generate example data for 20 players
example_data = [
    {
        "Player": f"Player {i+1}",
        "Deposited Amount (₹)": 1000 + i * 50,
        "Withdrawn Amount (₹)": 500 + i * 20,
        "Number of Deposits": 5 + i,
        "Number of Withdrawals": 3 + (i % 2),
        "Number of Games Played": 20 + i * 2
    }
    for i in range(20)
]

# Convert to DataFrame
df = pd.DataFrame(example_data)

# Function to calculate loyalty points
def calculate_loyalty_points(data):
    deposit_points = 0.01 * data["Deposited Amount (₹)"]
    withdrawal_points = 0.005 * data["Withdrawn Amount (₹)"]
    net_deposit_points = 0.001 * max(data["Number of Deposits"] - data["Number of Withdrawals"], 0)
    game_points = 0.2 * data["Number of Games Played"]
    total_points = deposit_points + withdrawal_points + net_deposit_points + game_points
    
    # Return breakdown and total
    return {
        "Deposit Points": deposit_points,
        "Withdrawal Points": withdrawal_points,
        "Net Deposit Points": net_deposit_points,
        "Game Points": game_points,
        "Total Points": total_points
    }

# Streamlit UI
st.title("Loyalty Point Calculator Demo")
st.subheader("Click on a player to see detailed calculations")

# Show the table of players
st.write("### Player Data")
st.dataframe(df)

# Select a player
player_choice = st.selectbox("Select a Player", df["Player"])

# Filter selected player data
selected_player_data = df[df["Player"] == player_choice].iloc[0]

# Perform calculations
calculation_results = calculate_loyalty_points(selected_player_data)

# Show detailed calculations
st.write(f"## Calculations for {player_choice}")
st.write(f"**Deposited Amount (₹):** {selected_player_data['Deposited Amount (₹)']}")
st.write(f"**Withdrawn Amount (₹):** {selected_player_data['Withdrawn Amount (₹)']}")
st.write(f"**Number of Deposits:** {selected_player_data['Number of Deposits']}")
st.write(f"**Number of Withdrawals:** {selected_player_data['Number of Withdrawals']}")
st.write(f"**Number of Games Played:** {selected_player_data['Number of Games Played']}")

st.write("### Point Breakdown")
st.write(f"- **Deposit Points:** {calculation_results['Deposit Points']:.2f}")
st.write(f"- **Withdrawal Points:** {calculation_results['Withdrawal Points']:.2f}")
st.write(f"- **Net Deposit Points:** {calculation_results['Net Deposit Points']:.2f}")
st.write(f"- **Game Points:** {calculation_results['Game Points']:.2f}")
st.write(f"### **Total Loyalty Points:** {calculation_results['Total Points']:.2f}")

# Additional note
st.info("This is a demonstration of loyalty point calculations based on the given formula. Adjust the parameters in the example data as needed for testing.")

