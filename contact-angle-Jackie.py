import matplotlib.pyplot as plt

# Define the materials and their contact angles
# https://www.accudynetest.com/polytable_03.html?sortby=contact_angle%20ASC
# https://www.matec-conferences.org/articles/matecconf/pdf/2018/01/matecconf_icmae2017_04004.pdf
materials = ["PVOH", "PMMA", "PDMS",  "Teflon", "Engraved PDMS", "Lotus Leaf"]
angles = [51, 70.9, 107.2, 109.2, 150.1, 151] # Average contact angle for Engraved PDMS
colors = ['#1167b1', '#1167b1', '#1167b1', '#1167b1', '#967bb6', '#1167b1']

# Create a DataFrame to sort the materials and angles
import pandas as pd
df_sorted = pd.DataFrame({"Materials": materials, "Angles": angles, "Colors": colors})
# df_sorted = df_sorted.sort_values("Angles")

# Create the bar chart
plt.figure(figsize=(12, 6))
bars = plt.bar(df_sorted["Materials"], df_sorted["Angles"], color=df_sorted["Colors"], edgecolor='black')
# Add error bar for the sample droplets
plt.errorbar(df_sorted[df_sorted["Materials"] == "Engraved PDMS"].index, angles[-2], yerr=0.10396, capsize=3, color='black', fmt='none')

# Remove the gridlines
plt.grid(False)

# Keep the tick marks on the outside
plt.tick_params(direction='out')

# Thicken the axis lines
plt.gca().spines['bottom'].set_linewidth(1.5)
plt.gca().spines['left'].set_linewidth(1.5)

# Increase the font size for the title, legend, and axis titles
# plt.title("Contact Angles of Engraved PDMS and Reference Materials", fontsize=16)
# plt.xlabel("Materials", fontsize=14)
plt.ylabel("Contact Angle (degrees)", fontsize=14)

# Show the average +/- the deviation at the top of the bar with the same font as the rest of the plot, slightly bigger, and positioned inside the bar, and bolded
plt.text(df_sorted[df_sorted["Materials"] == "Engraved PDMS"].index[0], angles[-2]-10, f"150.1 ± 0.1", ha='center', fontsize=10, fontweight='bold')

# Show the plot
plt.show()