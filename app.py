
import streamlit as st

st.set_page_config(page_title="Working Capital Dashboard", layout="wide")

st.title("📊 Working Capital Intelligence Dashboard")

st.markdown("Enter your financial details below:")

# --- INPUT SECTION ---
col1, col2 = st.columns(2)

with col1:
    monthly_sales = st.number_input("Monthly Sales (₹)", min_value=0.0, step=1000.0)
    monthly_cogs = st.number_input("Monthly COGS (₹)", min_value=0.0, step=1000.0)
    inventory_value = st.number_input("Inventory Value (₹)", min_value=0.0, step=1000.0)

with col2:
    receivables = st.number_input("Receivables (₹)", min_value=0.0, step=1000.0)
    payables = st.number_input("Payables (₹)", min_value=0.0, step=1000.0)

# --- CALCULATIONS ---
if monthly_sales > 0 and monthly_cogs > 0:
    daily_sales = monthly_sales / 30
    daily_cogs = monthly_cogs / 30

    inventory_days = inventory_value / daily_cogs if daily_cogs > 0 else 0
    receivable_days = receivables / daily_sales if daily_sales > 0 else 0
    payable_days = payables / daily_cogs if daily_cogs > 0 else 0

    ccc = inventory_days + receivable_days - payable_days
    working_capital = inventory_value + receivables - payables

    st.markdown("---")
    st.subheader("📈 Results")

    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric("Working Capital (₹)", f"{working_capital:,.2f}")
        st.metric("Cash Conversion Cycle (Days)", f"{ccc:.2f}")

    with col4:
        st.metric("Inventory Days (DIO)", f"{inventory_days:.2f}")
        st.metric("Receivable Days (DSO)", f"{receivable_days:.2f}")

    with col5:
        st.metric("Payable Days (DPO)", f"{payable_days:.2f}")

    st.markdown("---")

    st.info(
        "💡 Insight: Reducing receivable days or inventory days can significantly free up working capital."
    )

else:
    st.warning("Please enter Monthly Sales and Monthly COGS to calculate results.")
