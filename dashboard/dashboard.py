import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="E-Commerce Logistics Dashboard",
    layout="wide"
)

# =========================
# LOAD DATA
# =========================
@st.cache_data
def load_data():
    df = pd.read_csv("main_data.csv")

    df['order_purchase_timestamp'] = pd.to_datetime(
        df['order_purchase_timestamp']
    )

    df['month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

    df['revenue'] = df['price'] + df['freight_value']

    return df

df = load_data()

# =========================
# SIDEBAR FILTER
# =========================

st.sidebar.title("Filter")

category = st.sidebar.multiselect(
    "Product Category",
    df['product_category_name'].dropna().unique()
)

date_range = st.sidebar.date_input(
    "Date Range",
    [df['order_purchase_timestamp'].min(),
     df['order_purchase_timestamp'].max()]
)

df_filtered = df.copy()

if category:
    df_filtered = df_filtered[
        df_filtered['product_category_name'].isin(category)
    ]

df_filtered = df_filtered[
    (df_filtered['order_purchase_timestamp'] >= pd.to_datetime(date_range[0])) &
    (df_filtered['order_purchase_timestamp'] <= pd.to_datetime(date_range[1]))
]

# =========================
# HEADER
# =========================

st.title("E-Commerce Operations Dashboard")

# =========================
# KPI METRICS
# =========================

col1, col2, col3, col4 = st.columns(4)

total_revenue = df_filtered['revenue'].sum()
total_orders = df_filtered['order_id'].nunique()
cancel_rate = df_filtered['is_canceled'].mean()
avg_freight_ratio = df_filtered['freight_ratio'].mean()

col1.metric("Total Revenue", f"${total_revenue:,.0f}")
col2.metric("Total Orders", total_orders)
col3.metric("Cancellation Rate", f"{cancel_rate:.2%}")
col4.metric("Avg Freight Ratio", f"{avg_freight_ratio:.2f}")

st.divider()

# =========================
# KATEGORI PRODUK
# =========================

st.subheader("Kategori Produk & Pendapatan")

analysis_mode = st.radio(
    "Analisis berdasarkan:",
    ["Revenue", "Order Frequency"],
    horizontal=True
)

# =========================
# AGGREGATION LOGIC
# =========================

if analysis_mode == "Revenue":

    cat_data = (
        df_filtered
        .groupby('product_category_name')['revenue']
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    value_col = "revenue"
    title = "Top 10 Product Categories by Revenue"

else:

    cat_data = (
        df_filtered['product_category_name']
        .value_counts()
        .head(10)
        .reset_index()
    )

    cat_data.columns = ["product_category_name", "order_count"]

    value_col = "order_count"
    title = "Top 10 Product Categories by Order Frequency"


# =========================
# TREND DATA
# =========================

if not category:

    top_categories = cat_data['product_category_name']

    trend_df = df_filtered[
        df_filtered['product_category_name'].isin(top_categories)
    ]

else:
    trend_df = df_filtered


if analysis_mode == "Revenue":

    monthly_trend = (
        trend_df
        .groupby(['month', 'product_category_name'])['revenue']
        .sum()
        .reset_index()
    )

    y_col = "revenue"
    trend_title = "Monthly Revenue Trend"

else:

    monthly_trend = (
        trend_df
        .groupby(['month', 'product_category_name'])
        .size()
        .reset_index(name='order_count')
    )

    y_col = "order_count"
    trend_title = "Monthly Order Trend"


# =========================
# HORIZONTAL LAYOUT
# =========================

col1, col2 = st.columns(2)

with col1:

    fig_cat = px.pie(
        cat_data,
        names='product_category_name',
        values=value_col,
        title=title,
        hole=0.4
    )

    fig_cat.update_traces(textinfo='percent+label')

    st.plotly_chart(fig_cat, use_container_width=True)


with col2:

    fig_trend = px.line(
        monthly_trend,
        x='month',
        y=y_col,
        color='product_category_name',
        title=trend_title
    )

    st.plotly_chart(fig_trend, use_container_width=True)

# =========================
# TREN REVENUE
# =========================

rev_trend = (
    df_filtered
    .groupby('month')['revenue']
    .sum()
    .reset_index()
)

fig_trend = px.line(
    rev_trend,
    x='month',
    y='revenue',
    title="Monthly Revenue Trend"
)

st.plotly_chart(fig_trend, use_container_width=True)

st.divider()


# =========================
# EFISIENSI LOGISTIK
# =========================

st.subheader("Efisiensi Logistik (Actual vs Estimated)")

fig_delivery = px.scatter(
    df_filtered.sample(min(len(df_filtered), 5000)),
    x='estimated_delivery_days',
    y='actual_delivery_days',
    opacity=0.4,
    title="Actual vs Estimated Delivery Time"
)

st.plotly_chart(fig_delivery, use_container_width=True)

delay = df_filtered['actual_delivery_days'] - df_filtered['estimated_delivery_days']

fig_delay = px.histogram(
    delay,
    nbins=50,
    title="Distribution of Delivery Delay"
)

st.plotly_chart(fig_delay, use_container_width=True)

st.divider()

# =========================
# ANALISIS ONGKIR
# =========================

st.subheader("Freight Ratio Analysis")

fig_ratio = px.histogram(
    df_filtered,
    x='freight_ratio',
    nbins=50,
    title="Freight Ratio Distribution"
)

st.plotly_chart(fig_ratio, use_container_width=True)

fig_scatter = px.scatter(
    df_filtered.sample(5000),
    x='price',
    y='freight_value',
    opacity=0.4,
    title="Freight Value vs Product Price"
)

st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# =========================
# PEMBATALAN
# =========================

st.subheader("Analisis Pembatalan")

cancel_cat = (
    df_filtered
    .groupby('product_category_name')['is_canceled']
    .mean()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_cancel = px.bar(
    cancel_cat,
    x='product_category_name',
    y='is_canceled',
    title="Cancellation Rate by Category"
)

st.plotly_chart(fig_cancel, use_container_width=True)