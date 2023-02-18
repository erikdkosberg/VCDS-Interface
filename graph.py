import plotly.express as px
import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func
import pandas as pd
from sqlalchemy import create_engine, Column, Integer, Float, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import plotly.offline as pyo

Base = declarative_base()


class DataRecords(Base):
    __tablename__ = "DataRecords"
    RecordID = Column(Integer, primary_key=True)
    SessionID = Column(Integer)
    PartNumber = Column(String)
    Value = Column(Float)
    TimeStamp = Column(Float)


engine = create_engine("sqlite:///Database.db")
Session = sessionmaker(bind=engine)
session = Session()

df = session.query(DataRecords).order_by(DataRecords.TimeStamp).all()
df = pd.DataFrame(
    [(record.PartNumber, record.Value, record.TimeStamp) for record in df],
    columns=["PartNumber", "Value", "TimeStamp"],
)
df = df.sort_values(by=["TimeStamp"])

fig = px.scatter(df, x="TimeStamp", y="Value")

# Set number of y-axis and x-axis tick marks
fig.update_layout(yaxis_nticks=4, xaxis_nticks=10, hovermode="x")

# Group data by PartNumber
for part_number, group_df in df.groupby(by="PartNumber"):
    fig.add_scatter(
        x=group_df["TimeStamp"],
        y=group_df["Value"],
        mode="lines+markers",
        name=part_number,
        line_shape="spline",
    )
    fig.update_traces(
        marker=dict(
            size=1, color=["red", "blue", "green", "purple", "orange", "yellow", "pink"]
        )
    )

pyo.offline.plot(fig, filename="control_chart.html")

# Show plot
fig.show()

session.close()
