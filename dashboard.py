import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_parquet("titanic_cleaned.parquet")

print("Titanic dataset loaded successfully!")
print("Dataset shape:", df.shape)


# ==========================================
# 2. PREPARE DATA
# ==========================================

# Survival counts
survival_data = (
    df["Survived"]
    .value_counts()
    .sort_index()
)

# Gender-wise survival
gender_data = (
    df.groupby(["Sex", "Survived"])
    .size()
    .reset_index(name="Count")
)

# Class-wise survival
class_data = (
    df.groupby(["Pclass", "Survived"])
    .size()
    .reset_index(name="Count")
)

# Age distribution
age_data = df.dropna(subset=["Age"])

# Age vs Fare
scatter_data = df.dropna(subset=["Age", "Fare"])


# ==========================================
# 3. CREATE DASHBOARD LAYOUT
# ==========================================

fig = make_subplots(
    rows=3,
    cols=2,
    subplot_titles=(
        "1. Titanic Survival Count",
        "2. Survival by Gender",
        "3. Survival by Passenger Class",
        "4. Passenger Age Distribution",
        "5. Age vs Fare by Survival"
    ),
    specs=[
        [{"type": "bar"}, {"type": "bar"}],
        [{"type": "bar"}, {"type": "histogram"}],
        [{"type": "scatter", "colspan": 2}, None]
    ]
)


# ==========================================
# 4. CHART 1 - SURVIVAL COUNT
# ==========================================

fig.add_trace(
    go.Bar(
        x=["Not Survived", "Survived"],
        y=survival_data.values,
        name="Passengers",
        marker_color=["#EF553B", "#00CC96"]
    ),
    row=1,
    col=1
)


# ==========================================
# 5. CHART 2 - SURVIVAL BY GENDER
# ==========================================

for survived, label, color in [
    (0, "Not Survived", "#EF553B"),
    (1, "Survived", "#00CC96")
]:

    gender_subset = gender_data[
        gender_data["Survived"] == survived
    ]

    fig.add_trace(
        go.Bar(
            x=gender_subset["Sex"],
            y=gender_subset["Count"],
            name=label,
            marker_color=color,
            legendgroup=label
        ),
        row=1,
        col=2
    )


# ==========================================
# 6. CHART 3 - SURVIVAL BY CLASS
# ==========================================

for survived, label, color in [
    (0, "Not Survived", "#EF553B"),
    (1, "Survived", "#00CC96")
]:

    class_subset = class_data[
        class_data["Survived"] == survived
    ]

    fig.add_trace(
        go.Bar(
            x=class_subset["Pclass"],
            y=class_subset["Count"],
            name=label,
            marker_color=color,
            legendgroup=label,
            showlegend=False
        ),
        row=2,
        col=1
    )


# ==========================================
# 7. CHART 4 - AGE DISTRIBUTION
# ==========================================

fig.add_trace(
    go.Histogram(
        x=age_data["Age"],
        nbinsx=20,
        name="Age",
        marker_color="#636EFA",
        showlegend=False
    ),
    row=2,
    col=2
)


# ==========================================
# 8. CHART 5 - AGE VS FARE
# ==========================================

for survived, label, color in [
    (0, "Not Survived", "#EF553B"),
    (1, "Survived", "#00CC96")
]:

    scatter_subset = scatter_data[
        scatter_data["Survived"] == survived
    ]

    fig.add_trace(
        go.Scatter(
            x=scatter_subset["Age"],
            y=scatter_subset["Fare"],
            mode="markers",
            name=label,
            marker=dict(
                color=color,
                size=7,
                opacity=0.6
            ),
            legendgroup=label
        ),
        row=3,
        col=1
    )


# ==========================================
# 9. DASHBOARD DESIGN
# ==========================================

fig.update_layout(
    title={
        "text": "TITANIC DATA ANALYSIS DASHBOARD",
        "x": 0.5,
        "xanchor": "center"
    },
    template="plotly_white",
    height=1100,
    width=1300,
    barmode="group",
    showlegend=True
)

fig.update_xaxes(title_text="Survival Status", row=1, col=1)
fig.update_yaxes(title_text="Passenger Count", row=1, col=1)

fig.update_xaxes(title_text="Gender", row=1, col=2)
fig.update_yaxes(title_text="Passenger Count", row=1, col=2)

fig.update_xaxes(title_text="Passenger Class", row=2, col=1)
fig.update_yaxes(title_text="Passenger Count", row=2, col=1)

fig.update_xaxes(title_text="Age", row=2, col=2)
fig.update_yaxes(title_text="Frequency", row=2, col=2)

fig.update_xaxes(title_text="Age", row=3, col=1)
fig.update_yaxes(title_text="Fare", row=3, col=1)


# ==========================================
# 10. EXPORT DASHBOARD
# ==========================================

fig.write_html("titanic_dashboard.html")

fig.write_image("titanic_dashboard.png")

print("\nDashboard exported successfully!")
print("HTML: titanic_dashboard.html")
print("PNG: titanic_dashboard.png")


# ==========================================
# 11. DISPLAY DASHBOARD
# ==========================================

fig.show()
