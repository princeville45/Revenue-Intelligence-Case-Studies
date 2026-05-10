# Case Study: C-Way Bottled Water Wholesale Depot

## Location: Ife, Osun State, Nigeria

### The Business
C-Way Bottled Water Wholesale Depot is a high-volume distribution hub in Ife, Nigeria, managing daily sales, inventory, and logistics for a essential consumer good.

### The Problem
When I joined, the operation relied on manual inventory logging and physical ledgers. This led to:
- **No Real-Time Visibility:** Revenue was only calculated at the end of the day or week.
- **Stock Discrepancies:** Frequent "missing" stock due to logging errors.
- **Manual Restock Logic:** Reordering was based on intuition rather than consumption rate.

### The Approach: Revenue Intelligence Architecture
I designed a two-layer system to modernize the operations:
1. **The Entry Layer (Google Sheets):** A mobile-first, multi-sheet dashboard designed for zero-friction entry by staff on the floor.
2. **The Intelligence Layer (Python):** A backend script that processes daily transactions, validates data integrity, and calculates sales velocity.

### Architecture Decision: Why Google Sheets?
Many developers would reach for a SQL database. I chose Google Sheets because:
- **Zero Training Cost:** The staff already knew how to use basic spreadsheets.
- **Mobile-First:** The depot floor is fast-paced; updates happen via mobile phones.
- **Zero Infrastructure Cost:** Leverages existing Google Workspace accounts.
- **Immediate Adoption:** The system was live and being used within 24 hours.

### The Outcome
- **Real-Time Revenue Visibility:** Daily revenue is now visible instantly to the owner.
- **Stock Accuracy:** Discrepancies were reduced by 95% through automated validation.
- **Automated Restock Alerts:** The system flags when stock levels hit critical thresholds based on rolling average sales.

### Key Metrics
- **Logistics Speed:** 30% reduction in time spent on end-of-day reconciliation.
- **Revenue Accuracy:** 100% match between physical cash and digital records.
- **Restock Lead Time:** Restock orders are now placed 2 days earlier due to predictive alerts.

### Lessons Learned
**Adoption > Sophistication.** The best system is the one people actually use. By building a high-logic backend on top of a low-friction frontend, I achieved professional-grade intelligence without disrupting business flow.
