
import random
import csv
import statistics

print(" " + "=" * 50)
print("CATASTROPHE LOSS SIMULATOR")
print(" " + "=" * 50)

simulation_years = 10000


average_events = 2


minimum_loss = 1_000_000
most_likely_loss = 5_000_000
maximum_loss = 20_000_000


loss_threshold = 15_000_000




def simulate_event_count(average_events):

    limit = 2.71828 ** (-average_events)

    count = 0
    product = 1

    while product > limit:
        count += 1
        product *= random.random()

    return count - 1




def simulate_event_loss():

    loss = random.triangular(
        minimum_loss,
        maximum_loss,
        most_likely_loss
    )

    return round(loss, 2)

annual_losses = []


for year in range(1, simulation_years + 1):

    event_count = simulate_event_count(average_events)

    total_annual_loss = 0

    for event in range(event_count):

        event_loss = simulate_event_loss()

        total_annual_loss += event_loss

    annual_losses.append(total_annual_loss)




average_loss = statistics.mean(annual_losses)

median_loss = statistics.median(annual_losses)

maximum_annual_loss = max(annual_losses)

minimum_annual_loss = min(annual_losses)



exceed_count = sum(loss > loss_threshold for loss in annual_losses)

exceed_probability = ( exceed_count / simulation_years) * 100


print("SIMULATION RESULTS")

print(f"Years Simulated: {simulation_years:,}")

print(f"Average Annual Loss: ${average_loss:,.2f}")

print(f"Median Annual Loss: ${median_loss:,.2f}")

print(f"Maximum Annual Loss: ${maximum_annual_loss:,.2f}")

print(f"Minimum Annual Loss: ${minimum_annual_loss:,.2f}")

print(
    f"Probability of Exceeding "
    f"${loss_threshold:,.0f}: "
    f"{exceed_probability:.2f}%"
)



with open(
    "catastrophe_simulation_results.csv",
    "w",
    newline= ""
) as file:

    writer = csv.writer(file)

    writer.writerow(["Year", "Total Annual Catastrophe Loss"])

    for year, loss in enumerate(annual_losses, start=1):

        writer.writerow([year, round(loss, 2)])


print("Simulation results exported successfully!")

print("File: catastrophe_simulation_results.csv")
