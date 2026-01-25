import numpy as np
import plotly.graph_objects as go

hbar = 1.0
dx = np.linspace(0.05, 5, 600)
dp_min = hbar / (2*dx)

fig = go.Figure()

# Quantum limit
fig.add_trace(go.Scatter(
    x=dx, y=dp_min,
    mode="lines",
    name="Quantum limit",
    line=dict(color="gold", width=3)
))

# Forbidden region
fig.add_trace(go.Scatter(
    x=np.concatenate([dx, dx[::-1]]),
    y=np.concatenate([dp_min, np.zeros_like(dp_min)]),
    fill="toself",
    fillcolor="rgba(255,0,0,0.25)",
    line=dict(color="rgba(0,0,0,0)"),
    name="Forbidden region"
))

# Example fixed lines
for dp in [0.3, 0.8, 1.5]:
    fig.add_trace(go.Scatter(x=[0,5], y=[dp,dp], mode="lines", line=dict(dash="dash"), name=f"Δp={dp}"))

for dxv in [0.3, 0.8, 1.5]:
    fig.add_trace(go.Scatter(x=[dxv,dxv], y=[0,5], mode="lines", line=dict(dash="dot"), name=f"Δx={dxv}"))

fig.update_layout(
    title="Heisenberg Uncertainty Principle",
    xaxis_title="Δx", yaxis_title="Δp",
    template="plotly_dark"
)

# Save static figure
fig.write_image("../figures/heisenberg_plot.png", scale=3)
fig.show(config={"editable": True})
