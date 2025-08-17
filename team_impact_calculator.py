#!/usr/bin/env python3
def calculate_impact():
    print("\n⚡ TEAM IMPACT CALCULATOR (v1.2)\n")
    open_roles = int(input("Mission-critical roles open: "))
    avg_salary = int(input("Average fully-loaded salary ($): "))
    ttf_reduction = float(input("Expected TTF reduction % (e.g., 65): ")) / 100
    role_impact = float(input("Estimated role ARR impact ($): "))
    
    # Calculation model
    opportunity_cost = (open_roles * avg_salary * 0.3) * (ttf_reduction * 6)
    revenue_impact = open_roles * role_impact * (1 + ttf_reduction)
    
    print(f"\n✅ CAPITAL SAVINGS: ${opportunity_cost:,.0f}")
    print(f"✅ PROJECTED ARR IMPACT: ${revenue_impact:,.0f}\n")

if __name__ == "__main__":
    calculate_impact()
