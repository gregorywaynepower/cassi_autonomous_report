import plotly
import plotly.graph_objects as go
import pandas as pd
  
df = pd.read_excel("CASSI in Cary's Bond Park - Rider Survey_800AM_20230606_Analysis Workbook_20230619.xlsx", "Rider Survey Responses (Final)")

label = ["1 – Very safe","2 – Safe","3 – Neither safe nor unsafe (no opinion)","4 – Unsafe", "5 – Very unsafe", "1 – Very safe","2 – Safe","3 – Neither safe nor unsafe (no opinion)","4 – Unsafe", "5 – Very unsafe"]
#use dynamic programming to generate array of change in before and after data
before_list = df["BEFORE riding the shuttle, I felt that driverless vehicles are:"].to_list()
before = [int(x[0]) for x in before_list]

after_list = df["AFTER riding the shuttle, I feel that driverless vehicles are:"].to_list()
after = [int(y[0]) for y in after_list]

array = [[0] * 5 for _ in range(5)]
for i in range(0, len(before)):
    array[before[i]-1][after[i]-1]+=1
print(array)
flatten_array = sum(array, [])

source = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4]
target = [5,6,7,8,9,5,6,7,8,9,5,6,7,8,9,5,6,7,8,9,5,6,7,8,9]
value = flatten_array


colors = ["#0073B3","#5F9DC6","#8DB9D8","#BCD6E8","#BCBCBC",
          "#0073B3","#5F9DC6","#8DB9D8","#BCD6E8","#BCBCBC",
          "#0073B3","#5F9DC6","#8DB9D8","#BCD6E8","#BCBCBC",
          "#0073B3","#5F9DC6","#8DB9D8","#BCD6E8","#BCBCBC",
          "#0073B3","#5F9DC6","#8DB9D8","#BCD6E8","#BCBCBC"]
link = dict(source = source, target = target, value = value, color=colors)
node = dict(label = label, pad=50, thickness=5, color=colors)
data = go.Sankey(link = link, node=node)


print(data)

fig = go.Figure(data)
fig.update_layout(font=dict(size=20))
#fig.show()
plotly.io.write_html(fig,"sankey_diagram2.html", include_plotlyjs=False, full_html=False)