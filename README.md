# API Paywall & License Enforcement (Drop-in)

## 🔒 Paid Access Required

This repository provides a **production-ready API paywall** that you can attach to **any API** in minutes.

It enforces:
- API key validation
- Paid access gating
- License / usage enforcement
- Hard block when payment is missing

No dashboards.  
No SDKs.  
No vendor lock-in.

---

## 🚀 API Paywall for Paid Access & License Enforcement

If you run an API and need to:
- stop unauthorized usage
- sell API access
- enforce paid plans
- block abuse without building auth systems

👉 **This is the missing piece.**

You add **one HTTP call** before serving data.  
Remove it → your API becomes unsafe.

---

## 💳 Purchase API Access

All requests require a valid paid API key.

👉 **Buy access here:**  
https://jathangkip.gumroad.com/l/vtagec
You receive an API key immediately after purchase.

Requests without a key are automatically rejected.

---

## Try It (Free)

Validate integration before purchasing:

GET https://globalaienterprise-api-production.up.railway.app/free/validate

Free usage is limited.
When exhausted, a paid API key is required to continue.

---

## ⚠️ Important

This repository has **no security of its own**.

Security is enforced entirely by **GlobalAIEnterprise Shield**.  
If Shield is removed, protection is removed.

---

## How It Works

Before returning data, this API calls:

```
GET /shield/check
```

If the request is allowed → data is returned  
If blocked → request fails

---

## Why This Exists

This repository demonstrates how GlobalAIEnterprise Shield is used
as a mandatory dependency, not a feature.

Remove the Shield call and you remove protection.
