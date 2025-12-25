import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("../data/linkedin_profiles_100.csv")

print("Total Profiles:", len(df))

# ===============================
# 1. Job Title Distribution
# ===============================
plt.figure()
df['job_title'].value_counts().plot(kind='bar')
plt.title("Job Title Distribution")
plt.xlabel("Job Title")
plt.ylabel("Number of Profiles")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/job_titles.png")
plt.show()

# ===============================
# 2. Average Experience by Job Title
# ===============================
plt.figure()
df.groupby("job_title")["experience_years"].mean().plot(kind='bar')
plt.title("Average Experience by Job Title")
plt.xlabel("Job Title")
plt.ylabel("Average Years of Experience")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/avg_experience.png")
plt.show()

# ===============================
# 3. Connections vs Experience (Scatter)
# ===============================
plt.figure()
plt.scatter(df["experience_years"], df["connections"])
plt.title("Connections vs Experience")
plt.xlabel("Experience (Years)")
plt.ylabel("Number of Connections")
plt.tight_layout()
plt.savefig("../visuals/connections_vs_experience.png")
plt.show()

# ===============================
# 4. Industry Distribution (Pie Chart)
# ===============================
plt.figure()
df['industry'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Industry Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig("../visuals/industry_distribution.png")
plt.show()

# ===============================
# 5. Top 10 Profiles by Connections
# ===============================
top_connections = df.sort_values(by="connections", ascending=False).head(10)

plt.figure()
plt.bar(top_connections["name"], top_connections["connections"])
plt.title("Top 10 Profiles by Connections")
plt.xlabel("Profile Name")
plt.ylabel("Connections")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("../visuals/top_connections.png")
plt.show()

