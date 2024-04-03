   Data Generation (Parquet Files)        Data Ingestion (PostgreSQL)          Data Analysis & Visualization
┌───────────────────────────────┐      ┌─────────────────────────────┐      ┌───────────────────────────────┐
│                               │      │                                 │      │                               │
│      Synthetic Data           │      │     Pandas DataFrames          │      │       Visualizations        │
│       (Parquet Files)         │      │         Transformation         │      │      (Matplotlib/Seaborn)    │
│                               │      │           SQL Queries          │      │                               │
└───────────────────────────────┘      └─────────────────────────────┘      └───────────────────────────────┘
               │                               │                                  │
               │ Extract                       │ Transform                        │ Load
               │                               │                                  │
               ▼                               ▼                                  ▼
┌───────────────────────────────┐      ┌─────────────────────────────┐      ┌───────────────────────────────┐
│                               │      │                                 │      │                               │
│     Parquet Files            │◄─────┤         PostgreSQL DB          ├─────►│    Visualization Outputs    │
│    (Synthetic Data)          │      │      (Data Ingestion)          │      │    (Insights/Charts/Plots)   │
│                               │      │                                 │      │                               │
└───────────────────────────────┘      └─────────────────────────────┘      └───────────────────────────────┘
