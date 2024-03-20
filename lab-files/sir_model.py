import scipy.integrate

class SIRModel:
    def __init__(self, total_population, initial_infected, initial_recovered, beta, gamma):
        self.total_population = total_population
        self.initial_infected = initial_infected
        self.initial_recovered = initial_recovered
        self.beta = beta
        self.gamma = gamma

    def _deriv(self, y, t):
        S, I, R = y
        dSdt = -self.beta * S * I / self.total_population
        dIdt = self.beta * S * I / self.total_population - self.gamma * I
        dRdt = self.gamma * I
        return dSdt, dIdt, dRdt

    def solve(self, t):
        y0 = self.total_population - self.initial_infected - self.initial_recovered, self.initial_infected, self.initial_recovered
        return scipy.integrate.odeint(self._deriv, y0, t)

# Example usage:
model = SIRModel(total_population=1000, initial_infected=1, initial_recovered=0, beta=0.2, gamma=0.1)
t = range(180)
S, I, R = model.solve(t).T

# Create a Pandas DataFrame from the t, S, I, and R arrays
import pandas as pd
df = pd.DataFrame({'t': t, 'S': S, 'I': I, 'R': R})

# plot the df DataFrame using DataFrame.plot
plt = df.plot(x='t', y=['S', 'I', 'R'], kind='line')

# Save the plot to a file
fig = plt.get_figure()
fig.savefig("traces.png")
