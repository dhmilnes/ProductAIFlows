# Demo Database Schema

LearnFlow Technologies sample data for analysis demos.

## Tables

### daily_metrics
Aggregate daily metrics. Use for top-level trends.

| Column | Type | Notes |
|--------|------|-------|
| date | TEXT | Primary key, YYYY-MM-DD |
| sessions | INTEGER | Total site sessions |
| new_users | INTEGER | First-time visitors |
| signups | INTEGER | Account creations |
| trials_started | INTEGER | Trial activations |
| conversions | INTEGER | Completed purchases |
| revenue | REAL | Total revenue (USD) |
| avg_order_value | REAL | Revenue / conversions |

**Date range:** 2024-01-27 to 2026-01-26 (2 years)

---

### channel_metrics
Daily metrics broken down by acquisition channel.

| Column | Type | Notes |
|--------|------|-------|
| date | TEXT | YYYY-MM-DD |
| channel_id | TEXT | organic, paid_search, advisor, partner, direct |
| channel_name | TEXT | Human-readable name |
| sessions | INTEGER | |
| signups | INTEGER | |
| conversions | INTEGER | |
| revenue | REAL | |

---

### product_metrics
Daily metrics by product line.

| Column | Type | Notes |
|--------|------|-------|
| date | TEXT | YYYY-MM-DD |
| product_id | TEXT | core_curriculum, professional_cert, pathway_bundle, enterprise |
| product_name | TEXT | Human-readable name |
| units_sold | INTEGER | Units purchased |
| revenue | REAL | Product revenue |
| refunds | INTEGER | Refund count |
| refund_amount | REAL | Refund dollars |

---

### support_tickets
Individual support tickets.

| Column | Type | Notes |
|--------|------|-------|
| ticket_id | INTEGER | Primary key |
| created_date | TEXT | YYYY-MM-DD |
| category | TEXT | cancellation, billing, technical, account, content |
| subcategory | TEXT | Specific issue type |
| channel | TEXT | Where ticket originated |
| sentiment_score | REAL | -1.0 to 0 (all complaints) |
| resolution_hours | REAL | Time to resolve |
| escalated | INTEGER | 0 or 1 |

---

### weekly_funnel
Weekly conversion funnel metrics.

| Column | Type | Notes |
|--------|------|-------|
| week_start | TEXT | Monday of the week, YYYY-MM-DD |
| visitors | INTEGER | Unique visitors |
| product_views | INTEGER | Product page views |
| add_to_cart | INTEGER | Cart additions |
| checkout_started | INTEGER | Checkout initiations |
| checkout_completed | INTEGER | Completed purchases |
| conversion_rate | REAL | checkout_completed / visitors |

---

### lead_form_metrics
Daily B2B lead form performance by campaign.

| Column | Type | Notes |
|--------|------|-------|
| date | TEXT | YYYY-MM-DD (weekdays only) |
| campaign_id | TEXT | digital-badges, bootcamp-completion, ai-skills-verify, higher-ed-micro |
| campaign_name | TEXT | Human-readable name |
| lp_visits | INTEGER | Landing page visits from this campaign |
| form_starts | INTEGER | Users who started the lead form |
| form_completions | INTEGER | Users who submitted the form |
| conversion_rate | REAL | form_completions / lp_visits |

---

## Analysis Hints

### YoY Comparisons
Use 364-day lookback to align day-of-week:
```sql
date(date, '-364 days')
```
