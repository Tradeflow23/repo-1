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
    operating_cycle = inventory_days + receivable_days
    working_capital = inventory_value + receivables - payables
    wc_percent = (working_capital / monthly_sales) * 100 if monthly_sales > 0 else 0
    capital_efficiency = monthly_sales / working_capital if working_capital > 0 else 0

    # Risk Classification
    if ccc > 90:
        risk_level = "🔴 High Liquidity Risk"
    elif ccc > 60:
        risk_level = "🟠 Moderate Liquidity Risk"
    else:
        risk_level = "🟢 Healthy Liquidity Position"

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
        st.metric("Working Capital % of Sales", f"{wc_percent:.2f}%")

    st.markdown("---")

    st.subheader("📊 Additional Metrics")

    st.write(f"Operating Cycle: {operating_cycle:.2f} days")
    st.write(f"Capital Efficiency Ratio: {capital_efficiency:.2f}")
    st.write(f"Risk Assessment: {risk_level}")

    st.markdown("---")

    st.subheader("📘 What These Terms Mean")

    st.markdown("""
    - **DIO (Days Inventory Outstanding):** Average number of days inventory is held before being sold.
    - **DSO (Days Sales Outstanding):** Average number of days customers take to pay.
    - **DPO (Days Payables Outstanding):** Average number of days you take to pay suppliers.
    - **Cash Conversion Cycle (CCC):** Total time (in days) your cash is tied up in operations.
    - **Operating Cycle:** Time taken to convert inventory into cash (Inventory Days + Receivable Days).
    """)

else:
    st.warning("Please enter Monthly Sales and Monthly COGS to calculate results.")
