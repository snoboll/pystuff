import numpy as np
import matplotlib.pyplot as plt

# Constants
years = 40
initial_investment = 100000  # SEK
monthly_investment = 1000  # SEK
monthly_investment_annual = monthly_investment * 12  # Annualized monthly investment
isk_tax_rate = 0.01  # Assumed average ISK tax rate
capital_gains_tax = 0.30  # 30% capital gains tax
compounded_rates = [0.04, 0.10, 0.20]  # Compounding rates
inflation_rate = 0.05  # 5% inflation rate

# Function to generate savings data for each year, adjusted for inflation
def calculate_savings_yearly_inflation(compound_rate, tax_annual, tax_end=False):
    yearly_real_savings = [initial_investment]
    total_savings = initial_investment
    effective_rate = compound_rate - inflation_rate  # Adjust for inflation

    for year in range(1, years + 1):
        # Add yearly investment
        total_savings += monthly_investment_annual

        # Compound the investment with inflation adjustment
        total_savings *= (1 + effective_rate)

        # Tax calculation
        if tax_annual:
            tax = total_savings * isk_tax_rate
            total_savings -= tax
        elif year == years and tax_end:  # Tax at the end
            gain = total_savings - initial_investment - (monthly_investment_annual * years)
            tax = gain * capital_gains_tax
            total_savings -= tax

        yearly_real_savings.append(total_savings)

    return yearly_real_savings

# Generate inflation-adjusted data for each model
model1_yearly_inflation = calculate_savings_yearly_inflation(compounded_rates[0], tax_annual=True)
models2_yearly_inflation = [calculate_savings_yearly_inflation(rate, tax_annual=True) for rate in compounded_rates[1:]]
models3_yearly_inflation = [calculate_savings_yearly_inflation(rate, tax_annual=False, tax_end=True) for rate in compounded_rates[1:]]

# Data for plotting
years_x = list(range(0, years + 1))  # 0 to 20 years

# Plotting the results with inflation adjustment
plt.figure(figsize=(12, 6))

# Plot for the first model
plt.plot(years_x, model1_yearly_inflation, label='4% Compounded, Annual Tax (ISK style)', marker='o')

# Plots for models with varied compounding rates, annual tax
for rate, model in zip(compounded_rates[1:], models2_yearly_inflation):
    plt.plot(years_x, model, label=f'{rate*100}% Compounded, Annual Tax', marker='o')

# Plots for models with varied compounding rates, tax at end
for rate, model in zip(compounded_rates[1:], models3_yearly_inflation):
    plt.plot(years_x, model, label=f'{rate*100}% Compounded, Tax at End', linestyle='--')

plt.title('Inflation-Adjusted Savings Over 20 Years for Different Investment Models')
plt.xlabel('Years')
plt.ylabel('Real Total Savings (SEK, Inflation-Adjusted)')
plt.legend()
plt.grid(True)
plt.show()
