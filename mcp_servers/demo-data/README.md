# Demo Data MCP Server

A lightweight SQLite MCP server for demoing the ProductAIFlows `analyze` skill.

## What's Included

**Sample data for LearnFlow Technologies** (fictional ed-tech company):
- 2 years of daily metrics (sessions, conversions, revenue)
- Channel breakdown (organic, paid, advisor, partner, direct)
- Product breakdown (Core Curriculum, Professional Cert, Pathway Bundle, Enterprise)
- Support tickets with categories and sentiment
- Weekly funnel metrics

## Setup

### 1. Install dependencies

```bash
pip install mcp
```

### 2. Generate sample data (optional — already included)

```bash
python setup_sample_data.py
```

### 3. Add to Claude Code MCP config

Add to your `.claude/mcp.json`:

```json
{
  "mcpServers": {
    "demo-data": {
      "command": "python",
      "args": ["mcp_servers/demo-data/server.py"]
    }
  }
}
```

## Available Tools

| Tool | Purpose |
|------|---------|
| `query` | Execute SELECT queries against the database |
| `list_tables` | Show all tables with row counts |
| `describe_table` | Show schema and sample values for a table |
| `get_date_range` | Get min/max dates in a table |

## Tables

### `daily_metrics`
Aggregate daily metrics (731 rows, 2 years)

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | YYYY-MM-DD |
| sessions | INTEGER | Daily sessions |
| new_users | INTEGER | New user count |
| signups | INTEGER | Account signups |
| trials_started | INTEGER | Trial activations |
| conversions | INTEGER | Purchases |
| revenue | REAL | Daily revenue |
| avg_order_value | REAL | AOV |

### `channel_metrics`
Daily metrics by acquisition channel

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | YYYY-MM-DD |
| channel_id | TEXT | organic, paid_search, advisor, partner, direct |
| channel_name | TEXT | Display name |
| sessions, signups, conversions, revenue | | Metrics |

### `product_metrics`
Daily metrics by product

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | YYYY-MM-DD |
| product_id | TEXT | core_curriculum, professional_cert, pathway_bundle, enterprise |
| product_name | TEXT | Display name |
| units_sold | INTEGER | Units |
| revenue | REAL | Revenue |
| refunds | INTEGER | Refund count |
| refund_amount | REAL | Refund $ |

### `support_tickets`
Individual support tickets (~20k rows)

| Column | Type | Description |
|--------|------|-------------|
| ticket_id | INTEGER | Unique ID |
| created_date | TEXT | YYYY-MM-DD |
| category | TEXT | cancellation, billing, technical, account, content |
| subcategory | TEXT | Specific issue type |
| channel | TEXT | email, chat, app_review, social, partner_escalation |
| sentiment_score | REAL | -1.0 to 0 (all negative) |
| resolution_hours | REAL | Time to resolve |
| escalated | INTEGER | 0 or 1 |

### `lead_form_metrics`
Daily B2B lead form performance by campaign

| Column | Type | Description |
|--------|------|-------------|
| date | TEXT | YYYY-MM-DD (weekdays only) |
| campaign_id | TEXT | Campaign identifier |
| campaign_name | TEXT | Display name |
| lp_visits | INTEGER | Landing page visits |
| form_starts | INTEGER | Form interactions started |
| form_completions | INTEGER | Form submissions |
| conversion_rate | REAL | Completions / visits |

### `weekly_funnel`
Weekly conversion funnel

| Column | Type |
|--------|------|
| week_start | TEXT |
| visitors, product_views, add_to_cart, checkout_started, checkout_completed | INTEGER |
| conversion_rate | REAL |

## Swapping in Real Data

To use your own data:

1. Replace `sample_data.db` with your SQLite database
2. Or modify `server.py` to connect to a different database (Postgres, BigQuery, etc.)

The MCP tools (`query`, `list_tables`, etc.) will work with any SQL database.
