"""
C-Way Depot Revenue Intelligence Snapshot
Author: Irem Victor Chinonso (Prince Victor)
Description: Processes daily sales transactions to generate revenue intelligence.
"""

import pandas as pd

def analyze_revenue(transactions, min_threshold=50000):
    """
    Analyzes daily sales data.
    
    Args:
        transactions (list): List of dicts with keys 'product', 'quantity', 'unit_price'
        min_threshold (int): Minimum expected daily revenue for flagging.
        
    Returns:
        dict: Summary of revenue analytics.
    """
    df = pd.DataFrame(transactions)
    
    # Calculate revenue per transaction
    df['revenue'] = df['quantity'] * df['unit_price']
    
    # Total Daily Revenue
    total_revenue = df['revenue'].sum()
    
    # Revenue by Product
    product_revenue = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
    
    # Top 3 Products
    top_products = product_revenue.head(3).to_dict()
    
    # Threshold Check
    below_threshold = total_revenue < min_threshold
    
    return {
        "total_revenue": total_revenue,
        "product_breakdown": product_revenue.to_dict(),
        "top_3_products": top_products,
        "alert_low_revenue": below_threshold
    }

if __name__ == "__main__":
    # Mock data representing a typical day at C-Way Depot
    daily_sales = [
        {"product": "C-Way 75cl Case", "quantity": 120, "unit_price": 1200},
        {"product": "C-Way 1.5L Case", "quantity": 85, "unit_price": 1800},
        {"product": "Dispenser Refill", "quantity": 50, "unit_price": 800},
        {"product": "Sachet Water Bundle", "quantity": 200, "unit_price": 250},
    ]
    
    analytics = analyze_revenue(daily_sales)
    
    print("--- C-WAY REVENUE SNAPSHOT ---")
    print(f"Total Revenue: ₦{analytics['total_revenue']:,}")
    print("\nTop Revenue Generators:")
    for product, rev in analytics['top_3_products'].items():
        print(f"- {product}: ₦{rev:,}")
        
    if analytics['alert_low_revenue']:
        print("\n[ALERT] Daily revenue is below the target threshold.")
    else:
        print("\n[STATUS] Revenue targets met.")
